# UTM & 이벤트 스키마 (VKC)

## 1) UTM 표준
- utm_source: fb | zalo | tt | yt | organic | referral
- utm_medium: post | reel | short | story | group | dm | email | linktree
- utm_campaign: d-7_prep | d-5_launch | d-day | ab_g1_h1 | ab_g2_hook | ab_g3_pin
- utm_content: h1_a | h1_b | cta_a | cta_b | hook_a | hook_b | badge_top | badge_bottom
- utm_term: 선택(해시태그/키워드)

규칙
- 캠페인은 주간 루프/테스트 단위로 부여 (예: ab_g1_h1)
- content는 A/B 변수 라벨 고정(h1_a/h1_b 등)
- 링크 예: https://site.example/?utm_source=fb&utm_medium=group&utm_campaign=d-5_launch&utm_content=h1_a

## 2) 이벤트 명세 (웹/랜딩)
- page_view: url, referrer, utm_*
- scroll_75: url, dwell_ms
- cta_click: url, cta_id, variant(h1_a|h1_b), utm_*
- signup: method(google|email), utm_*
- first_question: category(visa|job|study|housing), length_chars, utm_*
- first_answer: sla_hours
- adoption: answer_id, time_to_adopt_hours

권장 수집 필드
- session_id, user_id(익명화), device(mobile|desktop), locale(kr|vi)

## 3) 리포팅 매핑 (A6)
- 퍼널: 방문(page_view) → 가입(signup) → 첫 질문(first_question) → 첫 답변(first_answer) → 채택(adoption)
- KPI: CVR(signup/visit), CTR(cta_click/page_view), 체류(dwell_ms), 저장률(플랫폼 지표)

## 4) 데이터 보존/컴플라이언스
- PII 최소 수집, 목적 달성 즉시 파기 고지
- "경험 공유, 법률 자문 아님" 고지 일관 노출
