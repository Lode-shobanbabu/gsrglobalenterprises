import os
from PIL import Image

src = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\about_procurement_facility_1795688793494.jpg"
dst = r"d:\shoban\GSR GLOBAL ENTERPRISES\assets\images\about-procurement-facility.webp"

if os.path.exists(src):
    im = Image.open(src)
    print(f"Loaded: {src} -> Size: {im.size}, Mode: {im.mode}")
    if im.mode != 'RGB':
        im = im.convert('RGB')
    im.save(dst, format='WEBP', quality=94, method=6)
    print(f"Saved: {dst} -> Size: {os.path.getsize(dst)} bytes")

# Update index.html to use this new image
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('assets/images/about-warehouse-logistics.webp', 'assets/images/about-procurement-facility.webp')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with new about-procurement-facility.webp!")
