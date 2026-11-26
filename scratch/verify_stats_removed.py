# scratch/verify_stats_removed.py

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("about-corp-stats-bar in HTML:", "about-corp-stats-bar" in html)
print("100+ Verified Consignments in HTML:", "Verified Consignments" in html)

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

print("about-corp-stats-bar in CSS:", "about-corp-stats-bar" in css)
print("about-stat-border in CSS:", "about-stat-border" in css)

open_b = css.count('{')
close_b = css.count('}')
print(f'CSS Braces: {open_b} open, {close_b} close (Balanced: {open_b == close_b})')
