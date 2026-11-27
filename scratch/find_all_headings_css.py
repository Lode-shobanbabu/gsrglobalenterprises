import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Find all occurrences of font-weight on headings
heading_keywords = [
    'hero-main-title',
    'about-ref-title',
    'services-section-title',
    'industries-section-title',
    'why-section-title',
    'clients-section-title',
    'process-section-title',
    'commitment-title',
    'contact-panel-title',
    'quote-card-title',
    'section-title'
]

pattern = re.compile(r'([^{}]*(' + '|'.join(heading_keywords) + r')[^{}]*)\{([^}]*)\}', re.DOTALL)
matches = pattern.findall(css)

print(f"Found {len(matches)} rules targeting headings:")
for m in matches:
    sel = m[0].strip()
    body = m[2]
    fw = re.findall(r'font-weight\s*:\s*([^;]+);', body)
    print(f"Selector: {sel[:80]}")
    print(f"  font-weight: {fw}")
