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

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
index_abs = os.path.abspath('index.html').replace('\\', '/')

# Helper to capture and inspect
def test_viewport(width, height, name):
    # Inject inspection script to get computed background image
    script = """
    <script>
    window.addEventListener('load', () => {
      document.querySelectorAll('.fade-up-element').forEach(el => {
        el.classList.add('in-view');
        el.style.opacity = '1';
        el.style.transform = 'none';
      });
      const hero = document.querySelector('.hero-section');
      const s = window.getComputedStyle(hero);
      const rect = hero.getBoundingClientRect();
      const res = {
        bgImage: s.backgroundImage,
        bgSize: s.backgroundSize,
        bgPos: s.backgroundPosition,
        height: Math.round(rect.height),
        top: Math.round(rect.top + window.scrollY),
        bottom: Math.round(rect.bottom + window.scrollY)
      };
      const d = document.createElement('div');
      d.id = 'hero-view-data';
      d.textContent = JSON.stringify(res);
      document.body.appendChild(d);
    });
    </script>
    """
    temp_name = f'temp_hero_{name}.html'
    with open('index.html', 'r', encoding='utf-8') as f:
        h = f.read().replace('</body>', script + '\n</body>')
    with open(temp_name, 'w', encoding='utf-8') as f:
        f.write(h)
    
    temp_abs = os.path.abspath(temp_name).replace('\\', '/')
    shot_path = os.path.abspath(rf'scratch\shot_{name}.png')

    cmd = [
        chrome_path, "--headless=new", "--disable-gpu", "--no-sandbox",
        "--hide-scrollbars",
        f"--window-size={width},{height}", "--virtual-time-budget=3000",
        f"--screenshot={shot_path}", "--dump-dom", f"file:///{temp_abs}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    dom = res.stdout

    if '<div id="hero-view-data">' in dom:
        s = dom.find('<div id="hero-view-data">') + len('<div id="hero-view-data">')
        e = dom.find('</div>', s)
        data = json.loads(dom[s:e])
        print(f"\n--- {name.upper()} VIEW ({width}x{height}) ---")
        print(f"Computed bgImage: {data['bgImage']}")
        print(f"Computed bgSize:  {data['bgSize']}")
        print(f"Computed bgPos:   {data['bgPos']}")
        print(f"Hero rect height: {data['height']}px")
        
        # Save cropped hero artifact
        if os.path.exists(shot_path):
            im = Image.open(shot_path)
            # Crop to show header + hero
            crop_im = im.crop((0, 0, width, min(im.size[1], data['bottom'] + 20)))
            artifact_file = rf"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\hero_{name}_view.png"
            crop_im.save(artifact_file)
            print(f"Saved artifact to {artifact_file}")
            
    if os.path.exists(temp_name):
        os.remove(temp_name)

test_viewport(1400, 950, 'desktop')
test_viewport(768, 1100, 'tablet')
test_viewport(390, 1000, 'mobile')
