from PIL import Image
import subprocess
import os

# We can take a screenshot of index.html with full-page height or scroll to contact
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_artifact = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\contact_live_index.png"
index_abs = os.path.abspath('index.html').replace('\\', '/')
file_url = f"file:///{index_abs}#contact"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,8000",
    "--virtual-time-budget=4000",
    f"--screenshot={out_artifact}",
    file_url
]

subprocess.run(cmd, capture_output=True, text=True)

if os.path.exists(out_artifact):
    im = Image.open(out_artifact)
    print("Full height:", im.size)
    # Find contact by looking at the bottom part
    w, h = im.size
    # Contact is roughly in the lower quarter
    crop_im = im.crop((0, h - 1600, w, h - 300))
    crop_im.save(r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\contact_section_in_site.png")
    print("Saved crop to contact_section_in_site.png")
