<?php
/**
 * HTIC 2026 — trang noi dung chung (chinh sach, dieu khoan, ...).
 *
 * @package HTIC_Law_Firm
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
htic26_open();
while ( have_posts() ) :
	the_post();
	$crumbs = array( array( 'Trang chủ', '/' ) );
	$parent = wp_get_post_parent_id( get_the_ID() );
	if ( $parent ) {
		$crumbs[] = array( get_the_title( $parent ), get_permalink( $parent ) );
	}
	$crumbs[] = array( get_the_title(), '' );
	htic26_hero( $crumbs, 'Công ty Luật HTIC', esc_html( get_the_title() ), has_excerpt() ? wp_strip_all_tags( get_the_excerpt() ) : '' );
	?>
<section class="py-space-2xl md:py-space-3xl bg-white"><div class="max-w-3xl mx-auto px-margin">
	<?php if ( has_post_thumbnail() ) : ?>
<figure class="mb-space-xl rounded-2xl overflow-hidden"><?php the_post_thumbnail( 'large', array( 'class' => 'w-full h-auto' ) ); ?></figure>
	<?php endif; ?>
<div class="htic-prose"><?php echo force_balance_tags( apply_filters( 'the_content', get_the_content() ) ); // phpcs:ignore ?></div>
	<?php wp_link_pages(); ?>
</div></section>
	<?php
endwhile;
htic26_cta();
htic26_close();
