import os
from PIL import Image

images = [
    (r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\service_pro_medical_1795685716157.jpg",
     r"d:\shoban\GSR GLOBAL ENTERPRISES\assets\images\service-pro-medical.webp"),
    (r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\service_pro_it_1795685725952.jpg",
     r"d:\shoban\GSR GLOBAL ENTERPRISES\assets\images\service-pro-it.webp"),
    (r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\service_pro_education_1795685821541.jpg",
     r"d:\shoban\GSR GLOBAL ENTERPRISES\assets\images\service-pro-education.webp"),
    (r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\service_pro_industrial_1795685747425.jpg",
     r"d:\shoban\GSR GLOBAL ENTERPRISES\assets\images\service-pro-industrial.webp"),
    (r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\service_pro_automotive_1795685766377.jpg",
     r"d:\shoban\GSR GLOBAL ENTERPRISES\assets\images\service-pro-automotive.webp"),
]

for src, dst in images:
    if not os.path.exists(src):
        print("Missing src:", src)
        continue
    img = Image.open(src)
    print(f"Loaded: {src} -> Size: {img.size}, Mode: {img.mode}")
    # Convert RGBA to RGB if needed
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Save as high quality WebP (quality=94, method=6 for crisp sharp rendering)
    img.save(dst, format='WEBP', quality=94, method=6)
    print(f"Saved: {dst} -> Size: {os.path.getsize(dst)} bytes")

# Now update index.html to point to the new high-resolution images
with open(r"d:\shoban\GSR GLOBAL ENTERPRISES\index.html", "r", encoding="utf-8") as f:
    html = f.read()

replacements = [
    ('assets/images/service-medical.webp', 'assets/images/service-pro-medical.webp'),
    ('assets/images/service-it.webp', 'assets/images/service-pro-it.webp'),
    ('assets/images/about-it-classroom.webp', 'assets/images/service-pro-education.webp'),
    ('assets/images/service-steel.webp', 'assets/images/service-pro-industrial.webp'),
    ('assets/images/service-transit.webp', 'assets/images/service-pro-automotive.webp'),
]

for old_val, new_val in replacements:
    # Only replace in the services section to avoid touching about us if it used any of those
    # Actually let's check count before and after
    print(f"Replacing {old_val} -> {new_val}")

# We can specifically replace within the services section:
sec_start = '<!-- ==========================================================================\n         C. OUR SERVICES'
sec_end = '<!-- ==========================================================================\n         E. OUR CLIENTS'

idx1 = html.find(sec_start)
idx2 = html.find(sec_end)

if idx1 != -1 and idx2 != -1:
    services_part = html[idx1:idx2]
    services_part = services_part.replace('assets/images/service-medical.webp', 'assets/images/service-pro-medical.webp')
    services_part = services_part.replace('assets/images/service-it.webp', 'assets/images/service-pro-it.webp')
    services_part = services_part.replace('assets/images/about-it-classroom.webp', 'assets/images/service-pro-education.webp')
    services_part = services_part.replace('assets/images/service-steel.webp', 'assets/images/service-pro-industrial.webp')
    services_part = services_part.replace('assets/images/service-transit.webp', 'assets/images/service-pro-automotive.webp')
    html = html[:idx1] + services_part + html[idx2:]
    with open(r"d:\shoban\GSR GLOBAL ENTERPRISES\index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully updated index.html with new high-res image paths in #services!")
else:
    print("Could not find services section markers!")
