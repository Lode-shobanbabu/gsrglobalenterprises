import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_full = os.path.abspath(r"scratch\full_page.png")
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

print("Running chrome...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit:", res.returncode)

crops_info = [
    ("services", 1500, 1800),
    ("Industries", 3170, 3480),
    ("why_us", 4080, 4390),
    ("clients", 4940, 5280),
    ("process", 5530, 5780)
]

if os.path.exists(out_full):
    im = Image.open(out_full)
    w, h = im.size
    print("Full image size:", im.size)
    
    cropped_imgs = []
    for name, top, bottom in crops_info:
        left = 100
        right = 1300
        c = im.crop((left, top, right, bottom))
        cropped_imgs.append((name, c))
    
    total_h = sum(c.size[1] for _, c in cropped_imgs) + len(cropped_imgs) * 20
    max_w = max(c.size[0] for _, c in cropped_imgs)
    
    combined = Image.new('RGB', (max_w, total_h), (240, 243, 246))
    curr_y = 10
    for name, c in cropped_imgs:
        combined.paste(c, (0, curr_y))
        curr_y += c.size[1] + 20
        
    out_artifact = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\equal_section_gaps_preview.png"
    combined.save(out_artifact)
    print("Combined preview saved to:", out_artifact)
else:
    print("Screenshot failed!")
