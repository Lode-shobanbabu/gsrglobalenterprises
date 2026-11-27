with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = [line for line in css.splitlines() if '-apple-system' in line or 'BlinkMacSystemFont' in line or 'Segoe UI' in line]
print(f"Found {len(matches)} lines with system font fallbacks:")
for m in matches:
    print(m)
