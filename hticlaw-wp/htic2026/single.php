<?php
/**
 * HTIC 2026 — trang doc bai: tieu de sang ro, cot doc vua mat, muc luc co dinh, thanh tien do doc.
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
	$content = force_balance_tags( $content );
	$words   = count( preg_split( '/\s+/u', trim( wp_strip_all_tags( $content ) ) ) );
	$minutes = max( 1, (int) round( $words / 230 ) );
	$url     = get_permalink();
	$updated = get_the_modified_date( 'Y-m-d' ) !== get_the_date( 'Y-m-d' );
	$is_tin  = 'Tin pháp lý' === $sec[0];
	?>
<div id="readbar" class="fixed left-0 top-0 z-[60] h-[3px] w-full origin-left scale-x-0 bg-[#0f71b9]" aria-hidden="true"></div>
<header class="-mt-[120px] pt-[146px] pb-space-xl bg-[#f4f6fa] border-b border-slate-200">
<div class="max-w-7xl mx-auto px-margin">
<nav class="flex flex-wrap items-center gap-1 text-[14px] text-slate-600" aria-label="Breadcrumb">
<a class="hover:text-[#0f71b9]" href="/">Trang chủ</a><?php echo htic26_i( 'chevron_right', 'text-[16px] opacity-50' ); // phpcs:ignore ?>
<a class="hover:text-[#0f71b9]" href="/tin-tuc/">Tin tức &amp; Bài viết</a><?php echo htic26_i( 'chevron_right', 'text-[16px] opacity-50' ); // phpcs:ignore ?>
<a class="hover:text-[#0f71b9]" href="<?php echo esc_url( $sec[1] ); ?>"><?php echo esc_html( $sec[0] ); ?></a>
</nav>
<div class="hero-in max-w-4xl mt-space-md flex flex-col gap-space-md">
<div class="flex flex-wrap items-center gap-2">
<a class="inline-flex items-center px-2.5 py-1 rounded-md text-[13px] font-bold <?php echo $is_tin ? 'bg-[#e6f1fa] text-[#0b5f9e]' : 'bg-[#eceff7] text-[#243e8f]'; ?>" href="<?php echo esc_url( $sec[1] ); ?>"><?php echo esc_html( $sec[0] ); ?></a>
</div>
<h1 class="text-[28px] md:text-[40px] leading-[1.22] font-extrabold tracking-tight text-[#16285c]"><?php the_title(); ?></h1>
	<?php if ( has_excerpt() ) : ?>
<p class="text-[17px] md:text-[19px] text-slate-600 leading-relaxed"><?php echo esc_html( wp_strip_all_tags( get_the_excerpt() ) ); ?></p>
	<?php endif; ?>
<div class="flex flex-wrap items-center gap-x-space-md gap-y-2 pt-space-xs text-[14px] text-slate-600">
<span class="flex items-center gap-2 font-semibold text-[#16285c]"><img src="/anh/brand/favicon-48.png" alt="" width="28" height="28" class="w-7 h-7 rounded-full bg-white ring-1 ring-slate-200" data-no-lazy="1"/>Công ty Luật HTIC</span>
<span class="flex items-center gap-1"><?php echo htic26_i( 'calendar_today', 'text-[16px] text-slate-400' ); // phpcs:ignore ?>Đăng <time datetime="<?php echo esc_attr( get_the_date( 'c' ) ); ?>"><?php echo esc_html( get_the_date( 'd/m/Y' ) ); ?></time></span>
	<?php if ( $updated ) : ?>
<span class="flex items-center gap-1"><?php echo htic26_i( 'update', 'text-[16px] text-slate-400' ); // phpcs:ignore ?>Cập nhật <time datetime="<?php echo esc_attr( get_the_modified_date( 'c' ) ); ?>"><?php echo esc_html( get_the_modified_date( 'd/m/Y' ) ); ?></time></span>
	<?php endif; ?>
<span class="flex items-center gap-1"><?php echo htic26_i( 'schedule', 'text-[16px] text-slate-400' ); // phpcs:ignore ?><?php echo (int) $minutes; ?> phút đọc</span>
</div>
</div>
</div>
</header>

<div class="bg-white">
<div class="max-w-7xl mx-auto px-margin py-space-xl md:py-space-2xl grid grid-cols-1 lg:grid-cols-[240px_minmax(0,1fr)] xl:grid-cols-[240px_minmax(0,1fr)_280px] gap-space-xl xl:gap-space-2xl">

<aside class="hidden lg:block" aria-label="Mục lục">
	<?php if ( count( $toc ) > 1 ) : ?>
<nav id="toc" class="sticky top-[140px] max-h-[calc(100vh-170px)] overflow-y-auto pr-2">
<p class="text-[12px] font-extrabold uppercase tracking-[0.16em] text-[#0f71b9] mb-space-sm">Nội dung bài</p>
<ol class="flex flex-col border-l-2 border-slate-200 text-[14px]">
		<?php foreach ( $toc as $i => $t ) : ?>
<li><a class="block -ml-[2px] border-l-2 border-transparent pl-3 py-1.5 leading-snug text-slate-600 hover:text-[#0f71b9] hover:border-slate-400" href="#<?php echo esc_attr( $t[0] ); ?>"><?php echo esc_html( $t[1] ); ?></a></li>
		<?php endforeach; ?>
</ol>
</nav>
	<?php endif; ?>
</aside>

<article class="min-w-0 max-w-[760px] w-full mx-auto lg:mx-0">
	<?php if ( count( $toc ) > 1 ) : ?>
<details class="lg:hidden mb-space-lg rounded-xl border border-slate-200 bg-[#f7f8fa]">
<summary class="list-none cursor-pointer flex items-center justify-between px-space-md py-3 font-bold text-[#16285c]"><span class="flex items-center gap-2"><?php echo htic26_i( 'list', 'text-[20px] text-[#0f71b9]' ); // phpcs:ignore ?>Nội dung bài (<?php echo count( $toc ); ?> mục)</span><?php echo htic26_i( 'expand_more', 'text-[20px] text-slate-600' ); // phpcs:ignore ?></summary>
<ol class="px-space-md pb-space-md flex flex-col gap-1 text-[15px]">
		<?php foreach ( $toc as $i => $t ) : ?>
<li><a class="flex gap-2 py-1.5 text-slate-700" href="#<?php echo esc_attr( $t[0] ); ?>"><span class="text-[#0f71b9] font-bold tabular-nums"><?php echo (int) $i + 1; ?>.</span><span><?php echo esc_html( $t[1] ); ?></span></a></li>
		<?php endforeach; ?>
</ol>
</details>
	<?php endif; ?>
	<?php if ( has_post_thumbnail() ) : ?>
<figure class="mb-space-xl rounded-2xl overflow-hidden bg-[#eef2f8]"><?php the_post_thumbnail( 'large', array( 'class' => 'w-full h-auto', 'fetchpriority' => 'high', 'loading' => 'eager', 'data-no-lazy' => '1' ) ); ?></figure>
	<?php endif; ?>
<div class="htic-prose"><?php echo $content; // phpcs:ignore ?></div>

<div class="mt-space-xl rounded-xl border-l-4 border-[#0f71b9] bg-[#f4f6fa] px-space-md py-space-sm text-[14px] leading-relaxed text-slate-600">
<strong class="text-[#16285c]">Lưu ý:</strong> Bài viết cung cấp thông tin pháp lý tham khảo theo quy định có hiệu lực tại thời điểm đăng<?php echo $updated ? ' hoặc cập nhật' : ''; ?>, không thay thế ý kiến tư vấn cho trường hợp cụ thể.
</div>
	<?php
	$tags = get_the_tags();
	if ( $tags ) :
		?>
<div class="mt-space-lg flex flex-wrap items-center gap-2"><span class="text-[14px] font-bold text-[#16285c] mr-1">Chủ đề:</span>
		<?php foreach ( $tags as $tg ) : ?>
<a class="px-3 py-1 rounded-full bg-[#eef2f8] text-[13px] font-semibold text-[#243e8f] hover:bg-[#243e8f] hover:text-white transition-colors" href="<?php echo esc_url( get_tag_link( $tg->term_id ) ); ?>"><?php echo esc_html( $tg->name ); ?></a>
		<?php endforeach; ?>
</div>
	<?php endif; ?>
<div class="mt-space-lg pt-space-lg border-t border-slate-200 flex flex-wrap items-center gap-space-sm">
<span class="text-[14px] font-bold text-[#16285c]">Chia sẻ:</span>
<a class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg bg-[#1466d6] text-white text-[13px] font-semibold hover:opacity-90" target="_blank" rel="noopener" href="https://www.facebook.com/sharer/sharer.php?u=<?php echo rawurlencode( $url ); ?>">Facebook</a>
<a class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg bg-[#0a66c2] text-white text-[13px] font-semibold hover:opacity-90" target="_blank" rel="noopener" href="https://www.linkedin.com/sharing/share-offsite/?url=<?php echo rawurlencode( $url ); ?>">LinkedIn</a>
<button type="button" class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg border border-slate-200 text-[13px] font-semibold text-[#243e8f] hover:border-[#243e8f]" onclick="var b=this;navigator.clipboard&&navigator.clipboard.writeText(location.href).then(function(){b.lastChild.textContent='Đã sao chép'})"><?php echo htic26_i( 'link', 'text-[18px]' ); // phpcs:ignore ?><span>Sao chép liên kết</span></button>
</div>
<div class="mt-space-xl rounded-2xl bg-[#16285c] text-white p-space-lg flex flex-col md:flex-row md:items-center justify-between gap-space-md">
<div><p class="text-[18px] font-extrabold">Cần áp dụng nội dung này cho doanh nghiệp của Quý khách?</p><p class="text-[15px] text-blue-100 mt-1">Luật sư HTIC sẽ xem xét hồ sơ cụ thể trước khi đưa ra ý kiến pháp lý.</p></div>
<a class="shrink-0 inline-flex items-center gap-2 bg-white text-[#243e8f] hover:bg-[#0f71b9] hover:text-white font-bold px-space-lg py-3 rounded-lg transition-colors" href="/lien-he/">Đặt lịch tư vấn <?php echo htic26_i( 'arrow_forward', 'text-[18px]' ); // phpcs:ignore ?></a>
</div>
</article>

<aside class="hidden xl:block" aria-label="Liên hệ và bài mới">
<div class="sticky top-[140px] flex flex-col gap-space-lg">
<div class="rounded-2xl border border-slate-200 p-space-lg flex flex-col gap-space-sm">
<p class="text-[16px] font-extrabold text-[#16285c]">Trao đổi với luật sư</p>
<p class="text-[14px] text-slate-600 leading-relaxed">Gửi câu hỏi hoặc tài liệu, HTIC sẽ liên hệ để làm rõ vấn đề.</p>
<a class="flex items-center gap-2 font-bold text-[#243e8f]" href="tel:+84379044299"><?php echo htic26_i( 'call', 'text-[20px] text-[#0f71b9]' ); // phpcs:ignore ?>0379 044 299</a>
<div class="flex gap-2"><a class="flex-1 text-center bg-[#243e8f] hover:bg-[#0f71b9] text-white text-[14px] font-bold py-2.5 rounded-lg" href="/lien-he/">Đặt lịch</a><a class="flex-1 text-center border border-slate-200 hover:border-[#243e8f] text-[#243e8f] text-[14px] font-bold py-2.5 rounded-lg" target="_blank" rel="noopener" href="https://zalo.me/1450763104944986971">Zalo</a></div>
</div>
	<?php
	$latest = new WP_Query( array( 'post_type' => 'post', 'posts_per_page' => 4, 'post__not_in' => array( $pid ), 'category__in' => array( 4, 59 ), 'ignore_sticky_posts' => true, 'no_found_rows' => true ) );
	if ( $latest->have_posts() ) :
		?>
<div class="rounded-2xl border border-slate-200 p-space-lg"><p class="text-[16px] font-extrabold text-[#16285c] mb-1">Bài mới</p><ul>
		<?php
		while ( $latest->have_posts() ) :
			$latest->the_post();
			?>
<li class="py-space-sm border-b border-slate-100 last:border-0"><a class="group block" href="<?php the_permalink(); ?>"><time class="text-[12px] font-semibold text-slate-600"><?php echo esc_html( get_the_date( 'd/m/Y' ) ); ?></time><span class="block text-[14px] leading-snug font-semibold text-[#16285c] group-hover:text-[#0f71b9] line-clamp-3"><?php the_title(); ?></span></a></li>
			<?php
		endwhile;
		wp_reset_postdata();
		?>
</ul></div>
	<?php endif; ?>
</div>
</aside>

</div>
</div>
	<?php
	$rel = new WP_Query(
		array(
			'post_type'           => 'post',
			'posts_per_page'      => 4,
			'post__not_in'        => array( $pid ),
			'category__in'        => wp_get_post_categories( $pid ),
			'ignore_sticky_posts' => true,
			'no_found_rows'       => true,
		)
	);
	if ( $rel->have_posts() ) :
		?>
<section class="py-space-2xl bg-[#f4f6fa] border-t border-slate-200"><div class="max-w-7xl mx-auto px-margin">
<div class="flex items-end justify-between gap-space-md mb-space-md"><h2 class="text-[24px] md:text-[28px] leading-tight font-extrabold text-[#16285c]">Đọc tiếp cùng chủ đề</h2><a class="shrink-0 inline-flex items-center gap-1 font-bold text-[#0f71b9]" href="<?php echo esc_url( $sec[1] ); ?>">Xem tất cả <?php echo htic26_i( 'arrow_forward', 'text-[18px]' ); // phpcs:ignore ?></a></div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-x-space-2xl bg-white rounded-2xl border border-slate-200 px-space-lg">
		<?php
		while ( $rel->have_posts() ) :
			$rel->the_post();
			echo htic26_row( get_the_ID() ); // phpcs:ignore
		endwhile;
		wp_reset_postdata();
		?>
</div></div></section>
		<?php
	endif;
endwhile;
?>
<script>
(function(){var bar=document.getElementById('readbar'),art=document.querySelector('.htic-prose'),toc=document.getElementById('toc');
function upd(){if(!art)return;var r=art.getBoundingClientRect(),h=r.height-innerHeight*0.6,p=h>0?Math.min(1,Math.max(0,-r.top+140)/h):1;bar.style.transform='scaleX('+p+')'}
addEventListener('scroll',upd,{passive:true});upd();
if(toc&&'IntersectionObserver' in window){var links={};toc.querySelectorAll('a').forEach(function(a){links[a.getAttribute('href').slice(1)]=a});
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){toc.querySelectorAll('a').forEach(function(a){a.classList.remove('text-[#0f71b9]','font-bold','border-[#0f71b9]')});var a=links[e.target.id];if(a){a.classList.add('text-[#0f71b9]','font-bold','border-[#0f71b9]')}}})},{rootMargin:'-140px 0px -65% 0px'});
Object.keys(links).forEach(function(id){var h=document.getElementById(id);if(h)io.observe(h)})}})();
</script>
<?php
htic26_close();
