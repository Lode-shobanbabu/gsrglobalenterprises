import subprocess
import os
from PIL import Image

# 1. CSS Syntax
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()
open_b = css.count('{')
close_b = css.count('}')
print(f"CSS Braces: open={open_b}, close={close_b}, diff={open_b - close_b}")
assert open_b == close_b, "Mismatched braces in css/style.css"

# 2. Check HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

assert 'A Straightforward Approach to Reliable<br>Procurement' in html, "Heading break missing"
print("Heading break verified in HTML")

# 3. Take screenshot of process section
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_full = os.path.abspath(r"scratch\process_full.png")
index_abs = os.path.abspath('index.html').replace('\\', '/')
file_url = f"file:///{index_abs}#process"

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

if os.path.exists(out_full):
    im = Image.open(out_full)
    w, h = im.size
    
    # Process section is roughly around Y=5500 to Y=6400
    # Let's crop from Y=5500 to Y=6350
    crop_im = im.crop((100, 5500, 1300, 6300))
    artifact_path = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\process_section_updated.png"
    crop_im.save(artifact_path)
    print("Process section screenshot saved to:", artifact_path)
