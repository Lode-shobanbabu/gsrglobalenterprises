# scratch/remove_service_image_badges.py
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find all badges and icon inside service-pro-media
pattern = r'(<div class="service-pro-media">\s*<img[^>]+loading="lazy">)\s*<span class="service-pro-num-badge">[^<]+</span>\s*<span class="service-pro-cat-pill">[^<]+</span>\s*<div class="service-pro-icon-circle">\s*<i[^>]+></i>\s*</div>'

matches = re.findall(pattern, html)
print(f"Found {len(matches)} service-pro-media overlays matching pattern!")

# Replace with just the media opening and img tag
new_html = re.sub(pattern, r'\1', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated index.html successfully!")
