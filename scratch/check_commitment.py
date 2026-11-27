import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'(<section[^>]*id=["\']commitment["\'].*?</section>)', text, re.DOTALL)
if match:
    print("Found commitment section:")
    print(match.group(1)[:1500])
    print("...")
    print(match.group(1)[-500:])
else:
    print("Not found")
