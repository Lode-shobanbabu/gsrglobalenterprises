import subprocess
import os
import json
from PIL import Image

# Inject a small script that forces all .fade-up-element to have .in-view
script = """
<script>
window.addEventListener('load', () => {
  document.querySelectorAll('.fade-up-element').forEach(el => {
    el.classList.add('in-view');
    el.style.opacity = '1';
    el.style.transform = 'none';
  });
  
  const el = document.querySelector('#Industries');
  const rect = el.getBoundingClientRect();
  const d = document.createElement('div');
  d.id = 'rect-val';
  d.textContent = JSON.stringify({
    top: Math.round(rect.top + window.scrollY),
    bottom: Math.round(rect.bottom + window.scrollY),
    left: Math.round(rect.left),
    right: Math.round(rect.right),
    height: Math.round(rect.height)
  });
  document.body.appendChild(d);
});
</script>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read().replace('</body>', script + '\n</body>')

temp_html = 'temp_industries_shot.html'
with open(temp_html, 'w', encoding='utf-8') as f:
    f.write(h)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_abs = os.path.abspath(temp_html).replace('\\', '/')

# Dump dom to get rect
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,9000",
    "--virtual-time-budget=3000",
    "--dump-dom",
    f"file:///{temp_abs}"
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
dom = res.stdout

if '<div id="rect-val">' in dom:
    s = dom.find('<div id="rect-val">') + len('<div id="rect-val">')
    e = dom.find('</div>', s)
    rect = json.loads(dom[s:e])
    print("Industries rect:", rect)

    out_full = os.path.abspath(r"scratch\full_page_inview.png")
    cmd_shot = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--window-size=1400,9000",
        "--virtual-time-budget=4000",
        f"--screenshot={out_full}",
        f"file:///{temp_abs}"
    ]
    subprocess.run(cmd_shot, capture_output=True, text=True)
    
    if os.path.exists(out_full):
        im = Image.open(out_full)
        # crop with 20px padding
        crop_box = (
            max(0, rect['left']),
            max(0, rect['top'] - 10),
            min(im.size[0], rect['right']),
            min(im.size[1], rect['bottom'] + 10)
        )
        crop_im = im.crop(crop_box)
        artifact_path = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\industries_exact_icons_preview.png"
        crop_im.save(artifact_path)
        print("Successfully saved industries_exact_icons_preview.png. Size:", crop_im.size)

if os.path.exists(temp_html):
    os.remove(temp_html)
