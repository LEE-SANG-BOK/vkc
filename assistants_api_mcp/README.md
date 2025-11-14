# Assistants API + MCP 스캐폴드

목표
- 코드로 재사용 가능한 에이전트(Assistants API)와 외부 도구(MCP 서버)를 연동합니다.
- 이 폴더는 VSCode에서 여는 현재 프로젝트에 포함되어 깃으로 버전관리할 수 있습니다.

구성
- app.py: Assistants API 실행 예제(기준선+에이전트 지시문 로딩)
- mcp_bridge.md: MCP 연동 방식 개요와 브리지 구현 포인트
- .env.example: 환경변수 예시(OPENAI_API_KEY 등)

사전 준비
1) Python 3.10+ 설치
2) 의존성 설치: `pip install -r assistants_api_mcp/requirements.txt`
3) .env 설정: `OPENAI_API_KEY=sk-...`
4) MCP 서버 실행: `bash vkc-agents/mcp/run_http.sh` (또는 별도 FastMCP 서버)

실행
1) 기준선/에이전트 지시문을 `vkc-agents`에서 편집합니다.
2) CLI 예시:
   ```bash
   python assistants_api_mcp/app.py \
     --agent operations \
     --input "이번주 작업 요약 리포트 만들어줘" \
     --mcp-url http://127.0.0.1:8000/mcp
   ```
   - `--model`, `--assistant-id`, `--tool-prefix`, `--keep-assistant` 옵션으로 세부 동작을 조정할 수 있습니다.

MCP 연동 개요
- MCP 서버(Figma, Google Sheets, Supabase 등)를 로컬/서버에 띄우고, `assistants_api_mcp/mcp_bridge.py`에서 해당 서버와 통신해 도구 호출을 처리합니다.
- 브리지는 Assistants API의 tool_call을 자동으로 MCP 서버에 위임하고, JSON 결과를 tool_output으로 다시 제출합니다.
- 툴 스키마는 기본적으로 `mcp_search`, `mcp_fetch` 두 가지이며 `--tool-prefix`로 접두사를 바꿀 수 있습니다.
- 상세 구조는 `assistants_api_mcp/mcp_bridge.md` 참고.
