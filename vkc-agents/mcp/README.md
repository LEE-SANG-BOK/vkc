# VKC MCP 서버 (로컬 파일 검색)

기능
- search(query): 레포 내 텍스트 파일에서 질의어 검색
- fetch(id): 파일 경로(id)의 전문 반환

디렉토리 범위
- canon/, gpts/, ops/, prompts/

설치
- pip install fastmcp

실행
- HTTP 서버: fastmcp run vkc-agents/mcp/server.py:mcp --transport http --port 8000
- stdio(개발용): python vkc-agents/mcp/server.py

연결(Responses API 예시)
- tools: [{"type":"mcp", "server_label":"vkc", "server_url":"http://localhost:8000"}, {"type":"file_search"}, {"type":"code_interpreter"}]
- file_search는 기존 벡터스토어와 병행 사용 가능

주의
- PDF 텍스트 추출은 미구현. 필요 시 텍스트 변환 후 prompts/ 또는 ops/에 배치.
