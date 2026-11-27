with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.(?:mockup|smartphone|journey|screen)[^{]+{[^}]+})', text)
print(f"Found {len(matches)} mockup/smartphone rules:")
for m in matches[:10]:
    print(m)
    print('-'*20)
