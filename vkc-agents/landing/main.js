document.addEventListener('DOMContentLoaded', () => {
  const translations = {
    ko: {
      nav_services: '서비스',
      nav_content: '콘텐츠',
      nav_success: '성공 사례',
      nav_why: '왜 VietKConnect?',
      nav_consultation: '상담 예약',
      nav_cards: '실행 카드(베타)',
      hero_badge: '베트남 인증 Q&A · AI 자동화',
      hero_title: '비자 · 생활 · 커리어 — 24시간 안에 인증된 답변',
      hero_subtitle: '행정사·시니어 멘토·AI 도구가 협업해 D‑10→E‑7→F‑2·F‑5까지 한 번에 연결합니다.',
      hero_cta: '웹사이트 열기',
      hero_secondary: '실행 카드 보기',
      stat1_title: '관리자·행정사 검수',
      stat1_desc: '24h 응답 SLA + 사례 검증',
      stat2_title: 'AI 문서 자동화',
      stat2_desc: '고용사유서/진정서/반성문 템플릿',
      stat3_title: '실시간 정책 피드',
      stat3_desc: '출입국 예약 · TOPIK · 지역특화 업데이트',
      services_title: 'We Solve the Whole Journey',
      services_subtitle: '비자 전환, 생활 리스크, 커리어 연결까지 한 화면에서 확인하세요.',
      service1_title: 'D‑10→E‑7→F‑2/F‑5 로드맵',
      service1_desc: '12주 타임라인, 서류 체크, 인터뷰 대비를 동시에 제공.',
      service2_title: '실시간 출입국 · 예약 배너',
      service2_desc: '하이코리아 업데이트를 자동 수집해 대기 시간을 줄입니다.',
      service3_title: '문서 · 반성문 자동 생성',
      service3_desc: '고용사유서, 진정서, 알바 신고서 등을 AI가 초안으로 제작.',
      service4_title: 'AI 챗봇 & 전문가 Q/A',
      service4_desc: '1345 FAQ + 검증 멘토 답변으로 24시간 대응.',
      policy_title: '최신 정책 브리핑',
      policy_subtitle: '출입국 공지·대학 안내·행정사 자료를 통합 요약해 바로 실행할 수 있게 정리합니다.',
      policy_card1_pill: 'D‑2 → D‑10 → E‑7 흐름',
      policy_card1_title: '체류 단계 요약',
      policy_card1_li1: 'D‑2 재학 중에는 교외 아르바이트 전 <strong>S‑3 허가</strong> 필수.',
      policy_card1_li2: '졸업/졸업예정 후 D‑10(구직) 전환, 2025‑10‑29부터 최대 3년 연장.',
      policy_card1_li3: '정규직 오퍼 확인 후 E‑7 변경, 직무 적합성과 임금 요건 체크.',
      policy_card1_hint: '출처: 대학 국제처, HiKorea, KOWORK, 행정사 가이드',
      policy_card2_pill: 'E‑7 임금 고시(2025)',
      policy_card2_title: '고정 연봉 2,867만원+',
      policy_card2_li1: '2025‑04‑01~12‑31: 직종별 <strong>고정 연봉 기준</strong> 적용.',
      policy_card2_li2: '총보수 산식(기본급+수당+상여)을 계약서에 명시.',
      policy_card2_li3: '별도 고시 직종/국민고용비율/세금 체납 여부도 함께 검토.',
      policy_card2_hint: '법무부 공고 제2025‑106호 · KOWORK · 행정사 자료',
      policy_card3_pill: '서류 & 컴플라이언스',
      policy_card3_title: '체류·근로 서류 팁',
      policy_card3_li1: 'D‑10 전환: 졸업(예정)증명, 체류지(임대차), 체재비 증빙 준비.',
      policy_card3_li2: 'E‑7 신청: 학력/경력 매칭 표, 고용계약서 임금 요건 충족 여부 확인.',
      policy_card3_li3: '최근 위반/과태료 여부, 근로계약서 필수 조항, 임금명세 보관.',
      policy_card3_hint: 'JB행정사, Ajou Univ., eLaw, HiKorea 가이드',
      content_title: '콘텐츠 & 실행 카드',
      content_subtitle: '숏폼·카드뉴스·실행 카드가 매일 최신 정책과 연동됩니다.',
      content_card1_pill: '오늘의 실행 카드',
      content_card1_title: 'Top5 체크리스트',
      content_card1_desc: '비자/근무/시험/생활/지역 매칭을 클릭형 카드로 정리.',
      content_card1_link: '바로 체험하기',
      content_card2_pill: '정책 피드',
      content_card2_title: '출입국 & 시험 변화',
      content_card2_desc: 'D‑10 연장, 25h 외활허가, TOPIK 일정 등을 실시간 배너로 제공.',
      content_card2_hint: '하이코리아, TOPIK, 지역특화 공고 자동 크롤링',
      content_card3_pill: '문서 라이브러리',
      content_card3_title: '사례 기반 템플릿',
      content_card3_desc: '증빙 파일/업데이트 내역을 함께 고지해 검증 가능성을 높입니다.',
      content_card3_hint: 'AI 초안 → 관리자 검수 → 사용자 배포',
      success_title: '실제 사용자 이야기',
      success_subtitle: 'VietKConnect를 통해 비자 전환 · 채용 · 정착을 이룬 사례.',
      story1_role: 'D‑2 → D‑10 → E‑7',
      story1_content: '“12주 로드맵과 고용사유서 템플릿 덕분에 회계 직무 오퍼를 지연 없이 승인받았어요.”',
      story2_role: 'F‑2‑R 지역특화',
      story2_content: '“부산·경남 기업 매칭 카드와 인터뷰 체크리스트로 지역특화 거주비자를 통과했습니다.”',
      story3_role: '알바 신고 & 주거',
      story3_content: '“AI 반성문/신고서 자동작성으로 사기 피해를 빠르게 해소하고 주거 계약을 지켰어요.”',
      success_cta: 'VietKConnect 후기 더보기',
      why_title: '왜 VietKConnect인가요?',
      feature1_title: '검증된 신뢰',
      feature1_desc: '행정사·시니어 멘토·운영진이 모든 답변을 검수합니다.',
      feature2_title: '옴니채널',
      feature2_desc: 'Facebook, TikTok, Email, Zalo, AMA가 동일 메시지로 연동됩니다.',
      feature3_title: 'AI + 사람 협업',
      feature3_desc: 'AI가 초안을 만들고 전문가가 보완해 속도와 정확도를 동시에 달성.',
      consult_title: 'VietKConnect 웹사이트',
      consult_desc: '정식 웹사이트(대시보드/실행 카드/커뮤니티)로 이동해 더 많은 기능을 체험하세요. 현재 베타 접속 링크는 곧 공개 예정입니다.',
      site_placeholder_text: '정식 웹사이트 URL이 등록되면 아래 버튼을 통해 바로 이동할 수 있습니다.',
      site_placeholder_cta: '웹사이트 열기',
      footer_text: '© VietKConnect. All rights reserved.',
      footer_cards: '실행 카드(설문) 버전 보기'
    },
    vi: {
      nav_services: 'Dịch vụ',
      nav_content: 'Nội dung',
      nav_success: 'Câu chuyện thành công',
      nav_why: 'Vì sao VietKConnect?',
      nav_consultation: 'Đặt lịch tư vấn',
      nav_cards: 'Thẻ hành động (Beta)',
      hero_badge: 'Q&A kiểm chứng · Tự động hóa AI',
      hero_title: 'Visa · Cuộc sống · Sự nghiệp — Nhận câu trả lời trong 24h',
      hero_subtitle: 'Chuyên gia hành chính + mentor + AI phối hợp giúp bạn đi từ D‑10→E‑7→F‑2/F‑5.',
      hero_cta: 'Mở website',
      hero_secondary: 'Xem thẻ hành động',
      stat1_title: 'Kiểm duyệt bởi chuyên gia',
      stat1_desc: 'Trả lời trong 24h kèm ví dụ đã xác thực',
      stat2_title: 'Tự động hóa hồ sơ',
      stat2_desc: 'Mẫu lý do tuyển dụng, đơn kiến nghị, báo cáo làm thêm',
      stat3_title: 'Bản tin chính sách',
      stat3_desc: 'Đặt lịch HiKorea · TOPIK · visa đặc thù vùng',
      services_title: 'Giải pháp toàn hành trình',
      services_subtitle: 'Lộ trình visa, rủi ro đời sống, kết nối nghề nghiệp trên cùng một trang.',
      service1_title: 'Lộ trình D‑10→E‑7→F‑2/F‑5',
      service1_desc: 'Theo dõi 12 tuần, checklist hồ sơ, chuẩn bị phỏng vấn.',
      service2_title: 'Banner lịch HiKorea realtime',
      service2_desc: 'Tự động lấy slot để bạn đặt lịch nhanh hơn.',
      service3_title: 'Tạo hồ sơ tự động',
      service3_desc: 'AI soạn thảo lý do tuyển dụng/đơn tường trình rồi chuyên gia rà soát.',
      service4_title: 'AI Chatbot & Q/A chuyên gia',
      service4_desc: 'Kế thừa 1345 + mentor để trả lời 24/7.',
      policy_title: 'Bản tin chính sách mới nhất',
      policy_subtitle: 'HiKorea, thông báo trường, dữ liệu hành chính được tóm gọn để bạn hành động ngay.',
      policy_card1_pill: 'Lộ trình D‑2 → D‑10 → E‑7',
      policy_card1_title: 'Tóm tắt giai đoạn',
      policy_card1_li1: 'Khi còn D‑2, phải xin <strong>S‑3</strong> trước khi làm thêm.',
      policy_card1_li2: 'Sau tốt nghiệp chuyển D‑10, từ 29/10/2025 được gia hạn tối đa 3 năm.',
      policy_card1_li3: 'Khi có offer full-time thì chuyển E‑7 và kiểm tra mức lương/đúng ngành.',
      policy_card1_hint: 'Nguồn: trường ĐHQG, HiKorea, KOWORK, tài liệu hành chính',
      policy_card2_pill: 'Thông báo lương E‑7 (2025)',
      policy_card2_title: 'Tối thiểu 28.67 triệu KRW/năm',
      policy_card2_li1: '04/2025~12/2025 áp dụng mức lương cố định theo nghề.',
      policy_card2_li2: 'Hợp đồng phải ghi rõ tổng thù lao (lương cơ bản + phụ cấp + thưởng).',
      policy_card2_li3: 'Kiểm tra ngành có bị áp quy chuẩn riêng, tỉ lệ tuyển dụng người Hàn, thuế.',
      policy_card2_hint: 'Bộ Tư pháp 2025-106, KOWORK, văn phòng hành chính',
      policy_card3_pill: 'Hồ sơ & compliance',
      policy_card3_title: 'Checklist giấy tờ',
      policy_card3_li1: 'Chuyển D‑10: chuẩn bị bằng/giấy tốt nghiệp, hợp đồng thuê nhà, tiền sinh hoạt.',
      policy_card3_li2: 'Xin E‑7: bảng khớp ngành học/kinh nghiệm, hợp đồng đúng mức lương.',
      policy_card3_li3: 'Kiểm tra vi phạm 3 năm gần nhất, hợp đồng lao động, sao kê lương.',
      policy_card3_hint: 'JB 행정사, Ajou, eLaw, HiKorea',
      content_title: 'Nội dung & thẻ hành động',
      content_subtitle: 'Short-form, cardnews và thẻ hành động cập nhật hằng ngày.',
      content_card1_pill: 'Thẻ hành động',
      content_card1_title: 'Top5 checklist',
      content_card1_desc: 'Visa/Làm thêm/Kỳ thi/Cuộc sống/Khu vực được gom thành thẻ chọn.',
      content_card1_link: 'Trải nghiệm ngay',
      content_card2_pill: 'Bản tin chính sách',
      content_card2_title: 'HiKorea & TOPIK',
      content_card2_desc: 'Gia hạn D‑10, 25h làm thêm, lịch TOPIK hiển thị realtime.',
      content_card2_hint: 'Crawler HiKorea, TOPIK, visa vùng',
      content_card3_pill: 'Thư viện hồ sơ',
      content_card3_title: 'Template theo tình huống',
      content_card3_desc: 'Thông báo tệp đính kèm và lần cập nhật để tăng độ tin cậy.',
      content_card3_hint: 'AI soạn → admin kiểm → phát hành',
      success_title: 'Câu chuyện thật',
      success_subtitle: 'Người dùng VietKConnect đã chuyển visa/thành công việc làm.',
      story1_role: 'D‑2 → D‑10 → E‑7',
      story1_content: '“Nhờ roadmap 12 tuần và mẫu lý do tuyển dụng nên hồ sơ kế toán của tôi được duyệt ngay.”',
      story2_role: 'F‑2‑R vùng Busan/Gyeongnam',
      story2_content: '“Thẻ matching doanh nghiệp và checklist phỏng vấn giúp tôi đạt F‑2‑R.”',
      story3_role: 'Báo cáo làm thêm & nhà ở',
      story3_content: '“Tự động tạo đơn tường trình giúp tôi xử lý vụ lừa đảo nhà trọ.”',
      success_cta: 'Xem thêm trên VietKConnect',
      why_title: 'Vì sao chọn VietKConnect?',
      feature1_title: 'Độ tin cậy',
      feature1_desc: 'Admin, mentor và chuyên gia hành chính kiểm từng câu trả lời.',
      feature2_title: 'Omni-channel',
      feature2_desc: 'Facebook, TikTok, Email, Zalo, AMA cùng một message.',
      feature3_title: 'AI + con người',
      feature3_desc: 'AI tăng tốc, chuyên gia đảm bảo chính xác.',
      consult_title: 'Website VietKConnect',
      consult_desc: 'Hãy truy cập website chính thức (dashboard/thẻ hành động/cộng đồng). Link beta sẽ được cập nhật sớm.',
      site_placeholder_text: 'Khi URL chính thức có sẵn, nút bên dưới sẽ đưa bạn tới website.',
      site_placeholder_cta: 'Mở website',
      footer_text: '© VietKConnect. Bản quyền thuộc VietKConnect.',
      footer_cards: 'Xem bản thẻ hành động (survey)'
    }
  };

  const langKoBtn = document.getElementById('lang-ko');
  const langViBtn = document.getElementById('lang-vi');
  const header = document.getElementById('header');
  const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
  const navbar = document.getElementById('navbar');
  const siteLinks = document.querySelectorAll('.js-site-link');
  let currentLang = 'ko';

  const setLanguage = (lang) => {
    currentLang = lang;
    document.documentElement.lang = lang;
    document.querySelectorAll('[data-lang-key]').forEach((el) => {
      const key = el.getAttribute('data-lang-key');
      if (translations[lang] && translations[lang][key]) {
        el.innerHTML = translations[lang][key];
      }
    });
    if (lang === 'vi') {
      langViBtn.classList.add('active');
      langKoBtn.classList.remove('active');
    } else {
      langKoBtn.classList.add('active');
      langViBtn.classList.remove('active');
    }
  };

  langKoBtn?.addEventListener('click', () => setLanguage('ko'));
  langViBtn?.addEventListener('click', () => setLanguage('vi'));
  setLanguage('ko');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
      header?.classList.add('scrolled');
    } else {
      header?.classList.remove('scrolled');
    }
  });

  mobileMenuToggle?.addEventListener('click', () => {
    navbar?.classList.toggle('active');
  });

  siteLinks.forEach((link) => {
    link.addEventListener('click', (event) => {
      const url = link.getAttribute('data-site-url');
      if (!url) {
        event.preventDefault();
        alert('웹사이트 베타 링크가 준비되는 대로 안내해 드릴게요.');
      }
    });
  });
});
