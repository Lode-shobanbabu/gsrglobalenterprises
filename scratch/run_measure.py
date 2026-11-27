
import subprocess
import json
import os

with open('scratch/eval_spacings.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

# Inject into index.html temporarily
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

inject = f'<script>\nwindow.addEventListener("DOMContentLoaded", () => {{\n{js_code}\n}});\n</script>'
temp_html = html.replace('</body>', inject + '\n</body>')

with open('temp_measure.html', 'w', encoding='utf-8') as f:
    f.write(temp_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_abs = os.path.abspath('temp_measure.html').replace('\\', '/')
url = f"file:///{temp_abs}"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,1000",
    "--virtual-time-budget=3000",
    "--enable-logging=stderr",
    "--v=1",
    url
]

res = subprocess.run(cmd, capture_output=True, text=True)
# Find JSON in output
output = res.stderr + "\n" + res.stdout
for line in output.splitlines():
    if line.strip().startswith('[') or line.strip().startswith('{'):
        print(line)

if os.path.exists('temp_measure.html'):
    os.remove('temp_measure.html')
