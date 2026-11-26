with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.[^{]*logo[^{]*)\{([^}]+)\}', css)
for sel, body in matches:
    print(f"=== {sel.strip()} ===")
    for line in body.split('\n'):
        if any(k in line for k in ['height', 'width', 'max', 'filter', 'object-fit']):
            print(f"  {line.strip()}")
