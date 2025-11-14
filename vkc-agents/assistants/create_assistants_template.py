#!/usr/bin/env python3
"""
Assistants API bootstrap script for VKC agents.

Prereqs:
- pip install openai>=1.40.0
- export OPENAI_API_KEY=... (Org/project scoping as needed)

What it does:
1) Uploads canon/PROJECT_CANON.md and knowledge/slides_vkc.pdf to a shared vector store
2) Creates 6 assistants (A1~A6) using instructions from gpts/*.md

Notes:
- Place actual PDFs under knowledge/. This script checks their existence.
- Adjust model name as desired (e.g., gpt-4o, gpt-4o-mini, o3-mini).
"""

import os
import sys
from pathlib import Path
from typing import List

try:
    from openai import OpenAI
except ImportError:
    print("Error: openai package is not installed. Run: pip install openai")
    sys.exit(1)


ROOT = Path(__file__).resolve().parents[1]

# Optional: load .env if present (vkc-agents/.env)
try:
    from dotenv import load_dotenv  # type: ignore
    # Prefer project-local .env
    env_path = ROOT / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=str(env_path))
    # Fallback: repository root .env (one level up) if present
    repo_env = (ROOT.parent / ".env")
    if repo_env.exists():
        load_dotenv(dotenv_path=str(repo_env))
except Exception:
    # Safe to ignore; fallback to system environment
    pass
CANON_PATH = ROOT / "canon" / "PROJECT_CANON.md"
KNOWLEDGE_DIR = ROOT / "knowledge"
SLIDES_PATH = KNOWLEDGE_DIR / "slides_vkc.pdf"


def get_api_key() -> str:
    """Return OPENAI_API_KEY, falling back to API_KEY if present."""
    val = os.environ.get("OPENAI_API_KEY") or os.environ.get("API_KEY")
    if not val:
        print("Error: environment variable OPENAI_API_KEY is not set.")
        print("Hint: set OPENAI_API_KEY in vkc-agents/.env or root .env.")
        return ""
    return val


def assert_exists(path: Path, label: str):
    if not path.exists():
        print(f"Error: required {label} not found at: {path}")
        if label == "slides PDF":
            print("Hint: place your presentation PDF at 'knowledge/slides_vkc.pdf'")
        sys.exit(1)


def open_streams(paths: List[Path]):
    streams = []
    for p in paths:
        streams.append(open(p, "rb"))
    return streams


def main():
    api_key = get_api_key()
    if not api_key:
        sys.exit(1)
    client = OpenAI(api_key=api_key)  # Project/org scope via env if configured

    # Validate required files
    assert_exists(CANON_PATH, "canon file")
    slides_present = SLIDES_PATH.exists()
    if not slides_present:
        print(f"Warning: slides PDF not found at {SLIDES_PATH}. Proceeding with canon only.")

    # Resolve vector stores API surface across SDK versions
    vs_module = None
    if hasattr(client, "beta") and hasattr(client.beta, "vector_stores"):
        vs_module = client.beta.vector_stores
    elif hasattr(client, "vector_stores"):
        vs_module = client.vector_stores
    else:
        print("Error: vector_stores API not found in this OpenAI SDK version.")
        sys.exit(1)

    print("Creating shared vector store and uploading knowledge files…")
    vs = vs_module.create(name="VKC-Knowledge")

    files = [CANON_PATH]
    if slides_present:
        files.append(SLIDES_PATH)
    file_streams = open_streams(files)
    try:
        # file_batches is available under the vector_stores module
        vs_module.file_batches.upload_and_poll(
            vector_store_id=vs.id,
            files=file_streams,
        )
    finally:
        for fs in file_streams:
            fs.close()

    # Common tools across assistants
    common_tools = [
        {"type": "file_search"},
        {"type": "code_interpreter"},
    ]
    tool_resources = {"file_search": {"vector_store_ids": [vs.id]}}

    # Assistant files mapping
    a_defs = [
        ("A1", "A1_research.md"),
        ("A2", "A2_prioritization.md"),
        ("A3", "A3_funnel.md"),
        ("A4", "A4_content.md"),
        ("A5", "A5_community.md"),
        ("A6", "A6_analytics.md"),
    ]

    # Resolve assistants API surface across SDK versions
    assistants_module = None
    if hasattr(client, "beta") and hasattr(client.beta, "assistants"):
        assistants_module = client.beta.assistants
    elif hasattr(client, "assistants"):
        assistants_module = client.assistants
    else:
        print("Error: assistants API not found in this OpenAI SDK version.")
        sys.exit(1)

    print("Creating assistants…")
    for key, filename in a_defs:
        path = ROOT / "gpts" / filename
        if not path.exists():
            print(f"Warning: missing instructions file {path}. Skipping {key}.")
            continue
        instructions = path.read_text(encoding="utf-8")
        assistant = assistants_module.create(
            name=f"VKC {key}",
            model="gpt-4o-mini",
            instructions=instructions,
            tools=common_tools,
            tool_resources=tool_resources,
        )
        print(f"{key} Assistant ID: {assistant.id}")

    print("Done.")


if __name__ == "__main__":
    main()
