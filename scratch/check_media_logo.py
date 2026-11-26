with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'@media[^{]+\{[^}]*brand-logo-img[^}]*\}', css)
print("Mobile media queries with brand-logo-img:")
for m in matches:
    print(m)
