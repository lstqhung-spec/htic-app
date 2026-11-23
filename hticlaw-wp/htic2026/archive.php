<?php
/**
 * HTIC 2026 — chuyen muc, the, tac gia, luu tru, tim kiem.
 *
 * @package HTIC_Law_Firm
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
htic26_open( 'header-news.html' );
$q = get_search_query();
if ( is_search() ) {
	$title = 'Kết quả tìm kiếm: “' . esc_html( $q ) . '”';
	$crumb = 'Tìm kiếm';
	$lead  = sprintf( 'Tìm thấy %d bài phù hợp.', (int) $GLOBALS['wp_query']->found_posts );
} elseif ( is_category() || is_tag() || is_tax() ) {
	$title = esc_html( single_term_title( '', false ) );
	$crumb = single_term_title( '', false );
	$desc  = wp_strip_all_tags( term_description() );
	$lead  = $desc ? $desc : 'Các bài viết pháp lý do luật sư Công ty Luật HTIC biên soạn thuộc chủ đề này.';
} elseif ( is_home() ) {
	$title = 'Tin tức &amp; Bài viết pháp lý';
	$crumb = 'Tin tức & Bài viết';
	$lead  = 'Tin pháp luật mới và bài phân tích chuyên sâu của luật sư HTIC.';
} else {
	$title = esc_html( wp_strip_all_tags( get_the_archive_title() ) );
	$crumb = wp_strip_all_tags( get_the_archive_title() );
	$lead  = 'Các bài viết pháp lý của Công ty Luật HTIC.';
}
htic26_hero( array( array( 'Trang chủ', '/' ), array( 'Tin tức & Bài viết', '/tin-tuc/' ), array( $crumb, '' ) ), 'Tin tức & Bài viết', $title, $lead );
?>
<section class="py-space-2xl md:py-space-3xl bg-[#f7f8fa]"><div class="max-w-7xl mx-auto px-margin">
<div class="flex flex-col md:flex-row md:items-center justify-between gap-space-md mb-space-xl">
<div class="flex flex-wrap gap-2"><a class="px-space-md py-2 rounded-full text-[14px] font-bold border bg-white text-[#243e8f] border-slate-200 hover:border-[#243e8f]" href="/tin-phap-ly/">Tin pháp lý</a><a class="px-space-md py-2 rounded-full text-[14px] font-bold border bg-white text-[#243e8f] border-slate-200 hover:border-[#243e8f]" href="/bai-viet-phap-ly/">Bài viết pháp lý</a></div>
<?php echo htic26_search_form( $q ); // phpcs:ignore ?>
</div>
<?php if ( have_posts() ) : ?>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-space-lg">
	<?php
	while ( have_posts() ) :
		the_post();
		echo htic26_card( get_the_ID() ); // phpcs:ignore
	endwhile;
	?>
</div>
	<?php
	$links = paginate_links( array( 'type' => 'array', 'mid_size' => 1, 'prev_text' => '‹', 'next_text' => '›' ) );
	if ( $links ) :
		?>
<nav class="htic-pages mt-space-2xl flex flex-wrap justify-center gap-2" aria-label="Phân trang"><?php echo implode( '', $links ); // phpcs:ignore ?></nav>
	<?php endif; ?>
<?php else : ?>
<div class="text-center py-space-2xl"><p class="text-[18px] font-bold text-[#16285c]">Chưa có bài viết phù hợp.</p><p class="text-slate-600 mt-2">Thử từ khóa khác hoặc xem <a class="text-[#0f71b9] font-semibold" href="/tin-tuc/">tất cả tin tức &amp; bài viết</a>.</p></div>
<?php endif; ?>
</div></section>
<?php
htic26_cta();
htic26_close();
