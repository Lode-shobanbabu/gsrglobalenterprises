with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
keywords = ['btn-gold', 'about-banner', 'why-card', 'contact-submit', 'faq-button', 'stat-card']

for kw in keywords:
    matches = re.findall(rf'([.#\w\-,\s]+)\{{([^}}]*{kw}[^}}]*)\}}', css)
    if not matches:
        # try selector match
        matches = re.findall(rf'([.#\w\-,\s]*{kw}[.#\w\-,\s]*)\{{([^}}]+)\}}', css)
    print(f"\n=== Matches for {kw} ===")
    for sel, body in matches[:5]:
        print(f"Selector: {sel.strip()[:50]}")
        for line in body.strip().split('\n')[:8]:
            print(f"  {line.strip()}")
