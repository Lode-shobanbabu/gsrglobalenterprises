with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'(/\* =+\s*F\. Our Commitment Section.*?(?=/\* =+\s*G\. Contact))', text, re.DOTALL)
if match:
    print("Found Section F in css/style.css, length:", len(match.group(1)))
    print(match.group(1)[:120])
    print("...")
    print(match.group(1)[-120:])
else:
    print("Not found")
