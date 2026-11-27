import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_full = os.path.abspath(r"scratch\full_page_600.png")
index_abs = os.path.abspath('index.html').replace('\\', '/')
file_url = f"file:///{index_abs}#services"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,3000",
    "--virtual-time-budget=3000",
    f"--screenshot={out_full}",
    file_url
]

subprocess.run(cmd, capture_output=True, text=True)

if os.path.exists(out_full):
    im = Image.open(out_full)
    # Services is around Y=1500 to Y=1750
    # Let's crop the exact heading area
    crop_im = im.crop((150, 1530, 1250, 1690))
    artifact_path = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\services_heading_600_preview.png"
    crop_im.save(artifact_path)
    print("Saved services heading crop to:", artifact_path)
