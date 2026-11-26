with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'\.header-cta-pill[^{]*\{[^}]+\}', css)
print("Matches in css for header-cta-pill:", len(matches))

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches_html = re.findall(r'header-cta-pill', html)
print("Matches in html for header-cta-pill:", len(matches_html))
