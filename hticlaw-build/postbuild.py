# -*- coding: utf-8 -*-
"""Gan header/footer chung vao trang chu, bien dich Tailwind, gan danh sach icon."""
import re, os, glob, subprocess, sys, time
sys.path.insert(0, os.path.dirname(__file__))
from data import SITE as S
B = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(B, '..', 'hticlaw-site')
TW = '/tmp/claude-0/-home-claude/29952afb-eca8-52b1-ab47-2e004f503ff4/scratchpad/tw'
VER = time.strftime('%Y%m%d%H%M')
idx = os.path.join(R, 'index.html'); h = open(idx, encoding='utf-8').read()
hdr = open(os.path.join(B, '_header.html'), encoding='utf-8').read()
ftr = open(os.path.join(B, '_footer.html'), encoding='utf-8').read()
h = re.sub(r'<header class="fixed top-0.*?</header>', lambda m: hdr, h, count=1, flags=re.S)
h = re.sub(r'<footer class="w-full bg-\[#16285c\].*?</footer>(\s*<a href="https://zalo.me[^>]*>.*?</a>)?', lambda m: ftr, h, count=1, flags=re.S)
# dia chi / gio lam viec thong nhat
for old in ['Tầng 2, số 79/6 Hoàng Văn Thái, KP.1, P. Tân Mỹ, TP.HCM', 'Tầng 2, 79/6 Hoàng Văn Thái, KP.1, P. Tân Mỹ, TP.HCM']:
    h = h.replace(old, S['address'])
h = h.replace('T2 – T7 · 08:00 – 17:30', S['hours_short'])
h = h.replace('href="#dat-lich-form">Liên hệ', 'href="/lien-he/">Liên hệ')
import json
def fix_ld(m):
    j = json.loads(m.group(1))
    for g in j.get('@graph', []):
        if g.get('@id', '').endswith('#firm'):
            g['address']['streetAddress'] = S['street_ld']
            g['openingHoursSpecification'] = [{"@type": "OpeningHoursSpecification", "dayOfWeek": S['days'], "opens": S['opens'], "closes": S['closes']}]
    return '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False) + '</script>'
h = re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix_ld, h, count=1, flags=re.S)
# tin moi nhat that tu WordPress cho trang chu
import build_pages as BP
_grid = '<div id="home-news" class="grid grid-cols-1 md:grid-cols-3 gap-space-lg">' + ''.join(BP.post_card(x) for x in BP.NEWS['all']['items'][:3]) + '</div>'
h = re.sub(r'(<section class="py-space-3xl bg-\[#f2f2f3\]" id="tin-phap-ly">.*?)<div (?:id="home-news" )?class="grid grid-cols-1 md:grid-cols-3 gap-space-lg">.*?</div>\s*</div>\s*</section>',
           lambda m: m.group(1) + _grid + '\n</div>\n</section>', h, count=1, flags=re.S)
mot = open(os.path.join(B, '_motion.html'), encoding='utf-8').read()
mh, mj = mot.split('\n', 1)
h = re.sub(r'<script id="htic-motion-head">.*?</script>\n?', '', h, flags=re.S)
h = re.sub(r'<script id="htic-motion">.*?</script>\s*<script type="speculationrules">.*?</script>\n?', '', h, flags=re.S)
h = h.replace('</head>', mh + '\n</head>', 1).replace('</body>', mj + '\n</body>', 1)
open(idx, 'w', encoding='utf-8').write(h)
pages = [idx] + glob.glob(os.path.join(R, '*/index.html')) + glob.glob(os.path.join(R, '*/*/index.html'))
pages = [p for p in pages if '/anh/' not in p]
icons = set()
for p in pages:
    icons |= set(re.findall(r'material-symbols-outlined[^"]*"[^>]*>\s*([a-z_0-9]+)\s*<', open(p, encoding='utf-8').read()))
WP = os.path.join(B, '..', 'hticlaw-wp')
for p in glob.glob(os.path.join(WP, '**', '*.php'), recursive=True):
    icons |= set(re.findall(r"htic26_i\(\s*'([a-z_0-9]+)'", open(p, encoding='utf-8').read()))
for p in glob.glob(os.path.join(R, 'assets', 'wp', '*.html')):
    icons |= set(re.findall(r'material-symbols-outlined[^"]*"[^>]*>\s*([a-z_0-9]+)\s*<', open(p, encoding='utf-8').read()))
ic = ','.join(sorted(icons))
link = f'<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0..1,0&amp;icon_names={ic}&amp;display=block" rel="stylesheet"/>'
os.makedirs(os.path.join(R, 'assets'), exist_ok=True)
css = os.path.join(R, 'assets', 'htic.css')
inp = os.path.join(B, 'tw-input.css')
if not os.path.exists(inp):
    open(inp, 'w').write("@tailwind base;@tailwind components;@tailwind utilities;\nhtml,body{font-family:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}\ndetails>summary::-webkit-details-marker{display:none}\n")
subprocess.run(['npx', 'tailwindcss', '-c', os.path.join(TW, 'tailwind.all.config.js'), '-i', inp, '-o', css, '--minify'], cwd=TW, check=True)
c = open(css, encoding='utf-8').read()
for p in pages:
    t = open(p, encoding='utf-8').read()
    t = re.sub(r'<link href="https://fonts.googleapis.com/css2\?family=Material\+Symbols[^>]*>', lambda m: link, t)
    t = t.replace('<!--ICONS-->', link).replace('__VER__', VER)
    if p == idx:
        t = re.sub(r'<style>\*,::backdrop.*?</style>', lambda m: '<style>' + c + '</style>', t, count=1, flags=re.S)
    open(p, 'w', encoding='utf-8').write(t)
print(len(pages), 'pages;', len(icons), 'icons;', len(c), 'css bytes')
# head dung chung cho trang WordPress
open(os.path.join(R, 'assets', 'wp', 'head.html'), 'w', encoding='utf-8').write(
    '<link rel="icon" href="/anh/brand/favicon-48.png" sizes="48x48" type="image/png"/>\n'
    '<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>\n'
    '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&amp;display=swap" rel="stylesheet"/>\n'
    + link + '\n<link rel="stylesheet" href="/assets/htic.css?v=' + VER + '"/>\n' + mh + '\n')
print('wp head ok')
