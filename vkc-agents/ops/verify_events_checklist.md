# Verify Events & UTM Checklist (Webflow)

Before publish
- Replace GA4 Measurement ID in funnel/ga4_gtag_snippet.html
- Replace Pixel ID in funnel/pixel_snippet.html
- Set CTA data-target-a/b in landing_hero_snippet.html to Forms URLs (forms_links.md)

After publish (test both variants)
- Open LP with ?variant=h1_a | ?variant=h1_b
- Check GA4 DebugView for events:
  - page_view_custom (url, utm_*, variant)
  - scroll_75 (detail.variant)
  - cta_click (id=hero_primary, variant, utm_*)
- Click CTA → Forms page loads with utm_* and variant preserved
- Pixel Chrome helper (if installed): PageView fires on LP, Lead on CTA

Troubleshooting
- No events: ensure snippet is in Head and no CSP blocks
- No UTM on Forms: landing_hero_snippet appendQuery() must keep current query params
- Variant not toggling: ensure Embed script not minified/removal by builder, or force via query
