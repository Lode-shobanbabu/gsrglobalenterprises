import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html"
output_img = r"scratch\glass_preview.png"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,1200",
    f"--screenshot={output_img}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)
print("Stdout:", res.stdout)
print("Stderr:", res.stderr)
