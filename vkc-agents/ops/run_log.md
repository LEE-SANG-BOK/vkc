# VKC 운영 로그 (단일 문서)

본 문서는 모든 일정/결정/성과를 일자별로 누적 기록합니다. 매일 맨 위에 섹션을 추가하세요.

형식
- 날짜: ISO + 사용자 표기 병행
- 섹션: 목표/진행/산출물/의사결정/리스크/다음 액션/메모

---

## 2025-11-13 (Thu) · 사용자 표기: 26.11.13 목요일

목표
- Assistants API 기반 6개 에이전트 생성 및 지식 연결
- 초기 마케팅 실행 패키지(전략/템플릿/가이드) 정리

진행 요약
- 6개 Assistants 생성(file_search+code_inter프리터). canon 연결 완료, 슬라이드 미배치 상태
- 운영 산출물/가이드 추가: UTM, 설문, 숏폼 템플릿, 데일리 리포트, A/B 명세, VI 커뮤니티 문안, 브랜드 기준선, 7일 일정, 예산안, 랜딩 카피
- MCP 스켈레톤(search/fetch) 추가

세부 진행(추가)
- 랜딩 퍼블리시 스펙 작성: funnel/landing_spec.md
- Google Forms 문항 텍스트(KR/VI) 정리: funnel/forms_text_kr_vi.md
- 카드뉴스 카피(5장, E‑7 체크리스트): content/cardnews_E7_checklist_setA_kr_vi.md
- 숏폼 스크립트(T1, 30s, KR/VI): prompts/shorts_scripts/T1_E7_checklist_30s_kr_vi.md
 - 7일치 컨텐츠 팩(개요/Day1~7 자원): content/week1/content_pack.md
 - Day1 Publish Kit 구성: content/week1/day1_publish_kit.md
 - Day1 Figma 템플릿 가이드: content/week1/day1_figma_template.md
- 랜딩 히어로 HTML/CSS 스니펫: funnel/landing_hero_snippet.html
- Day1 퍼블리시 체크리스트: ops/publish_checklist_day1.md
 - Webflow 통합 가이드: funnel/webflow_integration.md
 - GA4 매핑: funnel/ga4_mapping.md
 - Forms 링크 플레이스홀더: funnel/forms_links.md
 - Day2 숏폼 스크립트(T2 D‑2): prompts/shorts_scripts/T2_D2_misconceptions_30s_kr_vi.md
- Day2 카드뉴스 카피: content/cardnews_D2_roadmap_setA_kr_vi.md
 - Day1 자막 SRT: content/week1/day1_subtitles_kr_vi.srt
 - Day1 카드뉴스 Canva CSV: content/week1/day1_cardnews_canva.csv
 - GA4 gtag 스니펫: funnel/ga4_gtag_snippet.html
 - Pixel 스니펫: funnel/pixel_snippet.html
- Day1 채널별 캡션: content/week1/day1_captions_kr_vi.md
 - MCP 원격 연결 가이드: ops/ngrok_mcp_guide.md
- Day2 Publish Kit: content/week1/day2_publish_kit.md
- Shorts 스크립트 추가: T3/T4/T5/T6 (prompts/shorts_scripts/*.md)
- 카드뉴스 카피 추가: 생활비/알바, F‑6, KIIP/TOPIK, 주거계약, Q/A (content/*.md)
- Day2 SRT/CSV/캡션/체크리스트 추가 (content/week1/day2_*)
- Day3 SRT/CSV/캡션/체크리스트 추가 (content/week1/day3_*)
- Day5 SRT/CSV/캡션/체크리스트 추가 (content/week1/day5_*)
- Day6 SRT/CSV/캡션/체크리스트 추가 (content/week1/day6_*)
- Day7 SRT/CSV/캡션/체크리스트 추가 (content/week1/day7_*)
 - Week2 D8~D14 SRT/CSV/캡션/체크리스트 생성 완료 (content/week2/*)
 - Week3 D16~D21 SRT/CSV/캡션/체크리스트 생성 완료 (content/week3/*)
- Week4 D22~D28 패키지 생성 진행: D22~D24 완료, D25~D28 완료 (content/week4/*)
- 콘텐츠 인덱스 추가: content/week1/index.md, content/week2/index.md, content/week3/index.md, content/week4/index.md
- 퍼블리시 가이드 추가: content/README.md
 - 업로드 스케줄 생성: content/upload_schedule.csv
 - 이벤트/UTM 검증 체크리스트 추가: ops/verify_events_checklist.md
 - Day별 폴더 재패키징: content/days/day01..day28/manifest.json 생성, days/README 추가
 - 정적 랜딩 배포 킷 추가: landing/README_STATIC_DEPLOY.md, landing/index.html

다음 액션(업데이트)
- 랜딩 빌더 반영(A/B, 태깅) 및 퍼블리시
- Google Forms 2종 실제 발행 및 링크/QR 생성
- FB 그룹 파일럿 2곳 게시(자유게시 그룹 우선), 슈퍼팬 후보 트래킹 시작
- Day1 자산 우선 제작·업로드, 성과 기반 Day2 훅/길이 조정
- MCP 서버(옵션) 실행 테스트: mcp/run_http.sh → Atlas/연결자 등록
- (웹) GA4 Measurement ID/Pixel ID 삽입 및 이벤트 파이어 검증
 - (웹) Google Forms 실링크 forms_links.md 입력 및 CTA 링크 교체
- (웹) Day1 퍼블리시 후 지표 확인 → Day2 변형 업로드
 - (웹) Day3~Day7는 Day1/2 성과 반영해 훅/길이/오디오 조정 후 업로드
 - (웹) Day별 체크리스트 파일 참조로 일괄 업로드/검증 수행
 - (로컬) Week3/Week4도 동일 포맷으로 사전 생성 예정
 - (로컬) Week2 D8~D14 자산 생성 완료 표기, Week3 D16~D21, Week4 D22~D28 일괄 생성
 - Day2 자산 준비(성능 데이터 반영) 및 캘린더 잠금

산출물(파일 경로)
- 전략: ops/launch_marketing_plan.md, ops/weekly_schedule_targets.md, ops/budget_100k_plan.md
- 퍼널/카피: funnel/landing_copy_kr_vi.md, funnel/surveys_google_forms.md, funnel/surveys_sampling.md
- 콘텐츠: prompts/shorts_sora2_templates.md, gpts/A1~A6_*.md
- 데이터/운영: ops/utm_schema.md, ops/daily_report_template.md
- 커뮤니티: community/templates_vi.md
- MCP: mcp/server.py, mcp/README.md

Assistants IDs
- A1: asst_cMM63TdZi0vIM5dRVHUoZolm
- A2: asst_2GrjJcDdmbrjLKPGW4GmCJp9
- A3: asst_p4RyS2klOxBvAGsij4etODUU
- A4: asst_2v9PRaUbeGAK2XPe7lAHJIze
- A5: asst_AVG8omfCoE04cV87krIuZ3qc
- A6: asst_xZ3onZe6ZoIqX8HgM87sTIAD

의사결정
- 현재 단계는 Assistants API 단일 경로로 운영. MCP/LangGraph는 후속 확장
- 비광고 중심 채널(페북 그룹·숏폼)과 오프라인 설문 병행
- 주간 A/B 3건 고정(G1 H1, G2 훅, G3 고정)
 - MCP 로컬 서버 가동 테스트 완료(HTTP :8000) → Atlas/연결자 연동 예정

리스크/이슈
- slides_vkc.pdf 미배치 → 벡터스토어 검색 정밀도 제한. 파일 수급 필요
- 루트 .env와 vkc-agents/.env 혼용 위험 → 키는 vkc-agents/.env로 통일 권장

다음 액션(내일)
- knowledge/slides_vkc.pdf 배치 후 재업로드 실행
- Google Forms 2종 발행(사전/온보딩) 및 쿼터 운영 시작
- 랜딩 H1/CTA A/B 반영 및 UTM 태깅 점검
- 쇼츠 2편+카드 1세트 제작/스케줄링, FB 그룹 고정 3곳 협의 개시
- 09:00 리포트 포맷으로 집계 리허설

메모
- 브랜드/신뢰 기준선: brand/brand_baseline.md 준수. 면책 고지 상시 노출
- 이벤트/UTM: ops/utm_schema.md 기준. 퍼널 손실 상위 지점은 일일 점검
