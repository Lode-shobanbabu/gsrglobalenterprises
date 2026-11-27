import os
import re
import subprocess
from PIL import Image

# 1. Verify CSS styles
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Check brace balance
open_braces = css.count('{')
close_braces = css.count('}')
print(f"CSS Braces: {open_braces} open, {close_braces} close, diff = {open_braces - close_braces}")

# Check hero-dock-card rules
m = re.search(r'\.hero-dock-card\s*\{([^}]+)\}', css)
if m:
    card_body = m.group(1)
    print("\n.hero-dock-card rules:")
    print(card_body.strip())
    
    # Assert exact user glassmorphism properties
    assert "background: rgba(255, 255, 255, 0.2);" in card_body, "Missing background"
    assert "border-radius: 16px;" in card_body, "Missing border-radius"
    assert "box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);" in card_body, "Missing box-shadow"
    assert "backdrop-filter: blur(5px);" in card_body, "Missing backdrop-filter"
    assert "-webkit-backdrop-filter: blur(5px);" in card_body, "Missing -webkit-backdrop-filter"
    assert "border: 1px solid rgba(255, 255, 255, 0.3);" in card_body, "Missing border"
    print("\nALL GLASSMORPHISM PROPERTIES VERIFIED!")
else:
    print("ERROR: .hero-dock-card not found in css/style.css")

# 2. Verify HTML structure & section order
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check section order
sections = re.findall(r'<section[^>]+id=[\"\']([^\"\']+)[\"\']', html)
print(f"\nHTML Sections ({len(sections)}): {sections}")
expected_order = ['hero', 'sectors', 'about', 'services', 'Industries', 'why-us', 'clients', 'process', 'commitment', 'contact']
assert sections == expected_order, f"Expected {expected_order}, got {sections}"
print("Section order verified perfectly!")

# Check div tag balance
div_open = len(re.findall(r'<div\b', html))
div_close = html.count('</div>')
print(f"HTML <div>: {div_open} open, {div_close} close, diff = {div_open - div_close}")
assert div_open == div_close, f"Unbalanced divs: {div_open} vs {div_close}"

# Check section tag balance
sec_open = len(re.findall(r'<section\b', html))
sec_close = html.count('</section>')
print(f"HTML <section>: {sec_open} open, {sec_close} close, diff = {sec_open - sec_close}")
assert sec_open == sec_close, f"Unbalanced sections: {sec_open} vs {sec_close}"

# 3. Capture screenshot of rendered hero + dock cards
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html"
abs_out = os.path.abspath(r"scratch\glass_preview.png").replace('\\', '/')

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,1200",
    f"--screenshot={abs_out}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(abs_out):
    print(f"\nScreenshot created successfully at {abs_out}")
    img = Image.open(abs_out)
    w, h = img.size
    print(f"Screenshot size: {w}x{h}")
    # Crop around the dock cards area (y: 250 to 600)
    crop_dock = img.crop((80, 200, 1320, 600))
    crop_dock.save(r"scratch\dock_cards_rendered.png")
    print("Saved crop to scratch/dock_cards_rendered.png")
else:
    print(f"Could not create screenshot. Stderr: {res.stderr}")
