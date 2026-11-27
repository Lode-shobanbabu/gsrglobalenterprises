import os
import re
import subprocess
from PIL import Image

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

target = """.service-pro-checklist li i {
  color: #ff7900;
  font-size: 0.82rem;
  font-weight: 900;
  -webkit-text-stroke: 0.7px #000000;
  flex-shrink: 0;
  margin-top: 2px;
  transition: transform 0.22s ease, color 0.22s ease;
}

.service-pro-card:hover .service-pro-checklist li i {
  transform: translateX(3px);
  color: #000000;
}"""

replacement = """.service-pro-checklist li i {
  color: #FF7900;
  font-size: 0.85rem;
  font-weight: 700;
  flex-shrink: 0;
  margin-top: 2px;
  transition: transform 0.22s ease, color 0.22s ease;
}

.service-pro-card:hover .service-pro-checklist li i {
  transform: translateX(3px);
  color: #FF7900;
}"""

assert target in css, "target rule not found in css/style.css"
css = css.replace(target, replacement, 1)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: css/style.css updated!")

# Verify braces
open_b = css.count('{')
close_b = css.count('}')
print(f"CSS Braces: {open_b} open, {close_b} close (diff = {open_b - close_b})")
assert open_b == close_b

# Verify HTML tags
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
div_o = len(re.findall(r'<div\b', html))
div_c = html.count('</div>')
assert div_o == div_c
print("HTML tags verified!")

# Take screenshot of #services to check rendered right angle chevrons
html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html#services"
abs_out = os.path.abspath(r"scratch\services_rendered.png").replace('\\', '/')

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
    img = Image.open(abs_out)
    print("Screenshot captured of services, size:", img.size)
    # Check pixels of the right angles in the services checklist
    w, h = img.size
    orange_px = []
    for x in range(w):
        for y in range(h):
            r, g, b, *a = img.getpixel((x, y))
            # Match #FF7900 (r ~ 255, g ~ 121, b ~ 0)
            if r > 240 and 110 <= g <= 135 and b < 20:
                orange_px.append((x, y))
    print(f"Found {len(orange_px)} pure #FF7900 pixels!")
    if orange_px:
        min_x = min(p[0] for p in orange_px)
        max_x = max(p[0] for p in orange_px)
        min_y = min(p[1] for p in orange_px)
        max_y = max(p[1] for p in orange_px)
        print(f"Angle bounds: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]")
        crop = img.crop((max(0, min_x - 10), max(0, min_y - 10), min(w, min_x + 350), min(h, min_y + 150)))
        crop.save(r"scratch\chevrons_crop.png")
        print("Saved crop to scratch/chevrons_crop.png")
