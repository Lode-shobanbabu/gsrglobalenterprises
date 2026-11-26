with open('js/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
matches = [l for l in js.split('\n') if any(k in l.lower() for k in ['hero', 'slider', 'slide'])]
print(f"Total matching lines in js: {len(matches)}")
for m in matches[:10]:
    print(" ", m.strip()[:80])
