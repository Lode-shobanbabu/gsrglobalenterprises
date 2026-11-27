import subprocess
import os
import json
from PIL import Image

# 1. Take full screenshot
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_full = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\all_sections_full.png"
index_abs = os.path.abspath('index.html').replace('\\', '/')
file_url = f"file:///{index_abs}"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,8000",
    "--virtual-time-budget=4000",
    f"--screenshot={out_full}",
    file_url
]

subprocess.run(cmd, capture_output=True, text=True)

# 2. Get header rects
rects = {'services': {'top': 1511, 'bottom': 1689, 'height': 178}, 'Industries': {'top': 3185, 'bottom': 3382, 'height': 197}, 'why-us': {'top': 4094, 'bottom': 4282, 'height': 187}, 'clients': {'top': 4956, 'bottom': 5194, 'height': 237}, 'process': {'top': 5544, 'bottom': 5716, 'height': 172}}

if os.path.exists(out_full):
    im = Image.open(out_full)
    for sec_id, r in rects.items():
        crop_box = (100, max(0, r['top'] - 60), 1300, min(im.size[1], r['bottom'] + 80))
        crop_im = im.crop(crop_box)
        crop_path = rf"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\header_{sec_id}.png"
        crop_im.save(crop_path)
        print(f"Saved crop for {sec_id} to {crop_path}")
