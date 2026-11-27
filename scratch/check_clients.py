import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'(<section[^>]*id=["\']clients["\'].*?</section>)', text, re.DOTALL)
if match:
    print(match.group(1))
else:
    print("Not found")
