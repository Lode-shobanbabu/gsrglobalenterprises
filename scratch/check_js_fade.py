with open('js/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

print("Length of js:", len(js))
import re
for m in re.finditer(r'fade-up|observer|opacity', js, re.I):
    print(m.group(0), "at index", m.start())
