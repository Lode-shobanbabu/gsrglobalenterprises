with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
for m in re.finditer(r'<i[^>]*chevron[^>]*>', html, re.I):
    print("Found chevron in HTML:", m.group(0))

for m in re.finditer(r'<i[^>]*caret[^>]*>', html, re.I):
    print("Found caret in HTML:", m.group(0))

for m in re.finditer(r'<i[^>]*angle[^>]*>', html, re.I):
    print("Found angle in HTML:", m.group(0))

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

for m in re.finditer(r'checklist[^{]*\{[^}]*\}', css, re.I):
    print("CSS checklist rule:", m.group(0))
