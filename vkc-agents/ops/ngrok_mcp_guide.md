# MCP 원격 연결 가이드(ngrok)

목표
- 로컬 MCP 서버(http://127.0.0.1:8000/mcp)를 외부에서 접근 가능하도록 터널링

사전 준비
- MCP 서버 실행: `bash vkc-agents/mcp/run_http.sh`
- ngrok 설치: macOS `brew install ngrok` 또는 https://ngrok.com/download
- ngrok 로그인: `ngrok config add-authtoken <YOUR_TOKEN>`

실행
- `ngrok http 8000`
- 출력되는 Forwarding URL 예: `https://abcd-1234.ngrok-free.app`
- MCP 서버 URL은 `/mcp` 경로 포함: `https://abcd-1234.ngrok-free.app/mcp`

Atlas/ChatGPT 연결자 등록
- 연결자 추가 → 서버 라벨(vkc), 서버 URL에 위 ngrok URL 입력
- 보안: 공개 중에는 민감 파일 제외를 권장(현재 서버는 텍스트/PDF만 읽기)

종료/주의
- ngrok 세션은 터미널 종료 시 중지됩니다. 상시 운영 시 유료 플랜/고정 도메인 고려
