with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'(/\* =+\s*E\. Our Clients - Institutional Showcase.*?\*/\s*\.clients-section\s*\{.*?\.client-cred-scope i\s*\{[^\}]+\})', text, re.DOTALL)
if match:
    print("Found CSS block match, length:", len(match.group(1)))
    print(match.group(1)[:150])
    print("...")
    print(match.group(1)[-150:])
else:
    print("Not found")
