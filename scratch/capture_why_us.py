import os
import subprocess
from PIL import Image

html_file = os.path.abspath('scratch/test_why_us.html').replace('\\', '/')
out_img = os.path.abspath('scratch/why_us_live.png').replace('\\', '/')

cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1440,1100",
    "--virtual-time-budget=3000",
    f"--screenshot={out_img}",
    f"file:///{html_file}"
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome return code:", res.returncode)

if os.path.exists(out_img):
    im = Image.open(out_img)
    # Crop to section
    crop = im.crop((40, 40, 1400, 1020))
    artifact_path = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\why_us_gradient_preview.png"
    crop.save(artifact_path)
    print(f"Saved cropped preview to {artifact_path}, size={crop.size}")
else:
    print("Screenshot failed.")
