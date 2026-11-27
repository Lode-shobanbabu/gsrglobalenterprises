with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("Fonts in HTML:")
for m in re.finditer(r'<link[^>]*fonts[^>]*>', html, re.I):
    print(m.group(0))

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

print("\nFont variables/declarations in CSS:")
for line in css.splitlines()[:100]:
    if '--font' in line or 'font-family' in line:
        print(line)

print("\nOccurrences of Roboto or font-body:")
for i, line in enumerate(css.splitlines()):
    if 'Roboto' in line or '--font-body' in line:
        print(f"Line {i+1}: {line.strip()}")
