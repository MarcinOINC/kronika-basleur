#!/usr/bin/env python3
"""Wrap page.html (Claude Artifact form) into a standalone index.html.

The artifact platform supplies the doctype, <head> and <body> at publish time,
so page.html carries only <title>, <link>, <style> and the markup. Outside the
platform the document has to be complete, or the browser falls into quirks mode
and the layout breaks. Run this after every edit to page.html, then commit both.
"""
import io
import pathlib

BASE = 'https://marcinoinc.github.io/kronika-basleur'
ROOT = pathlib.Path(__file__).parent

# Fleur-de-lys as the favicon — same shape as the ornament on the title page.
LYS = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 48'>"
    "<path fill='%239a2a1c' d='M20 2C24 10 25 16 22.5 22h-5C15 16 16 10 20 2Z"
    "M17.2 22C10 22 5 18 5 13c0-4 3-6 6-4 2.5 1.6 3.5 6 6.2 9Z"
    "M22.8 22C30 22 35 18 35 13c0-4-3-6-6-4-2.5 1.6-3.5 6-6.2 9Z"
    "M13 22.6h14v3.4H13z"
    "M17.6 27h4.8c0 6 2.6 11 5.6 14-4 2-12 2-16 0 3-3 5.6-8 5.6-14Z'/></svg>"
)

src = io.open(ROOT / 'page.html', encoding='utf-8').read()
cut = src.index('</style>') + len('</style>')
head_inner, body_inner = src[:cut], src[cut:].strip()

doc = f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Materiały od Mistrza Gry do sesji Warhammer Fantasy Roleplay 2ed w Baronii Basleur.">
<meta property="og:type" content="article">
<meta property="og:title" content="Kronika Baronii Basleur">
<meta property="og:description" content="Materiały od Mistrza Gry do sesji Warhammer Fantasy Roleplay 2ed.">
<meta property="og:image" content="{BASE}/ryciny/dwor-barona.jpg">
<meta property="og:url" content="{BASE}/">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,{LYS}">
<style>body{{margin:0}}img{{max-width:100%}}</style>
{head_inner}
</head>
<body>
{body_inner}
</body>
</html>
'''
io.open(ROOT / 'index.html', 'w', encoding='utf-8').write(doc)
print(f'index.html: {len(doc)} znaków')
