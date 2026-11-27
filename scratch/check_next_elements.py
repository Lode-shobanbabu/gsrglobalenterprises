with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
secs = ['services', 'Industries', 'why-us', 'clients', 'process']
for s in secs:
    m = re.search(rf'<section[^>]*id=["\']{s}["\'][^>]*>(.*?)</section>', html, re.DOTALL)
    if not m: continue
    content = m.group(1)
    # Find text-center container
    h = re.search(r'(<div[^>]*class=["\']text-center[^>]*>.*?</div>\s*)(<div[^>]*>)', content, re.DOTALL)
    if h:
        print(f"[{s}] Next element after text-center: {h.group(2)[:60]}")
