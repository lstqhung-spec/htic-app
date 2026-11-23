# -*- coding: utf-8 -*-
"""Noi dung trang con hticlaw.vn (nguon: cac trang WordPress hticlaw.vn, 23/11/2026).
Cac thong tin can xac nhan duoc gom o SITE de sua mot cho."""

SITE = {
    "name": "Công ty Luật HTIC",
    "phone": "0379 044 299",
    "phone_tel": "+84379044299",
    "zalo": "https://zalo.me/0379044299",
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
    ("Bàn giao & hỗ trợ sau dịch vụ", "Bàn giao kết quả, hướng dẫn thực hiện và tiếp tục hỗ trợ khi phát sinh vấn đề liên quan."),
]

WHY = [
    ("person_pin", "Một đầu mối xuyên suốt", "Mỗi vụ việc do một luật sư phụ trách dẫn dắt từ đầu đến cuối, khách hàng không phải trao đổi lại với nhiều người."),
    ("receipt_long", "Báo giá rõ ràng trước khi làm", "Phạm vi công việc, thời gian và phí dịch vụ được thống nhất bằng văn bản trước khi triển khai."),
    ("public", "Am hiểu doanh nghiệp FDI", "Kinh nghiệm làm việc với doanh nghiệp Việt Nam và nhà đầu tư nước ngoài, có nhân sự hỗ trợ khách hàng Nhật Bản."),
    ("shield", "Phòng ngừa trước, xử lý sau", "Ưu tiên nhận diện và kiểm soát rủi ro từ sớm thay vì để vấn đề phát sinh thành tranh chấp."),
]

SERVICES = [
    {
        "slug": "luat-su-bat-dong-san-xay-dung", "name": "Bất động sản & Xây dựng", "icon": "domain",
        "img": "/anh/khu-cong-nghiep.webp",
        "lead": "Pháp lý trọn gói cho toàn bộ vòng đời dự án bất động sản và xây dựng: từ quỹ đất, đầu tư, cấp phép đến thi công, bàn giao và tranh chấp.",
        "card": "Thẩm định quỹ đất, thủ tục đầu tư, cấp phép xây dựng, hợp đồng EPC và chuyển nhượng dự án.",
        "overview": "HTIC đồng hành cùng chủ đầu tư, nhà thầu và nhà đầu tư trong và ngoài nước ở mọi giai đoạn của một dự án bất động sản – xây dựng. Chúng tôi không chỉ xử lý từng thủ tục riêng lẻ mà nhìn tổng thể vòng đời dự án để nhận diện rủi ro sớm, tối ưu tiến độ và bảo vệ quyền lợi khách hàng trong những giao dịch giá trị lớn.",
        "scope": [
            ("Thẩm định pháp lý dự án & quỹ đất", "Kiểm tra nguồn gốc, tình trạng pháp lý đất đai, quy hoạch, chủ trương đầu tư, nghĩa vụ tài chính và các hạn chế, thế chấp, tranh chấp trước khi nhận chuyển nhượng, góp vốn hay đầu tư."),
            ("Thủ tục đầu tư & đất đai", "Chấp thuận chủ trương đầu tư, giao đất, cho thuê đất, chuyển mục đích sử dụng đất, gia hạn thời hạn sử dụng đất, điều chỉnh quy hoạch."),
            ("Cấp phép xây dựng & tuân thủ thi công", "Thẩm định thiết kế, giấy phép xây dựng, thủ tục phòng cháy chữa cháy và môi trường; nghiệm thu, hoàn công và cấp Giấy chứng nhận."),
            ("Soạn thảo & đàm phán hợp đồng", "Hợp đồng EPC, thi công, tư vấn giám sát, mua bán căn hộ/nền, đặt cọc, hợp tác đầu tư với điều khoản phân bổ rủi ro rõ ràng."),
            ("Chuyển nhượng dự án", "Cấu trúc giao dịch chuyển nhượng toàn bộ hoặc một phần dự án, soạn thảo hợp đồng và hoàn tất thủ tục đăng ký, bàn giao."),
            ("Nghĩa vụ tài chính & tranh chấp", "Tư vấn tiền sử dụng đất, tiền thuê đất; đại diện giải quyết tranh chấp hợp đồng xây dựng, mua bán bất động sản."),
        ],
        "laws": ["Luật Đất đai 2024", "Luật Kinh doanh bất động sản 2023", "Luật Nhà ở 2023", "Luật Xây dựng và văn bản hướng dẫn hiện hành", "Luật Đầu tư hiện hành"],
    },
    {
        "slug": "tu-van-phap-ly-doanh-nghiep", "name": "Doanh nghiệp & Quản trị", "icon": "corporate_fare",
        "img": "/anh/htic/hop-chien-luoc-htic589364659224.jpg",
        "lead": "Đồng hành pháp lý cùng doanh nghiệp từ khi thành lập, trong suốt quá trình vận hành, tái cấu trúc và quản trị nội bộ, bao gồm mô hình Phòng Pháp chế thuê ngoài.",
        "card": "Thành lập, quản trị nội bộ, tái cấu trúc và dịch vụ Phòng Pháp chế thuê ngoài.",
        "overview": "HTIC là đối tác pháp lý dài hạn của doanh nghiệp, đồng hành từ khi thành lập đến khi mở rộng, tái cấu trúc hoặc rút lui. Dịch vụ Phòng Pháp chế thuê ngoài mang lại cho doanh nghiệp một bộ phận pháp chế chuyên nghiệp, chủ động phòng ngừa rủi ro mà không phải gánh chi phí xây dựng đội ngũ nội bộ.",
        "scope": [
            ("Thành lập & thay đổi đăng ký", "Thành lập doanh nghiệp, chi nhánh, văn phòng đại diện; thay đổi nội dung đăng ký kinh doanh."),
            ("Điều lệ & quy chế nội bộ", "Soạn thảo, chuẩn hoá điều lệ, quy chế nội bộ, thoả thuận cổ đông/thành viên."),
            ("Quản trị công ty", "Tổ chức họp và ban hành nghị quyết ĐHĐCĐ, HĐQT, HĐTV đúng trình tự, thủ tục."),
            ("Phòng Pháp chế thuê ngoài", "Rà soát hợp đồng, tư vấn thường xuyên, cảnh báo rủi ro và cập nhật pháp luật định kỳ."),
            ("Tổ chức lại doanh nghiệp", "Chia, tách, hợp nhất, sáp nhập, chuyển đổi loại hình doanh nghiệp."),
            ("Hệ thống uỷ quyền & tài liệu", "Xây dựng hệ thống uỷ quyền, phân cấp phê duyệt và quản lý tài liệu pháp lý."),
        ],
        "laws": ["Luật Doanh nghiệp 2020 (sửa đổi, bổ sung 2025)", "Luật Đầu tư hiện hành", "Văn bản hướng dẫn về đăng ký doanh nghiệp"],
    },
    {
        "slug": "tu-van-ma-dau-tu", "name": "M&A & Đầu tư", "icon": "hub",
        "img": "/anh/hop-dong-ma.webp",
        "lead": "Tư vấn trọn vẹn giao dịch mua bán – sáp nhập và đầu tư, từ thẩm định pháp lý đến cấu trúc giao dịch, đăng ký đầu tư và xử lý hậu M&A.",
        "card": "Thẩm định pháp lý, cấu trúc giao dịch, SPA/SHA, đăng ký đầu tư FDI và thoái vốn.",
        "overview": "HTIC tư vấn các thương vụ mua bán – sáp nhập và đầu tư trong nước, xuyên biên giới. Chúng tôi đồng hành từ khâu tiếp cận, thẩm định pháp lý, cấu trúc giao dịch đến đàm phán, ký kết và hoàn tất chuyển giao, giúp nhà đầu tư gia nhập, mở rộng và thoái vốn tại Việt Nam an toàn.",
        "scope": [
            ("Thẩm định pháp lý", "Legal due diligence doanh nghiệp, dự án mục tiêu; báo cáo rủi ro và khuyến nghị xử lý."),
            ("Cấu trúc giao dịch", "Phương án giao dịch, phương án thuế và điều kiện tiếp cận thị trường cho nhà đầu tư nước ngoài."),
            ("Hợp đồng giao dịch", "Soạn thảo, đàm phán hợp đồng chuyển nhượng vốn/tài sản, SPA, SHA."),
            ("Đăng ký đầu tư", "Giấy chứng nhận đăng ký đầu tư (IRC), đăng ký doanh nghiệp (ERC)."),
            ("Góp vốn, mua cổ phần", "Thủ tục đăng ký góp vốn, mua cổ phần, phần vốn góp của nhà đầu tư nước ngoài."),
            ("Thoái vốn & hậu M&A", "Thoái vốn, chuyển lợi nhuận ra nước ngoài, tích hợp và tuân thủ sau giao dịch."),
        ],
        "laws": ["Luật Đầu tư hiện hành", "Luật Doanh nghiệp 2020 (sửa đổi, bổ sung 2025)", "Luật Cạnh tranh 2018"],
    },
    {
        "slug": "tu-van-giay-phep-tuan-thu", "name": "Giấy phép & Tuân thủ", "icon": "verified_user",
        "img": "/anh/htic/htic-giay-phep-con-2026459373652042.jpg",
        "lead": "Hỗ trợ doanh nghiệp xin cấp phép, đáp ứng điều kiện kinh doanh và tuân thủ pháp luật chuyên ngành, tránh bị xử phạt hoặc đình chỉ.",
        "card": "Giấy phép con, giấy phép lao động, chương trình tuân thủ và đại diện khi thanh tra.",
        "overview": "Nhiều ngành nghề tại Việt Nam là kinh doanh có điều kiện, đòi hỏi giấy phép và tuân thủ chặt chẽ. HTIC đại diện khách hàng làm việc với cơ quan nhà nước để xin, gia hạn, điều chỉnh giấy phép, đồng thời xây dựng chương trình tuân thủ giúp doanh nghiệp vận hành an toàn.",
        "scope": [
            ("Giấy phép con", "Giấy phép theo ngành nghề kinh doanh có điều kiện: thương mại, sản xuất, dịch vụ, giáo dục…"),
            ("Lao động nước ngoài", "Giấy phép lao động, thẻ tạm trú, thị thực cho người nước ngoài."),
            ("Giấy phép chuyên ngành", "Phòng cháy chữa cháy, môi trường, an toàn thực phẩm."),
            ("Chương trình tuân thủ", "Xây dựng và rà soát chương trình tuân thủ nội bộ, bao gồm bảo vệ dữ liệu cá nhân."),
            ("Cập nhật pháp luật", "Cảnh báo thay đổi pháp luật liên quan đến hoạt động của doanh nghiệp."),
            ("Thanh tra, kiểm tra", "Đại diện giải trình, xử lý khi doanh nghiệp bị thanh tra, kiểm tra."),
        ],
        "laws": ["Luật Đầu tư hiện hành", "Luật Bảo vệ dữ liệu cá nhân 2025", "Bộ luật Lao động 2019"],
    },
    {
        "slug": "tu-van-tai-chinh-ngan-hang", "name": "Tài chính – Ngân hàng", "icon": "account_balance",
        "img": "/anh/htic/luat-su-tu-van-dn-quan-7-htic009633116392.jpg",
        "lead": "Tư vấn cấu trúc tín dụng, biện pháp bảo đảm, huy động vốn và xử lý tranh chấp tài chính cho doanh nghiệp.",
        "card": "Hợp đồng tín dụng, bảo đảm, trái phiếu doanh nghiệp, ngoại hối và xử lý nợ.",
        "overview": "HTIC tư vấn cho doanh nghiệp trong các giao dịch tài chính – ngân hàng: cấu trúc tín dụng, biện pháp bảo đảm, huy động vốn và xử lý nợ. Chúng tôi giúp khách hàng tiếp cận nguồn vốn an toàn, kiểm soát nghĩa vụ bảo đảm và bảo vệ quyền lợi khi phát sinh tranh chấp.",
        "scope": [
            ("Tín dụng & bảo đảm", "Rà soát, đàm phán hợp đồng tín dụng, thế chấp, cầm cố, bảo lãnh."),
            ("Huy động vốn", "Tư vấn phát hành trái phiếu doanh nghiệp và các phương án huy động vốn."),
            ("Bảo lãnh ngân hàng", "Bảo lãnh trong giao dịch bất động sản, xây dựng, thương mại."),
            ("Xử lý nợ", "Thu hồi nợ, xử lý tài sản bảo đảm, giải quyết tranh chấp tín dụng."),
            ("Ngoại hối", "Tuân thủ quy định ngoại hối, vay và trả nợ nước ngoài."),
            ("Giao dịch xuyên biên giới", "Thu xếp vốn, tài trợ dự án và giao dịch tài chính có yếu tố nước ngoài."),
        ],
        "laws": ["Luật Các tổ chức tín dụng 2024", "Pháp luật về quản lý ngoại hối hiện hành", "Bộ luật Dân sự 2015"],
    },
    {
        "slug": "luat-su-tranh-tung", "name": "Tranh chấp & Tố tụng", "icon": "gavel",
        "img": "/anh/htic/thoi-hieu-thi-hanh-ban-an021410587703.jpg",
        "lead": "Đại diện khách hàng giải quyết tranh chấp qua thương lượng, hoà giải, trọng tài và toà án, hướng tới kết quả thực chất.",
        "card": "Thương lượng, hoà giải, trọng tài thương mại, toà án và thi hành án.",
        "overview": "Đội ngũ luật sư tranh tụng của HTIC đại diện khách hàng tại Toà án các cấp và Trọng tài thương mại. Mỗi vụ việc được tiếp cận bằng chiến lược bài bản, đánh giá thực tế về rủi ro và chi phí, ưu tiên phương án hiệu quả nhất cho khách hàng.",
        "scope": [
            ("Đánh giá & chiến lược", "Đánh giá vụ việc, xây dựng chiến lược và phương án giải quyết phù hợp."),
            ("Thương lượng, hoà giải", "Đại diện thương lượng, hoà giải trước và trong quá trình tố tụng."),
            ("Toà án & trọng tài", "Tham gia tố tụng tại Toà án và Trọng tài thương mại trong nước, quốc tế."),
            ("Hồ sơ & chứng cứ", "Thu thập, củng cố chứng cứ; soạn thảo đơn khởi kiện, bản tự bảo vệ."),
            ("Biện pháp khẩn cấp tạm thời", "Yêu cầu áp dụng biện pháp khẩn cấp tạm thời để bảo toàn tài sản, chứng cứ."),
            ("Thi hành án", "Hỗ trợ thi hành án, thu hồi tài sản sau bản án, phán quyết."),
        ],
        "laws": ["Bộ luật Tố tụng dân sự 2015", "Luật Trọng tài thương mại 2010", "Luật Thi hành án dân sự hiện hành"],
    },
    {
        "slug": "tu-van-hop-dong", "name": "Hợp đồng", "icon": "contract",
        "img": "/anh/htic/htic-soan-thao-hop-dong-2026321611806850.jpg",
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
        "img": "/anh/htic/dich-vu-luat-su-danh-cho-doanh-nghiep-1-583386025116.png",
        "lead": "Tư vấn xác lập, bảo hộ và khai thác tài sản trí tuệ: nhãn hiệu, bản quyền, sáng chế, kiểu dáng, cả trong nước và quốc tế.",
        "card": "Đăng ký nhãn hiệu trong nước và Madrid, bản quyền, sáng chế, xử lý xâm phạm.",
        "overview": "Tài sản trí tuệ ngày càng là giá trị cốt lõi của doanh nghiệp. HTIC tư vấn xác lập, bảo hộ và khai thác quyền sở hữu trí tuệ tại Việt Nam và quốc tế, đồng thời xử lý hành vi xâm phạm, đặc biệt cho doanh nghiệp sản xuất, xuất khẩu và thương hiệu OEM.",
        "scope": [
            ("Tra cứu khả năng bảo hộ", "Tra cứu nhãn hiệu, kiểu dáng, sáng chế trước khi nộp đơn."),
            ("Đăng ký bảo hộ", "Nhãn hiệu, kiểu dáng công nghiệp, sáng chế, quyền tác giả, tên thương mại."),
            ("Đăng ký quốc tế", "Đăng ký nhãn hiệu quốc tế theo Hệ thống Madrid."),
            ("Theo dõi đơn", "Theo dõi đơn, xử lý phản đối, khiếu nại, yêu cầu chấm dứt hiệu lực."),
            ("Xử lý xâm phạm", "Biện pháp hành chính, dân sự; phản đối đơn đăng ký xấu."),
            ("Chuyển giao & li-xăng", "Hợp đồng chuyển giao, li-xăng và định giá tài sản trí tuệ."),
        ],
        "laws": ["Luật Sở hữu trí tuệ và các văn bản sửa đổi, bổ sung", "Thoả ước và Nghị định thư Madrid"],
    },
    {
        "slug": "tu-van-thue-ke-toan", "name": "Thuế & Kế toán", "icon": "calculate",
        "img": "/anh/htic/htic-cover418503887709.jpg",
        "lead": "Tư vấn tuân thủ nghĩa vụ thuế – kế toán, tối ưu chi phí thuế hợp pháp và đại diện làm việc với cơ quan thuế.",
        "card": "Nghĩa vụ thuế, quyết toán, giao dịch liên kết, thanh tra và tranh chấp thuế.",
        "overview": "HTIC kết hợp chuyên môn pháp lý và thuế – kế toán để giúp doanh nghiệp tuân thủ đúng và tối ưu chi phí thuế một cách hợp pháp: rà soát hồ sơ, hỗ trợ quyết toán, đại diện làm việc với cơ quan thuế và tư vấn cấu trúc giao dịch.",
        "scope": [
            ("Nghĩa vụ thuế", "Thuế thu nhập doanh nghiệp, giá trị gia tăng, nhà thầu, thu nhập cá nhân."),
            ("Kê khai & quyết toán", "Rà soát hồ sơ, hoá đơn, chứng từ; hỗ trợ kê khai, quyết toán thuế."),
            ("Thanh tra, kiểm tra thuế", "Đại diện giải trình, làm việc với cơ quan thuế."),
            ("Cấu trúc giao dịch", "Phương án thuế trong M&A, tái cấu trúc, giao dịch xuyên biên giới."),
            ("Giao dịch liên kết", "Chuyển giá và quy định thuế tối thiểu toàn cầu."),
            ("Khiếu nại thuế", "Khiếu nại, giải quyết tranh chấp về thuế."),
        ],
        "laws": ["Luật Quản lý thuế hiện hành", "Các luật thuế chuyên ngành", "Luật Kế toán 2015"],
    },
    {
        "slug": "tu-van-xuat-khau-lao-dong", "name": "Xuất khẩu lao động & Du học", "icon": "flight_takeoff",
        "img": "/anh/htic/tu-van-kcn-long-hau-japan665005815545.jpg",
        "lead": "Tư vấn pháp lý lĩnh vực đưa người lao động Việt Nam đi làm việc ở nước ngoài và tư vấn du học: giấy phép, hợp đồng và bảo vệ quyền lợi.",
        "card": "Giấy phép dịch vụ, hợp đồng cung ứng lao động, du học, thị thực và tranh chấp.",
        "overview": "Đưa người lao động Việt Nam đi làm việc ở nước ngoài và dịch vụ du học đòi hỏi tuân thủ chặt chẽ về giấy phép, hợp đồng và bảo vệ quyền lợi người lao động. HTIC tư vấn pháp lý toàn diện cho doanh nghiệp và cá nhân, giúp vận hành đúng quy định và giảm rủi ro.",
        "scope": [
            ("Giấy phép dịch vụ", "Giấy phép hoạt động dịch vụ đưa người lao động đi làm việc ở nước ngoài."),
            ("Hợp đồng", "Hợp đồng cung ứng, hợp đồng đưa người lao động đi làm việc ở nước ngoài."),
            ("Tuân thủ", "Ký quỹ, đào tạo định hướng, bảo vệ quyền lợi người lao động."),
            ("Thị thực & xuất nhập cảnh", "Thủ tục visa, giấy tờ cho người lao động và người nước ngoài."),
            ("Du học", "Pháp lý dịch vụ tư vấn du học, hợp đồng tư vấn du học."),
            ("Tranh chấp", "Xử lý tranh chấp phát sinh trong quan hệ lao động, dịch vụ."),
        ],
        "laws": ["Luật Người lao động Việt Nam đi làm việc ở nước ngoài theo hợp đồng 2020", "Bộ luật Lao động 2019"],
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
    ("C", "Commitment", "Cam kết", "Đồng hành đến cùng mỗi vụ việc, xem khách hàng là đối tác dài hạn."),
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
