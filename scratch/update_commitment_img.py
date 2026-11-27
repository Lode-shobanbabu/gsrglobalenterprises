with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Update image in commitment section to hero-procurement
html_new = html.replace(
    'assets/images/about-procurement-facility.webp',
    'assets/images/hero-procurement.webp'
)

if html_new != html:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_new)
    print("Updated index.html to hero-procurement.webp successfully.")
else:
    print("No change made or already using hero-procurement.webp")
