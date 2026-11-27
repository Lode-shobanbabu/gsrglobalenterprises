import os
import subprocess
from PIL import Image

# Test by rendering a standalone test html file that has only this section to inspect visual button rendering
test_html = """<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500&display=swap">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <link rel="stylesheet" href="css/style.css">
  <style>
    body { background: #f8fafc; padding: 40px; display: flex; justify-content: center; }
  </style>
</head>
<body>
  <div class="services-bottom-cta text-center">
    <a href="#contact" class="btn services-discuss-btn" aria-label="Have a Specific Requirement? Let's Discuss">
      <span>Have a Specific Requirement? Let's Discuss.</span>
      <i class="bi bi-arrow-right"></i>
    </a>
  </div>
</body>
</html>"""

with open('scratch/test_discuss_btn.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/scratch/test_discuss_btn.html"
abs_out = os.path.abspath(r"scratch\test_discuss_btn_shot.png").replace('\\', '/')

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=800,300",
    f"--screenshot={abs_out}",
    html_path
]

subprocess.run(cmd, capture_output=True, text=True)

if os.path.exists(abs_out):
    img = Image.open(abs_out)
    print("Screenshot captured! Size:", img.size)
    crop = img.crop((100, 30, 700, 150))
    crop.save(r"scratch\discuss_btn_rendered.png")
    
    import shutil
    shutil.copyfile(r"scratch\discuss_btn_rendered.png", r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\services_discuss_btn_preview.png")
    print("Saved preview to brain!")
