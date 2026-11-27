import os
import subprocess
from PIL import Image

html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html#about"
abs_out = os.path.abspath(r"scratch\about_perfect_equal.png").replace('\\', '/')

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

subprocess.run(cmd, capture_output=True, text=True)

full = Image.open(abs_out)
w, h = full.size

# Search left image bounds
img_pts = []
for x in range(120, 600, 5):
    for y in range(80, 850, 5):
        p = full.getpixel((x, y))
        if p != (255, 255, 255):
            img_pts.append((x, y))

min_y = min(p[1] for p in img_pts)
max_y = max(p[1] for p in img_pts)
print(f"Left Image frame: top={min_y}, bottom={max_y}, height={max_y - min_y}px")

# Search right content bounds
content_pts = []
for x in range(700, 1300, 5):
    for y in range(80, 850, 5):
        p = full.getpixel((x, y))
        if p != (255, 255, 255):
            content_pts.append((x, y))

min_cy = min(p[1] for p in content_pts)
max_cy = max(p[1] for p in content_pts)
print(f"Right Content: top={min_cy}, bottom={max_cy}, height={max_cy - min_cy}px")

# Save a cropped comparison
crop = full.crop((100, min_y - 20, 1320, max_y + 20))
crop.save(r"scratch\about_equal_height_perfect.png")
print("Saved comparison crop to scratch/about_equal_height_perfect.png")
