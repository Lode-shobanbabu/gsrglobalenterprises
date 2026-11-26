# scratch/remove_faq_code.py

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Marker for FAQ section start
faq_start = '/* ==========================================================================\n   FAQ Section'
# Marker for FAQ section end / Next section
faq_end = '/* ==========================================================================\n   G. Contact Us Section'

f_idx1 = css.find(faq_start)
f_idx2 = css.find(faq_end)

if f_idx1 == -1 or f_idx2 == -1:
    print(f"Error finding FAQ section in CSS: f_idx1={f_idx1}, f_idx2={f_idx2}")
    exit(1)

# Remove the FAQ section block
css = css[:f_idx1] + css[f_idx2:]

# Remove .faq-section from media queries
css = css.replace('  .faq-section,\n', '')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Removed FAQ CSS from css/style.css")

# 2. Update index.html to remove broken footer link
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

faq_link = '            <li><a href="#faq"><i class="bi bi-chevron-right"></i> FAQs</a></li>\n'
if faq_link in html:
    html = html.replace(faq_link, '')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Removed FAQs link from index.html footer")
else:
    print("FAQs link not found in index.html (or already removed)")

# 3. Check for any JS references
with open('js/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

if 'faq' in js.lower():
    print("Found 'faq' in script.js!")
else:
    print("No FAQ references in js/script.js.")
