with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'id=["\']contact[^"\']*["\']', html)
print("Matches for id=contact:", matches)

# Check line numbers for id="contact"
for i, l in enumerate(html.split('\n')):
    if 'id="contact' in l or 'id=\'contact' in l:
        print(f"L{i+1}: {l.strip()[:100]}")
