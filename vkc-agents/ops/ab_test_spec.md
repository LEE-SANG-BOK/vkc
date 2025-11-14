# A/B 테스트 명세서 템플릿 (주간 3건 고정)

목표: 한 주에 3건만 승인. 표본/기간/성공기준 사전 고정.

## 공통 메타
- 기간: YYYY-MM-DD ~ YYYY-MM-DD (7일)
- 세그먼트: 신규 방문자(utm_campaign=...)
- 측정: GA/픽셀 + 스프레드시트 집계 (ops/utm_schema.md 기준)

## G1. 랜딩 H1
- 가설: “검증된 선경험자”가 “관리자 인증”보다 CVR을 높인다
- 변수: H1_a(검증된 선경험자) vs H1_b(관리자 인증)
- 노출: 50/50 스플릿
- 표본: 방문 N≥X, 유의 기준 e.g. 95% (가이드)
- 성공: CVR(H1_a) ≥ CVR(H1_b) + 20%p 또는 절대 CVR ≥ 18%
- UTM: utm_campaign=ab_g1_h1, utm_content=h1_a|h1_b
- 리스크/메모: 체류≥35s 동시 달성 권장

## G2. 쇼츠 훅
- 가설: 페르소나 고통 직격 훅이 밈형 훅보다 3초 이탈률이 낮다
- 변수: hook_a(고통 직격) vs hook_b(밈/유행)
- 표본: 조회 N≥X, 완시율·3초 이탈률 비교
- 성공: 3초 이탈률 hook_a < hook_b 또는 VTR hook_a > hook_b
- 배포: TikTok/Shorts/Facebook Reels, 동일 본문 유지, 훅만 변경
- UTM: utm_campaign=ab_g2_hook, utm_content=hook_a|hook_b

## G3. FB 그룹 고정
- 가설: 고정 게시가 일반 게시 대비 CTR 1.8% 이상
- 변수: pinned vs normal
- 표본: 노출 N≥X, CTR 계산(클릭/노출)
- 성공: CTR pinned ≥ 1.8% 및 pinned > normal
- UTM: utm_campaign=ab_g3_pin, utm_content=pinned|normal

## 운영 체크리스트
- [ ] 링크 UTM 적용(ops/utm_schema.md)
- [ ] 이벤트 태깅(page_view/cta_click/signup)
- [ ] 테스트 카드 생성(A2 산출물)
- [ ] 결과 집계 시트/대시보드 연결
- [ ] 리포트: ops/daily_report_template.md 양식 포함
