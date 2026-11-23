<?php
/**
 * HTIC 2026 — khong tim thay trang.
 *
 * @package HTIC_Law_Firm
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
htic26_open();
htic26_hero( array( array( 'Trang chủ', '/' ), array( 'Không tìm thấy trang', '' ) ), 'Lỗi 404', 'Không tìm thấy trang', 'Trang bạn tìm có thể đã được di chuyển hoặc không còn tồn tại. Vui lòng quay về trang chủ, tìm bài viết hoặc liên hệ HTIC.' );
?>
<section class="py-space-2xl md:py-space-3xl bg-white"><div class="max-w-7xl mx-auto px-margin flex flex-col gap-space-xl">
<div class="flex flex-col md:flex-row md:items-center gap-space-md">
<a class="inline-flex items-center gap-2 bg-[#243e8f] hover:bg-[#0f71b9] text-white font-bold px-space-lg py-3 rounded-lg" href="/"><?php echo htic26_i( 'home', 'text-[18px]' ); // phpcs:ignore ?>Về trang chủ</a>
<a class="inline-flex items-center gap-2 border border-[#243e8f] text-[#243e8f] font-bold px-space-lg py-3 rounded-lg hover:bg-[#243e8f] hover:text-white" href="/dich-vu/">Lĩnh vực dịch vụ</a>
<?php echo htic26_search_form(); // phpcs:ignore ?>
</div>
<?php
$latest = new WP_Query( array( 'post_type' => 'post', 'posts_per_page' => 3, 'category__in' => array( 4, 59 ), 'ignore_sticky_posts' => true, 'no_found_rows' => true ) );
if ( $latest->have_posts() ) :
	?>
<div><h2 class="text-[24px] font-extrabold text-[#243e8f] mb-space-lg">Bài viết mới</h2><div class="grid grid-cols-1 md:grid-cols-3 gap-space-lg">
	<?php
	while ( $latest->have_posts() ) :
		$latest->the_post();
		echo htic26_card( get_the_ID() ); // phpcs:ignore
	endwhile;
	wp_reset_postdata();
	?>
</div></div>
<?php endif; ?>
</div></section>
<?php
htic26_close();
