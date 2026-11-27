import os
import re
import subprocess
from PIL import Image

# 1. Verify image files exist
src_webp = r'C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795772008054_d64f5bd1.webp'
img = Image.open(src_webp)
print("Source image loaded, size:", img.size)

img.save('assets/images/about-corporate-team-meeting.webp', 'WEBP', quality=92)
if img.mode != 'RGB':
    img = img.convert('RGB')
img.save('assets/images/about-corporate-team-meeting.jpg', 'JPEG', quality=92)
print("Images saved to assets/images/about-corporate-team-meeting.webp and .jpg")

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace <div class="row g-4 g-lg-5 align-items-center"> with align-items-stretch
target_row = '<div class="row g-4 g-lg-5 align-items-center">'
# Find the one in #about
about_pos = html.find('id="about"')
assert about_pos != -1
row_pos = html.find(target_row, about_pos)
assert row_pos != -1, "row in #about not found"

html = html[:row_pos] + '<div class="row g-4 g-lg-5 align-items-stretch">' + html[row_pos + len(target_row):]

# Add d-flex flex-column h-100 to columns in #about
old_left_col = """          <!-- Left Column: High-Resolution Geometric Cutout Image with Customizable Experience Badge -->
          <div class="col-lg-6 fade-up-element">
            <div class="about-ref-media-box">
              <div class="about-ref-img-frame">
                <picture class="about-ref-picture">
                  <source srcset="assets/images/about-corporate-team-meeting.webp" type="image/webp">
                  <img src="assets/images/about-corporate-team-meeting.jpg"
                    alt="GSR Global Enterprises Corporate Team Consultation and Procurement Strategy"
                    class="about-ref-img" width="1200" height="896" loading="lazy">
                </picture>
              </div>
            </div>
          </div>

          <!-- Right Column: Exact Reference Content Layout -->
          <div class="col-lg-6 fade-up-element">
            <div class="about-ref-content">"""

new_left_col = """          <!-- Left Column: High-Resolution Corporate Team Meeting Image (Equal Height) -->
          <div class="col-lg-6 d-flex flex-column fade-up-element">
            <div class="about-ref-media-box h-100">
              <div class="about-ref-img-frame h-100">
                <picture class="about-ref-picture h-100">
                  <source srcset="assets/images/about-corporate-team-meeting.webp" type="image/webp">
                  <img src="assets/images/about-corporate-team-meeting.jpg"
                    alt="GSR Global Enterprises Corporate Team Consultation and Procurement Strategy"
                    class="about-ref-img" width="1024" height="1024" loading="lazy">
                </picture>
              </div>
            </div>
          </div>

          <!-- Right Column: Exact Reference Content Layout (Equal Height) -->
          <div class="col-lg-6 d-flex flex-column justify-content-center fade-up-element">
            <div class="about-ref-content h-100 d-flex flex-column justify-content-center">"""

assert old_left_col in html, "old_left_col not found in index.html"
html = html.replace(old_left_col, new_left_col, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("SUCCESS: index.html updated for equal-height About section!")

# 3. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Locate the about styles in css/style.css
target_css = """/* Left Column: Geometric Cutout Frame & Customizable Floating Badge */
.about-ref-media-box {
  position: relative;
  display: block;
  width: 100%;
  max-width: 530px;
  margin: 0 auto;
}

/* Shadow Wrapper for Polygon Clip-Path */
.about-ref-img-frame-wrap {
  filter: drop-shadow(0 16px 36px rgba(6, 43, 85, 0.12));
  transition: filter 0.4s ease;
}

.about-ref-media-box:hover .about-ref-img-frame-wrap {
  filter: drop-shadow(0 22px 46px rgba(6, 43, 85, 0.18));
}

/* Geometric Cutout Frame (Exact Reference Polygon) */
.about-ref-img-frame {
  position: relative;
  width: 100%;
  aspect-ratio: 4 / 3;
  overflow: hidden;
  clip-path: polygon(0% 28px,
      28px 0%,
      50% 0%,
      58% 13%,
      66% 0%,
      calc(100% - 24px) 0%,
      100% 24px,
      100% 100%,
      75px 100%,
      0% calc(100% - 75px));
  background-color: var(--primary-navy);
}

.about-ref-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 25%;
  display: block;
  transition: transform 0.65s cubic-bezier(0.16, 1, 0.3, 1);
}

.about-ref-media-box:hover .about-ref-img {
  transform: scale(1.04);
}"""

replacement_css = """/* Left Column: Equal Height Media Box & Clean Modern Frame */
.about-ref-media-box {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  min-height: 480px;
  margin: 0 auto;
}

.about-ref-img-frame {
  position: relative;
  width: 100%;
  height: 100%;
  flex: 1;
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 16px 44px rgba(6, 43, 85, 0.10);
  border: 1px solid rgba(6, 43, 85, 0.08);
  background-color: var(--primary-navy);
}

.about-ref-picture {
  display: block;
  width: 100%;
  height: 100%;
}

.about-ref-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 20%;
  display: block;
  transition: transform 0.65s cubic-bezier(0.16, 1, 0.3, 1);
}

.about-ref-media-box:hover .about-ref-img {
  transform: scale(1.03);
}"""

assert target_css in css, "target_css not found in css/style.css"
css = css.replace(target_css, replacement_css, 1)

# Also update responsive rules for about-ref-media-box
old_resp = """@media (max-width: 991.98px) {
  .about-section {
    padding: 2.8rem 0;
  }

  .about-ref-content {
    padding-left: 0;
    margin-top: 1.25rem;
  }

  .about-ref-media-box {
    max-width: 480px;
  }"""

new_resp = """@media (max-width: 991.98px) {
  .about-section {
    padding: 2.8rem 0;
  }

  .about-ref-content {
    padding-left: 0;
    margin-top: 1.25rem;
  }

  .about-ref-media-box {
    max-width: 100%;
    min-height: 380px;
    height: 380px;
  }"""

if old_resp in css:
    css = css.replace(old_resp, new_resp, 1)
    print("Updated responsive about rules!")

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: css/style.css updated for equal height!")

# Verify CSS braces
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

# Take screenshot of the new About section
html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html#about"
abs_out = os.path.abspath(r"scratch\about_equal_height_preview.png").replace('\\', '/')

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
    print("Screenshot captured at", abs_out)
    img_shot = Image.open(abs_out)
    # Crop the about section (y: roughly 150 to 900)
    crop = img_shot.crop((50, 80, 1350, 850))
    crop.save(r"scratch\about_equal_crop.png")
    print("Crop saved to scratch/about_equal_crop.png")
