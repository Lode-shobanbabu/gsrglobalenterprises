import os
import re
import subprocess
from PIL import Image

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_cta = """        <!-- Centered Bottom CTA Section (Below All 6 Cards) -->
        <div class="services-bottom-cta text-center mt-5 fade-up-element">
          <p class="services-cta-heading mb-3">Have a Specific Requirement? Let's Discuss.</p>
          <a href="#contact" class="btn header-cta-orange services-center-cta" aria-label="Request a Procurement Quote">
            <span>Request a Quote</span>
            <i class="bi bi-arrow-right"></i>
          </a>
        </div>"""

replacement_cta = """        <!-- Centered Bottom CTA Section (Single Discuss Pill Button) -->
        <div class="services-bottom-cta text-center mt-5 fade-up-element">
          <a href="#contact" class="btn services-discuss-btn" aria-label="Have a Specific Requirement? Let's Discuss">
            <span>Have a Specific Requirement? Let's Discuss.</span>
            <i class="bi bi-arrow-right"></i>
          </a>
        </div>"""

assert target_cta in html, "target_cta not found in index.html"
html = html.replace(target_cta, replacement_cta, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("SUCCESS: index.html updated with single Discuss pill button!")

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

target_css = """/* Centered Bottom CTA Section Below All Cards */
.services-bottom-cta {
  padding-top: 1.5rem;
}

.services-cta-heading {
  font-family: var(--font-heading);
  font-size: clamp(1.2rem, 1.8vw, 1.5rem);
  font-weight: 600;
  color: var(--primary-navy);
  margin-bottom: 1rem;
}

.services-center-cta {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 0.72rem 2rem;
  font-size: 0.95rem;
}"""

replacement_css = """/* Centered Bottom CTA Section Below All Cards (Single Pill Button Without Underline) */
.services-bottom-cta {
  padding-top: 1.8rem;
}

.services-discuss-btn {
  background-color: var(--accent-orange);
  color: #ffffff !important;
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 0.94rem;
  padding: 0.75rem 2.2rem;
  border-radius: 50px;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  text-decoration: none !important;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 16px rgba(255, 121, 0, 0.35);
  border: none;
}

.services-discuss-btn:hover,
.services-discuss-btn:focus,
.services-discuss-btn:active {
  background-color: var(--brand-orange-hover);
  color: #ffffff !important;
  text-decoration: none !important;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 121, 0, 0.45);
}

.services-discuss-btn span {
  text-decoration: none !important;
}

.services-discuss-btn i {
  font-size: 0.95rem;
  transition: transform 0.2s ease;
  text-decoration: none !important;
}

.services-discuss-btn:hover i {
  transform: translateX(4px);
}"""

assert target_css in css, "target_css not found in css/style.css"
css = css.replace(target_css, replacement_css, 1)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("SUCCESS: css/style.css updated with .services-discuss-btn!")

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

# 4. Take Screenshot with Chrome Headless
html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html#services"
abs_out = os.path.abspath(r"scratch\discuss_btn_preview.png").replace('\\', '/')

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,2000",
    "--virtual-time-budget=2000",
    f"--screenshot={abs_out}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(abs_out):
    print("Screenshot captured at", abs_out)
    img_shot = Image.open(abs_out)
    w, h = img_shot.size
    # Crop the bottom CTA area
    crop_btn = img_shot.crop((200, 1000, 1200, 1600))
    crop_btn.save(r"scratch\discuss_button_crop.png")
    print("Crop saved to scratch/discuss_button_crop.png")
