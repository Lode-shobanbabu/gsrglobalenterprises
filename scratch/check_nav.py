import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

nav = re.search(r'<nav.*?</nav>', text, re.DOTALL)
if nav:
    links = re.findall(r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', nav.group(0), re.DOTALL)
    for href, label in links:
        clean_label = re.sub(r'<[^>]+>', '', label).strip()
        print(f"{href} -> {clean_label}")
