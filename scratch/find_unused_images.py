import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

used = set(re.findall(r'assets/images/([a-zA-Z0-9_\-\.\@]+)', text))

print("Unused images in assets/images:")
for f in sorted(os.listdir('assets/images')):
    if f.endswith(('.jpg', '.webp', '.png')) and f not in used and not f.startswith(('favicon', 'gsr-logo', 'client')):
        print(f"  {f}")
