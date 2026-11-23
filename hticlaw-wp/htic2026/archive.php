<?php
/**
 * HTIC 2026 — chuyen muc, the, luu tru, tim kiem: danh sach theo dong, nhom theo thang.
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
	$lead  = sprintf( 'Tìm thấy %d bài phù hợp, mới nhất trước.', (int) $GLOBALS['wp_query']->found_posts );
} elseif ( is_category() || is_tag() || is_tax() ) {
	$title = esc_html( single_term_title( '', false ) );
	$crumb = single_term_title( '', false );
	$desc  = wp_strip_all_tags( term_description() );
	$lead  = $desc ? $desc : 'Các bài viết pháp lý do luật sư Công ty Luật HTIC biên soạn thuộc chủ đề này, mới nhất trước.';
} elseif ( is_home() ) {
	$title = 'Tin tức &amp; Bài viết pháp lý';
	$crumb = 'Tin tức & Bài viết';
	$lead  = 'Tin pháp luật mới và bài phân tích chuyên sâu của luật sư HTIC.';
} else {
	$title = esc_html( wp_strip_all_tags( get_the_archive_title() ) );
	$crumb = wp_strip_all_tags( get_the_archive_title() );
	$lead  = 'Các bài viết pháp lý của Công ty Luật HTIC.';
}
?>
<header class="-mt-[120px] pt-[146px] pb-space-lg bg-[#f4f6fa] border-b border-slate-200">
<div class="max-w-7xl mx-auto px-margin">
<nav class="flex flex-wrap items-center gap-1 text-[14px] text-slate-500" aria-label="Breadcrumb"><a class="hover:text-[#0f71b9]" href="/">Trang chủ</a><?php echo htic26_i( 'chevron_right', 'text-[16px] opacity-50' ); // phpcs:ignore ?><a class="hover:text-[#0f71b9]" href="/tin-tuc/">Tin tức &amp; Bài viết</a><?php echo htic26_i( 'chevron_right', 'text-[16px] opacity-50' ); // phpcs:ignore ?><span class="text-slate-700"><?php echo esc_html( $crumb ); ?></span></nav>
<div class="hero-in mt-space-md flex flex-col gap-space-sm max-w-3xl">
<h1 class="text-[30px] md:text-[40px] leading-tight font-extrabold tracking-tight text-[#16285c]"><?php echo $title; // phpcs:ignore ?></h1>
<p class="text-[16px] md:text-[17px] text-slate-600 leading-relaxed"><?php echo esc_html( $lead ); ?></p>
</div>
<nav class="mt-space-lg inline-flex flex-wrap gap-1 p-1 rounded-xl bg-[#e8ecf4]" aria-label="Loại bài"><a class="px-space-md py-2 rounded-lg text-[14px] font-bold text-[#243e8f] hover:bg-white" href="/tin-tuc/">Tất cả</a><a class="px-space-md py-2 rounded-lg text-[14px] font-bold text-[#243e8f] hover:bg-white" href="/tin-phap-ly/">Tin pháp lý</a><a class="px-space-md py-2 rounded-lg text-[14px] font-bold text-[#243e8f] hover:bg-white" href="/bai-viet-phap-ly/">Bài viết pháp lý</a></nav>
</div>
</header>
<section class="py-space-lg md:py-space-xl bg-white"><div class="max-w-7xl mx-auto px-margin grid grid-cols-1 lg:grid-cols-12 gap-space-2xl">
<div class="lg:col-span-8 min-w-0">
<?php echo htic26_search_form( $q ); // phpcs:ignore ?>
<?php if ( have_posts() ) : ?>
<div class="mt-space-sm">
	<?php
	$last = '';
	while ( have_posts() ) :
		the_post();
		$mk = get_the_date( 'Y-m' );
		if ( $mk !== $last ) {
			$last = $mk;
			echo '<h2 class="pt-space-lg pb-1 text-[12px] font-extrabold uppercase tracking-[0.16em] text-[#0f71b9] flex items-center gap-3">Tháng ' . esc_html( get_the_date( 'n/Y' ) ) . '<span class="flex-1 h-px bg-slate-200"></span></h2>';
		}
		echo htic26_row( get_the_ID() ); // phpcs:ignore
	endwhile;
	?>
</div>
	<?php
	$links = paginate_links( array( 'type' => 'array', 'mid_size' => 1, 'prev_text' => '‹', 'next_text' => '›' ) );
	if ( $links ) :
		?>
<nav class="htic-pages mt-space-xl flex flex-wrap justify-center gap-2" aria-label="Phân trang"><?php echo implode( '', $links ); // phpcs:ignore ?></nav>
	<?php endif; ?>
<?php else : ?>
<div class="text-center py-space-2xl"><p class="text-[18px] font-bold text-[#16285c]">Chưa có bài viết phù hợp.</p><p class="text-slate-600 mt-2">Thử từ khóa khác hoặc xem <a class="text-[#0f71b9] font-semibold" href="/tin-tuc/">tất cả tin tức &amp; bài viết</a>.</p></div>
<?php endif; ?>
</div>
<aside class="lg:col-span-4"><div class="lg:sticky lg:top-[140px] flex flex-col gap-space-lg">
<div class="rounded-2xl bg-[#16285c] text-white p-space-lg flex flex-col gap-space-sm">
<p class="text-[18px] font-extrabold">Cần áp dụng cho trường hợp cụ thể?</p>
<p class="text-[14px] text-blue-100 leading-relaxed">Bài viết mang tính tham khảo. Gửi hồ sơ để luật sư HTIC xem xét và tư vấn đúng tình huống của Quý khách.</p>
<a class="flex items-center gap-2 font-bold text-[16px]" href="tel:+84379044299"><?php echo htic26_i( 'call', 'text-[20px] text-[#5aa8e6]' ); // phpcs:ignore ?>0379 044 299</a>
<div class="flex gap-2 pt-1"><a class="flex-1 text-center bg-[#0f71b9] hover:bg-white hover:text-[#243e8f] font-bold py-2.5 rounded-lg transition-colors" href="/lien-he/">Đặt lịch</a><a class="flex-1 text-center bg-white/10 hover:bg-white/20 font-bold py-2.5 rounded-lg border border-white/20" target="_blank" rel="noopener" href="https://zalo.me/1450763104944986971">Zalo</a></div>
</div>
</div></aside>
</div></section>
<?php
htic26_close();
