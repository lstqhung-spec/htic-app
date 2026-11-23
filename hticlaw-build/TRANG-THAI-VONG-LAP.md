# Trạng thái vòng lặp An (cập nhật 23/11/2026 14:10 ICT)
- Đợt 1 (nội dung + 12 ảnh): đã áp dụng, đăng.
- Đợt 2 (sửa phạm vi, FAQ, câu dùng chung, form "Soạn email"): đã áp dụng, đăng commit d11e1cddd6093e0437676421347a71db7b1e61b7.
  CHƯA báo An. Khi An xong việc chân dung/logo, gửi An: đợt 2 đã áp dụng; toàn văn 14 trang (gồm trang chủ):
  https://raw.githubusercontent.com/lstqhung-spec/htic-app/d11e1cddd6093e0437676421347a71db7b1e61b7/hticlaw-build/noi-dung-trang-con.md
- Đang chờ An: 16 chân dung làm đẹp (giữ nguyên mặt) + logo mới (màu, trắng, favicon 512).
  Chân dung: WP ảnh nằm /wp-content/uploads/2026/05/<tên>; trang chủ dùng /anh/htic/{hung,lang,khoa,duy}*.jpg.
  Khi nhận: upload vào public_html/anh/chan-dung/<tên gốc đổi đuôi .webp>, cập nhật TEAM_* trong data.py + ảnh đội ngũ trang chủ, build, deploy (window.__deploy(sha) ở tab DA).
  Logo: upload public_html/anh/brand/{logo.png,logo-white.png,favicon.png}; thay /wp-content/uploads/htic-brand/... trong build_pages.py + index.html (header/footer/favicon/JSON-LD). Cân nhắc cũng thay file htic-brand để WP trang tin tức dùng logo mới (sao lưu trước).
- Chờ anh Hưng: địa chỉ/giờ (thẻ quyết định), chữ C, chức danh, số liệu & "miễn phí" trang chủ, logo khách hàng.
- HÀNG CHỜ GỬI AN (khi An rảnh, gửi cùng báo cáo đợt 2): anh Hưng 14:10 yêu cầu "rà lại toàn bộ khách hàng mới/cũ để cập nhật số liệu khách hàng". Nhờ An rà nguồn nội bộ (TIM/SharePoint/hợp đồng) để chốt: số khách hàng doanh nghiệp, số vụ việc/dự án (định nghĩa + kỳ chốt), danh sách khách hàng được phép công bố logo/tên; trả số liệu + nguồn để cập nhật trang chủ (hiện 10+/155/355) và trang Giới thiệu. Không công bố tên/logo khách hàng chưa có đồng ý.
