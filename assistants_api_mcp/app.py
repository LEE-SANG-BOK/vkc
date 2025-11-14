import argparse
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

from dotenv import load_dotenv
from openai import OpenAI

from mcp_bridge import BridgeTool, MCPBridge


BASE_DIR = Path(__file__).resolve().parent.parent
AGENTS_DIR = BASE_DIR / "vkc-agents"
DEFAULT_MODEL = "gpt-4.1-mini"
DEFAULT_MCP_URL = "http://127.0.0.1:8000/mcp"
DEFAULT_TOOL_PREFIX = "mcp"


def load_text(path: Path) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def build_instructions(agent_key: str) -> str:
    cfg_path = AGENTS_DIR / "config/agents.yaml"
    if not cfg_path.exists():
        raise FileNotFoundError(f"agents.yaml not found: {cfg_path}")

    # 간단 파서(외부 의존성 없이)
    baseline_rel = None
    agents = {}
    current_section = None
    with open(cfg_path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            if s.startswith("baseline:"):
                baseline_rel = s.split(":", 1)[1].strip()
                continue
            if s.startswith("agents:"):
                current_section = "agents"
                continue
            if current_section == "agents":
                if s.startswith("-"):
                    # 새 항목 시작, 무시하고 다음 줄로 키를 읽는다
                    current = {"key": None, "name": None, "prompt": None}
                    agents[len(agents)] = current
                elif ":" in s and agents:
                    k, v = [x.strip() for x in s.split(":", 1)]
                    agents[max(agents.keys())][k] = v

    # 인덱스 → key 사전 재구성
    agent_map = {item["key"]: item for item in agents.values() if item.get("key")}
    if agent_key not in agent_map:
        raise ValueError(f"Unknown agent key: {agent_key}. Available: {list(agent_map)}")

    baseline_path = AGENTS_DIR / baseline_rel if baseline_rel else None
    agent_prompt_rel = agent_map[agent_key]["prompt"]
    agent_prompt_path = AGENTS_DIR / agent_prompt_rel

    parts = []
    if baseline_path and baseline_path.exists():
        parts.append(load_text(baseline_path))
    parts.append(load_text(agent_prompt_path))
    return "\n\n".join(parts)


def normalize_tool_prefix(prefix: str) -> str:
    cleaned = re.sub(r"[^a-z0-9_]+", "_", prefix.strip().lower())
    cleaned = cleaned.strip("_")
    return cleaned or "mcp"


def build_tool_config(prefix: str) -> Tuple[List[Dict[str, Any]], Dict[str, BridgeTool]]:
    normalized = normalize_tool_prefix(prefix)
    search_name = f"{normalized}_search"
    fetch_name = f"{normalized}_fetch"

    tools = [
        {
            "type": "function",
            "function": {
                "name": search_name,
                "description": "레포지토리 문서를 검색해 관련 스니펫을 찾습니다.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "찾고 싶은 키워드 또는 문장",
                        }
                    },
                    "required": ["query"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": fetch_name,
                "description": "지정한 파일 경로(id)의 전문을 반환합니다.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "fetch 대상 파일 경로",
                        }
                    },
                    "required": ["id"],
                },
            },
        },
    ]

    tool_map = {
        search_name: BridgeTool(assistant_name=search_name, mcp_name="search"),
        fetch_name: BridgeTool(assistant_name=fetch_name, mcp_name="fetch"),
    }
    return tools, tool_map


def submit_tool_outputs(client: OpenAI, thread_id: str, run_id: str, bridge: MCPBridge, tool_calls) -> None:
    tool_outputs = []
    for call in tool_calls:
        arguments_str = call.function.arguments or "{}"
        try:
            arguments = json.loads(arguments_str)
        except json.JSONDecodeError as exc:
            output = json.dumps({"error": f"Invalid arguments: {exc}"}, ensure_ascii=False)
        else:
            try:
                output = bridge.execute(call.function.name, arguments)
            except Exception as exc:  # noqa: BLE001
                output = json.dumps({"error": str(exc)}, ensure_ascii=False)
        tool_outputs.append({"tool_call_id": call.id, "output": output})

    client.beta.threads.runs.submit_tool_outputs(
        thread_id=thread_id,
        run_id=run_id,
        tool_outputs=tool_outputs,
    )


def ensure_assistant(client: OpenAI, *, instructions: str, model: str, tools: List[Dict[str, Any]], assistant_id: str | None) -> Tuple[str, bool]:
    if assistant_id:
        client.beta.assistants.update(
            assistant_id=assistant_id,
            instructions=instructions,
            model=model,
            tools=tools,
        )
        return assistant_id, False

    assistant = client.beta.assistants.create(
        name=f"local-{model}",
        instructions=instructions,
        model=model,
        tools=tools,
    )
    return assistant.id, True


def print_last_assistant_message(client: OpenAI, thread_id: str) -> None:
    msgs = client.beta.threads.messages.list(thread_id=thread_id)
    for m in msgs.data:
        if m.role == "assistant":
            for c in m.content:
                if c.type == "text":
                    print(c.text.value)
            break


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", required=True, help="agents.yaml의 key (operations|marketing|admin 등)")
    parser.add_argument("--input", required=True, help="사용자 입력 메시지")
    parser.add_argument("--assistant-id", default=os.getenv("OPENAI_ASSISTANT_ID"), help="기존 assistant_id를 재사용하려면 지정")
    parser.add_argument("--model", default=os.getenv("OPENAI_MODEL", DEFAULT_MODEL), help="생성 모델 (기본: gpt-4.1-mini)")
    parser.add_argument("--mcp-url", default=os.getenv("MCP_SERVER_URL", DEFAULT_MCP_URL), help="MCP 서버 URL (기본: http://127.0.0.1:8000/mcp)")
    parser.add_argument("--tool-prefix", default=os.getenv("MCP_TOOL_PREFIX", DEFAULT_TOOL_PREFIX), help="Assistants API에서 노출할 MCP 툴 접두사")
    parser.add_argument("--keep-assistant", action="store_true", help="임시 assistant를 삭제하지 않고 보존")
    args = parser.parse_args()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY가 .env에 설정되어야 합니다.")

    instructions = build_instructions(args.agent)
    tools, tool_map = build_tool_config(args.tool_prefix)

    client = OpenAI()
    assistant_id, created = ensure_assistant(
        client,
        instructions=instructions,
        model=args.model,
        tools=tools,
        assistant_id=args.assistant_id,
    )

    bridge = MCPBridge(server_url=args.mcp_url, tool_map=tool_map)

    thread = client.beta.threads.create()
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=args.input,
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )

    try:
        while True:
            r = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            if r.status in ("completed", "failed", "cancelled", "expired"):
                break
            if (
                r.status == "requires_action"
                and r.required_action
                and r.required_action.submit_tool_outputs
            ):
                tool_calls = r.required_action.submit_tool_outputs.tool_calls
                submit_tool_outputs(client, thread.id, run.id, bridge, tool_calls)

        print_last_assistant_message(client, thread.id)
    finally:
        if created and not args.keep_assistant:
            try:
                client.beta.assistants.delete(assistant_id)
            except Exception:
                pass


if __name__ == "__main__":
    main()
