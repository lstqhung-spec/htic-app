<?php
/**
 * HTIC 2026 — chi tiet bai viet.
 *
 * @package HTIC_Law_Firm
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
htic26_open( 'header-news.html' );
while ( have_posts() ) :
	the_post();
	$pid     = get_the_ID();
	$sec     = htic26_section( $pid );
	$content = apply_filters( 'the_content', get_the_content() );
	$toc     = array();
	$n       = 0;
	$content = preg_replace_callback(
		'/<h2([^>]*)>(.*?)<\/h2>/is',
		function ( $m ) use ( &$toc, &$n ) {
			$n++;
			$id    = 'muc-' . $n;
			$toc[] = array( $id, trim( wp_strip_all_tags( $m[2] ) ) );
			$attrs = preg_replace( '/\sid=("|\')[^"\']*\1/i', '', $m[1] );
			return '<h2 id="' . $id . '"' . $attrs . '>' . $m[2] . '</h2>';
		},
		$content
	);
	$words   = count( preg_split( '/\s+/u', trim( wp_strip_all_tags( $content ) ) ) );
	$minutes = max( 1, (int) round( $words / 230 ) );
	$url     = get_permalink();
	$meta    = '<div class="flex flex-wrap items-center gap-x-space-md gap-y-2 text-[14px] text-blue-100">'
		. '<a class="px-3 py-1 rounded-full bg-white/10 border border-white/20 font-semibold text-white hover:bg-white/20" href="' . esc_url( $sec[1] ) . '">' . esc_html( $sec[0] ) . '</a>'
		. '<span class="flex items-center gap-1">' . htic26_i( 'calendar_today', 'text-[16px] text-[#5aa8e6]' ) . '<time datetime="' . esc_attr( get_the_date( 'c' ) ) . '">' . esc_html( get_the_date( 'd/m/Y' ) ) . '</time></span>'
		. ( get_the_modified_date( 'Y-m-d' ) !== get_the_date( 'Y-m-d' ) ? '<span class="flex items-center gap-1">' . htic26_i( 'update', 'text-[16px] text-[#5aa8e6]' ) . 'Cập nhật ' . esc_html( get_the_modified_date( 'd/m/Y' ) ) . '</span>' : '' )
		. '<span class="flex items-center gap-1">' . htic26_i( 'schedule', 'text-[16px] text-[#5aa8e6]' ) . $minutes . ' phút đọc</span>'
		. '<span class="flex items-center gap-1">' . htic26_i( 'gavel', 'text-[16px] text-[#5aa8e6]' ) . 'Công ty Luật HTIC</span>'
		. '</div>';
	htic26_hero(
		array( array( 'Trang chủ', '/' ), array( 'Tin tức & Bài viết', '/tin-tuc/' ), array( $sec[0], $sec[1] ), array( get_the_title(), '' ) ),
		$sec[0],
		esc_html( get_the_title() ),
		has_excerpt() ? wp_strip_all_tags( get_the_excerpt() ) : '',
		$meta
	);
	?>
<section class="py-space-2xl md:py-space-3xl bg-white">
<div class="max-w-7xl mx-auto px-margin grid grid-cols-1 lg:grid-cols-12 gap-space-2xl">
<article class="lg:col-span-8 min-w-0">
	<?php if ( has_post_thumbnail() ) : ?>
<figure class="mb-space-xl rounded-2xl overflow-hidden bg-[#eef2f8]"><?php the_post_thumbnail( 'large', array( 'class' => 'w-full h-auto', 'fetchpriority' => 'high', 'loading' => 'eager' ) ); ?></figure>
	<?php endif; ?>
<div class="htic-prose"><?php echo $content; // phpcs:ignore ?></div>
	<?php
	$tags = get_the_tags();
	if ( $tags ) :
		?>
<div class="mt-space-xl flex flex-wrap items-center gap-2"><span class="text-[14px] font-bold text-[#16285c] mr-1">Chủ đề:</span>
		<?php foreach ( $tags as $tg ) : ?>
<a class="px-3 py-1 rounded-full bg-[#eef2f8] text-[13px] font-semibold text-[#243e8f] hover:bg-[#243e8f] hover:text-white transition-colors" href="<?php echo esc_url( get_tag_link( $tg->term_id ) ); ?>"><?php echo esc_html( $tg->name ); ?></a>
		<?php endforeach; ?>
</div>
	<?php endif; ?>
<div class="mt-space-xl pt-space-lg border-t border-slate-200 flex flex-wrap items-center gap-space-sm">
<span class="text-[14px] font-bold text-[#16285c]">Chia sẻ:</span>
<a class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg bg-[#1877f2] text-white text-[13px] font-semibold hover:opacity-90" target="_blank" rel="noopener" href="https://www.facebook.com/sharer/sharer.php?u=<?php echo rawurlencode( $url ); ?>">Facebook</a>
<a class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg bg-[#0a66c2] text-white text-[13px] font-semibold hover:opacity-90" target="_blank" rel="noopener" href="https://www.linkedin.com/sharing/share-offsite/?url=<?php echo rawurlencode( $url ); ?>">LinkedIn</a>
<button type="button" class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg border border-slate-200 text-[13px] font-semibold text-[#243e8f] hover:border-[#243e8f]" onclick="navigator.clipboard&&navigator.clipboard.writeText(location.href).then(function(){this.textContent='Đã sao chép liên kết'}.bind(this))"><?php echo htic26_i( 'link', 'text-[18px]' ); // phpcs:ignore ?>Sao chép liên kết</button>
</div>
<div class="mt-space-xl rounded-2xl bg-[#eef2f8] border border-[#d8e1f0] p-space-lg flex flex-col md:flex-row md:items-center justify-between gap-space-md">
<div><p class="text-[18px] font-extrabold text-[#16285c]">Cần áp dụng nội dung này cho trường hợp của doanh nghiệp?</p><p class="text-[15px] text-slate-600 mt-1">Bài viết mang tính tham khảo. Luật sư HTIC sẽ xem xét hồ sơ cụ thể trước khi đưa ra ý kiến pháp lý.</p></div>
<a class="shrink-0 inline-flex items-center gap-2 bg-[#243e8f] hover:bg-[#0f71b9] text-white font-bold px-space-lg py-3 rounded-lg transition-colors" href="/lien-he/">Đặt lịch tư vấn <?php echo htic26_i( 'arrow_forward', 'text-[18px]' ); // phpcs:ignore ?></a>
</div>
</article>
<aside class="lg:col-span-4"><div class="lg:sticky lg:top-[140px] flex flex-col gap-space-lg">
	<?php if ( count( $toc ) > 1 ) : ?>
<nav class="rounded-2xl border border-slate-200 p-space-lg bg-white" aria-label="Mục lục">
<p class="flex items-center gap-2 text-[15px] font-extrabold text-[#16285c] mb-space-sm"><?php echo htic26_i( 'list', 'text-[20px] text-[#0f71b9]' ); // phpcs:ignore ?>Mục lục</p>
<ol class="flex flex-col gap-1 text-[14px] max-h-[50vh] overflow-y-auto pr-1">
		<?php foreach ( $toc as $i => $t ) : ?>
<li><a class="flex gap-2 py-1.5 text-slate-600 hover:text-[#0f71b9] leading-snug" href="#<?php echo esc_attr( $t[0] ); ?>"><span class="text-[#0f71b9] font-bold tabular-nums"><?php echo esc_html( $i + 1 ); ?>.</span><span><?php echo esc_html( $t[1] ); ?></span></a></li>
		<?php endforeach; ?>
</ol></nav>
	<?php endif; ?>
<div class="rounded-2xl bg-[#16285c] text-white p-space-lg flex flex-col gap-space-sm">
<p class="text-[18px] font-extrabold">Trao đổi với luật sư HTIC</p>
<p class="text-[14px] text-blue-100 leading-relaxed">Gửi câu hỏi hoặc tài liệu liên quan, HTIC sẽ liên hệ để làm rõ vấn đề và phạm vi hỗ trợ.</p>
<a class="flex items-center gap-2 font-bold text-[16px]" href="tel:+84379044299"><?php echo htic26_i( 'call', 'text-[20px] text-[#5aa8e6]' ); // phpcs:ignore ?>0379 044 299</a>
<div class="flex gap-2 pt-1"><a class="flex-1 text-center bg-[#0f71b9] hover:bg-white hover:text-[#243e8f] font-bold py-2.5 rounded-lg transition-colors" href="/lien-he/">Đặt lịch</a><a class="flex-1 text-center bg-white/10 hover:bg-white/20 font-bold py-2.5 rounded-lg border border-white/20" target="_blank" rel="noopener" href="https://zalo.me/1450763104944986971">Zalo</a></div>
</div>
</div></aside>
</div>
</section>
	<?php
	$rel = new WP_Query(
		array(
			'post_type'           => 'post',
			'posts_per_page'      => 3,
			'post__not_in'        => array( $pid ),
			'category__in'        => wp_get_post_categories( $pid ),
			'ignore_sticky_posts' => true,
			'no_found_rows'       => true,
		)
	);
	if ( $rel->have_posts() ) :
		?>
<section class="py-space-2xl md:py-space-3xl bg-[#f7f8fa]"><div class="max-w-7xl mx-auto px-margin">
<div class="flex items-end justify-between gap-space-md mb-space-xl"><div class="flex flex-col gap-2"><span class="text-[12px] uppercase tracking-[0.18em] font-bold text-[#0f71b9]">Đọc thêm</span><h2 class="text-[28px] md:text-[32px] leading-tight font-extrabold text-[#243e8f]">Bài viết liên quan</h2></div><a class="shrink-0 inline-flex items-center gap-1 font-bold text-[#0f71b9]" href="<?php echo esc_url( $sec[1] ); ?>">Xem tất cả <?php echo htic26_i( 'arrow_forward', 'text-[18px]' ); // phpcs:ignore ?></a></div>
<div class="grid grid-cols-1 md:grid-cols-3 gap-space-lg">
		<?php
		while ( $rel->have_posts() ) :
			$rel->the_post();
			echo htic26_card( get_the_ID() ); // phpcs:ignore
		endwhile;
		wp_reset_postdata();
		?>
</div></div></section>
		<?php
	endif;
endwhile;
htic26_cta();
htic26_close();
