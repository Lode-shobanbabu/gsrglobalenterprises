import subprocess
from PIL import Image

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

target = """.hero-dock-card {
  background: #ffffff;
  border-radius: 14px;
  border: 1px solid rgba(6, 43, 85, 0.09);
  box-shadow: 0 10px 28px rgba(6, 43, 85, 0.08), 0 2px 8px rgba(6, 43, 85, 0.04);
  padding: 1.65rem 1.15rem 1.35rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  position: relative;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.hero-dock-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 18px 44px rgba(6, 43, 85, 0.14), 0 4px 12px rgba(6, 43, 85, 0.06);
  border-color: rgba(255, 121, 0, 0.4);
}"""

replacement = """.hero-dock-card {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  padding: 1.65rem 1.15rem 1.35rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  position: relative;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.hero-dock-card:hover {
  transform: translateY(-8px);
  background: rgba(255, 255, 255, 0.35);
  box-shadow: 0 10px 36px rgba(0, 0, 0, 0.15);
  border-color: rgba(255, 121, 0, 0.45);
}"""

if target in css:
    css = css.replace(target, replacement)
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("SUCCESS: css/style.css updated with exact glassmorphism styles.")
else:
    print("WARNING: target not found exactly. Checking if already updated or partial match...")
    if "backdrop-filter: blur(5px);" in css:
        print("Glassmorphism already in css/style.css!")
    else:
        print("Target not found, investigate!")

# 2. Capture screenshot with Chrome Headless
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html"
output_img = r"D:\shoban\GSR GLOBAL ENTERPRISES\scratch\glass_preview.png"

cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--window-size=1400,1200",
    f"--screenshot={output_img}",
    html_path
]

try:
    subprocess.run(cmd, capture_output=True, timeout=20)
    print("Screenshot captured to scratch/glass_preview.png")
    
    # Crop the hero and dock card region
    img = Image.open(output_img)
    # The hero and dock cards should be around y=300 to y=800
    cropped = img.crop((100, 250, 1300, 750))
    cropped.save(r"D:\shoban\GSR GLOBAL ENTERPRISES\scratch\dock_cards_crop.png")
    print("Cropped dock cards saved to scratch/dock_cards_crop.png")
except Exception as e:
    print(f"Screenshot error: {e}")
