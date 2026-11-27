with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'(\.commitment[^{]+{[^}]+})', text)
for m in matches:
    print(m.group(0))
    print('-'*30)
