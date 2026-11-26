# scratch/verify_compact.py
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find each card
card_pattern = re.compile(r'<div class="service-pro-card[^"]*">(.*?)</div>\s*</div>\s*</div>', re.DOTALL)
cards = card_pattern.findall(html)
print(f'Total cards matched: {len(cards)}')

# Let's count li tags in each service-pro-checklist
lists = re.findall(r'<ul class="service-pro-checklist">(.*?)</ul>', html, re.DOTALL)
print(f'Total checklists found: {len(lists)}')
for idx, l in enumerate(lists, 1):
    items = re.findall(r'<li>.*?<span>(.*?)</span>.*?</li>', l, re.DOTALL)
    print(f'Card {idx}: {len(items)} items -> {items}')

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

open_b = css.count('{')
close_b = css.count('}')
print(f'CSS Braces: {open_b} open, {close_b} close (Balanced: {open_b == close_b})')
