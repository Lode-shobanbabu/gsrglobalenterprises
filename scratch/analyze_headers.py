import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all sections and their header / content margins
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\'][^>]*>(.*?)</section>', html, re.DOTALL)
print(f"Total sections found: {len(sections)}")

for sec_id, sec_content in sections:
    print(f"\n================ Section: #{sec_id} ================")
    # Look for header div
    header_match = re.search(r'<(div|header)[^>]*class=["\']([^"\']*(?:section-header|header|title)[^"\']*)["\'][^>]*>(.*?)</\1>', sec_content, re.DOTALL)
    if header_match:
        tag, classes, inner = header_match.groups()
        print(f"  Header classes: {classes}")
        # Look for mb-* classes on header or within header
        mb_classes = re.findall(r'class=["\'][^"\']*\b(mb-[0-9]|my-[0-9]|pb-[0-9])\b[^"\']*["\']', inner)
        print(f"  Internal margin classes: {mb_classes}")
        # Find the tag itself's margin
        header_mb = re.findall(r'\b(mb-[0-9]|my-[0-9]|pb-[0-9])\b', classes)
        print(f"  Header container margin: {header_mb}")
        # Look for title and subtitle
        h2 = re.search(r'<h2[^>]*class=["\']([^"\']*)["\'][^>]*>(.*?)</h2>', inner, re.DOTALL)
        if h2:
            print(f"  h2 classes: {h2.group(1)} | text: {' '.join(h2.group(2).split())[:40]}")
        p = re.search(r'<p[^>]*class=["\']([^"\']*)["\'][^>]*>(.*?)</p>', inner, re.DOTALL)
        if p:
            print(f"  p classes: {p.group(1)} | text: {' '.join(p.group(2).split())[:40]}")
    else:
        # Check if there is an h2 directly
        h2 = re.search(r'<h2[^>]*class=["\']([^"\']*)["\'][^>]*>(.*?)</h2>', sec_content, re.DOTALL)
        if h2:
            print(f"  Direct h2 classes: {h2.group(1)} | text: {' '.join(h2.group(2).split())[:40]}")
        else:
            print("  No header found")
