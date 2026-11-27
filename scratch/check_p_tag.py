import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

p_open = len(re.findall(r'<p\b', html))
p_close = html.count('</p>')
print(f"<p>: {p_open} open, {p_close} close (Balanced: {p_open == p_close})")
