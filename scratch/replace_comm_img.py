with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Update image in commitment section to hero-procurement
html_new = html.replace(
    '<source srcset="assets/images/hero-logistics-global.webp" type="image/webp">\n          <img src="assets/images/hero-logistics-global.jpg" alt="Global Procurement Logistics" loading="lazy">',
    '<source srcset="assets/images/hero-procurement.webp" type="image/webp">\n          <img src="assets/images/hero-procurement.jpg" alt="Global Procurement Operations &amp; Supply Facility" loading="lazy">'
)

if html_new != html:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_new)
    print("Updated index.html to hero-procurement successfully.")
else:
    print("Error: Could not replace image in index.html")
