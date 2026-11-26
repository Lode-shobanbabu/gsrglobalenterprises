# scratch/verify_faq_cleanup.py
import subprocess

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

open_b = css.count('{')
close_b = css.count('}')
print(f'CSS Braces: {open_b} open, {close_b} close (Balanced: {open_b == close_b})')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
print("FAQ in HTML:", "faq" in html.lower())

with open('js/script.js', 'r', encoding='utf-8') as f:
    js = f.read()
print("FAQ in JS:", "faq" in js.lower())

print("FAQ in CSS:", "faq" in css.lower())
