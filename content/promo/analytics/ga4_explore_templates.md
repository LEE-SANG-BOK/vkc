제목: GA4 Explore 템플릿(이벤트 기반 퍼널)

세그먼트
- by_variant: event parameter variant = h1_a / h1_b
- by_source: utm_source = tt/ig/yt/fb

퍼널(4단계)
1) page_view_custom
2) scroll_75
3) cta_click (id=hero_primary or ref_copy)
4) sign_up (params: form=pre_survey|onboarding_survey)

지표
- 각 단계 전환율, 평균 소요시간, 유입별 전환(variant×source 교차)

세이브뷰
- “launch_top5_funnel_v1” 보드 생성 → 일단위 필터, 비교: variant
