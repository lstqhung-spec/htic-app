<?php
/**
 * HTIC 2026 — dua cac trang WordPress tieng Viet (bai viet, trang, chuyen muc, tim kiem, 404)
 * ve cung bo khung voi website tinh moi (header/footer/CSS chung trong /assets/wp/).
 * Tat: xoa thu muc /assets/wp/ hoac bo dong require trong functions.php.
 *
 * @package HTIC_Law_Firm
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'HTIC26_VER', '20261123f' );

function htic26_path() {
	$p = isset( $_SERVER['REQUEST_URI'] ) ? (string) $_SERVER['REQUEST_URI'] : '/';
	$q = strpos( $p, '?' );
	return false === $q ? $p : substr( $p, 0, $q );
}

function htic26_is_vi() {
	return ! preg_match( '#^/(en|ja|ko|zh-cn|zh)(/|$)#i', htic26_path() );
}

function htic26_file( $name ) {
	$f = ABSPATH . 'assets/wp/' . $name;
	return is_readable( $f ) ? (string) file_get_contents( $f ) : '';
}

function htic26_ready() {
	return '' !== htic26_file( 'header.html' ) && '' !== htic26_file( 'footer.html' );
}

function htic26_i( $name, $cls = 'text-[20px]' ) {
	return '<span class="material-symbols-outlined ' . esc_attr( $cls ) . '" aria-hidden="true">' . esc_html( $name ) . '</span>';
}

/* Don cache LiteSpeed mot lan moi khi doi phien ban bo khung. */
add_action( 'init', function () {
	if ( get_option( 'htic26_ver' ) !== HTIC26_VER ) {
		update_option( 'htic26_ver', HTIC26_VER, false );
		do_action( 'litespeed_purge_all' );
	}
} );

/* Chuyen huong 301 cac trang WordPress cu da co trang moi thay the. */
add_action( 'init', function () {
	if ( is_admin() || wp_doing_ajax() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) || 'GET' !== ( isset( $_SERVER['REQUEST_METHOD'] ) ? $_SERVER['REQUEST_METHOD'] : 'GET' ) ) {
		return;
	}
	$map = array(
		'/bai-viet/'                       => '/bai-viet-phap-ly/',
		'/tintuc/'                         => '/tin-phap-ly/',
		'/doi-ngu/'                        => '/gioi-thieu/#doi-ngu',
		'/dich-vu/so-huu-tri-tue/'         => '/dich-vu/tu-van-so-huu-tri-tue/',
		'/dich-vu/hop-dong/'               => '/dich-vu/tu-van-hop-dong/',
		'/dich-vu/tu-van-doanh-nghiep/'    => '/dich-vu/tu-van-phap-ly-doanh-nghiep/',
		'/dich-vu/dau-tu-irc/'             => '/dich-vu/tu-van-ma-dau-tu/',
		'/dich-vu/thue-ke-toan/'           => '/dich-vu/tu-van-thue-ke-toan/',
		'/dich-vu/tranh-tung/'             => '/dich-vu/luat-su-tranh-tung/',
		'/dich-vu/phap-che-thue-ngoai/'    => '/dich-vu/tu-van-phap-ly-doanh-nghiep/',
		'/dich-vu/giay-phep-odi/'          => '/dich-vu/tu-van-giay-phep-tuan-thu/',
		'/dich-vu/m-and-a/'                => '/dich-vu/tu-van-ma-dau-tu/',
		'/dich-vu/bat-dong-san-xay-dung/'  => '/dich-vu/luat-su-bat-dong-san-xay-dung/',
	);
	$k = rtrim( htic26_path(), '/' ) . '/';
	if ( isset( $map[ $k ] ) ) {
		wp_safe_redirect( home_url( $map[ $k ] ), 301 );
		exit;
	}
}, 0 );

/* Chon template moi cho trang tieng Viet. */
add_filter( 'template_include', function ( $t ) {
	if ( is_admin() || is_feed() || is_embed() || is_front_page() || ! htic26_is_vi() || ! htic26_ready() ) {
		return $t;
	}
	if ( is_singular( 'post' ) ) {
		$n = 'single.php';
	} elseif ( is_page() ) {
		$n = 'page.php';
	} elseif ( is_404() ) {
		$n = '404.php';
	} elseif ( is_search() || is_archive() || is_home() ) {
		$n = 'archive.php';
	} else {
		return $t;
	}
	$f = get_template_directory() . '/htic2026/' . $n;
	if ( ! is_readable( $f ) ) {
		return $t;
	}
	$GLOBALS['htic26_on'] = true;
	return $f;
}, 99 );

/* Bo CSS/JS cua giao dien cu tren cac trang dung bo khung moi. */
add_action( 'wp_enqueue_scripts', function () {
	if ( empty( $GLOBALS['htic26_on'] ) ) {
		return;
	}
	global $wp_styles, $wp_scripts;
	if ( $wp_styles instanceof WP_Styles ) {
		foreach ( (array) $wp_styles->queue as $h ) {
			$src = isset( $wp_styles->registered[ $h ] ) ? (string) $wp_styles->registered[ $h ]->src : '';
			if ( false !== strpos( $src, '/themes/' ) || 0 === strpos( $h, 'htic' ) ) {
				wp_dequeue_style( $h );
			}
		}
	}
	if ( $wp_scripts instanceof WP_Scripts ) {
		foreach ( (array) $wp_scripts->queue as $h ) {
			$src = isset( $wp_scripts->registered[ $h ] ) ? (string) $wp_scripts->registered[ $h ]->src : '';
			if ( false !== strpos( $src, '/themes/' ) ) {
				wp_dequeue_script( $h );
			}
		}
	}
}, 9999 );

/* ------------------------------------------------------------ khung trang */
function htic26_open( $header = 'header.html' ) {
	?><!DOCTYPE html>
<html <?php language_attributes(); ?> class="scroll-smooth">
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<?php echo htic26_file( 'head.html' ); // phpcs:ignore ?>
<?php wp_head(); ?>
</head>
<body <?php body_class( 'bg-white text-text-primary antialiased' ); ?>>
<?php wp_body_open(); ?>
<a class="sr-only focus:not-sr-only" href="#noi-dung">Bỏ qua đến nội dung</a>
<?php echo htic26_file( $header ); // phpcs:ignore ?>
<main id="noi-dung" class="w-full pt-[120px]">
	<?php
}

function htic26_close() {
	?>
</main>
<?php echo htic26_file( 'footer.html' ); // phpcs:ignore ?>
<?php wp_footer(); ?>
</body></html>
	<?php
}

/* Chuyen muc chinh cua bai: [ten, duong dan]. */
function htic26_section( $pid ) {
	$ids = wp_get_post_categories( $pid );
	if ( in_array( 4, array_map( "intval", $ids ), true ) ) {
		return array( 'Tin pháp lý', '/tin-phap-ly/' );
	}
	if ( in_array( 59, array_map( "intval", $ids ), true ) ) {
		return array( 'Bài viết pháp lý', '/bai-viet-phap-ly/' );
	}
	$c = get_the_category( $pid );
	return array( $c ? $c[0]->name : 'Tin tức', '/tin-tuc/' );
}

function htic26_crumbs( $items ) {
	$out = '<nav class="flex flex-wrap items-center gap-1 text-[14px] text-blue-100/80" aria-label="Breadcrumb">';
	$n   = count( $items );
	foreach ( $items as $i => $it ) {
		if ( $i === $n - 1 ) {
			$out .= '<span class="text-white line-clamp-1" aria-current="page">' . esc_html( $it[0] ) . '</span>';
		} else {
			$out .= '<a class="hover:text-white" href="' . esc_url( $it[1] ) . '">' . esc_html( $it[0] ) . '</a>' . htic26_i( 'chevron_right', 'text-[16px] opacity-60' );
		}
	}
	return $out . '</nav>';
}

function htic26_hero( $crumbs, $eyebrow, $title_html, $lead = '', $meta = '' ) {
	?>
<section class="relative -mt-[120px] pt-[150px] pb-space-2xl md:pb-space-3xl bg-[#16285c] text-white overflow-hidden">
<img alt="" aria-hidden="true" class="absolute inset-0 w-full h-full object-cover opacity-30" src="/anh/htic/htic-cover418503887709.jpg" fetchpriority="high"/>
<div class="absolute inset-0 bg-gradient-to-r from-[#16285c] via-[#16285c]/92 to-[#243e8f]/70"></div>
<div class="relative max-w-7xl mx-auto px-margin">
<?php echo htic26_crumbs( $crumbs ); // phpcs:ignore ?>
<div class="hero-in max-w-4xl flex flex-col gap-space-md mt-space-lg">
<span class="text-[12px] uppercase tracking-[0.18em] font-bold text-[#5aa8e6]"><?php echo esc_html( $eyebrow ); ?></span>
<h1 class="text-[30px] md:text-[42px] leading-[1.18] font-extrabold tracking-tight"><?php echo $title_html; // phpcs:ignore ?></h1>
<?php if ( $lead ) : ?><p class="text-[17px] md:text-[18px] text-blue-100 leading-relaxed max-w-3xl"><?php echo esc_html( $lead ); ?></p><?php endif; ?>
<?php echo $meta; // phpcs:ignore ?>
</div>
</div>
</section>
	<?php
}

function htic26_card( $pid ) {
	$img = get_the_post_thumbnail_url( $pid, 'medium_large' );
	if ( ! $img ) {
		$img = '/anh/htic/htic-cover418503887709.jpg';
	}
	$sec = htic26_section( $pid );
	$l   = get_permalink( $pid );
	$ex  = wp_trim_words( wp_strip_all_tags( get_the_excerpt( $pid ) ), 34, '…' );
	return '<article class="group flex flex-col bg-white rounded-2xl border border-slate-200 overflow-hidden hover:border-[#0f71b9]/40 hover:shadow-[0_16px_40px_rgba(36,62,143,0.12)] transition-all duration-300">'
		. '<a class="block aspect-[16/9] overflow-hidden bg-[#eef2f8]" href="' . esc_url( $l ) . '" tabindex="-1" aria-hidden="true"><img loading="lazy" decoding="async" alt="" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" src="' . esc_url( $img ) . '"/></a>'
		. '<div class="flex flex-col gap-space-xs p-space-md flex-1">'
		. '<div class="flex items-center gap-2 text-[12px] font-semibold text-slate-500"><span class="px-2 py-0.5 rounded-full bg-[#eef2f8] text-[#243e8f]">' . esc_html( $sec[0] ) . '</span><time datetime="' . esc_attr( get_the_date( 'Y-m-d', $pid ) ) . '">' . esc_html( get_the_date( 'd/m/Y', $pid ) ) . '</time></div>'
		. '<h3 class="text-[17px] leading-snug font-bold text-[#16285c] group-hover:text-[#0f71b9] transition-colors"><a href="' . esc_url( $l ) . '">' . esc_html( get_the_title( $pid ) ) . '</a></h3>'
		. '<p class="text-[14px] text-slate-600 leading-relaxed line-clamp-3">' . esc_html( $ex ) . '</p>'
		. '<a class="mt-auto pt-space-xs inline-flex items-center gap-1 text-[14px] font-bold text-[#0f71b9]" href="' . esc_url( $l ) . '">Đọc tiếp ' . htic26_i( 'arrow_forward', 'text-[16px]' ) . '</a>'
		. '</div></article>';
}

function htic26_search_form( $value = '' ) {
	return '<form action="' . esc_url( home_url( '/index.php' ) ) . '" method="get" role="search" class="flex items-center gap-2 bg-white border border-slate-200 rounded-full pl-4 pr-1 py-1 w-full md:w-[380px] focus-within:border-[#0f71b9]">'
		. '<label class="sr-only" for="htic-s">Tìm bài viết</label>' . htic26_i( 'search', 'text-[20px] text-slate-400' )
		. '<input id="htic-s" name="s" value="' . esc_attr( $value ) . '" class="flex-1 bg-transparent border-0 focus:ring-0 text-[15px] py-1.5 outline-none" placeholder="Tìm theo từ khóa, số hiệu văn bản…"/>'
		. '<button class="bg-[#243e8f] hover:bg-[#0f71b9] text-white text-[14px] font-bold px-4 py-2 rounded-full">Tìm</button></form>'
		. '<script>document.currentScript.previousElementSibling.addEventListener("submit",function(e){var v=this.elements.s.value.trim();if(v){e.preventDefault();location.href="/search/"+encodeURIComponent(v).replace(/%20/g,"+")+"/"}})</script>';
}

function htic26_cta() {
	$tel = '+84379044299';
	?>
<section class="py-space-2xl md:py-space-3xl bg-white"><div class="max-w-7xl mx-auto px-margin">
<div class="relative overflow-hidden rounded-3xl bg-gradient-to-br from-[#243e8f] to-[#16285c] text-white p-space-xl md:p-space-2xl flex flex-col lg:flex-row items-start lg:items-center justify-between gap-space-lg">
<div class="max-w-2xl flex flex-col gap-space-sm"><h2 class="text-[26px] md:text-[32px] font-extrabold leading-tight">Cần tư vấn cho một vấn đề pháp lý cụ thể?</h2><p class="text-blue-100 text-[16px] leading-relaxed">Gửi thông tin cho HTIC để được luật sư liên hệ, đánh giá sơ bộ và báo giá rõ ràng trước khi triển khai.</p></div>
<div class="flex flex-wrap gap-space-sm"><a class="inline-flex items-center gap-2 bg-white text-[#243e8f] hover:bg-[#0f71b9] hover:text-white font-bold px-space-lg py-3.5 rounded-lg shadow-xl transition-all" href="/lien-he/">Đặt lịch tư vấn <?php echo htic26_i( 'arrow_forward', 'text-[18px]' ); // phpcs:ignore ?></a><a class="inline-flex items-center gap-2 bg-white/10 hover:bg-white/20 font-semibold px-space-lg py-3.5 rounded-lg border border-white/25" href="tel:<?php echo esc_attr( $tel ); ?>"><?php echo htic26_i( 'call', 'text-[18px]' ); // phpcs:ignore ?>0379 044 299</a></div>
</div></div></section>
	<?php
}
