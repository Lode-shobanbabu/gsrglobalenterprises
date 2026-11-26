import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html"
output_img = r"D:\shoban\GSR GLOBAL ENTERPRISES\scratch\services_rendered.png"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1400,2800",
    f"--screenshot={output_img}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
print("Return code:", res.returncode)
print("Stdout:", res.stdout)
print("Stderr:", res.stderr)

import os
print("File exists:", os.path.exists(output_img))
