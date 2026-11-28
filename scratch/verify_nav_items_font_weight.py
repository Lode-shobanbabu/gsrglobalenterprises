import subprocess
import os
import json
from PIL import Image

# 1. CSS Syntax check
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()
open_b = css.count('{')
close_b = css.count('}')
print(f"CSS Braces: open={open_b}, close={close_b}, diff={open_b - close_b}")
assert open_b == close_b, f"Mismatched braces in css/style.css: {open_b} != {close_b}"

# 2. Measurement in Headless Chrome
measure_script = """
<script>
window.addEventListener('load', () => {
  const navLinks = Array.from(document.querySelectorAll('.navbar-corporate .nav-link')).map(el => {
    const s = window.getComputedStyle(el);
    return {
      text: el.textContent.trim(),
      fontWeight: s.fontWeight,
      fontFamily: s.fontFamily,
      fontSize: s.fontSize,
      color: s.color
    };
  });
  
  const navbar = document.querySelector('.navbar-corporate');
  const rect = navbar ? navbar.getBoundingClientRect() : null;
  
  const res = {
    navLinks: navLinks,
    navbarRect: rect ? {
      top: Math.round(rect.top + window.scrollY),
      bottom: Math.round(rect.bottom + window.scrollY),
      left: Math.round(rect.left),
      right: Math.round(rect.right),
      height: Math.round(rect.height)
    } : null
  };
  
  const d = document.createElement('div');
  d.id = 'nav-verify-out';
  d.textContent = JSON.stringify(res, null, 2);
  document.body.appendChild(d);
});
</script>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

temp_html = 'temp_nav_verify.html'
with open(temp_html, 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', measure_script + '\n</body>'))

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_abs = os.path.abspath(temp_html).replace('\\', '/')

# Run headless chrome to dump dom
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,2000",
    "--virtual-time-budget=3000",
    "--dump-dom",
    f"file:///{temp_abs}"
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
dom = res.stdout

if '<div id="nav-verify-out">' in dom:
    s = dom.find('<div id="nav-verify-out">') + len('<div id="nav-verify-out">')
    e = dom.find('</div>', s)
    res_data = json.loads(dom[s:e])
    print("\n=== COMPUTED NAV ITEMS FONT-WEIGHT ===")
    print(f"{'Nav Item Text':<20} | {'Font Family':<25} | {'Weight':<8} | {'Size'}")
    print("-" * 75)
    for item in res_data['navLinks']:
        txt = item['text']
        ff = item['fontFamily'][:23]
        fw = item['fontWeight']
        fs = item['fontSize']
        print(f"{txt:<20} | {ff:<25} | {fw:<8} | {fs}")
        assert fw == '600', f"Nav link '{txt}' does not have font-weight 600! Got: {fw}"
    print("\nSUCCESS: ALL NAV ITEMS ARE STRICTLY FONT-WEIGHT 600!")

    # Take screenshot of the navbar + hero top
    out_full = os.path.abspath(r"scratch\nav_full_shot.png")
    cmd_shot = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--window-size=1400,2000",
        "--virtual-time-budget=3000",
        f"--screenshot={out_full}",
        f"file:///{temp_abs}"
    ]
    subprocess.run(cmd_shot, capture_output=True, text=True)
    
    if os.path.exists(out_full):
        im = Image.open(out_full)
        # crop top 0 to 220px to show top utility bar + main navbar
        crop_im = im.crop((0, 0, 1400, 210))
        artifact_path = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\nav_items_font_weight_600.png"
        crop_im.save(artifact_path)
        print(f"Saved navigation screenshot to {artifact_path}")

if os.path.exists(temp_html):
    os.remove(temp_html)
