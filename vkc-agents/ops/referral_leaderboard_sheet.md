제목: 리더보드 집계 시트 템플릿(스키마/수식)

입력 시트(columns)
- timestamp, form_name, action_type(pre|onb|question|answer|accepted|bookmark|follow), ref, ga_cid, utm_source, utm_medium, utm_campaign, utm_content, variant, referrer

전처리
- 유효초대: ref로 그룹핑 → pre>=1 AND (onb OR question OR answer OR bookmark OR follow)>=1 → unique user 수
- 활동일: ga_cid+date 기준 하루 1점 처리

점수 시트(예시 수식)
- 초대점수: =MIN(40, 유효초대)
- 채택점수: =MIN(5, 채택수)*6 + MIN(10, (답변수-채택수))*1
- 출석점수: =MIN(15, 활동일수)
- 질문점수: =MIN(5, 질문수)*2
- 북/팔점수: =MIN(10, 북마크수+팔로우수)*0.5
- 총점: =SUM(각 점수)

리더보드
- 정렬: 총점 DESC → 채택수 DESC → 유효초대 DESC → 최초 timestamp ASC
- 공개: 상위 20명 닉네임/총점/유효초대/채택/활동일

운영 팁
- Netlify Forms CSV는 일 1회 export → ‘raw’ 시트에 붙여넣기
- 스크립트 없이 수식으로 운영 후, 필요 시 Apps Script로 자동화
