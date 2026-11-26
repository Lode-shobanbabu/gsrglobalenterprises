# remove_why_us_css.py

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Marker start
start_marker = '/* ==========================================================================\n   F. Why Partner With GSR GLOBAL ENTERPRISES - Circular Infographic Showcase\n   ========================================================================== */'
# Marker end (right before FAQ Section)
end_marker = '/* ==========================================================================\n   FAQ Section: Modern Numbered Accordion'

idx1 = css.find(start_marker)
idx2 = css.find(end_marker)

if idx1 != -1 and idx2 != -1:
    css = css[:idx1] + css[idx2:]
    print("Removed entire Why Partner / Why Choose Us CSS block (338 lines)!")
else:
    print(f"Markers not found as exact strings: idx1={idx1}, idx2={idx2}")

# Remove references in responsive media queries at the bottom
css = css.replace('  .why-us-section,\n', '')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update index.html footer link
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace footer quick link pointing to #why-us
old_link = '<li><a href="#why-us"><i class="bi bi-chevron-right"></i> Why Us</a></li>'
new_link = '<li><a href="#sectors"><i class="bi bi-chevron-right"></i> Core Sectors</a></li>'

if old_link in html:
    html = html.replace(old_link, new_link)
    print("Updated footer quick link from #why-us to #sectors!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("All cleanup done!")
