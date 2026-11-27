with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '<div class="services-bottom-cta text-center mt-5 fade-up-element">'
replacement = '<div class="services-bottom-cta text-center mt-5">'

assert target in html, "target not found in index.html"
html = html.replace(target, replacement, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html: removed fade-up-element from services-bottom-cta so it's always visible!")
