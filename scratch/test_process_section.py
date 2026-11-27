import os
import subprocess
from PIL import Image

os.makedirs('scratch', exist_ok=True)
html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html"
abs_out = os.path.abspath(r"scratch/process_full.png").replace('\\', '/')

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1440,7000",
    "--virtual-time-budget=3000",
    f"--screenshot={abs_out}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome return code:", res.returncode)

if os.path.exists(abs_out):
    im = Image.open(abs_out)
    w, h = im.size
    print(f"Captured full screenshot: {w}x{h}")
    
    # Locate Section 8: search for blue checkmark badge pixels or specific colors in process section
    # Blue badge color is #2563eb: r=37, g=99, b=235
    blue_pts = []
    for x in range(100, 1340, 2):
        for y in range(3000, 6000, 2):
            r, g, b, *a = im.getpixel((x, y))
            if 30 <= r <= 45 and 90 <= g <= 110 and 220 <= b <= 245:
                blue_pts.append((x, y))
                
    print("Found blue checkmark badge pixels:", len(blue_pts))
    if blue_pts:
        min_x = min(p[0] for p in blue_pts)
        max_x = max(p[0] for p in blue_pts)
        min_y = min(p[1] for p in blue_pts)
        max_y = max(p[1] for p in blue_pts)
        print(f"Blue badges bounds: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]")
        
        # Crop the entire process section (header + image + steps)
        # Header starts about 220px above first badge, ends about 100px below last badge
        crop_top = max(0, min_y - 250)
        crop_bottom = min(h, max_y + 160)
        process_crop = im.crop((80, crop_top, 1360, crop_bottom))
        
        save_target = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\process_section_preview.png"
        process_crop.save(save_target)
        print(f"Saved process crop ({process_crop.size[0]}x{process_crop.size[1]}) to {save_target}")
else:
    print("Screenshot file not found.")
