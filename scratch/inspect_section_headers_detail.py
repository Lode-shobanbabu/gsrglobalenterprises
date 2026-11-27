import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\'][^>]*>(.*?)</section>', html, re.DOTALL)

for sec_id, sec_content in sections:
    print(f"\n================ Section: #{sec_id} ================")
    # Print the first 600 characters of section
    lines = sec_content.strip().splitlines()
    print('\n'.join(lines[:25]))
