# scratch/remove_testimonials_code.py

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

test_start = '/* ==========================================================================\n   G. Testimonials Section'
test_end = '/* ==========================================================================\n   G. Contact Us Section'

t_idx1 = css.find(test_start)
t_idx2 = css.find(test_end)

if t_idx1 == -1 or t_idx2 == -1:
    print(f"Error finding Testimonials section in CSS: t_idx1={t_idx1}, t_idx2={t_idx2}")
    exit(1)

css = css[:t_idx1] + css[t_idx2:]

# Remove .testimonials-section from media query selectors
css = css.replace('  .testimonials-section,\n', '')
css = css.replace('  .testimonials-section\n', '')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Removed Testimonials CSS from css/style.css")

# 2. Update js/script.js
with open('js/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js_start = '  // 10. 3D Cover-Flow Testimonials Carousel Engine'
js_end = '});'

j_idx1 = js.find(js_start)
j_idx2 = js.rfind(js_end)

if j_idx1 == -1 or j_idx2 == -1:
    print(f"Error finding Testimonials in JS: j_idx1={j_idx1}, j_idx2={j_idx2}")
    exit(1)

js = js[:j_idx1] + '});\n'

with open('js/script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Removed Testimonials engine from js/script.js")

# 3. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

test_link = '            <li><a href="#testimonials"><i class="bi bi-chevron-right"></i> Testimonials</a></li>\n'
if test_link in html:
    html = html.replace(test_link, '')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Removed Testimonials footer link from index.html")
else:
    print("Testimonials link not found in index.html (or already removed)")
