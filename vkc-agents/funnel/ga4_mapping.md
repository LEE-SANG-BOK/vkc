# GA4 이벤트/파라미터 매핑

이벤트
- page_view_custom
  - params: url, referrer, variant, utm: {source, medium, campaign, content}
- scroll_75
  - params: url, dwell_ms(선택), variant
- cta_click
  - params: id(hero_primary 등), variant, utm: {source, medium, campaign, content}
- signup (폼 완료 후 트리거)
  - params: method(google|email|form), variant, utm_*

권장 디멘션
- variant (A/B), utm_source/medium/campaign/content, locale(kr|vi)

보고서 뷰
- 퍼널(방문→가입→첫 질문→첫 답변→채택)
- 채널/캠페인별 CVR/CTR/체류, 테스트 세그먼트(G1/G2/G3)
