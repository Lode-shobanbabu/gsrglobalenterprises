import os
import re
import subprocess
from PIL import Image

# Read CSS
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .navbar-corporate .nav-link
target_nav = """.navbar-corporate .nav-link {
  font-family: var(--font-heading);
  font-size: 0.94rem;
  font-weight: 600;
  color: var(--primary-navy);
  padding: 0.4rem 0.2rem;
  position: relative;
  transition: color 0.2s ease;
  letter-spacing: 0.01em;
}"""

replacement_nav = """.navbar-corporate .nav-link {
  font-family: var(--font-heading);
  font-size: 0.90rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--primary-navy);
  padding: 0.4rem 0.2rem;
  position: relative;
  transition: color 0.2s ease;
}"""

assert target_nav in css, "target_nav not found in css/style.css"
css = css.replace(target_nav, replacement_nav, 1)

# 2. Update .offcanvas-body .nav-link for mobile
target_mobile_nav = """.offcanvas-body .nav-link {
    color: var(--primary-navy) !important;
    font-family: var(--font-heading);
    font-size: 0.95rem;
    font-weight: 500;
    padding: 0.85rem 0 !important;
    display: flex !important;
    align-items: center;
    justify-content: space-between;
    transition: all 0.2s ease;
  }"""

replacement_mobile_nav = """.offcanvas-body .nav-link {
    color: var(--primary-navy) !important;
    font-family: var(--font-heading);
    font-size: 0.92rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 0.85rem 0 !important;
    display: flex !important;
    align-items: center;
    justify-content: space-between;
    transition: all 0.2s ease;
  }"""

assert target_mobile_nav in css, "target_mobile_nav not found in css/style.css"
css = css.replace(target_mobile_nav, replacement_mobile_nav, 1)

# 3. Update About Us button .btn-ref-cta to Request a Quote orange color
target_btn = """.btn-ref-cta {
  background-color: var(--primary-navy);
  color: #ffffff;
  padding: 0.72rem 1.85rem;
  border-radius: 50px;
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  box-shadow: 0 4px 16px rgba(6, 43, 85, 0.22);
  transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
  border: 1.5px solid transparent;
}

.btn-ref-cta i {
  font-size: 0.92rem;
  transition: transform 0.25s ease;
}

.btn-ref-cta:hover {
  background-color: var(--accent-orange);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(255, 121, 0, 0.38);
  border-color: var(--accent-orange);
}"""

replacement_btn = """.btn-ref-cta {
  background-color: var(--accent-orange);
  color: #ffffff;
  padding: 0.72rem 1.85rem;
  border-radius: 50px;
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  box-shadow: 0 4px 16px rgba(255, 121, 0, 0.35);
  transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
  border: 1.5px solid transparent;
}

.btn-ref-cta i {
  font-size: 0.92rem;
  transition: transform 0.25s ease;
}

.btn-ref-cta:hover {
  background-color: var(--brand-orange-hover);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(255, 121, 0, 0.48);
  border-color: var(--brand-orange-hover);
}"""

assert target_btn in css, "target_btn not found in css/style.css"
css = css.replace(target_btn, replacement_btn, 1)

# Write updated CSS
with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: css/style.css updated!")

# Verify braces
open_braces = css.count('{')
close_braces = css.count('}')
print(f"CSS Braces: {open_braces} open, {close_braces} close, diff = {open_braces - close_braces}")
assert open_braces == close_braces, "Unbalanced braces in CSS"

# Take screenshot to verify navbar and about button
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html"
abs_out = os.path.abspath(r"scratch\nav_about_preview.png").replace('\\', '/')

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,1600",
    f"--screenshot={abs_out}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(abs_out):
    print("Screenshot captured successfully!")
    img = Image.open(abs_out)
    
    # 1. Navbar crop
    crop_nav = img.crop((50, 0, 1350, 120))
    crop_nav.save(r"scratch\navbar_capitalized.png")
    print("Navbar crop saved to scratch/navbar_capitalized.png")
    
    # 2. About section button crop
    # About section is roughly y=700 to y=1200
    crop_about = img.crop((50, 700, 1350, 1250))
    crop_about.save(r"scratch\about_btn_orange.png")
    print("About button crop saved to scratch/about_btn_orange.png")
else:
    print("Screenshot failed:", res.stderr)
