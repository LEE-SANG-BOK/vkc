# Static Landing (Netlify / GitHub Pages)

이 폴더에는 정적 호스팅(예: Netlify, GitHub Pages)로 즉시 배포 가능한 랜딩 페이지 템플릿이 포함되어 있습니다. A/B(variant), UTM 전파, GA4/Pixel 이벤트(page_view_custom/scroll_75/cta_click) 전송을 지원합니다.

## 파일 구성
- `index.html`: 배포용 단일 파일(헤더 스니펫/히어로/이벤트 바인딩 포함)
- (선택) 정적 자산이 있으면 같은 폴더에 추가

## 사전 준비
1) Google Forms 2종 생성(사전/온보딩)
   - 문항 템플릿: `vkc-agents/funnel/forms_text_kr_vi.md`
   - 생성 링크는 추후 `index.html`의 `data-target-a/b`에 입력
2) 추적 ID 준비(선택)
   - GA4 Measurement ID: `G-XXXXXXXX` → 실제 ID로 교체
   - Meta Pixel ID: `PIXEL_ID` → 실제 ID로 교체

## Netlify(권장) Git 연동 배포

0) 사전 준비
- 이 저장소를 GitHub에 푸시(예: `vietkconnect-landing`).
- 루트 `netlify.toml`의 `publish = "vkc-agents/landing"`가 설정되어 있습니다.

1) Netlify → Add new site → Import from Git → GitHub 연결
- 리포지토리 선택 → Build command 비워두기 → Publish directory 자동 인식(`netlify.toml`).

2) 환경/스니펫 교체(선택)
- GA4 Measurement ID: `vkc-agents/landing/index.html`의 `G-XXXXXXXX` 교체
- Meta Pixel ID: 동일 파일의 `PIXEL_ID` 교체(선택)

3) 폼 링크 교체(필수)
- `vkc-agents/landing/index.html`의 `data-target-a/b`를 Google Forms 실링크로 교체
- 참고: `vkc-agents/funnel/forms_links.md`

4) 배포 후 검증(3분)
- H1 A/B 강제: `?variant=h1_a|h1_b`
- UTM/variant 전파: CTA 클릭 후 Forms URL에 그대로 유지되는지 확인
- 이벤트: GA4 DebugView에서 `page_view_custom`/`scroll_75`/`cta_click` 확인

## Netlify 수동 배포(드래그&드롭)
1) Netlify 계정 생성/로그인 → 대시보드 `Add new site` → `Deploy manually`
2) 이 폴더(`index.html`)를 드래그&드롭 업로드
3) 배포 URL 생성(예: `https://your-site.netlify.app`)
4) 검증: 아래 체크리스트 참고

## GitHub Pages 배포(대안)
1) GitHub 저장소 생성 → `index.html` 푸시
2) Repository `Settings` → `Pages` → `Branch: main`/`root` 지정 → 활성화
3) 배포 URL 생성(예: `https://username.github.io/repo`)
4) 검증: 아래 체크리스트 참고

## 설정 포인트(필수)
- `index.html` 내 TODO
  - `G-XXXXXXXX` → 실제 GA4 ID로 교체(없으면 유지 가능)
  - `PIXEL_ID` → 실제 Pixel ID로 교체(없으면 유지 가능)
  - CTA 링크: `data-target-a`/`data-target-b`에 각각 Google Forms URL 입력

## 퍼블리시 후 검증 체크리스트
- URL에 `?variant=h1_a` / `?variant=h1_b`를 붙였을 때 헤드라인이 토글되는가
- GA4 DebugView에서 이벤트 수집
  - `page_view_custom`(url, utm, variant)
  - `scroll_75`
  - `cta_click`(id, variant, utm)
- CTA 클릭 시 Forms로 이동하며 utm_* 및 variant가 보존되는가
- Meta Pixel Helper(설치 시)에서 PageView/Lead 이벤트 확인

## 참고
- 랜딩 카피/섹션 구조: `vkc-agents/funnel/landing_copy_kr_vi.md`
- UTM/이벤트 표준: `vkc-agents/ops/utm_schema.md`
- 검증 체크리스트(상세): `vkc-agents/ops/verify_events_checklist.md`

## 공유/프리뷰(OG/Twitter)
- 권장 이미지: `og-image-1200x630.png` (1200×630, 1:1.91)
- 임시로 `og-template.svg`를 제공하거나, PNG를 동일 경로에 업로드해 교체하세요.

## 리퍼럴/리더보드 연결
- 초대 링크: 랜딩 상단의 “내 초대링크”에서 자동 생성(ref 코드)
- 히든 필드: `ref`, `ga_cid`가 폼에 자동 주입되어 CSV로 수집됩니다.
- 리더보드: Google Sheets를 ‘웹에 게시(CSV)’로 공개 → `<meta name="leaderboard-url" content="https://...csv">`로 설정
  - JSON을 직접 배포해도 됩니다(`/leaderboard.json`). 샘플: `vkc-agents/landing/leaderboard_sample.json`
  - 컬럼 예시: user,score,invites,accepted,days

## Netlify Forms(내장 설문) 사용 안내
- 이 템플릿에는 Netlify Forms 2종이 포함되어 있습니다.
  - `pre_survey` (사전 12문) — 섹션 id `#pre_survey`
  - `onboarding_survey` (온보딩 5문) — 섹션 id `#onboarding_survey`
- CTA는 각각 `#pre_survey`/`#onboarding_survey`로 이동하며, 제출 시 Netlify Submissions에 저장됩니다.
- 숨김 필드로 `utm_*`/`variant`/`referrer`가 자동 주입됩니다.
- 제출 데이터: Netlify Dashboard → Site → Forms → Submissions에서 확인
