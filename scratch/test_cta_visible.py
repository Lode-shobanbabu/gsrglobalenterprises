import os
import subprocess
from PIL import Image

html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html"
abs_out = os.path.abspath(r"scratch\check_cta_visible.png").replace('\\', '/')

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,2800",
    "--virtual-time-budget=2000",
    f"--screenshot={abs_out}",
    html_path
]

subprocess.run(cmd, capture_output=True, text=True)

full = Image.open(abs_out)
w, h = full.size

orange_pts = []
for x in range(200, 1200, 2):
    for y in range(1200, 2400, 2):
        r, g, b, *a = full.getpixel((x, y))
        if r > 240 and 110 <= g <= 135 and b < 20:
            orange_pts.append((x, y))

print("Total orange button pixels found in full screenshot:", len(orange_pts))
if orange_pts:
    min_x = min(p[0] for p in orange_pts)
    max_x = max(p[0] for p in orange_pts)
    min_y = min(p[1] for p in orange_pts)
    max_y = max(p[1] for p in orange_pts)
    print(f"Discuss Button bounds: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}], width={max_x - min_x}px, height={max_y - min_y}px")
    
    tight = full.crop((max(0, min_x - 30), max(0, min_y - 20), min(w, max_x + 30), min(h, max_y + 20)))
    tight.save(r"scratch\discuss_btn_tight.png")
    
    import shutil
    shutil.copyfile(r"scratch\discuss_btn_tight.png", r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\services_discuss_btn_preview.png")
    print("Saved preview to brain directory.")
