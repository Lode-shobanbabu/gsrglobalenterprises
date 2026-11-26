with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.finditer(r'@media\s*\((max-width:\s*[0-9.]+px)\)\s*\{', css)
print("Breakpoints found in css:")
for m in matches:
    print(m.group(0))
