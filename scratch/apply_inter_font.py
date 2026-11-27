import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_html = """  <!-- Google Fonts: Poppins (Headings: 600/700) & Roboto (Body: 300/400/500/700) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link
    href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Roboto:wght@300;400;500;700&display=swap"
    rel="stylesheet">"""

replacement_html = """  <!-- Google Fonts: Poppins (Headings: 500/600/700) & Inter (Body: 300/400/500/600/700) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link
    href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap"
    rel="stylesheet">"""

assert target_html in html, "target_html not found in index.html"
html = html.replace(target_html, replacement_html, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("SUCCESS: index.html updated with Google Fonts Inter link.")

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update font-body variable
target_var = """  /* Body: Roboto 300 / 400 / 500 / 700 */
  --font-body: 'Roboto', sans-serif;"""

replacement_var = """  /* Body: Inter 300 / 400 / 500 / 600 / 700 */
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;"""

assert target_var in css, "target_var not found in css/style.css"
css = css.replace(target_var, replacement_var, 1)

# Replace all var(--font-body, "Roboto", sans-serif) with var(--font-body, 'Inter', sans-serif)
css = css.replace('var(--font-body, "Roboto", sans-serif)', "var(--font-body, 'Inter', sans-serif)")

# Update the bottom site-wide body content standard to enforce font-family: var(--font-body) !important;
target_bottom = """.contact-panel-desc {
  font-size: 0.98rem !important;
  font-weight: 400 !important;
  line-height: 1.62 !important;
}"""

replacement_bottom = """.contact-panel-desc {
  font-family: var(--font-body) !important;
  font-size: 0.98rem !important;
  font-weight: 400 !important;
  line-height: 1.62 !important;
}"""

assert target_bottom in css, "target_bottom not found in css/style.css"
css = css.replace(target_bottom, replacement_bottom, 1)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("SUCCESS: css/style.css updated with Inter body font.")

# 3. Verification
open_b = css.count('{')
close_b = css.count('}')
print(f"CSS Braces: {open_b} open, {close_b} close (diff = {open_b - close_b})")
assert open_b == close_b

div_o = len(re.findall(r'<div\b', html))
div_c = html.count('</div>')
sec_o = len(re.findall(r'<section\b', html))
sec_c = html.count('</section>')
print(f"HTML <div>: {div_o} vs {div_c}")
print(f"HTML <section>: {sec_o} vs {sec_c}")
assert div_o == div_c
assert sec_o == sec_c

sections = re.findall(r'<section[^>]+id=[\"\']([^\"\']+)[\"\']', html)
expected = ['hero', 'sectors', 'about', 'services', 'Industries', 'why-us', 'clients', 'process', 'commitment', 'contact']
print(f"HTML Sections: {sections}")
assert sections == expected
print("ALL CHECKS PASSED PERFECTLY!")
