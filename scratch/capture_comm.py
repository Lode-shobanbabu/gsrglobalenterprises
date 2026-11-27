import os
import subprocess
from PIL import Image

html_file = os.path.abspath('scratch/temp_comm_measure.html').replace('\\', '/')
out_img = os.path.abspath('scratch/comm_current_shot.png').replace('\\', '/')

cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1440,3000",
    "--virtual-time-budget=2500",
    f"--screenshot={out_img}",
    f"file:///{html_file}"
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)

if os.path.exists(out_img):
    im = Image.open(out_img)
    # Find commitment section by blue overlay / background
    # Background color is #125197 (RGB: 18, 81, 151)
    comm_pts = []
    for y in range(im.height):
        for x in [100, 200, 300, 500]:
            r, g, b = im.getpixel((x, y))[:3]
            # blue gradient overlay
            if 15 <= r <= 35 and 70 <= g <= 115 and 145 <= b <= 200:
                comm_pts.append(y)
                break
    if comm_pts:
        top_y, bot_y = min(comm_pts), max(comm_pts)
        print(f"Commitment bounds in full page: top={top_y}, bottom={bot_y}, height={bot_y - top_y}px")
        crop = im.crop((0, max(0, top_y - 20), im.width, min(im.height, bot_y + 20)))
        artifact_path = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\commitment_current_preview.png"
        crop.save(artifact_path)
        print(f"Saved crop to {artifact_path}, size={crop.size}")
