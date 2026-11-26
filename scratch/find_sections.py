with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', html)
print("Section IDs found in index.html:", sections)
