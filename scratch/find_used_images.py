import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

imgs_used = re.findall(r'assets/images/[a-zA-Z0-9_\-\.\@]+', text)
print("Images used in index.html:")
for img in sorted(set(imgs_used)):
    print(f"  {img}")
