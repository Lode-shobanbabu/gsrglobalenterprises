import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = [
    'about',
    'services',
    'Industries',
    'why-us',
    'clients',
    'process',
    'commitment',
    'contact'
]

for s in sections:
    print(f"\n================ SECTION: #{s} ================")
    m = re.search(rf'<section[^>]*id=["\']{s}["\'][^>]*>(.*?)</section>', html, re.DOTALL)
    if not m:
        print("  Not found!")
        continue
    content = m.group(1)
    
    # Find eyebrow
    eb = re.search(r'<(div|span|p)[^>]*class=["\']([^"\']*(?:eyebrow|tag|pill)[^"\']*)["\'][^>]*>(.*?)</\1>', content, re.DOTALL)
    if eb:
        print(f"  Eyebrow tag: <{eb.group(1)} class='{eb.group(2)}'>")
        print(f"  Eyebrow text: {' '.join(eb.group(3).split())[:60]}")
    
    # Find h2
    h2 = re.search(r'<h2[^>]*class=["\']([^"\']*)["\'][^>]*>(.*?)</h2>', content, re.DOTALL)
    if h2:
        print(f"  H2 class: '{h2.group(1)}'")
        print(f"  H2 text: {' '.join(h2.group(2).split())[:60]}")
    
    # Find subtitle / lead p
    # Look for the p right after h2 or inside header
    header_box = re.search(r'<(div)[^>]*class=["\']([^"\']*(?:text-center|mb-5|mb-4|header)[^"\']*)["\'][^>]*>(.*?)</\1>', content, re.DOTALL)
    if header_box:
        print(f"  Header container: class='{header_box.group(2)}'")
        p = re.search(r'<p[^>]*class=["\']([^"\']*)["\'][^>]*>(.*?)</p>', header_box.group(3), re.DOTALL)
        if p:
            print(f"  Subtitle class: '{p.group(1)}'")
            print(f"  Subtitle text: {' '.join(p.group(2).split())[:60]}")
    else:
        # Check first p
        p = re.search(r'<p[^>]*class=["\']([^"\']*)["\'][^>]*>(.*?)</p>', content, re.DOTALL)
        if p:
            print(f"  First p class: '{p.group(1)}'")
            print(f"  First p text: {' '.join(p.group(2).split())[:60]}")
