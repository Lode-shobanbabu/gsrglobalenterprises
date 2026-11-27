import os
import subprocess
from PIL import Image

test_html = """<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500&display=swap">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <link rel="stylesheet" href="../css/style.css">
  <style>
    body { background: #f8fafc; padding: 40px; display: flex; justify-content: center; }
  </style>
</head>
<body>
  <div class="services-bottom-cta text-center">
    <a href="#contact" class="btn services-discuss-btn" aria-label="Have a Specific Requirement? Let's Discuss">
      <span>Have a Specific Requirement? Let's Discuss.</span>
      <i class="bi bi-arrow-right"></i>
    </a>
  </div>
</body>
</html>"""

with open('scratch/test_discuss_btn.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/scratch/test_discuss_btn.html"
abs_out = os.path.abspath(r"scratch\test_discuss_btn_shot.png").replace('\\', '/')

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=800,300",
    f"--screenshot={abs_out}",
    html_path
]

subprocess.run(cmd, capture_output=True, text=True)

img = Image.open(abs_out)
w, h = img.size

orange_px = 0
for x in range(w):
    for y in range(h):
        r, g, b, *a = img.getpixel((x, y))
        if r > 240 and 110 <= g <= 135 and b < 20:
            orange_px += 1

print(f"Orange pixels found with correct CSS path: {orange_px}")
assert orange_px > 5000, "Expected orange pill background"

# Find bounds of the button
orange_pts = [(x, y) for x in range(w) for y in range(h) if img.getpixel((x, y))[0] > 240 and 110 <= img.getpixel((x, y))[1] <= 135 and img.getpixel((x, y))[2] < 20]
min_x = min(p[0] for p in orange_pts)
max_x = max(p[0] for p in orange_pts)
min_y = min(p[1] for p in orange_pts)
max_y = max(p[1] for p in orange_pts)
print(f"Button rendered at: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}] ({max_x-min_x}x{max_y-min_y}px)")

crop = img.crop((min_x - 10, min_y - 10, max_x + 10, max_y + 10))
crop.save(r"scratch\discuss_btn_rendered.png")

import shutil
shutil.copyfile(r"scratch\discuss_btn_rendered.png", r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\services_discuss_btn_preview.png")
print("Saved perfect button preview to brain!")
