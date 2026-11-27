import os
import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_artifact = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\contact_full_context_preview.png"
index_abs = os.path.abspath('index.html').replace('\\', '/')
file_url = f"file:///{index_abs}"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,2600",
    "--virtual-time-budget=4000",
    f"--screenshot={out_artifact}",
    file_url
]

print("Capturing full page...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit:", res.returncode)

if os.path.exists(out_artifact):
    print("Full page screenshot created.")
    # Crop to show bottom of Commitment, entire Contact, and top of Footer
    from PIL import Image
    im = Image.open(out_artifact)
    print("Full page size:", im.size)
    # Contact is towards the bottom of the page
    # Let's save a crop of the contact area
    w, h = im.size
    # Contact is roughly in the last 1200px before footer
    contact_crop = im.crop((0, max(0, h - 1400), w, h))
    crop_path = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\contact_in_site_preview.png"
    contact_crop.save(crop_path)
    print("Cropped context saved to:", crop_path)
