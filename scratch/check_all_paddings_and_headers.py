import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's list all sections
section_ids = [
    'hero',
    'sectors',
    'about',
    'services',
    'Industries',
    'why-us',
    'clients',
    'process',
    'commitment',
    'contact'
]

print("=== CHECKING SECTION PADDINGS IN CSS ===")
for sid in section_ids:
    # Find CSS rules for .sid-section or #sid
    matches = re.findall(rf'([^{{}}]*\b(?:#{sid}|{sid}-section|{sid}-six-section|{sid}-ref-section)\b[^{{}}]*)\{{([^}}]+)\}}', css)
    for sel, rules in matches:
        if 'padding' in rules:
            p_lines = [r.strip() for r in rules.split(';') if 'padding' in r]
            print(f"[{sid}] {sel.strip()} -> {'; '.join(p_lines)}")

print("\n=== CHECKING SECTION HEADER CLASSES IN HTML ===")
for sid in section_ids:
    m = re.search(rf'<section[^>]*id=["\']{sid}["\'][^>]*>(.*?)</section>', html, re.DOTALL)
    if not m:
        continue
    content = m.group(1)
    
    # Check headers
    headers = re.findall(r'<(div|header)[^>]*class=["\']([^"\']*(?:text-center|section-header|header)[^"\']*)["\']', content)
    print(f"[{sid}] Header containers: {headers}")
    
    # Check first row or content container margin-top
    rows = re.findall(r'<(div)[^>]*class=["\']([^"\']*(?:row|container|grid)[^"\']*)["\']', content)
    first_rows = [r for r in rows if 'mt-' in r[1] or 'pt-' in r[1] or 'my-' in r[1]]
    if first_rows:
        print(f"[{sid}] Content top-margin elements: {first_rows[:2]}")
