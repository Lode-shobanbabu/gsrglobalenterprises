with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.about-[^{]*\{[^}]*\})', css)
for m in matches:
    print(m)
    print('-'*30)
