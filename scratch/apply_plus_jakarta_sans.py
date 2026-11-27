import os
import re
import subprocess
from PIL import Image

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_html = """  <!-- Google Fonts: Poppins (Headings: 500/600/700) & Inter (Body: 300/400/500/600/700) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link
    href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap"
    rel="stylesheet">"""

replacement_html = """  <!-- Google Fonts: Plus Jakarta Sans (Headings: 400/500/600/700/800) & Inter (Body: 300/400/500/600/700) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link
    href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap"
    rel="stylesheet">"""

assert target_html in html, "target_html not found in index.html"
html = html.replace(target_html, replacement_html, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("SUCCESS: index.html updated with Plus Jakarta Sans!")

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update --font-heading
target_var = """  /* Headings: Poppins 600 / 700 */
  --font-heading: 'Poppins', sans-serif;"""

replacement_var = """  /* Headings: Plus Jakarta Sans 500 / 600 / 700 / 800 */
  --font-heading: 'Plus Jakarta Sans', sans-serif;"""

assert target_var in css, "target_var not found in css/style.css"
css = css.replace(target_var, replacement_var, 1)

# Replace all fallback "Poppins" with 'Plus Jakarta Sans'
css = css.replace('var(--font-heading, "Poppins", sans-serif)', "var(--font-heading, 'Plus Jakarta Sans', sans-serif)")

# Ensure all headings explicitly declare font-family: var(--font-heading) !important;
target_headings_rule = """/* All Large Section Headings - Refined Font Weight 500 */
h2,
.services-section-title,
.industries-section-title,
.why-section-title,
.clients-section-title,
.about-ref-title,
.process-section-title,
.commitment-title,
.contact-panel-title {
  font-weight: 500;
}"""

replacement_headings_rule = """/* All Large Section Headings - Refined Font Weight 500 & Plus Jakarta Sans */
h1,
h2,
h3,
h4,
h5,
h6,
.hero-main-title,
.services-section-title,
.industries-section-title,
.why-section-title,
.clients-section-title,
.about-ref-title,
.process-section-title,
.commitment-title,
.contact-panel-title {
  font-family: var(--font-heading) !important;
  font-weight: 500;
}"""

assert target_headings_rule in css, "target_headings_rule not found in css/style.css"
css = css.replace(target_headings_rule, replacement_headings_rule, 1)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("SUCCESS: css/style.css updated with Plus Jakarta Sans!")

# Verification
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
print("ALL CODE VERIFIED PERFECTLY!")

# Capture screenshot with Chrome Headless
html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html"
abs_out = os.path.abspath(r"scratch\plus_jakarta_preview.png").replace('\\', '/')

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,1200",
    "--virtual-time-budget=2000",
    f"--screenshot={abs_out}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(abs_out):
    print("Screenshot captured successfully at", abs_out)
    img = Image.open(abs_out)
    # Crop the hero title
    crop_title = img.crop((50, 100, 1100, 450))
    crop_title.save(r"scratch\hero_title_pjs.png")
    print("Hero title crop saved to scratch/hero_title_pjs.png")
