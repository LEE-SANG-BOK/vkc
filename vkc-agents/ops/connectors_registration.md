# MCP 연결자 등록 가이드 (ChatGPT / Atlas)

전제
- 로컬 MCP 서버 실행 중: `bash vkc-agents/mcp/run_http.sh`
- 원격 접속 필요 시: `ngrok http 8000` → 발급 URL 뒤에 `/mcp` 붙여 사용
  - 예: `https://abcd-1234.ngrok-free.app/mcp`

ChatGPT(웹) 등록 절차
1) 우상단 프로필 → Settings → Developer(또는 Build) → Connectors
2) New Connector 클릭
3) Server label: `vkc`
4) Server URL: `http://127.0.0.1:8000/mcp` (같은 컴퓨터), 원격이면 ngrok URL + `/mcp`
5) Save → 대화창에서 tools에 `mcp(vkc)` 표시 확인
6) 간단 테스트: “mcp.search로 ‘E‑7’ 검색” → 로컬 문서 스니펫 반환 확인

Atlas 등록 절차(동일 개념)
1) Atlas 좌측/상단 메뉴에서 Connectors 패널 열기
2) Add Connector → Label `vkc` → URL `https://…/mcp`
3) Save → 에이전트/세션 생성 시 tools 목록에 mcp 추가

문제 해결 팁
- 404/502: 서버 미기동 또는 URL에 `/mcp` 누락
- 외부 접근 불가: ngrok 재시도, 방화벽/프록시 확인
- PDF 검색 품질: 벡터스토어(file_search)와 병행 사용 권장(Assistants에 이미 연결)
