with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'@media[^{]*991\.98px[^{]*\{([^}]+(?:\}[^}]+)*)\}', css)
for m in matches[:3]:
    if 'navbar' in m or 'nav-link' in m or 'header-cta' in m:
        print("Mobile nav block found:\n", m[:300])
