import subprocess
import os
import json
from PIL import Image

# Get rect of .services-section-title and .process-section-title
script = """
<script>
window.addEventListener('load', () => {
  const titles = [
    { name: 'services', sel: '.services-section-title' },
    { name: 'process', sel: '.process-section-title' },
    { name: 'industries', sel: '.industries-section-title' }
  ];
  const r = {};
  titles.forEach(t => {
    const el = document.querySelector(t.sel);
    if (el) {
      const rect = el.getBoundingClientRect();
      r[t.name] = {
        top: Math.round(rect.top + window.scrollY),
        bottom: Math.round(rect.bottom + window.scrollY),
        left: Math.round(rect.left),
        right: Math.round(rect.right)
      };
    }
  });
  const d = document.createElement('div');
  d.id = 'rect-res';
  d.textContent = JSON.stringify(r);
  document.body.appendChild(d);
});
</script>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('temp_rect.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', script + '\n</body>'))

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_abs = os.path.abspath('temp_rect.html').replace('\\', '/')

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,8000",
    "--virtual-time-budget=3000",
    "--dump-dom",
    f"file:///{temp_abs}"
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
dom = res.stdout

if '<div id="rect-res">' in dom:
    s = dom.find('<div id="rect-res">') + len('<div id="rect-res">')
    e = dom.find('</div>', s)
    rects = json.loads(dom[s:e])
    print(rects)
    
    # Take screenshot of the 8000px page
    out_full = os.path.abspath(r"scratch\full_page_8000.png")
    cmd_shot = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--window-size=1400,8000",
        "--virtual-time-budget=4000",
        f"--screenshot={out_full}",
        f"file:///{temp_abs}"
    ]
    subprocess.run(cmd_shot, capture_output=True, text=True)
    
    if os.path.exists(out_full):
        im = Image.open(out_full)
        for name, r in rects.items():
            # Crop title with 20px padding around it
            crop_im = im.crop((max(0, r['left'] - 30), max(0, r['top'] - 20), min(im.size[0], r['right'] + 30), r['bottom'] + 20))
            crop_path = rf"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\heading_600_{name}.png"
            crop_im.save(crop_path)
            print(f"Saved {name} heading to {crop_path}")

if os.path.exists('temp_rect.html'):
    os.remove('temp_rect.html')
