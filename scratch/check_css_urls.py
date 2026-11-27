import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'url\([\"\']?([^\)\"\']+)[\"\']?\)', text):
    print(m.group(1))
