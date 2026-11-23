# -*- coding: utf-8 -*-
"""Xuat toan van cac trang (trang chu + 13 trang con) ra noi-dung-trang-con.md de An ra soat."""
import re, glob, html, time, os
from html.parser import HTMLParser
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
class P(HTMLParser):
    def __init__(s): super().__init__(); s.out = []; s.skip = 0; s.inmain = 0
    def handle_starttag(s, t, a):
        if t == 'main': s.inmain = 1
        if t in ('script', 'style', 'svg'): s.skip += 1
        if t in ('h1', 'h2', 'h3', 'p', 'li', 'summary', 'blockquote', 'figcaption', 'div', 'a', 'button', 'label'): s.out.append('\n')
        if t == 'h1': s.out.append('# ')
        if t == 'h2': s.out.append('## ')
        if t == 'h3': s.out.append('### ')
        if t == 'summary': s.out.append('Hỏi: ')
    def handle_endtag(s, t):
        if t == 'main': s.inmain = 0
        if t in ('script', 'style', 'svg'): s.skip -= 1
    def handle_data(s, d):
        if s.inmain and not s.skip: s.out.append(d)
files = ['hticlaw-site/index.html', 'hticlaw-site/gioi-thieu/index.html', 'hticlaw-site/dich-vu/index.html', 'hticlaw-site/lien-he/index.html'] + sorted(glob.glob('hticlaw-site/dich-vu/*/index.html'))
out = ['# Toàn văn 14 trang hticlaw.vn (trang chủ + 13 trang con), bản đang đăng ' + time.strftime('%d/%m/%Y %H:%M UTC') + '\n']
for f in files:
    h = open(f, encoding='utf-8').read()
    h = re.sub(r'<span class="material-symbols-outlined[^>]*>[^<]*</span>', '', h)
    p = P(); p.feed(h); txt = ''.join(p.out)
    txt = re.sub(r'[ \t]+', ' ', txt); txt = re.sub(r'\n\s*\n+', '\n', txt).strip()
    url = 'https://hticlaw.vn/' + f.replace('hticlaw-site/', '').replace('index.html', '')
    title = re.search(r'<title>(.*?)</title>', h, re.S).group(1).strip()
    desc = re.search(r'name="description" content="(.*?)"', h).group(1)
    out.append(f'\n\n=====================\nURL: {url}\nTITLE: {html.unescape(title)}\nMETA: {html.unescape(desc)}\n---------------------\n{txt}')
open('hticlaw-build/noi-dung-trang-con.md', 'w', encoding='utf-8').write(''.join(out))
print(len(files), 'pages', len(''.join(out)), 'chars')
