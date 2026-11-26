import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

srcs = re.findall(r'src=["\']([^"\']+\.(?:webp|jpg|png|svg))["\']', html)
print(f"Total images found in index.html: {len(srcs)}")
for s in srcs:
    print(" -", s, "exists:", os.path.exists(s))
missing = [s for s in srcs if not os.path.exists(s)]
if missing:
    print("Missing files:", missing)
else:
    print("SUCCESS: Every single image referenced in index.html exists on disk!")

# Check specific images
print("about-medical.webp exists:", os.path.exists("assets/images/about-medical.webp"))
print("about-steel.webp exists:", os.path.exists("assets/images/about-steel.webp"))
print("about-solar.webp exists:", os.path.exists("assets/images/about-solar.webp"))
