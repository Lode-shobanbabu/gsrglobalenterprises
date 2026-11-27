import os
import subprocess
from PIL import Image

# Let's create a small test script that scrolls to #about before taking screenshot
html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html#about"
abs_out = os.path.abspath(r"scratch\about_rendered.png").replace('\\', '/')

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
    print("Screenshot captured! Size:", img.size)
    # Search for orange button in the screenshot
    w, h = img.size
    orange_px = []
    for x in range(w):
        for y in range(h):
            r, g, b, *a = img.getpixel((x, y))
            if r > 240 and 100 <= g <= 140 and b < 30:
                orange_px.append((x, y))
    print(f"Orange pixels found in scrolled view: {len(orange_px)}")
    if orange_px:
        min_x = min(p[0] for p in orange_px)
        max_x = max(p[0] for p in orange_px)
        min_y = min(p[1] for p in orange_px)
        max_y = max(p[1] for p in orange_px)
        print(f"Button bounds: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]")
        crop = img.crop((max(0, min_x - 30), max(0, min_y - 20), min(w, max_x + 30), min(h, max_y + 20)))
        crop.save(r"scratch\scrolled_about_btn.png")
        print("Saved crop to scratch/scrolled_about_btn.png")
