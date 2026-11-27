with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(@media[^{]+{[^{}]+(?:{[^{}]+}[^{}]*)*})', text)
for m in matches:
    if '.client' in m:
        print(m[:300])
        print('-'*30)
