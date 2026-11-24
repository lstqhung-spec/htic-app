# -*- coding: utf-8 -*-
"""Sinh cac trang con tinh cho hticlaw.vn theo thiet ke trang chu moi.
Chay: python3 build_pages.py  (ghi vao ../hticlaw-site/)"""
import html, json, os, re, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import SITE, PROCESS, WHY, FAQ, SERVICES, TEAM_LAWYERS, TEAM_EXPERTS, VALUES, TIMELINE, GALLERY

ROOT = os.path.join(os.path.dirname(__file__), '..', 'hticlaw-site')
BASE = 'https://hticlaw.vn'
E = html.escape
S = SITE

CLIENTS = ["Unimates", "KCN Long Hậu", "Đối tác", "Tulip", "HDBank", "Hitek", "PQR", "Unidepot", "Maruyama", "Unimates Education",
           "Seikosha Việt Nam", "Tôn Đông Á", "KCN Hiệp Phước", "VMR", "Enagic", "Sugiko", "ARI", "ACB", "Nhật ngữ Tâm Việt",
           "BB Decor", "Cao đẳng Lý Tự Trọng", "Cao đẳng Bách khoa Sài Gòn", "Kizuna", "Kiến Thạch", "HRC Education"]
CLIENT_FILES = sorted(os.path.basename(p) for p in glob.glob(os.path.join(ROOT, 'anh/htic/z680*')))

FB_URL = 'https://www.facebook.com/hticlawfirm'
FB_SVG = '<svg aria-hidden="true" viewBox="0 0 24 24" class="{c}" fill="currentColor"><path d="M24 12.07C24 5.41 18.63 0 12 0S0 5.41 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.05V9.41c0-3.02 1.79-4.69 4.53-4.69 1.31 0 2.68.24 2.68.24v2.97h-1.51c-1.49 0-1.96.93-1.96 1.89v2.25h3.33l-.53 3.49h-2.8V24C19.61 23.1 24 18.1 24 12.07z"/></svg>'
def fb(c='w-4 h-4'):
    return FB_SVG.replace('{c}', c)

def icon(name, cls='text-[20px]'):
    return f'<span class="material-symbols-outlined {cls}" aria-hidden="true">{name}</span>'

# ---------------------------------------------------------------- header/footer
ABOUT_MENU = [('/gioi-thieu/#loi-chao', 'Về HTIC'), ('/gioi-thieu/#gia-tri', 'Giá trị cốt lõi H·T·I·C'), ('/gioi-thieu/#doi-ngu', 'Đội ngũ luật sư & chuyên gia'),
              ('/gioi-thieu/#hanh-trinh', 'Hành trình phát triển'), ('/gioi-thieu/#hinh-anh', 'Hình ảnh hoạt động'), ('/gioi-thieu/#khach-hang', 'Khách hàng tiêu biểu')]
NEWS_MENU = [('/tin-phap-ly/', 'Tin pháp lý'), ('/bai-viet-phap-ly/', 'Bài viết pháp lý'), ('/tin-tuc/', 'Tất cả tin tức & bài viết')]
def nav_dd_item(href, label):
    return f'<a class="px-space-md py-2 text-[14px] text-slate-700 hover:bg-[#f2f2f3] hover:text-[#243e8f] rounded-lg transition-colors" href="{href}">{E(label)}</a>'

def header(active=''):
    def top(key, href, label):
        on = 'text-[#243e8f]' if key == active else 'text-slate-700'
        return on, href, label
    svc_items = ''.join(nav_dd_item(f'/dich-vu/{s["slug"]}/', s['name']) for s in SERVICES)
    def cls(key):
        return 'text-[#243e8f]' if key == active else 'text-slate-700'
    about_items = ''.join(nav_dd_item(h, l) for h, l in ABOUT_MENU)
    news_items = ''.join(nav_dd_item(h, l) for h, l in NEWS_MENU)
    mob_about = ''.join(f'<a class="block py-2 pl-4 text-[15px] text-slate-600" href="{h}">{E(l)}</a>' for h, l in ABOUT_MENU)
    mob_news = ''.join(f'<a class="block py-2 pl-4 text-[15px] text-slate-600" href="{h}">{E(l)}</a>' for h, l in NEWS_MENU)
    mob_svc = ''.join(f'<a class="block py-2 pl-4 text-[15px] text-slate-600" href="/dich-vu/{s["slug"]}/">{E(s["name"])}</a>' for s in SERVICES)
    return f'''<header id="site-header" class="fixed top-0 inset-x-0 z-50 shadow-[0_1px_8px_rgba(36,62,143,0.08)] transition-shadow duration-300">
<div class="bg-[#16285c] text-white text-[13px] border-b border-white/10">
<div class="max-w-7xl mx-auto px-margin flex items-center justify-between h-10">
<div class="flex items-center gap-space-lg">
<a class="flex items-center gap-space-xs text-white" href="tel:{S['phone_tel']}">{icon('phone_in_talk','text-[16px] text-[#5aa8e6]')}<span class="font-semibold tracking-wide">{S['phone']}</span></a>
<a class="hidden sm:flex items-center gap-space-xs text-blue-100/90 hover:text-white" href="mailto:{S['email']}">{icon('mail','text-[16px] text-[#5aa8e6]')}<span>{S['email']}</span></a>
<div class="hidden lg:flex items-center gap-space-xs text-blue-100/80">{icon('schedule','text-[16px] text-[#5aa8e6]')}<span>{S['hours_short']}</span></div>
</div>
<div class="flex items-center gap-3 text-[12px] font-semibold text-blue-100/80"><a class="flex items-center gap-1.5 text-white hover:text-[#5aa8e6]" href="{FB_URL}" target="_blank" rel="noopener" aria-label="Facebook Công ty Luật HTIC">{fb('w-4 h-4')}<span class="hidden md:inline">Facebook</span></a><span class="opacity-40">|</span><a class="text-white" href="/">VI</a><span class="opacity-40">·</span><a class="hover:text-white" href="/en/home-en/">EN</a><span class="opacity-40">·</span><a class="hover:text-white" href="/ja/">JA</a></div>
</div>
</div>
<div class="bg-white/95 backdrop-blur-xl border-b border-slate-200">
<div class="h-20 max-w-7xl mx-auto px-margin flex items-center justify-between gap-space-md">
<a class="flex items-center" href="/" aria-label="Công ty Luật HTIC – Trang chủ"><img alt="Công ty Luật HTIC" class="h-12 w-auto object-contain" width="120" height="48" fetchpriority="high" src="/anh/brand/logo.png"/></a>
<nav class="hidden xl:flex items-center gap-space-lg text-[15px]" aria-label="Điều hướng chính">
<div class="relative group py-space-sm">
<a class="flex items-center gap-1 {cls('gioi-thieu')} hover:text-[#243e8f] font-semibold py-2" href="/gioi-thieu/">Giới thiệu {icon('expand_more','text-[16px] text-slate-500 group-hover:rotate-180 transition-transform')}</a>
<div class="dd absolute left-0 top-full hidden group-hover:flex flex-col gap-0.5 bg-white rounded-xl shadow-[0_12px_40px_rgba(36,62,143,0.16)] border border-slate-100 p-space-sm w-[260px]">{about_items}</div>
</div>
<div class="relative group py-space-sm">
<a class="flex items-center gap-1 {cls('dich-vu')} hover:text-[#243e8f] font-semibold py-2" href="/dich-vu/">Lĩnh vực dịch vụ {icon('expand_more','text-[16px] text-slate-500 group-hover:rotate-180 transition-transform')}</a>
<div class="dd absolute left-1/2 -translate-x-1/2 top-full hidden group-hover:grid grid-cols-2 gap-1 bg-white rounded-xl shadow-[0_12px_40px_rgba(36,62,143,0.16)] border border-slate-100 p-space-sm w-[520px]">{svc_items}<a class="col-span-2 mt-1 px-space-md py-2 text-[14px] font-bold text-[#0f71b9] border-t border-slate-100" href="/dich-vu/">Xem tất cả lĩnh vực →</a></div>
</div>
<div class="relative group py-space-sm">
<a class="flex items-center gap-1 {cls('tin-tuc')} hover:text-[#243e8f] font-semibold py-2" href="/tin-tuc/">Tin tức &amp; Bài viết {icon('expand_more','text-[16px] text-slate-500 group-hover:rotate-180 transition-transform')}</a>
<div class="dd absolute left-0 top-full hidden group-hover:flex flex-col gap-0.5 bg-white rounded-xl shadow-[0_12px_40px_rgba(36,62,143,0.16)] border border-slate-100 p-space-sm w-[240px]">{news_items}</div>
</div>
<a class="{cls('lien-he')} hover:text-[#243e8f] font-semibold py-2" href="/lien-he/">Liên hệ</a>
</nav>
<div class="flex items-center gap-space-sm">
<a class="hidden sm:inline-flex items-center gap-space-xs bg-[#243e8f] hover:bg-[#0f71b9] text-white text-[15px] font-bold px-space-md py-2.5 rounded-lg shadow-md transition-all" href="/lien-he/">{icon('calendar_today','text-[18px]')}<span>Đặt lịch tư vấn</span></a>
<details class="xl:hidden relative" id="mnav"><summary class="list-none cursor-pointer w-11 h-11 rounded-lg border border-slate-200 flex items-center justify-center text-[#243e8f]" aria-label="Mở menu">{icon('menu','text-[26px]')}</summary>
<div class="fixed left-0 right-0 top-[120px] bottom-0 overflow-y-auto bg-white border-t border-slate-200 px-margin py-space-md">
<a class="block py-3 text-[17px] font-semibold text-[#16285c] border-b border-slate-100" href="/">Trang chủ</a>
<a class="block py-3 text-[17px] font-semibold text-[#16285c]" href="/gioi-thieu/">Giới thiệu</a>
<div class="border-b border-slate-100 pb-2">{mob_about}</div>
<a class="block py-3 text-[17px] font-semibold text-[#16285c]" href="/dich-vu/">Lĩnh vực dịch vụ</a>
<div class="border-b border-slate-100 pb-2">{mob_svc}</div>
<a class="block py-3 text-[17px] font-semibold text-[#16285c]" href="/tin-tuc/">Tin tức &amp; Bài viết</a>
<div class="border-b border-slate-100 pb-2">{mob_news}</div>
<a class="block py-3 text-[17px] font-semibold text-[#16285c] border-b border-slate-100" href="/lien-he/">Liên hệ</a>
<a class="mt-space-md flex items-center justify-center gap-2 bg-[#243e8f] text-white font-bold py-3.5 rounded-lg" href="tel:{S['phone_tel']}">{icon('call','text-[18px]')}Gọi {S['phone']}</a>
</div></details>
</div>
</div>
</div>
</header>'''

def footer():
    svc = ''.join(f'<li><a class="text-blue-100 hover:text-white transition-colors" href="/dich-vu/{s["slug"]}/">{E(s["name"])}</a></li>' for s in SERVICES)
    return f'''<footer class="w-full bg-[#16285c] text-white">
<div class="max-w-7xl mx-auto px-margin pt-space-3xl pb-space-2xl">
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-space-xl">
<div class="lg:col-span-4 flex flex-col gap-space-md">
<img loading="lazy" decoding="async" alt="Công ty Luật HTIC" class="h-14 w-auto object-contain self-start" width="140" height="56" src="/anh/brand/logo-white.png"/>
<p class="text-[14px] text-blue-100 leading-relaxed">Công ty luật đồng hành cùng cá nhân, doanh nghiệp trong nước và nhà đầu tư nước ngoài.</p>
<div class="flex flex-col gap-space-xs text-[14px] text-blue-100">
<div class="flex items-start gap-space-xs">{icon('location_on','text-[18px] text-[#5aa8e6] mt-0.5')}<span>{E(S['address'])}</span></div>
<a class="flex items-center gap-space-xs hover:text-white" href="tel:{S['phone_tel']}">{icon('call','text-[18px] text-[#5aa8e6]')}<span>{S['phone']}</span></a>
<a class="flex items-center gap-space-xs hover:text-white" href="mailto:{S['email']}">{icon('mail','text-[18px] text-[#5aa8e6]')}<span>{S['email']}</span></a>
<div class="flex items-center gap-space-xs">{icon('schedule','text-[18px] text-[#5aa8e6]')}<span>{S['hours']}</span></div>
</div>
</div>
<div class="lg:col-span-5"><h4 class="text-base font-bold mb-space-md">Lĩnh vực tư vấn</h4><ul class="grid grid-cols-1 sm:grid-cols-2 gap-x-space-md gap-y-2 text-[14px]">{svc}</ul></div>
<div class="lg:col-span-3"><h4 class="text-base font-bold mb-space-md">Về HTIC</h4><ul class="flex flex-col gap-2 text-[14px]">
<li><a class="text-blue-100 hover:text-white" href="/gioi-thieu/">Giới thiệu</a></li>
<li><a class="text-blue-100 hover:text-white" href="/gioi-thieu/#doi-ngu">Đội ngũ luật sư</a></li>
<li><a class="text-blue-100 hover:text-white" href="/tin-phap-ly/">Tin pháp lý</a></li>
<li><a class="text-blue-100 hover:text-white" href="/bai-viet-phap-ly/">Bài viết pháp lý</a></li>
<li><a class="text-blue-100 hover:text-white" href="/lien-he/">Liên hệ</a></li></ul>
<p class="mt-space-md text-[13px] text-blue-100/80 leading-relaxed">Thành viên Đoàn Luật sư TP.HCM. Thông tin khách hàng được bảo mật theo Luật Luật sư.</p>
<div class="flex gap-3 mt-space-md text-[13px] font-semibold"><a class="flex items-center gap-2 px-3 py-1.5 rounded-md bg-[#1877f2] hover:bg-[#0f5fd0]" href="{FB_URL}" rel="noopener" target="_blank">{fb('w-4 h-4')}Facebook</a><a class="px-3 py-1.5 rounded-md bg-white/10 hover:bg-white/20" href="https://www.linkedin.com/company/htic-law" rel="noopener" target="_blank">LinkedIn</a><a class="px-3 py-1.5 rounded-md bg-white/10 hover:bg-white/20" href="{S['zalo']}" rel="noopener" target="_blank">Zalo</a></div>
</div>
</div>
<div class="mt-space-2xl pt-space-lg border-t border-white/10 flex flex-col md:flex-row items-center justify-between gap-space-md text-[13px] text-blue-200">
<p>© 2026 Công ty Luật HTIC. Toàn bộ quyền được bảo lưu.</p>
<div class="flex items-center gap-space-md"><a class="hover:text-white" href="/chinh-sach-bao-mat/">Chính sách bảo mật</a><span>·</span><a class="hover:text-white" href="/dieu-khoan-dich-vu/">Điều khoản sử dụng</a></div>
</div>
</div>
</footer>
<div class="htic-fab fixed right-4 bottom-4 z-40 flex flex-col items-end gap-3" aria-label="Liên hệ nhanh">
<a href="{S['zalo']}" target="_blank" rel="noopener" class="group relative flex items-center" aria-label="Chat Zalo với HTIC"><span class="fab-tip">Chat Zalo</span><span class="fab-btn bg-[#0068ff]"><span class="absolute inset-0 rounded-full bg-[#0068ff] animate-ping opacity-25"></span><span class="relative text-white font-extrabold text-[13px] tracking-tight">Zalo</span></span></a>
<a href="https://m.me/hticlawfirm" target="_blank" rel="noopener" class="group relative flex items-center" aria-label="Nhắn Messenger cho HTIC"><span class="fab-tip">Nhắn Messenger</span><span class="fab-btn bg-gradient-to-br from-[#00b2ff] to-[#006aff]"><svg aria-hidden="true" viewBox="0 0 24 24" class="w-7 h-7 text-white" fill="currentColor"><path d="M12 2C6.36 2 2 6.13 2 11.7c0 2.91 1.19 5.44 3.14 7.17.16.14.26.35.27.57l.05 1.78c.02.57.6.94 1.12.71l1.99-.88c.17-.07.36-.09.53-.04.91.25 1.88.39 2.9.39 5.64 0 10-4.13 10-9.7S17.64 2 12 2zm6 7.46l-2.93 4.67c-.47.73-1.47.92-2.17.4l-2.33-1.75a.6.6 0 0 0-.72 0l-3.15 2.4c-.42.32-.97-.18-.69-.63l2.93-4.67c.47-.73 1.47-.92 2.17-.4l2.33 1.75a.6.6 0 0 0 .72 0l3.15-2.4c.42-.32.97.18.69.63z"/></svg></span></a>
<a href="tel:{S['phone_tel']}" class="group relative flex items-center" aria-label="Gọi {S['phone']}"><span class="fab-tip">{S['phone']}</span><span class="fab-btn bg-[#243e8f]">{icon('call','text-[24px] text-white')}</span></a>
</div>'''

FORM_JS = r'''<script>
(function(){var f=document.getElementById('bookingForm');if(!f)return;var m=document.getElementById('formMsg');
var q=new URLSearchParams(location.search).get('dv');if(q&&f.elements.topic){[].forEach.call(f.elements.topic.options,function(o){if(o.getAttribute('data-slug')===q)o.selected=true})}
f.addEventListener('submit',function(e){e.preventDefault();var g=function(n){var x=f.elements[n];return x?x.value.trim():''};
if(!g('name')||!/^[0-9 +().-]{9,15}$/.test(g('phone'))){m.textContent='Vui lòng nhập họ tên và số điện thoại hợp lệ.';m.className='text-[14px] font-semibold text-red-600';return}
var body='Họ tên: '+g('name')+'\nCông ty: '+g('company')+'\nĐiện thoại: '+g('phone')+'\nEmail: '+g('email')+'\nLĩnh vực: '+g('topic')+'\n\n'+g('message');
window.location.href='mailto:__EMAIL__?subject='+encodeURIComponent('Yêu cầu tư vấn từ hticlaw.vn - '+g('name'))+'&body='+encodeURIComponent(body);
m.textContent='Đã mở bản nháp email. Quý khách cần bấm Gửi trong ứng dụng email để hoàn tất. Nếu không mở được ứng dụng email, vui lòng gọi __PHONE__ hoặc nhắn Zalo.';m.className='text-[14px] font-semibold text-emerald-700';});})();
</script>'''

MOTION_HEAD = '<script id="htic-motion-head">if(!matchMedia("(prefers-reduced-motion: reduce)").matches)document.documentElement.classList.add("js-motion")</script>'
MOTION_JS = r"""<script id="htic-motion">
(function(){var d=document,h=d.getElementById('site-header');
function sc(){if(h)h.classList.toggle('scrolled',scrollY>8)}sc();addEventListener('scroll',sc,{passive:true});
var mn=d.getElementById('mnav');if(mn)mn.addEventListener('click',function(e){if(e.target.closest('a'))mn.removeAttribute('open')});
if(!d.documentElement.classList.contains('js-motion')||!('IntersectionObserver' in window))return;
var vh=innerHeight,io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var t=e.target;t.classList.add('in');io.unobserve(t);setTimeout(function(){t.classList.remove('rv','in');t.style.removeProperty('--d')},1300)}})},{rootMargin:'0px 0px -8% 0px',threshold:0.08});
function mark(el,i){if(el.getBoundingClientRect().top<vh*0.92||el.offsetHeight>vh*0.9)return;el.classList.add('rv');el.style.setProperty('--d',Math.min(i*70,420)+'ms');io.observe(el)}
d.querySelectorAll('main section').forEach(function(s,si){if(si===0&&s.querySelector('h1'))return;
var head=s.querySelector('h2');if(head)mark(head.closest('div')||head,0);
s.querySelectorAll('.grid').forEach(function(g){if(g.closest('.rv'))return;var kids=[].slice.call(g.children);if(kids.length<2||kids.length>30){mark(g,0);return}kids.forEach(function(k,i){mark(k,i%6)})})});
d.querySelectorAll('main img[loading=lazy]').forEach(function(im){if(im.complete||im.closest('.rv'))return;im.classList.add('lz');im.addEventListener('load',function(){im.classList.add('ld')},{once:true});im.addEventListener('error',function(){im.classList.add('ld')},{once:true})});
})();
</script>
<script type="speculationrules">{"prerender":[{"where":{"and":[{"href_matches":"/*"},{"not":{"href_matches":"/wp-*"}},{"not":{"selector_matches":"[target=_blank],[rel~=nofollow]"}}]},"eagerness":"moderate"}]}</script>"""

def page(path, title, desc, body, active='', image='/anh/hero-ban-lam-viec.webp', jsonld=None, crumbs=None):
    url = BASE + path
    graph = []
    if crumbs:
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + h} for i, (n, h) in enumerate(crumbs)]})
    if jsonld:
        graph.extend(jsonld)
    ld = f'<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)}</script>' if graph else ''
    return f'''<!DOCTYPE html>
<html class="scroll-smooth" lang="vi"><head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}"/>
<link rel="canonical" href="{url}"/>
<meta name="robots" content="index,follow,max-image-preview:large"/>
<meta name="theme-color" content="#16285c"/>
<link rel="icon" href="/anh/brand/favicon-48.png" sizes="48x48" type="image/png"/>
<link rel="icon" href="/anh/brand/favicon.png" sizes="512x512" type="image/png"/>
<link rel="apple-touch-icon" href="/anh/brand/apple-touch-icon.png"/>
<meta property="og:type" content="website"/>
<meta property="og:site_name" content="Công ty Luật HTIC"/>
<meta property="og:locale" content="vi_VN"/>
<meta property="og:title" content="{E(title)}"/>
<meta property="og:description" content="{E(desc)}"/>
<meta property="og:url" content="{url}"/>
<meta property="og:image" content="{BASE + image if image.startswith('/') else image}"/>
<meta name="twitter:card" content="summary_large_image"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&amp;display=swap" rel="stylesheet"/>
<!--ICONS-->
<link rel="stylesheet" href="/assets/htic.css?v=__VER__"/>
{MOTION_HEAD}
{ld}
</head>
<body class="bg-white text-text-primary antialiased selection:bg-[#0f71b9]/15 selection:text-[#243e8f]">
<a class="sr-only focus:not-sr-only" href="#noi-dung">Bỏ qua đến nội dung</a>
{header(active)}
<main id="noi-dung" class="w-full pt-[120px]">
{body}
</main>
{footer()}
{FORM_JS.replace('__EMAIL__', S['email']).replace('__PHONE__', S['phone']) if 'bookingForm' in body else ''}
{MOTION_JS}
</body></html>'''

# ---------------------------------------------------------------- blocks
def breadcrumb(items):
    parts = []
    for i, (n, h) in enumerate(items):
        if i == len(items) - 1:
            parts.append(f'<span class="text-white" aria-current="page">{E(n)}</span>')
        else:
            parts.append(f'<a class="hover:text-white" href="{h}">{E(n)}</a>{icon("chevron_right","text-[16px] opacity-60")}')
    return f'<nav class="flex flex-wrap items-center gap-1 text-[13px] text-blue-100/80" aria-label="Breadcrumb">{"".join(parts)}</nav>'

def hero(crumbs, eyebrow, h1, lead, img, ctas=True, side=None):
    btns = ''
    if ctas:
        btns = f'''<div class="flex flex-wrap gap-space-sm pt-space-sm">
<a class="inline-flex items-center gap-2 bg-[#0f71b9] hover:bg-white hover:text-[#243e8f] text-white font-bold px-space-lg py-3.5 rounded-lg shadow-xl transition-all" href="{ctas if isinstance(ctas,str) else '/lien-he/'}">Đặt lịch tư vấn {icon('arrow_forward','text-[18px]')}</a>
<a class="inline-flex items-center gap-2 bg-white/10 hover:bg-white/20 text-white font-semibold px-space-lg py-3.5 rounded-lg border border-white/25" href="tel:{S['phone_tel']}">{icon('call','text-[18px]')}{S['phone']}</a></div>'''
    return f'''<section class="relative -mt-[120px] pt-[150px] pb-space-2xl md:pb-space-3xl bg-[#16285c] text-white overflow-hidden">
<img alt="" aria-hidden="true" class="absolute inset-0 w-full h-full object-cover opacity-40" src="{img}" fetchpriority="high"/>
<div class="absolute inset-0 bg-gradient-to-r from-[#16285c] via-[#16285c]/90 to-[#243e8f]/60"></div>
<div class="relative max-w-7xl mx-auto px-margin">
{breadcrumb(crumbs)}
<div class="grid grid-cols-1 lg:grid-cols-12 gap-space-xl items-end mt-space-lg">
<div class="hero-in lg:col-span-8 flex flex-col gap-space-md">
<span class="text-[12px] uppercase tracking-[0.18em] font-bold text-[#5aa8e6]">{E(eyebrow)}</span>
<h1 class="text-[34px] md:text-[48px] leading-[1.12] font-extrabold tracking-tight">{h1}</h1>
<p class="text-[17px] md:text-[18px] text-blue-100 leading-relaxed max-w-2xl">{E(lead)}</p>
{btns}
</div>
{side or ''}
</div>
</div>
</section>'''

def section_head(eyebrow, title, sub='', center=False, dark=False):
    al = 'text-center mx-auto items-center' if center else ''
    tc = 'text-white' if dark else 'text-[#243e8f]'
    sc = 'text-blue-100' if dark else 'text-text-secondary'
    s = f'<p class="text-[16px] {sc} leading-relaxed max-w-2xl">{E(sub)}</p>' if sub else ''
    return f'''<div class="flex flex-col gap-2 mb-space-xl max-w-3xl {al}"><span class="text-[12px] uppercase tracking-[0.18em] font-bold text-[#0f71b9]">{E(eyebrow)}</span>
<h2 class="text-[28px] md:text-[36px] leading-tight font-extrabold tracking-tight {tc}">{title}</h2>{s}</div>'''

def cta_band(title='Cần tư vấn cho một vấn đề pháp lý cụ thể?', text='Gửi thông tin cho HTIC để được luật sư liên hệ, đánh giá sơ bộ và báo giá rõ ràng trước khi triển khai.', href='/lien-he/'):
    return f'''<section class="py-space-2xl bg-white"><div class="max-w-7xl mx-auto px-margin">
<div class="relative rounded-2xl overflow-hidden bg-[#243e8f] text-white px-space-lg py-space-xl md:px-space-2xl md:py-space-2xl">
<div class="absolute -right-24 -top-24 w-80 h-80 rounded-full bg-[#0f71b9]/40"></div>
<div class="relative grid grid-cols-1 lg:grid-cols-12 gap-space-lg items-center">
<div class="lg:col-span-8"><h2 class="text-[26px] md:text-[32px] font-extrabold leading-tight tracking-tight">{E(title)}</h2><p class="mt-2 text-blue-100 text-[16px] leading-relaxed">{E(text)}</p></div>
<div class="lg:col-span-4 flex flex-col sm:flex-row lg:flex-col gap-space-sm lg:items-end">
<a class="inline-flex justify-center items-center gap-2 bg-white text-[#243e8f] hover:bg-[#e8eaf1] font-bold px-space-lg py-3.5 rounded-lg" href="{href}">Gửi yêu cầu tư vấn {icon('arrow_forward','text-[18px]')}</a>
<a class="inline-flex justify-center items-center gap-2 border border-white/30 hover:bg-white/10 font-semibold px-space-lg py-3.5 rounded-lg" href="tel:{S['phone_tel']}">{icon('call','text-[18px]')}Hotline {S['phone']}</a></div>
</div></div></div></section>'''

def process_block(dark=False):
    items = ''.join(f'''<li class="relative flex flex-col gap-2 p-space-md rounded-xl bg-white border border-slate-200">
<span class="w-10 h-10 rounded-full bg-[#243e8f] text-white font-extrabold flex items-center justify-center">{i+1}</span>
<h3 class="font-bold text-[#16285c] text-[16px] leading-snug">{E(t)}</h3><p class="text-[14px] text-text-secondary leading-relaxed">{E(d)}</p></li>''' for i, (t, d) in enumerate(PROCESS))
    return f'<ol class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-space-md">{items}</ol>'

def why_block():
    return '<div class="grid grid-cols-1 sm:grid-cols-2 gap-space-md">' + ''.join(f'''<div class="flex gap-space-md p-space-md rounded-xl bg-[#f2f2f3]">
<span class="w-11 h-11 shrink-0 rounded-lg bg-white text-[#0f71b9] flex items-center justify-center shadow-sm">{icon(ic,'text-[24px]')}</span>
<div><h3 class="font-bold text-[#16285c]">{E(t)}</h3><p class="text-[14px] text-text-secondary leading-relaxed mt-1">{E(d)}</p></div></div>''' for ic, t, d in WHY) + '</div>'

def svc_card(s, i):
    bullets = ''.join(f'<li class="flex gap-2">{icon("check","text-[18px] text-[#0f71b9] shrink-0")}<span>{E(t)}</span></li>' for t, _ in s['scope'][:3])
    return f'''<a class="group flex flex-col bg-white rounded-2xl border border-slate-200 hover:border-[#0f71b9] shadow-sm hover:shadow-xl transition-all overflow-hidden" href="/dich-vu/{s['slug']}/">
<div class="relative h-44 overflow-hidden"><img loading="lazy" decoding="async" alt="{E(s['name'])}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="{s['img']}"/>
<div class="absolute inset-0 bg-gradient-to-t from-[#16285c]/80 to-transparent"></div>
<span class="absolute top-3 left-3 text-[12px] font-extrabold text-white bg-[#0f71b9] px-2.5 py-1 rounded-md">{i+1:02d}</span>
<span class="absolute bottom-3 left-3 w-11 h-11 rounded-lg bg-white text-[#243e8f] flex items-center justify-center shadow-md">{icon(s['icon'],'text-[24px]')}</span></div>
<div class="flex flex-col flex-1 p-space-lg gap-space-sm"><h3 class="text-[19px] font-extrabold text-[#16285c] leading-snug">{E(s['name'])}</h3>
<p class="text-[14px] text-text-secondary leading-relaxed">{E(s['card'])}</p>
<ul class="flex flex-col gap-1.5 text-[14px] text-slate-700">{bullets}</ul>
<span class="mt-auto pt-space-sm flex items-center justify-between text-[#0f71b9] font-bold text-[14px] border-t border-slate-100">Xem chi tiết {icon('arrow_forward','text-[18px] group-hover:translate-x-1 transition-transform')}</span></div></a>'''

def topic_options(selected_slug=None):
    o = ''.join(f'<option data-slug="{s["slug"]}">{E(s["name"])}</option>' for s in SERVICES)
    return '<option value="">Chọn lĩnh vực</option>' + o + '<option>Khác / chưa rõ</option>'

def booking_form():
    inp = 'w-full rounded-lg border border-slate-300 bg-white px-4 py-3 text-[15px] focus:border-[#0f71b9] focus:ring-2 focus:ring-[#0f71b9]/20 outline-none'
    lab = 'text-[12px] uppercase tracking-wide font-bold text-[#243e8f]'
    return f'''<form class="flex flex-col gap-space-md" id="bookingForm" novalidate="">
<div class="grid grid-cols-1 md:grid-cols-2 gap-space-md">
<label class="flex flex-col gap-1.5"><span class="{lab}">Họ và tên *</span><input class="{inp}" name="name" autocomplete="name" required/></label>
<label class="flex flex-col gap-1.5"><span class="{lab}">Công ty</span><input class="{inp}" name="company" autocomplete="organization"/></label>
<label class="flex flex-col gap-1.5"><span class="{lab}">Số điện thoại *</span><input class="{inp}" name="phone" type="tel" autocomplete="tel" required/></label>
<label class="flex flex-col gap-1.5"><span class="{lab}">Email</span><input class="{inp}" name="email" type="email" autocomplete="email"/></label>
</div>
<label class="flex flex-col gap-1.5"><span class="{lab}">Lĩnh vực cần tư vấn</span><select class="{inp}" name="topic">{topic_options()}</select></label>
<label class="flex flex-col gap-1.5"><span class="{lab}">Mô tả ngắn vấn đề</span><textarea class="{inp} min-h-[130px]" name="message" placeholder="Ví dụ: cần rà soát hợp đồng phân phối với đối tác Nhật Bản trước ngày ký…"></textarea></label>
<p class="text-[13px] text-text-muted flex gap-2">{icon('lock','text-[16px] text-[#0f71b9]')}Thông tin được bảo mật theo nghĩa vụ nghề nghiệp luật sư và chỉ dùng để phản hồi yêu cầu của quý khách.</p>
<button class="inline-flex justify-center items-center gap-2 bg-[#243e8f] hover:bg-[#0f71b9] text-white font-bold px-space-lg py-3.5 rounded-lg shadow-md transition-all" type="submit">Soạn email {icon('send','text-[18px]')}</button>
<p id="formMsg" class="text-[14px] font-semibold" role="status"></p>
</form>'''

# ---------------------------------------------------------------- pages
def faq_block(slug):
    items = FAQ.get(slug, [])
    if not items: return ''
    q = ''.join(f'''<details class="group rounded-xl border border-slate-200 bg-white open:border-[#0f71b9] open:shadow-sm">
<summary class="list-none cursor-pointer flex items-start justify-between gap-space-md p-space-md font-bold text-[#16285c] text-[16px]">{E(a)}{icon('expand_more','text-[22px] text-[#0f71b9] shrink-0 group-open:rotate-180 transition-transform')}</summary>
<p class="px-space-md pb-space-md -mt-1 text-[15px] text-text-secondary leading-relaxed">{E(b)}</p></details>''' for a, b in items)
    return f'<div id="hoi-dap"><h2 class="text-[26px] md:text-[30px] font-extrabold text-[#243e8f] tracking-tight mb-space-md">Câu hỏi thường gặp</h2><div class="flex flex-col gap-space-sm">{q}</div></div>'

def build_service(i, s):
    others = [x for x in SERVICES if x is not s]
    related = others[i % len(others):] + others[:i % len(others)]
    rel = ''.join(svc_card(r, SERVICES.index(r)) for r in related[:3])
    scope = ''.join(f'''<div class="flex gap-space-md p-space-md rounded-xl border border-slate-200 bg-white hover:border-[#0f71b9] transition-colors">
<span class="text-[22px] font-extrabold text-[#0f71b9]/40 leading-none w-8 shrink-0">{k+1:02d}</span>
<div><h3 class="font-bold text-[#16285c] text-[16px]">{E(t)}</h3><p class="text-[14px] text-text-secondary leading-relaxed mt-1">{E(d)}</p></div></div>''' for k, (t, d) in enumerate(s['scope']))
    laws = ''.join(f'<li class="flex gap-2 items-start">{icon("menu_book","text-[18px] text-[#0f71b9] shrink-0 mt-0.5")}<span>{E(l)}</span></li>' for l in s['laws'])
    side_nav = ''.join(f'<a class="flex items-center justify-between px-4 py-2.5 rounded-lg text-[14px] {"bg-[#243e8f] text-white font-bold" if x is s else "text-slate-700 hover:bg-[#f2f2f3] hover:text-[#243e8f]"}" href="/dich-vu/{x["slug"]}/">{E(x["name"])}{icon("chevron_right","text-[18px] opacity-60")}</a>' for x in SERVICES)
    facts = [('person_pin', 'Luật sư phụ trách được thống nhất theo vụ việc'), ('receipt_long', 'Báo giá rõ ràng trước khi triển khai'), ('lock', 'Bảo mật thông tin theo Luật Luật sư')]
    facts_html = ''.join(f'<div class="flex items-center gap-3 py-space-md">{icon(ic,"text-[24px] text-[#0f71b9]")}<span class="font-semibold text-[#16285c] text-[15px]">{E(t)}</span></div>' for ic, t in facts)
    body = hero([('Trang chủ', '/'), ('Dịch vụ', '/dich-vu/'), (s['name'], f'/dich-vu/{s["slug"]}/')],
                f'Lĩnh vực dịch vụ {i+1:02d}', E(s['name']), s['lead'], s['img'], ctas=f'/lien-he/?dv={s["slug"]}')
    body += f'''<div class="bg-white border-b border-slate-200"><div class="max-w-7xl mx-auto px-margin grid grid-cols-1 md:grid-cols-3 md:divide-x divide-slate-200 [&>*]:md:pl-space-lg [&>*:first-child]:md:pl-0">{facts_html}</div></div>
<section class="py-space-2xl md:py-space-3xl bg-white"><div class="max-w-7xl mx-auto px-margin grid grid-cols-1 lg:grid-cols-12 gap-space-2xl">
<div class="lg:col-span-8 flex flex-col gap-space-2xl">
<div><span class="text-[12px] uppercase tracking-[0.18em] font-bold text-[#0f71b9]">Tổng quan</span>
<p class="mt-space-sm text-[18px] md:text-[20px] leading-relaxed text-[#16285c] font-medium">{E(s['overview'])}</p></div>
<div><h2 class="text-[26px] md:text-[30px] font-extrabold text-[#243e8f] tracking-tight mb-space-md">Phạm vi công việc</h2>
<div class="grid grid-cols-1 md:grid-cols-2 gap-space-md">{scope}</div></div>
<div class="rounded-2xl bg-[#f2f2f3] p-space-lg md:p-space-xl"><h2 class="text-[22px] font-extrabold text-[#243e8f] mb-space-md">Căn cứ pháp lý chính</h2>
<ul class="grid grid-cols-1 md:grid-cols-2 gap-space-sm text-[15px] text-slate-700">{laws}</ul>
<p class="mt-space-md text-[13px] text-text-muted">Căn cứ pháp lý được xác định theo thời điểm phát sinh quan hệ, giao dịch hoặc vụ việc và các quy định chuyển tiếp có liên quan.</p></div>
<div><h2 class="text-[26px] md:text-[30px] font-extrabold text-[#243e8f] tracking-tight mb-space-md">Vì sao chọn HTIC</h2>{why_block()}</div>
{faq_block(s['slug'])}
</div>
<aside class="lg:col-span-4"><div class="lg:sticky lg:top-[140px] flex flex-col gap-space-md">
<div class="rounded-2xl bg-[#16285c] text-white p-space-lg flex flex-col gap-space-sm">
<span class="text-[12px] uppercase tracking-[0.18em] font-bold text-[#5aa8e6]">Trao đổi với luật sư</span>
<p class="text-[20px] font-extrabold leading-snug">Cần tư vấn về {E(s['name'])}?</p>
<p class="text-[14px] text-blue-100">Gửi yêu cầu hoặc gọi trực tiếp, luật sư HTIC sẽ liên hệ trong giờ làm việc.</p>
<a class="mt-1 inline-flex justify-center items-center gap-2 bg-[#0f71b9] hover:bg-white hover:text-[#243e8f] font-bold py-3 rounded-lg transition-colors" href="/lien-he/?dv={s['slug']}">Đặt lịch tư vấn {icon('arrow_forward','text-[18px]')}</a>
<a class="inline-flex justify-center items-center gap-2 border border-white/25 hover:bg-white/10 font-semibold py-3 rounded-lg" href="tel:{S['phone_tel']}">{icon('call','text-[18px]')}{S['phone']}</a>
<a class="inline-flex justify-center items-center gap-2 text-[14px] text-blue-100 hover:text-white" href="mailto:{S['email']}">{icon('mail','text-[16px]')}{S['email']}</a></div>
<nav class="rounded-2xl border border-slate-200 p-space-sm flex flex-col gap-0.5" aria-label="Các lĩnh vực dịch vụ"><p class="px-4 pt-2 pb-1 text-[12px] uppercase tracking-wider font-bold text-text-muted">Lĩnh vực dịch vụ</p>{side_nav}</nav>
</div></aside>
</div></section>
<section class="py-space-2xl md:py-space-3xl bg-[#f2f2f3]"><div class="max-w-7xl mx-auto px-margin">{section_head('Quy trình làm việc', 'Năm bước rõ ràng, từ tiếp nhận đến bàn giao')}{process_block()}</div></section>
<section class="py-space-2xl md:py-space-3xl bg-white"><div class="max-w-7xl mx-auto px-margin">{section_head('Lĩnh vực liên quan', 'Dịch vụ thường đi kèm')}<div class="grid grid-cols-1 md:grid-cols-3 gap-space-md">{rel}</div></div></section>
{cta_band('Cần tư vấn về ' + s['name'] + '?', href='/lien-he/?dv=' + s['slug'])}'''
    ld = [{"@type": "Service", "name": s['name'], "serviceType": s['name'], "description": s['lead'], "url": f"{BASE}/dich-vu/{s['slug']}/",
           "areaServed": "VN", "provider": {"@id": BASE + "/#firm"}}]
    if FAQ.get(s['slug']):
        ld.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": a, "acceptedAnswer": {"@type": "Answer", "text": b}} for a, b in FAQ[s['slug']]]})
    return page(f'/dich-vu/{s["slug"]}/', f'{s["name"]} | Luật sư tư vấn tại TP.HCM – Công ty Luật HTIC', s['lead'], body, 'dich-vu', s['img'], ld,
                [('Trang chủ', '/'), ('Dịch vụ', '/dich-vu/'), (s['name'], f'/dich-vu/{s["slug"]}/')])

def build_services_index():
    cards = ''.join(svc_card(s, i) for i, s in enumerate(SERVICES))
    models = [('assignment', 'Theo vụ việc', 'Phí cố định cho một công việc cụ thể: soạn thảo, rà soát hợp đồng, xin giấy phép, đăng ký bảo hộ…'),
              ('workspaces', 'Theo dự án', 'Một đội luật sư đồng hành suốt dự án hoặc thương vụ: thẩm định, đàm phán, hoàn tất thủ tục.'),
              ('support_agent', 'Pháp chế thuê ngoài', 'Gói tư vấn thường xuyên hằng tháng, thay thế hoặc hỗ trợ bộ phận pháp chế nội bộ.')]
    m = ''.join(f'''<div class="flex flex-col gap-space-sm p-space-lg rounded-2xl bg-white/5 border border-white/15">
<span class="w-12 h-12 rounded-xl bg-[#0f71b9] flex items-center justify-center">{icon(ic,'text-[26px]')}</span><h3 class="text-[20px] font-extrabold">{E(t)}</h3><p class="text-[15px] text-blue-100 leading-relaxed">{E(d)}</p></div>''' for ic, t, d in models)
    body = hero([('Trang chủ', '/'), ('Dịch vụ', '/dich-vu/')], 'Lĩnh vực dịch vụ', 'Dịch vụ pháp lý toàn diện cho doanh nghiệp',
                'Mười lĩnh vực chuyên sâu, một đầu mối xuyên suốt, dành cho doanh nghiệp Việt Nam và nhà đầu tư nước ngoài. Chọn một lĩnh vực để xem phạm vi công việc chi tiết.',
                '/anh/htic/cong-ty-tu-van-luat-htic279274646012.jpg')
    body += f'''<section class="py-space-2xl md:py-space-3xl bg-white"><div class="max-w-7xl mx-auto px-margin">{section_head('10 lĩnh vực tư vấn', 'Chọn lĩnh vực bạn cần hỗ trợ')}
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-space-md">{cards}
<div class="flex flex-col justify-between gap-space-md p-space-lg rounded-2xl bg-[#243e8f] text-white sm:col-span-2 lg:col-span-2">
<div><h3 class="text-[22px] font-extrabold">Chưa rõ vấn đề thuộc lĩnh vực nào?</h3><p class="mt-2 text-blue-100">Mô tả ngắn tình huống, luật sư HTIC sẽ xác định vấn đề pháp lý và hướng xử lý phù hợp.</p></div>
<div class="flex flex-wrap gap-space-sm"><a class="inline-flex items-center gap-2 bg-white text-[#243e8f] font-bold px-space-lg py-3 rounded-lg" href="/lien-he/">Gửi mô tả vấn đề {icon('arrow_forward','text-[18px]')}</a><a class="inline-flex items-center gap-2 border border-white/30 font-semibold px-space-lg py-3 rounded-lg" href="tel:{S['phone_tel']}">{icon('call','text-[18px]')}{S['phone']}</a></div></div>
</div></div></section>
<section class="py-space-2xl md:py-space-3xl bg-[#16285c] text-white"><div class="max-w-7xl mx-auto px-margin">{section_head('Hình thức hợp tác', 'Linh hoạt theo nhu cầu của doanh nghiệp', dark=True)}<div class="grid grid-cols-1 md:grid-cols-3 gap-space-md">{m}</div></div></section>
<section class="py-space-2xl md:py-space-3xl bg-[#f2f2f3]"><div class="max-w-7xl mx-auto px-margin">{section_head('Quy trình làm việc', 'Năm bước rõ ràng, từ tiếp nhận đến bàn giao')}{process_block()}</div></section>
{cta_band()}'''
    ld = [{"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": s['name'], "url": f"{BASE}/dich-vu/{s['slug']}/"} for i, s in enumerate(SERVICES)]}]
    return page('/dich-vu/', 'Dịch vụ pháp lý cho doanh nghiệp | Công ty Luật HTIC TP.HCM',
                'Công ty Luật HTIC tư vấn 10 lĩnh vực: doanh nghiệp, hợp đồng, M&A và đầu tư FDI, bất động sản, giấy phép, tài chính, thuế, sở hữu trí tuệ, tranh chấp và lao động ngoài nước.',
                body, 'dich-vu', '/anh/htic/cong-ty-tu-van-luat-htic279274646012.jpg', ld, [('Trang chủ', '/'), ('Dịch vụ', '/dich-vu/')])

def person(n, r, img, big=False):
    return f'''<figure class="group"><div class="relative rounded-2xl overflow-hidden aspect-[3/4] bg-[#e8eaf1] shadow-sm">
<img loading="lazy" decoding="async" alt="{E(n)}" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500" src="{img}"/></div>
<figcaption class="pt-space-sm"><p class="font-bold text-[#16285c] {"text-[17px]" if big else "text-[15px]"}">{E(n)}</p><p class="text-[13px] text-text-secondary">{E(r)}</p></figcaption></figure>'''

def build_about():
    stats = [('2011', 'Năm khởi đầu (tiền thân Pháp Chính)'), ('10', 'Lĩnh vực tư vấn'), ('12', 'Luật sư & chuyên gia'), ('VI · EN · JA', 'Ngôn ngữ làm việc')]
    st = ''.join(f'<div class="py-space-md"><div class="text-[34px] md:text-[40px] font-extrabold text-[#243e8f] tracking-tight">{a}</div><div class="text-[13px] uppercase tracking-wider font-semibold text-text-secondary mt-1">{E(b)}</div></div>' for a, b in stats)
    vals = ''.join(f'''<div class="relative p-space-lg rounded-2xl bg-white border border-slate-200 overflow-hidden">
<span class="absolute -right-2 -top-6 text-[120px] font-extrabold text-[#243e8f]/[0.06] leading-none select-none">{k}</span>
<span class="w-12 h-12 rounded-xl bg-[#243e8f] text-white text-[22px] font-extrabold flex items-center justify-center">{k}</span>
<h3 class="mt-space-md text-[19px] font-extrabold text-[#16285c]">{E(en)} <span class="text-[#0f71b9]">· {E(vi)}</span></h3><p class="mt-1 text-[14px] text-text-secondary leading-relaxed">{E(d)}</p></div>''' for k, en, vi, d in VALUES)
    tl = ''.join(f'''<li class="relative pl-space-lg md:pl-0 md:pt-space-lg">
<span class="absolute left-0 top-1.5 md:top-0 md:left-0 w-3.5 h-3.5 rounded-full bg-[#0f71b9] ring-4 ring-[#0f71b9]/25"></span>
<p class="text-[28px] font-extrabold text-white">{y}</p><h3 class="font-bold text-[#5aa8e6]">{E(t)}</h3><p class="text-[14px] text-blue-100 leading-relaxed mt-1">{E(d)}</p></li>''' for y, t, d in TIMELINE)
    law = ''.join(person(*p, big=True) for p in TEAM_LAWYERS)
    mgr = ''.join(person(*p) for p in TEAM_EXPERTS[:4])
    stf = ''.join(person(*p) for p in TEAM_EXPERTS[4:])
    gal = ''.join(f'<figure class="relative rounded-xl overflow-hidden {"md:col-span-2 md:row-span-2" if k == 0 else ""} group"><img loading="lazy" decoding="async" alt="{E(c)}" class="w-full h-full object-cover min-h-[180px] group-hover:scale-105 transition-transform duration-500" src="{u}"/><figcaption class="absolute bottom-0 inset-x-0 p-3 text-[13px] font-semibold text-white bg-gradient-to-t from-[#16285c]/90 to-transparent">{E(c)}</figcaption></figure>' for k, (u, c) in enumerate(GALLERY))
    logos = ''.join(f'<div class="flex items-center justify-center h-24 p-space-sm rounded-xl bg-white border border-slate-200"><img loading="lazy" decoding="async" alt="{E(n)}" class="max-h-16 max-w-full object-contain grayscale hover:grayscale-0 opacity-80 hover:opacity-100 transition" src="/anh/htic/{f}"/></div>' for f, n in zip(CLIENT_FILES, CLIENTS))
    side = '''<div class="lg:col-span-4 hidden lg:block"><div class="rounded-2xl overflow-hidden border border-white/20 shadow-2xl"><img alt="Luật sư HTIC làm việc cùng khách hàng" class="w-full h-[300px] object-cover" src="/anh/htic/cong-ty-tu-van-luat-htic279274646012.jpg"/></div></div>'''
    body = hero([('Trang chủ', '/'), ('Giới thiệu', '/gioi-thieu/')], 'Về Công ty Luật HTIC', 'Phụng sự công lý,<br/>bảo vệ lợi ích khách hàng',
                'HTIC đồng hành pháp lý cùng doanh nghiệp Việt Nam, nhà đầu tư nước ngoài và khách hàng cá nhân, với nền tảng từ năm 2011 và đội ngũ luật sư, chuyên gia nhiều lĩnh vực.',
                '/anh/dv/gioi-thieu.webp', side=side)
    body += f'''<div class="bg-white border-b border-slate-200"><div class="max-w-7xl mx-auto px-margin grid grid-cols-2 md:grid-cols-4 gap-space-md text-center md:text-left">{st}</div></div>
<section class="py-space-2xl md:py-space-3xl bg-white" id="loi-chao"><div class="max-w-7xl mx-auto px-margin grid grid-cols-1 lg:grid-cols-12 gap-space-2xl items-center">
<div class="lg:col-span-5"><div class="relative max-w-sm mx-auto"><div class="absolute -inset-3 rounded-3xl bg-[#243e8f]/10 rotate-2"></div>
<img loading="lazy" decoding="async" alt="Luật sư Trần Quốc Hưng, Giám đốc Công ty Luật HTIC" class="relative w-full aspect-[4/5] object-cover object-top rounded-2xl shadow-xl" src="{TEAM_LAWYERS[0][2]}"/></div></div>
<div class="lg:col-span-7 flex flex-col gap-space-md"><span class="text-[12px] uppercase tracking-[0.18em] font-bold text-[#0f71b9]">Lời chào từ Giám đốc</span>
{icon('format_quote','text-[56px] text-[#0f71b9] -mb-4')}
<blockquote class="text-[20px] md:text-[24px] leading-relaxed text-[#16285c] font-semibold">HTIC luôn từng bước cố gắng để khẳng định chất lượng dịch vụ. Với đội ngũ giàu kinh nghiệm, am hiểu nhiều lĩnh vực, chúng tôi cung cấp dịch vụ tư vấn pháp lý toàn diện, đáp ứng những yêu cầu khắt khe của khách hàng.</blockquote>
<p class="text-[16px] text-text-secondary leading-relaxed">HTIC mong muốn được phục vụ nhiều khách hàng hơn và từng bước phấn đấu trở thành tổ chức hành nghề luật có uy tín tại Việt Nam. Chúng tôi rất mong nhận được sự ủng hộ của quý khách hàng và đối tác.</p>
<div class="pt-space-sm border-t border-slate-200"><p class="font-extrabold text-[#243e8f] text-[18px]">LS. Trần Quốc Hưng</p><p class="text-[14px] text-text-secondary">Giám đốc, Công ty Luật HTIC</p></div></div>
</div></section>
<section class="py-space-2xl md:py-space-3xl bg-[#f2f2f3]" id="gia-tri"><div class="max-w-7xl mx-auto px-margin">{section_head('Ý nghĩa thương hiệu', 'Bốn giá trị tạo nên H.T.I.C', 'Bốn chữ cái trong tên HTIC cũng là bốn nguyên tắc chúng tôi giữ trong mọi vụ việc.')}<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-space-md">{vals}</div></div></section>
<section class="py-space-2xl md:py-space-3xl bg-[#16285c] text-white overflow-hidden" id="hanh-trinh"><div class="max-w-7xl mx-auto px-margin">{section_head('Hành trình từ 2011', 'Lịch sử và phát triển', 'Từ Công ty Tư vấn Pháp Chính đến Công ty Luật HTIC, với điểm kết nối khách hàng tại Việt Nam và Nhật Bản.', dark=True)}
<ol class="relative grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6 gap-space-lg border-l-2 md:border-l-0 md:border-t-2 border-white/15 pl-0 md:pt-0">{tl}</ol></div></section>
<section class="py-space-2xl md:py-space-3xl bg-white" id="doi-ngu"><div class="max-w-7xl mx-auto px-margin">{section_head('Con người HTIC', 'Đội ngũ luật sư', 'Mỗi vụ việc do luật sư có chuyên môn phù hợp trực tiếp phụ trách.')}
<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-space-md">{law}</div>
<h3 class="mt-space-2xl mb-space-lg text-[22px] font-extrabold text-[#243e8f]">Chuyên gia – Quản lý</h3>
<div class="grid grid-cols-2 md:grid-cols-4 gap-space-md">{mgr}</div>
<h3 class="mt-space-2xl mb-space-lg text-[22px] font-extrabold text-[#243e8f]">Chuyên viên</h3>
<div class="grid grid-cols-2 md:grid-cols-4 gap-space-md">{stf}</div></div></section>
<section class="py-space-2xl md:py-space-3xl bg-[#f2f2f3]" id="hinh-anh"><div class="max-w-7xl mx-auto px-margin">{section_head('Hoạt động', 'HTIC cùng khách hàng và đối tác')}
<div class="grid grid-cols-2 md:grid-cols-4 md:grid-rows-2 gap-space-sm md:h-[460px]">{gal}</div></div></section>
<section class="py-space-2xl md:py-space-3xl bg-white" id="khach-hang"><div class="max-w-7xl mx-auto px-margin">{section_head('Khách hàng', 'Doanh nghiệp đã đồng hành cùng HTIC', center=True)}
<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-space-sm">{logos}</div></div></section>
{cta_band('Bắt đầu bằng một buổi trao đổi với luật sư', 'Chia sẻ nhu cầu của doanh nghiệp, HTIC sẽ đề xuất hướng xử lý và báo giá rõ ràng trước khi triển khai.')}'''
    ld = [{"@type": "AboutPage", "url": BASE + "/gioi-thieu/", "name": "Giới thiệu Công ty Luật HTIC"},
          {"@type": "LegalService", "@id": BASE + "/#firm", "name": "Công ty Luật HTIC", "url": BASE + "/", "telephone": S['phone_tel'], "email": S['email'],
           "foundingDate": "2011", "slogan": "Honesty – Trust – Integrity – Commitment",
           "address": {"@type": "PostalAddress", "streetAddress": S['address'], "addressLocality": "TP. Hồ Chí Minh", "addressCountry": "VN"},
           "employee": [{"@type": "Person", "name": n.replace('LS. ', ''), "jobTitle": r} for n, r, _ in TEAM_LAWYERS]}]
    return page('/gioi-thieu/', 'Giới thiệu Công ty Luật HTIC | Đội ngũ luật sư tại TP.HCM',
                'Công ty Luật HTIC: nền tảng từ năm 2011, đội ngũ luật sư và chuyên gia tư vấn doanh nghiệp, đầu tư nước ngoài, hợp đồng và tranh chấp tại TP.HCM.',
                body, 'gioi-thieu', '/anh/hero-ban-lam-viec.webp', ld, [('Trang chủ', '/'), ('Giới thiệu', '/gioi-thieu/')])

def build_contact():
    cards = [('call', 'Hotline / Zalo', S['phone'], f'tel:{S["phone_tel"]}', 'Gọi hoặc nhắn Zalo trong giờ làm việc'),
             ('mail', 'Email', S['email'], f'mailto:{S["email"]}', 'Gửi tài liệu và yêu cầu tư vấn'),
             ('fb', 'Facebook', 'facebook.com/hticlawfirm', FB_URL, 'Cập nhật pháp lý và hoạt động của HTIC'),
             ('location_on', 'Văn phòng', S['address_short'], f'https://www.google.com/maps/search/?api=1&query={S["map_q"].replace(" ", "+")}', S['hours'])]
    c = ''.join(f'''<a class="group flex gap-space-md p-space-lg rounded-2xl bg-white border border-slate-200 hover:border-[#0f71b9] hover:shadow-lg transition-all" href="{h}" {'target="_blank" rel="noopener"' if h.startswith('http') else ''}>
<span class="w-12 h-12 shrink-0 rounded-xl {'bg-[#1877f2]' if ic=='fb' else 'bg-[#243e8f] group-hover:bg-[#0f71b9]'} text-white flex items-center justify-center transition-colors">{fb('w-6 h-6') if ic=='fb' else icon(ic,'text-[24px]')}</span>
<div><p class="text-[12px] uppercase tracking-wider font-bold text-text-muted">{E(t)}</p><p class="font-extrabold text-[#16285c] text-[17px] mt-0.5 break-words">{E(v)}</p><p class="text-[13px] text-text-secondary mt-1">{E(n)}</p></div></a>''' for ic, t, v, h, n in cards)
    prep = ['Giấy tờ pháp lý của doanh nghiệp hoặc cá nhân liên quan', 'Hợp đồng, thư từ, tài liệu trao đổi với đối tác', 'Mốc thời gian quan trọng (hạn ký, hạn nộp, ngày xảy ra sự việc)', 'Kết quả mong muốn và các phương án đã cân nhắc']
    pr = ''.join(f'<li class="flex gap-2">{icon("task_alt","text-[18px] text-[#0f71b9] shrink-0")}<span>{E(p)}</span></li>' for p in prep)
    mq = S['map_q'].replace(' ', '+')
    body = hero([('Trang chủ', '/'), ('Liên hệ', '/lien-he/')], 'Liên hệ HTIC', 'Trao đổi với luật sư HTIC',
                'Gửi yêu cầu để HTIC liên hệ trao đổi và thống nhất lịch tư vấn. Phạm vi công việc và phí dịch vụ được trao đổi rõ trước khi thực hiện.',
                '/anh/dv/lien-he.webp', ctas=False)
    body += f'''<section class="relative -mt-space-xl md:-mt-space-2xl pb-space-xl"><div class="max-w-7xl mx-auto px-margin grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-space-md">{c}</div></section>
<section class="pb-space-2xl md:pb-space-3xl bg-white"><div class="max-w-7xl mx-auto px-margin grid grid-cols-1 lg:grid-cols-12 gap-space-2xl">
<div class="lg:col-span-7 rounded-2xl border border-slate-200 p-space-lg md:p-space-xl shadow-sm">
<h2 class="text-[26px] md:text-[30px] font-extrabold text-[#243e8f] tracking-tight">Gửi yêu cầu tư vấn</h2>
<p class="mt-1 mb-space-lg text-text-secondary">Điền thông tin để soạn email gửi đến {S['email']}. Quý khách cần bấm Gửi trong ứng dụng email để hoàn tất. Nếu không mở được ứng dụng email, vui lòng liên hệ qua số điện thoại hoặc Zalo trên trang.</p>
{booking_form()}</div>
<div class="lg:col-span-5 flex flex-col gap-space-md">
<div class="rounded-2xl overflow-hidden border border-slate-200 h-[320px] bg-[#e8eaf1]"><iframe title="Bản đồ văn phòng HTIC" class="w-full h-full" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q={mq}&amp;z=16&amp;output=embed"></iframe></div>
<div class="rounded-2xl bg-[#16285c] text-white p-space-lg"><h3 class="text-[18px] font-extrabold">Văn phòng HTIC</h3><p class="mt-1 text-blue-100 text-[15px]">{E(S['address'])}</p><p class="mt-2 text-[14px] text-blue-100 flex gap-2">{icon('schedule','text-[18px] text-[#5aa8e6]')}{S['hours']}</p>
<p class="mt-space-md pt-space-md border-t border-white/15 text-[14px] text-blue-100">Khách hàng tại Nhật Bản: HTIC có điểm tiếp nhận thông tin tại Gunma, Osaka và Hiroshima. Vui lòng liên hệ email để được kết nối.</p></div>
<div class="rounded-2xl bg-[#f2f2f3] p-space-lg"><h3 class="text-[18px] font-extrabold text-[#243e8f]">Chuẩn bị cho buổi tư vấn</h3><ul class="mt-space-sm flex flex-col gap-2 text-[14px] text-slate-700">{pr}</ul></div>
</div></div></section>'''
    ld = [{"@type": "ContactPage", "url": BASE + "/lien-he/", "name": "Liên hệ Công ty Luật HTIC"},
          {"@type": "LegalService", "@id": BASE + "/#firm", "name": "Công ty Luật HTIC", "telephone": S['phone_tel'], "email": S['email'],
           "address": {"@type": "PostalAddress", "streetAddress": S['address'], "addressLocality": "TP. Hồ Chí Minh", "addressCountry": "VN"}}]
    return page('/lien-he/', 'Liên hệ Công ty Luật HTIC | Đặt lịch tư vấn luật sư TP.HCM',
                f'Liên hệ Công ty Luật HTIC: hotline {S["phone"]}, email {S["email"]}, văn phòng tại TP.HCM. Gửi yêu cầu tư vấn trực tuyến.',
                body, 'lien-he', '/anh/htic/banner-lien-he-law993993344719.jpg', ld, [('Trang chủ', '/'), ('Liên hệ', '/lien-he/')])

# ---------------------------------------------------------------- tin tuc / bai viet (WP REST)
NEWS = json.load(open(os.path.join(os.path.dirname(__file__), 'news.json'), encoding='utf-8'))
CATS = {
    'all': {'cat': '4,59', 'path': '/tin-tuc/', 'name': 'Tất cả', 'h1': 'Tin tức &amp; Bài viết pháp lý',
            'lead': 'Tin pháp luật mới và bài phân tích chuyên sâu do luật sư HTIC biên soạn, sắp xếp theo thời gian để Quý khách dễ theo dõi.'},
    'tin': {'cat': '4', 'path': '/tin-phap-ly/', 'name': 'Tin pháp lý', 'h1': 'Tin pháp lý',
            'lead': 'Văn bản pháp luật mới, thời điểm hiệu lực và điểm thay đổi đáng chú ý, kèm nhận định ngắn của luật sư HTIC về tác động đối với doanh nghiệp và cá nhân.'},
    'bai': {'cat': '59', 'path': '/bai-viet-phap-ly/', 'name': 'Bài viết pháp lý', 'h1': 'Bài viết pháp lý',
            'lead': 'Bài phân tích chuyên sâu về bất động sản, xây dựng, đầu tư, hợp đồng, doanh nghiệp và tranh chấp, dựa trên quy định hiện hành và thực tiễn hành nghề của HTIC.'},
}
TOPICS = ['Xây dựng', 'Đất đai', 'Bất động sản', 'Nhà ở', 'Hợp đồng', 'Doanh nghiệp', 'Đầu tư', 'Thuế', 'Lao động', 'Tranh chấp']
FALLBACK_IMG = '/anh/htic/htic-cover418503887709.jpg'

def fmt_date(d):
    y, m, dd = d.split('-'); return f'{dd}/{m}/{y}'

def type_name(x):
    return 'Tin pháp lý' if 4 in x.get('c', [4]) else 'Bài viết pháp lý'

def type_chip(name):
    if name == 'Tin pháp lý':
        return f'<span class="inline-flex items-center px-2 py-0.5 rounded-md bg-[#e6f1fa] text-[#0f71b9] text-[12px] font-bold">{name}</span>'
    return f'<span class="inline-flex items-center px-2 py-0.5 rounded-md bg-[#eceff7] text-[#243e8f] text-[12px] font-bold">{name}</span>'

def post_card(x, tag=None):
    """The dung tren trang chu."""
    tag = tag or type_name(x)
    img = x.get('i') or FALLBACK_IMG
    return f'''<article class="group flex flex-col bg-white rounded-2xl border border-slate-200 overflow-hidden hover:border-[#0f71b9]/40 hover:shadow-[0_16px_40px_rgba(36,62,143,0.12)] transition-all duration-300">
<a class="block aspect-[16/9] overflow-hidden bg-[#eef2f8]" href="{x['l']}" tabindex="-1" aria-hidden="true"><img loading="lazy" decoding="async" alt="" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" src="{img}"/></a>
<div class="flex flex-col gap-space-xs p-space-md flex-1">
<div class="flex items-center gap-2 text-[12px] font-semibold text-slate-500">{type_chip(tag)}<time datetime="{x['d']}">{fmt_date(x['d'])}</time></div>
<h3 class="text-[17px] leading-snug font-bold text-[#16285c] group-hover:text-[#0f71b9] transition-colors"><a href="{x['l']}">{x['t']}</a></h3>
<p class="text-[14px] text-slate-600 leading-relaxed line-clamp-3">{E(x['e'])}</p>
</div></article>'''

def post_row(x):
    img = x.get('s') or x.get('i') or FALLBACK_IMG
    return f'''<article class="nr group relative flex gap-space-md py-space-md border-b border-slate-200">
<a class="shrink-0 block w-[104px] sm:w-[168px] aspect-[4/3] rounded-lg overflow-hidden bg-[#eef2f8]" href="{x['l']}" tabindex="-1" aria-hidden="true"><img loading="lazy" decoding="async" alt="" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="{img}"/></a>
<div class="min-w-0 flex flex-col gap-1.5">
<div class="flex flex-wrap items-center gap-2 text-[13px] text-slate-500">{type_chip(type_name(x))}<time datetime="{x['d']}">{fmt_date(x['d'])}</time></div>
<h3 class="text-[16px] sm:text-[18px] leading-snug font-bold text-[#16285c] group-hover:text-[#0f71b9] transition-colors line-clamp-3 sm:line-clamp-2"><a class="after:absolute after:inset-0" href="{x['l']}">{x['t']}</a></h3>
<p class="max-sm:hidden text-[14px] text-slate-600 leading-relaxed line-clamp-2">{E(x['e'])}</p>
</div></article>'''

def month_head(d):
    y, m, _ = d.split('-')
    return f'<h2 class="nm pt-space-lg pb-1 text-[12px] font-extrabold uppercase tracking-[0.16em] text-[#0f71b9] flex items-center gap-3">Tháng {int(m)}/{y}<span class="flex-1 h-px bg-slate-200"></span></h2>'

def featured(x):
    img = x.get('i') or FALLBACK_IMG
    return f'''<article id="newsFeatured" class="group relative grid grid-cols-1 md:grid-cols-2 gap-space-lg items-start pb-space-lg border-b border-slate-200">
<a class="block aspect-[16/10] rounded-2xl overflow-hidden bg-[#eef2f8]" href="{x['l']}" tabindex="-1" aria-hidden="true"><img fetchpriority="high" decoding="async" alt="" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" src="{img}"/></a>
<div class="flex flex-col gap-space-sm">
<div class="flex flex-wrap items-center gap-2 text-[13px] text-slate-500"><span class="text-[12px] font-extrabold uppercase tracking-[0.14em] text-[#0f71b9]">Mới nhất</span>{type_chip(type_name(x))}<time datetime="{x['d']}">{fmt_date(x['d'])}</time></div>
<h2 class="text-[20px] md:text-[22px] leading-snug font-extrabold text-[#16285c] group-hover:text-[#0f71b9] transition-colors line-clamp-4"><a class="after:absolute after:inset-0" href="{x['l']}">{x['t']}</a></h2>
<p class="text-[15px] text-slate-600 leading-relaxed line-clamp-4">{E(x['e'])}</p>
<span class="inline-flex items-center gap-1 text-[14px] font-bold text-[#0f71b9]">Đọc bài {icon('arrow_forward','text-[16px]')}</span>
</div></article>'''

def rows_grouped(items):
    out, last = [], None
    for x in items:
        mk = x['d'][:7]
        if mk != last:
            out.append(month_head(x['d'])); last = mk
        out.append(post_row(x))
    return ''.join(out)

NEWS_JS = r"""<script>
(function(){var L=document.getElementById('newsList');if(!L)return;
var cat=L.getAttribute('data-cat'),total=+L.getAttribute('data-total'),q='',busy=false,
last=L.getAttribute('data-last'),more=document.getElementById('newsMore'),info=document.getElementById('newsInfo'),F=document.getElementById('newsFeatured'),form=document.getElementById('newsSearch'),chips=document.querySelectorAll('[data-topic]');
function esc(s){var d=document.createElement('div');d.textContent=s||'';return d.innerHTML}
function dmy(s){var d=s.slice(0,10).split('-');return d[2]+'/'+d[1]+'/'+d[0]}
function chip(c){return c.indexOf(4)>-1?'<span class="inline-flex items-center px-2 py-0.5 rounded-md bg-[#e6f1fa] text-[#0f71b9] text-[12px] font-bold">Tin pháp lý</span>':'<span class="inline-flex items-center px-2 py-0.5 rounded-md bg-[#eceff7] text-[#243e8f] text-[12px] font-bold">Bài viết pháp lý</span>'}
function img(p){var m=p._embedded&&p._embedded['wp:featuredmedia']&&p._embedded['wp:featuredmedia'][0];if(!m||!m.source_url)return '/anh/htic/htic-cover418503887709.jpg';var z=m.media_details&&m.media_details.sizes||{};return (z.medium||z.thumbnail||{}).source_url||m.source_url}
function row(p){var l=p.link.replace(location.origin,''),ex=(p.excerpt.rendered||'').replace(/<[^>]+>/g,'').replace(/\s+/g,' ').trim();
return '<article class="nr group relative flex gap-space-md py-space-md border-b border-slate-200"><a class="shrink-0 block w-[104px] sm:w-[168px] aspect-[4/3] rounded-lg overflow-hidden bg-[#eef2f8]" href="'+l+'" tabindex="-1" aria-hidden="true"><img loading="lazy" decoding="async" alt="" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="'+img(p)+'"/></a><div class="min-w-0 flex flex-col gap-1.5"><div class="flex flex-wrap items-center gap-2 text-[13px] text-slate-500">'+chip(p.categories||[])+'<time>'+dmy(p.date)+'</time></div><h3 class="text-[16px] sm:text-[18px] leading-snug font-bold text-[#16285c] group-hover:text-[#0f71b9] transition-colors line-clamp-3 sm:line-clamp-2"><a class="after:absolute after:inset-0" href="'+l+'">'+p.title.rendered+'</a></h3><p class="max-sm:hidden text-[14px] text-slate-600 leading-relaxed line-clamp-2">'+esc(ex)+'</p></div></article>'}
function head(s){var d=s.slice(0,10).split('-');return '<h2 class="nm pt-space-lg pb-1 text-[12px] font-extrabold uppercase tracking-[0.16em] text-[#0f71b9] flex items-center gap-3">Tháng '+(+d[1])+'/'+d[0]+'<span class="flex-1 h-px bg-slate-200"></span></h2>'}
function base(){return F&&!q?1:0}
function rows(){return L.querySelectorAll('article').length}
function setInfo(){var n=base()+rows();info.textContent=q?('Tìm thấy '+total+' bài cho “'+q+'”'+(total?', mới nhất trước':'')):('Đang hiển thị '+Math.min(n,total)+' / '+total+' bài, mới nhất trước')}
function load(reset){if(busy)return;busy=true;more.disabled=true;more.textContent='Đang tải…';
if(reset){L.innerHTML='';last='';if(F)F.hidden=!!q}
var u='/wp-json/wp/v2/posts?categories='+cat+'&per_page=12&offset='+(base()+rows())+'&_embed=wp:featuredmedia&_fields=id,link,title,date,excerpt,categories,_links,_embedded'+(q?'&search='+encodeURIComponent(q):'');
fetch(u).then(function(r){var t=+r.headers.get('X-WP-Total');return r.json().then(function(a){return{a:a,t:t}})}).then(function(o){
if(o.t||o.t===0)total=o.t;var h='';o.a.forEach(function(p){var mk=p.date.slice(0,7);if(mk!==last){h+=head(p.date);last=mk}h+=row(p)});L.insertAdjacentHTML('beforeend',h);
if(!rows())L.innerHTML='<p class="py-space-xl text-center text-slate-600">Chưa có bài phù hợp. Thử từ khóa khác hoặc chọn “Tất cả chủ đề”.</p>';
more.hidden=base()+rows()>=total;setInfo()}).catch(function(){info.textContent='Không tải được danh sách. Vui lòng thử lại.'}).then(function(){busy=false;more.disabled=false;more.textContent='Xem thêm bài'})}
function search(v){q=(v||'').trim();chips.forEach(function(c){var on=(c.getAttribute('data-topic')||'')===q;c.classList.toggle('bg-[#243e8f]',on);c.classList.toggle('text-white',on);c.classList.toggle('border-[#243e8f]',on);c.classList.toggle('bg-white',!on);c.setAttribute('aria-pressed',on)});
if(form)form.elements.q.value=q;try{var s=new URL(location.href);if(q)s.searchParams.set('q',q);else s.searchParams.delete('q');history.replaceState(null,'',s)}catch(e){}
load(true)}
more.addEventListener('click',function(){load(false)});
if(form)form.addEventListener('submit',function(e){e.preventDefault();search(form.elements.q.value)});
chips.forEach(function(c){c.addEventListener('click',function(){search(c.getAttribute('data-topic'))})});
var q0=new URLSearchParams(location.search).get('q');if(q0)search(q0);else setInfo();})();
</script>"""

def build_news(key):
    c = CATS[key]; d = NEWS[key]; items = d['items']
    feat, rest = items[0], items[1:]
    tabs = ''.join(
        f'<a class="px-space-md py-2 rounded-lg text-[14px] font-bold transition-colors {"bg-[#243e8f] text-white shadow-sm" if k == key else "text-[#243e8f] hover:bg-white"}" href="{CATS[k]["path"]}"{" aria-current=page" if k == key else ""}>{CATS[k]["name"]} <span class="ml-1 opacity-70 font-semibold">{NEWS[k]["total"]}</span></a>'
        for k in ('all', 'tin', 'bai'))
    chips = '<button type="button" data-topic="" aria-pressed="true" class="shrink-0 px-3 py-1.5 rounded-full border text-[13px] font-semibold transition-colors bg-[#243e8f] text-white border-[#243e8f]">Tất cả chủ đề</button>' + ''.join(
        f'<button type="button" data-topic="{t}" aria-pressed="false" class="shrink-0 px-3 py-1.5 rounded-full border border-slate-200 bg-white text-[13px] font-semibold text-slate-700 hover:border-[#243e8f] hover:text-[#243e8f] transition-colors">{t}</button>' for t in TOPICS)
    other = 'bai' if key == 'tin' else 'tin'
    side_items = NEWS[other]['items'][:5] if key != 'all' else NEWS['bai']['items'][:5]
    side_title = CATS[other]['name'] + ' mới' if key != 'all' else 'Bài phân tích mới'
    side_path = CATS[other]['path'] if key != 'all' else '/bai-viet-phap-ly/'
    side_list = ''.join(f'<li class="py-space-sm border-b border-slate-100 last:border-0"><a class="group block" href="{x["l"]}"><time class="text-[12px] font-semibold text-slate-500" datetime="{x["d"]}">{fmt_date(x["d"])}</time><span class="block text-[14px] leading-snug font-semibold text-[#16285c] group-hover:text-[#0f71b9] line-clamp-3">{x["t"]}</span></a></li>' for x in side_items)
    crumbs = [('Trang chủ', '/'), ('Tin tức & Bài viết', '/tin-tuc/')] + ([(c['name'], c['path'])] if key != 'all' else [])
    crumb_html = ''.join((f'<a class="hover:text-[#0f71b9]" href="{h}">{E(n)}</a>{icon("chevron_right","text-[16px] opacity-50")}' if i < len(crumbs) - 1 else f'<span class="text-slate-700" aria-current="page">{E(n)}</span>') for i, (n, h) in enumerate(crumbs))
    body = f'''<section class="-mt-[120px] pt-[146px] pb-space-lg bg-[#f4f6fa] border-b border-slate-200">
<div class="max-w-7xl mx-auto px-margin">
<nav class="flex flex-wrap items-center gap-1 text-[14px] text-slate-500" aria-label="Breadcrumb">{crumb_html}</nav>
<div class="hero-in mt-space-md flex flex-col gap-space-sm max-w-3xl">
<h1 class="text-[32px] md:text-[42px] leading-tight font-extrabold tracking-tight text-[#16285c]">{c['h1']}</h1>
<p class="text-[16px] md:text-[17px] text-slate-600 leading-relaxed">{E(c['lead'])}</p>
</div>
<nav class="mt-space-lg inline-flex flex-wrap gap-1 p-1 rounded-xl bg-[#e8ecf4]" aria-label="Loại bài">{tabs}</nav>
</div></section>
<section class="py-space-lg md:py-space-xl bg-white"><div class="max-w-7xl mx-auto px-margin grid grid-cols-1 lg:grid-cols-12 gap-space-2xl">
<div class="lg:col-span-8 min-w-0">
<form id="newsSearch" class="flex items-center gap-2 bg-white border border-slate-300 rounded-xl pl-4 pr-1.5 py-1.5 focus-within:border-[#0f71b9] focus-within:ring-2 focus-within:ring-[#0f71b9]/15" role="search"><label class="sr-only" for="q">Tìm bài</label>{icon('search','text-[22px] text-slate-400')}<input id="q" name="q" type="search" class="flex-1 min-w-0 bg-transparent border-0 focus:ring-0 text-[15px] py-2 outline-none" placeholder="Tìm theo từ khóa, số hiệu văn bản (vd: 135/2025/QH15)"/><button class="bg-[#243e8f] hover:bg-[#0f71b9] text-white text-[14px] font-bold px-5 py-2.5 rounded-lg">Tìm</button></form>
<div class="mt-space-sm flex gap-2 overflow-x-auto pb-2 -mx-1 px-1" role="group" aria-label="Chủ đề nhanh">{chips}</div>
<p id="newsInfo" class="mt-space-sm mb-space-md text-[14px] text-slate-500" aria-live="polite">Đang hiển thị {len(items)} / {d['total']} bài, mới nhất trước</p>
{featured(feat)}
<div id="newsList" data-cat="{c['cat']}" data-total="{d['total']}" data-last="{rest[-1]['d'][:7] if rest else ''}">{rows_grouped(rest)}</div>
<button id="newsMore" class="mt-space-lg w-full inline-flex items-center justify-center gap-2 border border-[#243e8f] text-[#243e8f] hover:bg-[#243e8f] hover:text-white font-bold py-3.5 rounded-xl transition-colors" {'hidden' if int(d['total']) <= len(items) else ''}>Xem thêm bài</button>
</div>
<aside class="lg:col-span-4"><div class="lg:sticky lg:top-[140px] flex flex-col gap-space-lg">
<div class="rounded-2xl border border-slate-200 p-space-lg"><div class="flex items-center justify-between gap-2 mb-1"><p class="text-[16px] font-extrabold text-[#16285c]">{side_title}</p><a class="text-[13px] font-bold text-[#0f71b9]" href="{side_path}">Xem tất cả</a></div><ul>{side_list}</ul></div>
<div class="rounded-2xl bg-[#16285c] text-white p-space-lg flex flex-col gap-space-sm">
<p class="text-[18px] font-extrabold">Cần áp dụng cho trường hợp cụ thể?</p>
<p class="text-[14px] text-blue-100 leading-relaxed">Bài viết mang tính tham khảo. Gửi hồ sơ để luật sư HTIC xem xét và tư vấn đúng tình huống của Quý khách.</p>
<a class="flex items-center gap-2 font-bold text-[16px]" href="tel:{S['phone_tel']}">{icon('call','text-[20px] text-[#5aa8e6]')}{S['phone']}</a>
<div class="flex gap-2 pt-1"><a class="flex-1 text-center bg-[#0f71b9] hover:bg-white hover:text-[#243e8f] font-bold py-2.5 rounded-lg transition-colors" href="/lien-he/">Đặt lịch</a><a class="flex-1 text-center bg-white/10 hover:bg-white/20 font-bold py-2.5 rounded-lg border border-white/20" target="_blank" rel="noopener" href="{S['zalo']}">Zalo</a></div>
</div>
<div class="rounded-2xl border border-slate-200 p-space-lg"><p class="text-[15px] font-extrabold text-[#16285c]">Theo dõi tin mới từ HTIC</p><p class="text-[14px] text-slate-600 mt-1">Nhận cập nhật pháp luật qua Facebook và Zalo OA của HTIC.</p><div class="flex gap-2 mt-space-sm"><a class="flex-1 inline-flex items-center justify-center gap-1.5 bg-[#1877f2] text-white text-[14px] font-bold py-2.5 rounded-lg" target="_blank" rel="noopener" href="{FB_URL}">{fb('w-4 h-4')}Facebook</a><a class="flex-1 text-center bg-[#0f71b9] text-white text-[14px] font-bold py-2.5 rounded-lg" target="_blank" rel="noopener" href="{S['zalo']}">Zalo OA</a></div></div>
</div></aside>
</div></section>'''
    ld = [{"@type": "CollectionPage", "name": html.unescape(c['h1']) + ' – Công ty Luật HTIC', "url": BASE + c['path'], "inLanguage": "vi",
           "publisher": {"@id": BASE + "/#firm"},
           "hasPart": [{"@type": "Article", "headline": html.unescape(x['t']), "url": BASE + x['l'], "datePublished": x['d']} for x in items]}]
    title = f"{c['name']} | Công ty Luật HTIC" if key != 'all' else 'Tin tức & Bài viết pháp lý | Công ty Luật HTIC'
    c = dict(c, name=c['name'] if key != 'all' else 'Tin tức & Bài viết')
    return page(c['path'], title, c['lead'][:155], body + NEWS_JS, 'tin-tuc', FALLBACK_IMG, ld, crumbs)

def build_news_hub():
    return build_news('all')


def write(rel, content):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(content)
    return rel

if __name__ == '__main__':
    out = [write('gioi-thieu/index.html', build_about()), write('dich-vu/index.html', build_services_index()), write('lien-he/index.html', build_contact())]
    out += [write('tin-tuc/index.html', build_news_hub()), write('tin-phap-ly/index.html', build_news('tin')), write('bai-viet-phap-ly/index.html', build_news('bai'))]
    for i, s in enumerate(SERVICES):
        out.append(write(f'dich-vu/{s["slug"]}/index.html', build_service(i, s)))
    # shared header/footer snippets for the homepage
    write('../hticlaw-build/_header.html', header())
    write('../hticlaw-build/_footer.html', footer())
    write('../hticlaw-build/_motion.html', MOTION_HEAD + '\n' + MOTION_JS)
    # bo khung dung chung cho cac trang WordPress (theme doc tu /assets/wp/)
    write('assets/wp/header.html', header())
    write('assets/wp/header-news.html', header('tin-tuc'))
    LAZY_FIX = """<script id="htic-lazyfix">(function(){[].forEach.call(document.querySelectorAll('img[data-src]'),function(i){if(i.src&&i.src.indexOf('data:')!==0)return;if(!i.closest('#site-header,.hero-in')&&i.getBoundingClientRect().top>innerHeight)i.loading='lazy';if(i.dataset.srcset)i.srcset=i.dataset.srcset;if(i.dataset.sizes)i.sizes=i.dataset.sizes;i.src=i.dataset.src;i.removeAttribute('data-src');i.classList.remove('litespeed-lazy')});[].forEach.call(document.querySelectorAll('iframe[data-src]'),function(f){if(!f.src||f.src.indexOf('about:')===0){f.loading='lazy';f.src=f.dataset.src}})})();</script>"""
    write('assets/wp/footer.html', footer() + '\n' + LAZY_FIX + '\n' + MOTION_JS)
    print('\n'.join(out))
