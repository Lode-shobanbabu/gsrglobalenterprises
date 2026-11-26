with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

targets = [
    'btn-ref-action', 'btn-enroll-now', 'about-ref-banner', 'client-cred-card',
    'why-callout-card', 'why-character-box', 'contact-form-panel',
    'service-card', 'faq-card', 'footer-corporate'
]

for t in targets:
    regex = rf'(\.[^{{]*{t}[^{{]*)\{{([^}}]+)\}}'
    for match in re.finditer(regex, css):
        sel = match.group(1).strip()
        body = match.group(2).strip()
        print(f"=== {sel} ===")
        for line in body.split('\n'):
            line = line.strip()
            if any(k in line for k in ['background', 'color', 'border', 'font', 'box-shadow']):
                print(f"   {line}")
