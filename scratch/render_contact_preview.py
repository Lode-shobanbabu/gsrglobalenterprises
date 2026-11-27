import os
import subprocess

# 1. Verify CSS brace balance
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

open_b = css.count('{')
close_b = css.count('}')
print(f"CSS Braces: open={open_b}, close={close_b}, diff={open_b - close_b}")
assert open_b == close_b, "Mismatched braces in css/style.css!"

# 2. Extract Section 10 HTML from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_idx = html.find('id="contact"')
assert start_idx != -1, "Contact section not found in index.html!"

sec_start = html.rfind('<section', 0, start_idx)
sec_end = html.find('</section>', start_idx) + len('</section>')
contact_html = html[sec_start:sec_end]

# Create a standalone preview HTML in the workspace root
preview_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Section Preview</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
  <style>
    body {{
      background: #f8fafc;
      margin: 0;
      padding: 20px 0;
    }}
    .fade-up-element {{
      opacity: 1 !important;
      transform: none !important;
    }}
  </style>
</head>
<body>
{contact_html}
</body>
</html>
"""

temp_file = 'temp_contact_preview.html'
with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(preview_html)

# 3. Screenshot with headless Chrome
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_artifact = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\contact_section_preview.png"
temp_file_abs = os.path.abspath(temp_file).replace('\\', '/')
file_url = f"file:///{temp_file_abs}"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,950",
    "--virtual-time-budget=3000",
    f"--screenshot={out_artifact}",
    file_url
]

print("Running headless Chrome...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit:", res.returncode)

if os.path.exists(out_artifact):
    print("Screenshot successfully created at:", out_artifact)
    file_size = os.path.getsize(out_artifact)
    print(f"File size: {file_size} bytes")
else:
    print("Failed to create screenshot.")
    print("Stdout:", res.stdout)
    print("Stderr:", res.stderr)

# Cleanup
if os.path.exists(temp_file):
    os.remove(temp_file)
    print("Temporary file cleaned up.")
