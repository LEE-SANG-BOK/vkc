# MCP 연동 브리지 개요

역할
- Assistants API에서 발생한 도구 호출(require_action → tool_calls)을 MCP 서버에 위임하고, 결과를 다시 Assistants API에 제출합니다.

구성 아이디어
1) `assistants_api_mcp/mcp_bridge.py`에서 MCP 클라이언트를 초기화하고 Streamable HTTP로 서버에 접속합니다.
2) tool_calls 루프: 각 호출의 name/parameters를 파싱해 대응되는 MCP 명령으로 변환합니다 (`mcp_search`→`search`, `mcp_fetch`→`fetch`).
3) 결과 제출: Assistants API의 run step에 tool_output 형태로 제출합니다.

설정
- 각 MCP 서버별 자격증명은 .env 또는 OS 키체인에 보관하고 최소권한으로 발급합니다.
- 네임스페이스 충돌을 피하기 위해 도구명 접두사(예: figma.*, sheets.*, supabase.*)를 일관되게 사용합니다.

구현 포인트
- `assistants_api_mcp/app.py`의 requires_action 분기가 `MCPBridge`를 호출하도록 연결되어 있습니다.
- 장기적으로는 고정 assistant_id를 생성하거나 `--assistant-id`로 재사용하면서 tools 스키마를 assistant에 등록해 자동 검증을 활용합니다.

테스트
- 각 MCP 명령에 대해 단위 테스트를 추가하고, 샌드박스 워크스페이스(예: 테스트용 스프레드시트/프로젝트)로 검증하세요.
