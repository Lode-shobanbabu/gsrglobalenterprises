with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'([.#][\w\-]+(?:\s*,\s*[.#][\w\-]+)*)\s*\{([^}]+)\}', css)
print(f"Total CSS rules found: {len(matches)}")

targets = [
    'hero-section', 'about-section', 'services-section', 'clients-section', 
    'why-section', 'contact-section', 'faq-section', 'footer-corporate',
    'btn-gold', 'btn-hero-action', 'header-cta-pill', 'service-card',
    'why-card', 'contact-card', 'about-banner-navy', 'top-utility-bar',
    'navbar-corporate'
]

print("\n--- Key Component Rules ---")
for sel, body in matches:
    for target in targets:
        if target in sel:
            bg_match = re.search(r'background(?:-color)?:\s*([^;]+);', body)
            color_match = re.search(r'(?<!-)color:\s*([^;]+);', body)
            font_match = re.search(r'font-family:\s*([^;]+);', body)
            bg = bg_match.group(1).strip() if bg_match else "-"
            col = color_match.group(1).strip() if color_match else "-"
            print(f"{sel.strip()[:35]:35} | bg: {bg[:35]:35} | col: {col}")
            break
