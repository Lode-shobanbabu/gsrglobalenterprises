import subprocess
import os

html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html"
abs_out = os.path.abspath(r"scratch\inter_font_preview.png").replace('\\', '/')

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,1200",
    "--virtual-time-budget=2000",
    f"--screenshot={abs_out}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(abs_out):
    print("Screenshot captured successfully at", abs_out)
else:
    print("Failed to capture screenshot:", res.stderr)
