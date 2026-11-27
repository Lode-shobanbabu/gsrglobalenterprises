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
assert open_b == close_b, f"Mismatched braces in css/style.css! {open_b} != {close_b}"

# 2. Check measurement in Headless Chrome
measure_script = """
<script>
window.addEventListener('load', () => {
  const section = document.querySelector('#Industries');
  const grid = document.querySelector('.industries-grid');
  const cards = document.querySelectorAll('.industry-support-card');
  const icons = document.querySelectorAll('.industry-icon-circle');
  const titles = document.querySelectorAll('.industry-card-title');
  const descs = document.querySelectorAll('.industry-card-desc');
  
  const iconBgColors = Array.from(icons).map(ic => window.getComputedStyle(ic).backgroundColor);
  const cardTitleWeights = Array.from(titles).map(t => window.getComputedStyle(t).fontWeight);
  const gridTemplate = grid ? window.getComputedStyle(grid).gridTemplateColumns : '';
  
  const rect = section ? section.getBoundingClientRect() : null;
  
  const result = {
    cardCount: cards.length,
    iconCount: icons.length,
    iconBgColors: iconBgColors,
    cardTitleWeights: cardTitleWeights,
    gridTemplateColumns: gridTemplate,
    sectionRect: rect ? {
      top: Math.round(rect.top + window.scrollY),
      bottom: Math.round(rect.bottom + window.scrollY),
      left: Math.round(rect.left),
      right: Math.round(rect.right),
      width: Math.round(rect.width),
      height: Math.round(rect.height)
    } : null
  };
  
  const d = document.createElement('div');
  d.id = 'industries-measure-result';
  d.textContent = JSON.stringify(result, null, 2);
  document.body.appendChild(d);
});
</script>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

temp_html = 'temp_industries_verify.html'
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
    "--window-size=1400,8000",
    "--virtual-time-budget=3000",
    "--dump-dom",
    f"file:///{temp_abs}"
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
dom = res.stdout

if '<div id="industries-measure-result">' in dom:
    s = dom.find('<div id="industries-measure-result">') + len('<div id="industries-measure-result">')
    e = dom.find('</div>', s)
    res_data = json.loads(dom[s:e])
    print("\n=== MEASUREMENT RESULTS ===")
    print(f"Cards count: {res_data['cardCount']} (expected: 6)")
    print(f"Icons count: {res_data['iconCount']} (expected: 6)")
    print(f"Icon background colors: {res_data['iconBgColors']}")
    print(f"Card title font weights: {res_data['cardTitleWeights']}")
    print(f"Grid template columns: {res_data['gridTemplateColumns']}")
    print(f"Section rect: {res_data['sectionRect']}")
    
    # Assertions
    assert res_data['cardCount'] == 6
    assert res_data['iconCount'] == 6
    for bg in res_data['iconBgColors']:
        assert bg in ['rgba(0, 0, 0, 0)', 'transparent'], f"Icon has non-transparent background: {bg}"
    for fw in res_data['cardTitleWeights']:
        assert fw == '600', f"Card title font weight is not 600: {fw}"

    # Take screenshot of the page and crop to Section 5
    out_full = os.path.abspath(r"scratch\full_industries_test.png")
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
        r = res_data['sectionRect']
        # Add 15px padding top and bottom
        crop_box = (
            max(0, r['left'] - 10),
            max(0, r['top'] - 10),
            min(im.size[0], r['right'] + 10),
            min(im.size[1], r['bottom'] + 10)
        )
        crop_im = im.crop(crop_box)
        artifact_path = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\industries_exact_icons_preview.png"
        crop_im.save(artifact_path)
        print(f"\nSUCCESS: Screenshot of Section 5 saved to {artifact_path}")

if os.path.exists(temp_html):
    os.remove(temp_html)
