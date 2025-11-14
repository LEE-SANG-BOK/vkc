# Webflow 통합 가이드 (A/B + 태깅)

목표
- landing_hero_snippet.html를 Webflow 섹션에 임베드하여 A/B(variant) 및 이벤트 태깅 대응

1) 구조
- Webflow Designer에서 Hero 섹션에 Embed 컴포넌트 추가
- vkc-agents/funnel/landing_hero_snippet.html의 내용 전체를 붙여넣기
- CTA 버튼의 클릭 시 이동할 URL(가입/설문 링크)을 프로젝트에 맞게 수정

2) A/B 분기
- 기본은 클라이언트 랜덤 50/50 (query `?variant=h1_a|h1_b` 강제 가능)
- 서버/스플릿 테스트를 쓸 경우, 페이지 진입 시 쿼리 파라미터로 variant를 전달하도록 설정

3) GA4 태깅(예시)
- Webflow 프로젝트 설정 → Custom Code → Head에 GA4 gtag 스니펫 삽입
- 아래 커스텀 이벤트를 window 이벤트 리스너로 수집

```html
<script>
window.addEventListener('page_view', (e) => {
  const p = e.detail || {}; gtag('event', 'page_view_custom', p);
});
window.addEventListener('scroll_75', (e) => {
  const p = e.detail || {}; gtag('event', 'scroll_75', p);
});
window.addEventListener('cta_click', (e) => {
  const p = e.detail || {}; gtag('event', 'cta_click', p);
});
</script>
```

4) Meta Pixel(선택)
- Pixel 코드 설치 후 `cta_click` 시 `Lead`(또는 `CompleteRegistration`)를 트리거

```html
<script>
window.addEventListener('cta_click', (e) => {
  fbq('track', 'Lead', e.detail || {});
});
</script>
```

5) UTM/설문 연동
- CTA 클릭 시 이동 URL에 현재 쿼리의 utm_* 및 variant를 그대로 전달
- 설문 링크는 vkc-agents/funnel/forms_links.md에 관리 (실링크 입력)

6) 접근성/성능
- LCP<2.5s 목표(이미지 최적화, WebP), 모바일 폰트 16px 이상, 대비 준수

체크리스트
- [ ] Embed 반영 및 CTA 링크 갱신
- [ ] gtag/Pixel 정상 수집 확인(디버거)
- [ ] variant 표시/전달, utm_* 전파 확인
- [ ] 폰트/색상/배지/면책 노출 검수
