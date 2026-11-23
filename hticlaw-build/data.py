# -*- coding: utf-8 -*-
"""Noi dung trang con hticlaw.vn (nguon: cac trang WordPress hticlaw.vn, 23/11/2026).
Cac thong tin can xac nhan duoc gom o SITE de sua mot cho."""

SITE = {
    "name": "Công ty Luật HTIC",
    "phone": "0379 044 299",
    "phone_tel": "+84379044299",
    "zalo": "https://zalo.me/1450763104944986971",
    "email": "contact@htic.com.vn",
    "address": "Phòng 16.05, Tầng 16, Tòa nhà Golden King, 15 Nguyễn Lương Bằng, P. Tân Mỹ, TP. Hồ Chí Minh",
    "address_short": "Tầng 16, Golden King, 15 Nguyễn Lương Bằng, P. Tân Mỹ, TP.HCM",
    "map_q": "Golden King, 15 Nguyễn Lương Bằng, Tân Mỹ, Thành phố Hồ Chí Minh",
    "hours": "Thứ 2 – Thứ 6 · 08:30 – 18:00",
    "hours_short": "T2 – T6 · 08:30 – 18:00",
    "street_ld": "Phòng 16.05, Tầng 16, Tòa nhà Golden King, 15 Nguyễn Lương Bằng",
    "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "08:30", "closes": "18:00",
}

PROCESS = [
    ("Tiếp nhận & đánh giá sơ bộ", "Luật sư lắng nghe nhu cầu, xem tài liệu ban đầu và xác định vấn đề pháp lý cốt lõi."),
    ("Thẩm định & nhận diện rủi ro", "Rà soát hồ sơ, đối chiếu quy định hiện hành, chỉ rõ rủi ro và mức độ ảnh hưởng."),
    ("Đề xuất phương án & báo giá", "Đưa ra phương án xử lý, phạm vi công việc, thời gian và phí dịch vụ rõ ràng trước khi triển khai."),
    ("Triển khai", "Soạn thảo, đàm phán, đại diện làm việc với cơ quan nhà nước hoặc đối tác theo phương án đã thống nhất."),
    ("Bàn giao", "Bàn giao tài liệu và hướng dẫn theo phạm vi dịch vụ đã thống nhất. Yêu cầu phát sinh được trao đổi riêng về công việc, thời hạn và phí, nếu có."),
]

WHY = [
    ("person_pin", "Luật sư phụ trách rõ ràng", "Luật sư phụ trách và cách phối hợp được thống nhất theo từng vụ việc; thay đổi nhân sự phụ trách được thông báo cho khách hàng."),
    ("receipt_long", "Báo giá rõ ràng trước khi làm", "Phạm vi công việc, thời gian và phí dịch vụ được thống nhất bằng văn bản trước khi triển khai."),
    ("public", "Am hiểu doanh nghiệp FDI", "Kinh nghiệm làm việc với doanh nghiệp Việt Nam và nhà đầu tư nước ngoài, có nhân sự hỗ trợ khách hàng Nhật Bản."),
    ("shield", "Phòng ngừa trước, xử lý sau", "Ưu tiên nhận diện và kiểm soát rủi ro từ sớm thay vì để vấn đề phát sinh thành tranh chấp."),
]

SERVICES = [
    {
        "slug": "luat-su-bat-dong-san-xay-dung", "name": "Bất động sản & Xây dựng", "icon": "domain",
        "img": "/anh/dv/dv-bat-dong-san.webp",
        "lead": "Tư vấn pháp lý xuyên suốt vòng đời dự án bất động sản và xây dựng: từ quỹ đất, đầu tư, cấp phép đến thi công, bàn giao và tranh chấp.",
        "card": "Thẩm định pháp lý dự án, tư vấn thủ tục đầu tư, đất đai, xây dựng, hợp đồng EPC và chuyển nhượng dự án.",
        "overview": "HTIC đồng hành cùng chủ đầu tư, nhà thầu và nhà đầu tư trong và ngoài nước ở mọi giai đoạn của một dự án bất động sản – xây dựng. Chúng tôi không chỉ xử lý từng thủ tục riêng lẻ mà nhìn tổng thể vòng đời dự án để nhận diện rủi ro sớm, tối ưu tiến độ và bảo vệ quyền lợi khách hàng trong những giao dịch giá trị lớn.",
        "scope": [
            ("Thẩm định pháp lý dự án & quỹ đất", "Kiểm tra nguồn gốc, tình trạng pháp lý đất đai, quy hoạch, chủ trương đầu tư, nghĩa vụ tài chính và các hạn chế, thế chấp, tranh chấp trước khi nhận chuyển nhượng, góp vốn hay đầu tư."),
            ("Thủ tục đầu tư & đất đai", "Chấp thuận chủ trương đầu tư, giao đất, cho thuê đất, chuyển mục đích sử dụng đất, gia hạn thời hạn sử dụng đất, điều chỉnh quy hoạch."),
            ("Hồ sơ xây dựng & tuân thủ thi công", "Tư vấn điều kiện pháp lý, rà soát và hỗ trợ chuẩn bị hồ sơ liên quan đến thiết kế, giấy phép xây dựng, phòng cháy chữa cháy, môi trường, nghiệm thu, hoàn công và cấp giấy chứng nhận. Hoạt động chuyên môn kỹ thuật và việc cấp phép thuộc đơn vị đủ điều kiện hoặc cơ quan có thẩm quyền."),
            ("Soạn thảo & đàm phán hợp đồng", "Hợp đồng EPC, thi công, tư vấn giám sát, mua bán căn hộ/nền, đặt cọc, hợp tác đầu tư với điều khoản phân bổ rủi ro rõ ràng."),
            ("Chuyển nhượng dự án", "Cấu trúc giao dịch chuyển nhượng toàn bộ hoặc một phần dự án, soạn thảo hợp đồng và hoàn tất thủ tục đăng ký, bàn giao."),
            ("Nghĩa vụ tài chính & tranh chấp", "Tư vấn tiền sử dụng đất, tiền thuê đất; đại diện giải quyết tranh chấp hợp đồng xây dựng, mua bán bất động sản."),
        ],
        "laws": ["Luật Đất đai 2024", "Luật Kinh doanh bất động sản 2023", "Luật Nhà ở 2023", "Luật Xây dựng 2025 (Luật số 135/2025/QH15, hiệu lực 01/07/2026)", "Luật Đầu tư 2025 (Luật số 143/2025/QH15)"],
    },
    {
        "slug": "tu-van-phap-ly-doanh-nghiep", "name": "Doanh nghiệp & Quản trị", "icon": "corporate_fare",
        "img": "/anh/dv/dv-doanh-nghiep.webp",
        "lead": "Đồng hành pháp lý cùng doanh nghiệp từ khi thành lập, trong suốt quá trình vận hành, tái cấu trúc và quản trị nội bộ, bao gồm mô hình Phòng Pháp chế thuê ngoài.",
        "card": "Thành lập, quản trị nội bộ, tái cấu trúc và dịch vụ Phòng Pháp chế thuê ngoài.",
        "overview": "HTIC cung cấp tư vấn pháp lý thường xuyên theo nhu cầu doanh nghiệp, từ thành lập, quản trị đến tái cấu trúc hoặc chấm dứt hoạt động. Phạm vi phối hợp với bộ phận pháp chế nội bộ được thống nhất trong hợp đồng dịch vụ.",
        "scope": [
            ("Thành lập & thay đổi đăng ký", "Thành lập doanh nghiệp, chi nhánh, văn phòng đại diện; thay đổi nội dung đăng ký kinh doanh."),
            ("Điều lệ & quy chế nội bộ", "Soạn thảo, chuẩn hoá điều lệ, quy chế nội bộ, thoả thuận cổ đông/thành viên."),
            ("Quản trị công ty", "Tổ chức họp và ban hành nghị quyết ĐHĐCĐ, HĐQT, HĐTV đúng trình tự, thủ tục."),
            ("Phòng Pháp chế thuê ngoài", "Rà soát hợp đồng, tư vấn thường xuyên, cảnh báo rủi ro và cập nhật pháp luật định kỳ."),
            ("Tổ chức lại doanh nghiệp", "Chia, tách, hợp nhất, sáp nhập, chuyển đổi loại hình doanh nghiệp."),
            ("Hệ thống uỷ quyền & tài liệu", "Xây dựng hệ thống uỷ quyền, phân cấp phê duyệt và quản lý tài liệu pháp lý."),
        ],
        "laws": ["Luật Doanh nghiệp 2020, sửa đổi bởi Luật số 76/2025/QH15", "Luật Đầu tư 2025 (Luật số 143/2025/QH15)", "Văn bản hướng dẫn về đăng ký doanh nghiệp"],
    },
    {
        "slug": "tu-van-ma-dau-tu", "name": "M&A & Đầu tư", "icon": "hub",
        "img": "/anh/dv/dv-ma-dau-tu.webp",
        "lead": "Tư vấn trọn vẹn giao dịch mua bán – sáp nhập và đầu tư, từ thẩm định pháp lý đến cấu trúc giao dịch, đăng ký đầu tư và xử lý hậu M&A.",
        "card": "Thẩm định pháp lý, cấu trúc giao dịch, SPA/SHA, đăng ký đầu tư FDI và thoái vốn.",
        "overview": "HTIC tư vấn các thương vụ mua bán – sáp nhập và đầu tư trong nước, xuyên biên giới. Chúng tôi đồng hành từ khâu tiếp cận, thẩm định pháp lý, cấu trúc giao dịch đến đàm phán, ký kết và hoàn tất chuyển giao, hỗ trợ nhà đầu tư gia nhập, mở rộng và thoái vốn tại Việt Nam trên cơ sở đánh giá điều kiện pháp lý, nghĩa vụ và rủi ro của giao dịch.",
        "scope": [
            ("Thẩm định pháp lý", "Legal due diligence doanh nghiệp, dự án mục tiêu; báo cáo rủi ro và khuyến nghị xử lý."),
            ("Cấu trúc giao dịch", "Phương án giao dịch, phương án thuế và điều kiện tiếp cận thị trường cho nhà đầu tư nước ngoài."),
            ("Hợp đồng giao dịch", "Soạn thảo, đàm phán hợp đồng chuyển nhượng vốn/tài sản, SPA, SHA."),
            ("Đăng ký đầu tư", "Giấy chứng nhận đăng ký đầu tư (IRC), đăng ký doanh nghiệp (ERC)."),
            ("Góp vốn, mua cổ phần", "Thủ tục đăng ký góp vốn, mua cổ phần, phần vốn góp của nhà đầu tư nước ngoài."),
            ("Thoái vốn & hậu M&A", "Thoái vốn, chuyển lợi nhuận ra nước ngoài, tích hợp và tuân thủ sau giao dịch."),
        ],
        "laws": ["Luật Đầu tư 2025 (Luật số 143/2025/QH15, hiệu lực 01/03/2026)", "Luật Doanh nghiệp 2020, sửa đổi bởi Luật số 76/2025/QH15", "Luật Cạnh tranh 2018"],
    },
    {
        "slug": "tu-van-giay-phep-tuan-thu", "name": "Giấy phép & Tuân thủ", "icon": "verified_user",
        "img": "/anh/dv/dv-giay-phep.webp",
        "lead": "Tư vấn điều kiện kinh doanh, hồ sơ giấy phép và nghĩa vụ tuân thủ; hỗ trợ doanh nghiệp nhận diện rủi ro vi phạm và chuẩn bị phương án xử lý.",
        "card": "Giấy phép con, giấy phép lao động, chương trình tuân thủ và đại diện khi thanh tra.",
        "overview": "Nhiều ngành nghề tại Việt Nam là kinh doanh có điều kiện, đòi hỏi giấy phép và tuân thủ chặt chẽ. HTIC tư vấn điều kiện, hồ sơ và thủ tục xin, gia hạn, điều chỉnh giấy phép, đồng thời hỗ trợ doanh nghiệp xây dựng chương trình tuân thủ nội bộ.",
        "scope": [
            ("Giấy phép con", "Giấy phép theo ngành nghề kinh doanh có điều kiện: thương mại, sản xuất, dịch vụ, giáo dục…"),
            ("Lao động nước ngoài", "Giấy phép lao động, thẻ tạm trú, thị thực cho người nước ngoài."),
            ("Giấy phép chuyên ngành", "Phòng cháy chữa cháy, môi trường, an toàn thực phẩm."),
            ("Chương trình tuân thủ", "Xây dựng và rà soát chương trình tuân thủ nội bộ, bao gồm bảo vệ dữ liệu cá nhân."),
            ("Cập nhật pháp luật", "Cảnh báo thay đổi pháp luật liên quan đến hoạt động của doanh nghiệp."),
            ("Thanh tra, kiểm tra", "Đại diện giải trình, xử lý khi doanh nghiệp bị thanh tra, kiểm tra."),
        ],
        "laws": ["Luật Đầu tư 2025 (Luật số 143/2025/QH15)", "Luật Bảo vệ dữ liệu cá nhân 2025", "Bộ luật Lao động 2019"],
    },
    {
        "slug": "tu-van-tai-chinh-ngan-hang", "name": "Tài chính – Ngân hàng", "icon": "account_balance",
        "img": "/anh/dv/dv-tai-chinh.webp",
        "lead": "Tư vấn cấu trúc tín dụng, biện pháp bảo đảm, huy động vốn và xử lý tranh chấp tài chính cho doanh nghiệp.",
        "card": "Hợp đồng tín dụng, bảo đảm, trái phiếu doanh nghiệp, ngoại hối và xử lý nợ.",
        "overview": "HTIC tư vấn các vấn đề pháp lý trong giao dịch tín dụng, bảo đảm, huy động vốn và xử lý tranh chấp; hỗ trợ khách hàng rà soát nghĩa vụ và rủi ro trước khi giao kết.",
        "scope": [
            ("Tín dụng & bảo đảm", "Rà soát, đàm phán hợp đồng tín dụng, thế chấp, cầm cố, bảo lãnh."),
            ("Huy động vốn", "Tư vấn phát hành trái phiếu doanh nghiệp và các phương án huy động vốn."),
            ("Bảo lãnh ngân hàng", "Bảo lãnh trong giao dịch bất động sản, xây dựng, thương mại."),
            ("Thu hồi nợ & tranh chấp", "Tư vấn, thương lượng và đại diện theo phạm vi pháp luật cho phép trong việc yêu cầu thực hiện nghĩa vụ thanh toán, giải quyết tranh chấp và thi hành án."),
            ("Ngoại hối", "Tuân thủ quy định ngoại hối, vay và trả nợ nước ngoài."),
            ("Huy động vốn & tài trợ dự án", "Tư vấn pháp lý đối với giao dịch huy động vốn, tài trợ dự án và cấu trúc bảo đảm."),
        ],
        "laws": ["Luật Các tổ chức tín dụng 2024 (lưu ý luật sửa đổi số 23/2026/QH16 có hiệu lực từ 01/12/2026)", "Pháp luật về quản lý ngoại hối", "Bộ luật Dân sự 2015"],
    },
    {
        "slug": "luat-su-tranh-tung", "name": "Tranh chấp & Tố tụng", "icon": "gavel",
        "img": "/anh/dv/dv-tranh-tung.webp",
        "lead": "Đại diện khách hàng giải quyết tranh chấp qua thương lượng, hoà giải, trọng tài và toà án, hướng tới kết quả thực chất.",
        "card": "Thương lượng, hoà giải, trọng tài thương mại, toà án và thi hành án.",
        "overview": "HTIC tư vấn phương án giải quyết tranh chấp, hỗ trợ thương lượng, hoà giải và tham gia tố tụng với tư cách phù hợp theo quy định pháp luật. Phương án được xem xét trên cơ sở hồ sơ, mục tiêu của khách hàng, rủi ro, thời gian và chi phí dự kiến.",
        "scope": [
            ("Đánh giá & chiến lược", "Đánh giá vụ việc, xây dựng chiến lược và phương án giải quyết phù hợp."),
            ("Thương lượng, hoà giải", "Đại diện thương lượng, hoà giải trước và trong quá trình tố tụng."),
            ("Toà án & trọng tài", "Tham gia tố tụng tại Toà án và Trọng tài thương mại trong nước, quốc tế."),
            ("Hồ sơ & chứng cứ", "Thu thập, củng cố chứng cứ; soạn thảo đơn khởi kiện, bản tự bảo vệ."),
            ("Biện pháp khẩn cấp tạm thời", "Yêu cầu áp dụng biện pháp khẩn cấp tạm thời để bảo toàn tài sản, chứng cứ."),
            ("Thi hành án", "Hỗ trợ thi hành án, thu hồi tài sản sau bản án, phán quyết."),
        ],
        "laws": ["Bộ luật Tố tụng dân sự 2015 (sửa đổi, bổ sung bởi Luật số 85/2025/QH15)", "Luật Trọng tài thương mại 2010", "Luật Thi hành án dân sự"],
    },
    {
        "slug": "tu-van-hop-dong", "name": "Hợp đồng", "icon": "contract",
        "img": "/anh/dv/dv-hop-dong.webp",
        "lead": "Soạn thảo, rà soát và đàm phán hợp đồng nhằm bảo vệ quyền lợi và giảm thiểu rủi ro pháp lý cho doanh nghiệp ngay từ khâu ký kết.",
        "card": "Soạn thảo, rà soát, đàm phán hợp đồng thương mại, song ngữ và có yếu tố nước ngoài.",
        "overview": "Hợp đồng là nền tảng pháp lý của mọi giao dịch, và cũng là nơi rủi ro thường bắt đầu. HTIC thiết kế điều khoản phân bổ rủi ro rõ ràng; với kinh nghiệm xử lý tranh chấp, chúng tôi biết những điều khoản nào thường gây rủi ro để giúp khách hàng phòng ngừa từ trước.",
        "scope": [
            ("Hợp đồng thương mại", "Mua bán, dịch vụ, hợp tác kinh doanh, thuê tài sản."),
            ("Hợp đồng chuyên ngành", "Xây dựng (EPC, chìa khoá trao tay), phân phối, đại lý, nhượng quyền."),
            ("Hợp đồng song ngữ", "Hợp đồng lao động và hợp đồng có yếu tố nước ngoài (Việt – Anh, Việt – Nhật)."),
            ("Điều khoản trọng yếu", "Thanh toán, phạt vi phạm, bồi thường, chấm dứt, bất khả kháng."),
            ("Giải quyết tranh chấp", "Điều khoản giải quyết tranh chấp, luật áp dụng, cơ quan tài phán."),
            ("Rà soát hợp đồng đối tác", "Đánh giá rủi ro, đàm phán và điều chỉnh hợp đồng do đối tác đưa ra."),
        ],
        "laws": ["Bộ luật Dân sự 2015", "Luật Thương mại 2005", "Bộ luật Lao động 2019"],
    },
    {
        "slug": "tu-van-so-huu-tri-tue", "name": "Sở hữu trí tuệ", "icon": "lightbulb",
        "img": "/anh/dv/dv-so-huu-tri-tue.webp",
        "lead": "Tư vấn xác lập, bảo hộ và khai thác tài sản trí tuệ: nhãn hiệu, bản quyền, sáng chế, kiểu dáng, cả trong nước và quốc tế.",
        "card": "Tư vấn bảo hộ nhãn hiệu, sáng chế, kiểu dáng công nghiệp, quyền tác giả và xử lý xâm phạm.",
        "overview": "Tài sản trí tuệ ngày càng là giá trị cốt lõi của doanh nghiệp. HTIC tư vấn xác lập, bảo hộ và khai thác quyền sở hữu trí tuệ tại Việt Nam và quốc tế, đồng thời xử lý hành vi xâm phạm, đặc biệt cho doanh nghiệp sản xuất, xuất khẩu và thương hiệu OEM.",
        "scope": [
            ("Tra cứu khả năng bảo hộ", "Tra cứu nhãn hiệu, kiểu dáng, sáng chế trước khi nộp đơn."),
            ("Hồ sơ bảo hộ", "Tư vấn điều kiện bảo hộ và chuẩn bị hồ sơ liên quan đến nhãn hiệu, kiểu dáng công nghiệp, sáng chế và quyền tác giả; tư vấn xác lập, sử dụng và bảo vệ tên thương mại. Hoạt động đại diện sở hữu công nghiệp được thực hiện theo điều kiện hành nghề áp dụng."),
            ("Đăng ký quốc tế", "Tư vấn phương án đăng ký nhãn hiệu qua Hệ thống Madrid, phạm vi quốc gia chỉ định và việc phối hợp với đại diện đáp ứng điều kiện khi cần thiết."),
            ("Theo dõi đơn", "Theo dõi đơn, xử lý phản đối, khiếu nại, yêu cầu chấm dứt hiệu lực."),
            ("Xử lý xâm phạm", "Biện pháp hành chính, dân sự; phản đối đơn đăng ký xấu."),
            ("Chuyển giao & li-xăng", "Tư vấn hợp đồng chuyển nhượng, chuyển quyền sử dụng và các vấn đề pháp lý khi khai thác tài sản trí tuệ; phối hợp với đơn vị chuyên môn khi cần xác định giá trị."),
        ],
        "laws": ["Luật Sở hữu trí tuệ (sửa đổi, bổ sung bởi Luật số 131/2025/QH15, hiệu lực 01/04/2026)", "Thoả ước và Nghị định thư Madrid"],
    },
    {
        "slug": "tu-van-thue-ke-toan", "name": "Thuế & Kế toán", "icon": "calculate",
        "img": "/anh/dv/dv-thue.webp",
        "lead": "Tư vấn pháp lý về nghĩa vụ thuế, rà soát rủi ro thuế trong giao dịch và đại diện làm việc với cơ quan thuế.",
        "card": "Tư vấn pháp lý về nghĩa vụ thuế, giao dịch liên kết, kiểm tra, thanh tra và tranh chấp thuế.",
        "overview": "HTIC tư vấn pháp lý về nghĩa vụ thuế, hồ sơ giao dịch, làm việc với cơ quan thuế và giải quyết tranh chấp thuế. Phạm vi dịch vụ được xác định theo từng yêu cầu và không bao gồm trực tiếp thực hiện nghiệp vụ kế toán hoặc đại lý thuế.",
        "scope": [
            ("Nghĩa vụ thuế", "Thuế thu nhập doanh nghiệp, giá trị gia tăng, nhà thầu, thu nhập cá nhân."),
            ("Rà soát hồ sơ thuế", "Rà soát hồ sơ, hoá đơn, chứng từ dưới góc độ pháp lý trước kê khai, quyết toán."),
            ("Thanh tra, kiểm tra thuế", "Đại diện giải trình, làm việc với cơ quan thuế."),
            ("Cấu trúc giao dịch", "Rà soát nghĩa vụ thuế và vấn đề pháp lý của cấu trúc giao dịch trong M&A, tái cấu trúc, giao dịch xuyên biên giới."),
            ("Giao dịch liên kết", "Tư vấn nghĩa vụ pháp lý về giao dịch liên kết, hồ sơ xác định giá giao dịch liên kết và thuế tối thiểu toàn cầu."),
            ("Khiếu nại thuế", "Khiếu nại, giải quyết tranh chấp về thuế."),
        ],
        "laws": ["Luật Quản lý thuế 2025 (Luật số 108/2025/QH15, hiệu lực 01/07/2026)", "Các luật thuế chuyên ngành", "Luật Kế toán 2015"],
    },
    {
        "slug": "tu-van-xuat-khau-lao-dong", "name": "Xuất khẩu lao động & Du học", "icon": "flight_takeoff",
        "img": "/anh/dv/dv-xuat-khau-lao-dong.webp",
        "lead": "Tư vấn pháp lý lĩnh vực đưa người lao động Việt Nam đi làm việc ở nước ngoài và tư vấn du học: giấy phép, hợp đồng và bảo vệ quyền lợi.",
        "card": "Tư vấn pháp lý về điều kiện kinh doanh, hợp đồng và tranh chấp trong lĩnh vực đưa người lao động đi làm việc ở nước ngoài, du học và thị thực.",
        "overview": "Đưa người lao động Việt Nam đi làm việc ở nước ngoài và dịch vụ du học đòi hỏi tuân thủ chặt chẽ về giấy phép, hợp đồng và bảo vệ quyền lợi người lao động. HTIC tư vấn pháp lý cho doanh nghiệp dịch vụ và người lao động; HTIC không trực tiếp tuyển chọn hay đưa người lao động đi làm việc ở nước ngoài.",
        "scope": [
            ("Giấy phép dịch vụ", "Tư vấn điều kiện, thủ tục và hồ sơ đề nghị cấp, điều chỉnh giấy phép hoạt động dịch vụ đưa người lao động Việt Nam đi làm việc ở nước ngoài theo hợp đồng."),
            ("Hợp đồng", "Hợp đồng cung ứng, hợp đồng đưa người lao động đi làm việc ở nước ngoài."),
            ("Tuân thủ", "Tư vấn quy định về ký quỹ, nghĩa vụ đào tạo và bảo vệ quyền, lợi ích hợp pháp của người lao động."),
            ("Thị thực & xuất nhập cảnh", "Thủ tục visa, giấy tờ cho người lao động và người nước ngoài."),
            ("Du học", "Pháp lý dịch vụ tư vấn du học, hợp đồng tư vấn du học."),
            ("Tranh chấp", "Xử lý tranh chấp phát sinh trong quan hệ lao động, dịch vụ."),
        ],
        "laws": ["Luật Người lao động Việt Nam đi làm việc ở nước ngoài theo hợp đồng 2020 (lưu ý luật sửa đổi số 22/2026/QH16 có hiệu lực từ 01/03/2027)", "Bộ luật Lao động 2019"],
    },
]

TEAM_LAWYERS = [
    ("LS. Trần Quốc Hưng", "Giám đốc", "/wp-content/uploads/2026/05/01_ls_tran_quoc_hung.jpg"),
    ("LS. Nguyễn Đăng Hợp", "Phó Giám đốc", "/wp-content/uploads/2026/05/02_ls_nguyen_dang_hop.jpg"),
    ("LS. Hoàng Giang Tử Lăng", "Luật sư cấp cao · Bảo hiểm & Đầu tư", "/wp-content/uploads/2026/05/03_ls_hoang_giang_tu_lang.jpg"),
    ("LS. Dương Anh Khoa", "Luật sư · Tranh tụng & Đại diện", "/wp-content/uploads/2026/05/06_ls_duong_anh_khoa.jpg"),
    ("LS. Tống Thị Bích Nguyệt", "Luật sư · BĐS & Hợp đồng thương mại", "/wp-content/uploads/2026/05/07_ls_tong_thi_bich_nguyet.jpg"),
]
TEAM_EXPERTS = [
    ("Nguyễn Phương Thuỳ Trang", "Trưởng phòng Khách hàng Nhật Bản", "/wp-content/uploads/2026/05/04_nguyen_phuong_thuy_trang.jpg"),
    ("Morita Shoki", "Cố vấn thị trường Nhật Bản", "/wp-content/uploads/2026/05/05_morita_shoki.jpg"),
    ("Trần Thị Thu Hiền", "Chuyên gia Kế toán – Thuế", "/wp-content/uploads/2026/05/08_tran_thi_thu_hien.jpg"),
    ("Trương Thanh Hải", "Trưởng phòng Đối ngoại", "/wp-content/uploads/2026/05/09_truong_thanh_hai.jpg"),
    ("Nguyễn Thị Kim Ngọc", "Chuyên viên Pháp chế", "/wp-content/uploads/2026/05/10_nguyen_thi_kim_ngoc.png"),
    ("Cao Ý Mỹ", "Chuyên viên Pháp chế", "/wp-content/uploads/2026/05/11_cao_y_my.jpg"),
    ("Nguyễn Thị Thu Trang", "Chuyên viên Pháp chế", "/wp-content/uploads/2026/05/12_nguyen_thi_thu_trang.jpg"),
]

VALUES = [
    ("H", "Honesty", "Trung thực", "Minh bạch thông tin, đánh giá đúng rủi ro và không hứa những gì không thể thực hiện."),
    ("T", "Trust", "Tin cậy", "Chất lượng dịch vụ ổn định, chuyên môn được cập nhật liên tục cho từng vụ việc."),
    ("I", "Integrity", "Chính trực", "Không xung đột lợi ích, không đánh đổi quyền lợi hợp pháp của khách hàng."),
    ("C", "Commitment", "Cam kết", "Thực hiện công việc theo phạm vi đã thống nhất, thông tin kịp thời về tiến độ và những vấn đề cần khách hàng quyết định."),
]

TIMELINE = [
    ("2011", "Khởi đầu", "Thành lập Công ty Tư vấn Pháp Chính tại TP.HCM, tiền thân của HTIC, tư vấn doanh nghiệp và đầu tư."),
    ("2014", "Tư vấn FDI Nhật Bản", "Tư vấn đầu tư và xúc tiến thương mại cho doanh nghiệp Nhật Bản vào thị trường Việt Nam."),
    ("2019", "Công ty Luật HTIC", "Chính thức trở thành tổ chức hành nghề luật sư, phục vụ doanh nghiệp và cá nhân."),
    ("2021", "Pháp chế thuê ngoài", "Ra mắt dịch vụ Phòng Pháp chế thuê ngoài cho doanh nghiệp."),
    ("2023", "Hiệp hội Việt – Nhật", "Gia nhập Hiệp hội Xúc tiến Thương mại Việt Nam – Nhật Bản, hỗ trợ pháp lý cho hội viên."),
    ("2024", "Kết nối Nhật Bản", "Mở điểm tiếp nhận thông tin tại Gunma, Osaka, Hiroshima."),
]

GALLERY = [
    ("/anh/htic/htic-kcn-long-hau956107481368.jpg", "HTIC cùng đối tác tại KCN Long Hậu"),
    ("/anh/htic/z7364086989013-5992ac9ec761c25482e962bd40be8b2b991008353200.jpg", "Hội thảo pháp lý cho doanh nghiệp"),
    ("/anh/htic/ky-hop-dong-tu-van-thuong-xuyen-cho-thuong-hieu-viva-star-ca-phe755940686954.jpg", "Ký hợp đồng tư vấn thường xuyên"),
    ("/anh/htic/tu-van-kcn-long-hau-japan665005815545.jpg", "Làm việc với nhà đầu tư Nhật Bản"),
    ("/anh/htic/hop-chien-luoc-htic589364659224.jpg", "Họp chiến lược nội bộ"),
]

FAQ = {
    "luat-su-bat-dong-san-xay-dung": [
        ("Cần kiểm tra hồ sơ gì trước khi nhận chuyển nhượng dự án hoặc quỹ đất?", "Tối thiểu gồm nguồn gốc và tình trạng pháp lý đất, quy hoạch, chủ trương đầu tư, nghĩa vụ tài chính đã thực hiện, các biện pháp bảo đảm, kê biên và tranh chấp đang có. Phạm vi cụ thể phụ thuộc loại tài sản và cấu trúc giao dịch."),
        ("Có Giấy chứng nhận đã đủ để kết luận giao dịch an toàn chưa?", "Chưa. Giấy chứng nhận là căn cứ quan trọng nhưng cần đối chiếu thêm quy hoạch, thế chấp, nghĩa vụ tài chính, tình trạng tranh chấp và điều kiện chuyển nhượng theo quy định hiện hành."),
        ("Hợp đồng xây dựng nên có cơ chế xử lý phát sinh nào?", "Thường cần quy định rõ điều chỉnh khối lượng, giá, tiến độ, nghiệm thu, bảo hành, phạt vi phạm, bồi thường và cách giải quyết tranh chấp để hạn chế bất đồng khi thực hiện."),
    ],
    "tu-van-phap-ly-doanh-nghiep": [
        ("Cần chuẩn bị gì trước khi thành lập doanh nghiệp?", "Xác định loại hình, ngành nghề (có điều kiện hay không), vốn điều lệ, cơ cấu sở hữu, người đại diện theo pháp luật và địa chỉ trụ sở. Với nhà đầu tư nước ngoài cần xem thêm thủ tục đầu tư."),
        ("Khi nào cần sửa điều lệ và quy chế nội bộ?", "Khi thay đổi cơ cấu sở hữu, mô hình quản trị, quyền hạn người quản lý hoặc khi pháp luật doanh nghiệp được sửa đổi làm điều lệ hiện tại không còn phù hợp."),
        ("Pháp chế thuê ngoài hỗ trợ những công việc nào?", "Tuỳ phạm vi thống nhất, thường gồm rà soát hợp đồng, tư vấn thường xuyên, chuẩn hoá biểu mẫu, cập nhật pháp luật và hỗ trợ khi làm việc với cơ quan nhà nước."),
    ],
    "tu-van-ma-dau-tu": [
        ("Thẩm định pháp lý doanh nghiệp mục tiêu gồm những gì?", "Thường gồm tư cách pháp lý, cơ cấu vốn, giấy phép, tài sản, hợp đồng trọng yếu, lao động, thuế, tranh chấp và nghĩa vụ tiềm ẩn. Phạm vi được điều chỉnh theo mục tiêu giao dịch."),
        ("Nhà đầu tư nước ngoài cần kiểm tra điều kiện nào?", "Điều kiện tiếp cận thị trường của ngành nghề, tỷ lệ sở hữu, thủ tục đăng ký góp vốn, mua cổ phần hoặc đăng ký đầu tư, cùng các quy định chuyên ngành liên quan."),
        ("Rủi ro phát hiện khi thẩm định được xử lý trong hợp đồng thế nào?", "Có thể qua điều kiện tiên quyết, cam đoan và bảo đảm, cơ chế bồi hoàn, điều chỉnh giá hoặc giữ lại một phần thanh toán, tuỳ mức độ rủi ro."),
    ],
    "tu-van-giay-phep-tuan-thu": [
        ("Có Giấy chứng nhận đăng ký doanh nghiệp đã đủ để hoạt động chưa?", "Chưa chắc. Với ngành nghề kinh doanh có điều kiện, doanh nghiệp còn phải đáp ứng điều kiện hoặc có giấy phép chuyên ngành trước khi hoạt động."),
        ("Thay đổi địa điểm kinh doanh có phải điều chỉnh giấy phép không?", "Nhiều loại giấy phép gắn với địa điểm, nên thường phải thông báo hoặc điều chỉnh. Cần kiểm tra quy định của từng loại giấy phép cụ thể."),
        ("HTIC hỗ trợ những bước nào?", "Xác định giấy phép cần có, kiểm tra điều kiện, chuẩn bị hồ sơ, theo dõi xử lý và giải trình với cơ quan có thẩm quyền theo phạm vi thống nhất."),
    ],
    "tu-van-tai-chinh-ngan-hang": [
        ("Cần rà soát gì trước khi ký hợp đồng tín dụng?", "Lãi suất và cách điều chỉnh, phí, điều kiện giải ngân, nghĩa vụ cam kết, sự kiện vi phạm, quyền thu hồi nợ trước hạn và tài sản bảo đảm."),
        ("Luật sư có bảo đảm khoản vay được phê duyệt không?", "Không. Quyết định cấp tín dụng thuộc tổ chức tín dụng. Luật sư hỗ trợ rà soát điều khoản, chuẩn bị hồ sơ pháp lý và đàm phán để bảo vệ quyền lợi của khách hàng."),
        ("Khi phát sinh tranh chấp tín dụng cần chuẩn bị tài liệu nào?", "Hợp đồng tín dụng, hợp đồng bảo đảm, chứng từ giải ngân và thanh toán, thông báo nợ, thư từ trao đổi và các văn bản liên quan đến tài sản bảo đảm."),
    ],
    "luat-su-tranh-tung": [
        ("Luật sư có cam kết thắng kiện không?", "Không. Kết quả phụ thuộc chứng cứ, quy định pháp luật và quyết định của cơ quan tài phán. Luật sư đánh giá khách quan rủi ro và bảo vệ tốt nhất quyền lợi hợp pháp của khách hàng."),
        ("Khi nào giải quyết tại toà án, khi nào tại trọng tài?", "Trọng tài giải quyết tranh chấp thuộc thẩm quyền luật định khi có thoả thuận trọng tài hợp lệ và có thể thực hiện. Việc xác định toà án hoặc trọng tài có thẩm quyền cần xem xét loại tranh chấp, thoả thuận của các bên và các điều kiện tố tụng liên quan."),
        ("Cần chuẩn bị gì trước buổi làm việc với luật sư?", "Hợp đồng, hoá đơn, chứng từ thanh toán, thư từ, tin nhắn trao đổi, biên bản làm việc và bản tóm tắt diễn biến theo thời gian."),
    ],
    "tu-van-hop-dong": [
        ("Những điều khoản nào cần kiểm tra trước khi ký?", "Đối tượng và chất lượng, giá và thanh toán, thời hạn, nghĩa vụ các bên, phạt vi phạm và bồi thường, chấm dứt, bất khả kháng, luật áp dụng và giải quyết tranh chấp."),
        ("Hợp đồng song ngữ nên quy định bản ưu tiên thế nào?", "Nên ghi rõ bản ngôn ngữ nào được ưu tiên khi có khác biệt, đồng thời rà soát để hai bản thống nhất về nội dung ngay từ đầu."),
        ("Có thể sửa đổi hợp đồng đã ký bằng cách nào?", "Thông thường bằng phụ lục hoặc văn bản sửa đổi được các bên ký theo đúng hình thức mà hợp đồng và pháp luật yêu cầu."),
    ],
    "tu-van-so-huu-tri-tue": [
        ("Đăng ký tên doanh nghiệp có thay thế bảo hộ nhãn hiệu không?", "Không. Đăng ký tên doanh nghiệp không thay thế việc xác lập quyền đối với nhãn hiệu. Thông thường, quyền đối với nhãn hiệu được xác lập khi được cấp văn bằng bảo hộ hoặc được công nhận đăng ký quốc tế theo điều ước áp dụng. Riêng nhãn hiệu nổi tiếng, quyền được xác lập trên cơ sở sử dụng, không phụ thuộc thủ tục đăng ký."),
        ("Nộp đơn có đồng nghĩa được cấp văn bằng không?", "Không. Đơn phải qua thẩm định hình thức và nội dung; kết quả phụ thuộc khả năng phân biệt và các đối tượng đã được bảo hộ trước. Tra cứu trước khi nộp giúp đánh giá khả năng này."),
        ("Khi nào nên bảo hộ kiểu dáng công nghiệp?", "Nên đánh giá khả năng bảo hộ và thời điểm nộp đơn trước khi công bố hoặc đưa sản phẩm ra thị trường. Kiểu dáng phải đáp ứng các điều kiện luật định về tính mới, tính sáng tạo và khả năng áp dụng công nghiệp; trường hợp đã công bố cần xem xét quy định về ngoại lệ liên quan."),
    ],
    "tu-van-thue-ke-toan": [
        ("Tư vấn pháp lý thuế khác dịch vụ kế toán thế nào?", "Tư vấn pháp lý thuế tập trung vào nghĩa vụ, rủi ro và việc áp dụng pháp luật. Phạm vi HTIC giới thiệu tại trang này là tư vấn pháp lý, không bao gồm trực tiếp ghi sổ, lập báo cáo tài chính hoặc thực hiện dịch vụ đại lý thuế. Các nghiệp vụ có điều kiện cần được thực hiện bởi chủ thể đáp ứng điều kiện theo quy định."),
        ("Cần chuẩn bị hồ sơ gì khi bị kiểm tra thuế?", "Hồ sơ khai thuế, sổ sách, hoá đơn, chứng từ, hợp đồng của các giao dịch được kiểm tra và văn bản giải trình trước đó nếu có."),
        ("Phạm vi trách nhiệm của đơn vị tư vấn được xác định ra sao?", "Hợp đồng dịch vụ cần xác định công việc, trách nhiệm cung cấp thông tin, thời hạn, phí và trách nhiệm của mỗi bên. Thoả thuận về trách nhiệm phải phù hợp với các quy định pháp luật bắt buộc áp dụng."),
    ],
    "tu-van-xuat-khau-lao-dong": [
        ("Cần kiểm tra gì trước khi ký hợp đồng đi làm việc ở nước ngoài?", "Giấy phép của doanh nghiệp dịch vụ, nội dung công việc, tiền lương, thời hạn, chi phí phải nộp, điều kiện chấm dứt và cơ chế giải quyết tranh chấp."),
        ("Làm sao kiểm tra doanh nghiệp dịch vụ có giấy phép?", "Đối chiếu danh sách doanh nghiệp được cấp phép do cơ quan quản lý lao động công bố và kiểm tra giấy phép còn hiệu lực."),
        ("Khi phát sinh tranh chấp, người lao động cần lưu giữ tài liệu nào?", "Hợp đồng, biên lai các khoản đã nộp, thư từ, tin nhắn trao đổi và giấy tờ liên quan đến công việc ở nước ngoài."),
    ],
}
