import os
from PIL import Image

src = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\about_corporate_team_discussion_1795689013165.jpg"
dst = r"d:\shoban\GSR GLOBAL ENTERPRISES\assets\images\about-corporate-team.webp"

if os.path.exists(src):
    im = Image.open(src)
    print(f"Loaded: {src} -> Size: {im.size}, Mode: {im.mode}")
    if im.mode != 'RGB':
        im = im.convert('RGB')
    im.save(dst, format='WEBP', quality=94, method=6)
    print(f"Saved: {dst} -> Size: {os.path.getsize(dst)} bytes")
else:
    print("Source image not found:", src)

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any previous image in about section
s_idx = html.find('id="about"')
c_idx = html.find('id="services"')
about_part = html[s_idx:c_idx]

import re
old_img_match = re.search(r'<img\s+src="([^"]+)"\s+alt="[^"]*Multi-Sector[^"]*"', about_part)
if old_img_match:
    old_src = old_img_match.group(1)
    print(f"Replacing {old_src} with assets/images/about-corporate-team.webp")
    about_part = about_part.replace(old_src, 'assets/images/about-corporate-team.webp')
    html = html[:s_idx] + about_part + html[c_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully updated index.html with new team image!")
else:
    # Direct replacement
    html = html.replace('assets/images/about-procurement-facility.webp', 'assets/images/about-corporate-team.webp')
    html = html.replace('assets/images/about-warehouse-logistics.webp', 'assets/images/about-corporate-team.webp')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Directly replaced image in index.html!")
