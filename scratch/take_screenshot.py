import subprocess
import time

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html"
output_img = r"D:\shoban\GSR GLOBAL ENTERPRISES\scratch\services_rendered.png"

cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--window-size=1400,2200",
    f"--screenshot={output_img}",
    html_path
]

print("Running chrome screenshot...")
subprocess.run(cmd, capture_output=True, timeout=30)
print("Finished!")
