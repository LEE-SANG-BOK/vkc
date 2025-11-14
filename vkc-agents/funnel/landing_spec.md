# 랜딩 퍼블리시 스펙 (A/B + 태깅)

목표
- LP CVR ≥ 18%, 평균 체류 35s+, A/B 3건 중 G1(H1) 검증

A/B 카피(한·베는 landing_copy_kr_vi.md 참조)
- Variant A (h1_a)
  - H1: 검증된 선경험자의 답변
  - H2: 관리자 인증을 거친 실제 경험만 모았습니다
  - CTA: 10초 만에 시작하기
  - 신뢰요소: 인증 배지(상단), 채택 사례 2, 면책
- Variant B (h1_b)
  - H1: 관리자 인증 답변을 바로 받으세요
  - H2: 익명이 아닌, 증빙으로 검증된 답변만
  - CTA: 첫 질문 남기고 답변 받기
  - 신뢰요소: 하단 배치

섹션 구조
- 히어로(H1/H2/CTA/배지)
- 문제 제기(익명 정보 한계)
- 해결 방식(경험 인증 → 증빙 확인 → 검증 답변, 24h SLA)
- 페르소나 카드(E‑7‑4/D‑2/F‑6/현지 취업 TOP3)
- FAQ 6(익명/증빙/오류/답변 SLA/채택/면책)

추적/태깅(ops/utm_schema.md 준수)
- 파라미터: utm_source / utm_medium / utm_campaign / utm_content
  - 캠페인: d-5_launch, ab_g1_h1 등
  - 콘텐츠: h1_a | h1_b
- 이벤트(데이터 계층)
  - page_view: url, referrer, utm_*
  - scroll_75: url, dwell_ms
  - cta_click: url, cta_id(‘hero_primary’ 등), variant(h1_a|h1_b), utm_*
  - signup: method(google|email), utm_*

구현 체크리스트
- A/B 분기: 50/50 노출(서버/클라이언트 무관, 변이 표시 variant)
- GA4: page_view, scroll, click, signup 커스텀 이벤트/파라미터 매핑
- Meta Pixel: ViewContent, Lead(or CompleteRegistration) 매핑
- 성능: LCP<2.5s, 모바일 가독 16px+, 대비 준수
- KR/VI 토글 또는 동시 표시(문구 동등성 유지)

출시 전 점검
- 링크 UTM 적용, 이벤트 파이어 확인(개발자 도구/디버거)
- A/B 노출 비율, variant 전달 여부, 전환 퍼널 테스트(가입/첫 질문 플로우)
- 면책/개인정보 고지 노출
