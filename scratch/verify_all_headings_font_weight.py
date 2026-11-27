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
assert open_b == close_b, "Mismatched braces in css/style.css"

# 2. Measurement in Headless Chrome
measure_script = """
<script>
window.addEventListener('load', () => {
  const headingSelectors = [
    { name: 'Hero Main Title', sel: '.hero-main-title' },
    { name: 'Dock Card 1 Title', sel: '.hero-dock-card:nth-child(1) .dock-card-title' },
    { name: 'About Us Title', sel: '.about-ref-title' },
    { name: 'Services Title', sel: '.services-section-title' },
    { name: 'Service Card Title', sel: '.service-pro-title' },
    { name: 'Industries Title', sel: '.industries-section-title' },
    { name: 'Industry Card Title', sel: '.industry-card-title' },
    { name: 'Why Us Title', sel: '.why-section-title' },
    { name: 'Why Us Card Title', sel: '.why-ref-title' },
    { name: 'Clients Title', sel: '.clients-section-title' },
    { name: 'Process Title', sel: '.process-section-title' },
    { name: 'Process Step Title', sel: '.procurement-step-title' },
    { name: 'Commitment Title', sel: '.commitment-title' },
    { name: 'Contact Panel Title', sel: '.contact-panel-title' },
    { name: 'Quote Card Title', sel: '.quote-card-title' }
  ];
  
  const results = headingSelectors.map(item => {
    const el = document.querySelector(item.sel);
    if (!el) return { name: item.name, selector: item.sel, error: 'Element not found' };
    const s = window.getComputedStyle(el);
    return {
      name: item.name,
      selector: item.sel,
      text: el.textContent.trim().replace(/\\s+/g, ' ').substring(0, 45),
      fontFamily: s.fontFamily,
      fontWeight: s.fontWeight
    };
  });
  
  const d = document.createElement('div');
  d.id = 'heading-weights-result';
  d.textContent = JSON.stringify(results, null, 2);
  document.body.appendChild(d);
});
</script>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('temp_heading_weights.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', measure_script + '\n</body>'))

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_abs = os.path.abspath('temp_heading_weights.html').replace('\\', '/')

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

if '<div id="heading-weights-result">' in dom:
    s = dom.find('<div id="heading-weights-result">') + len('<div id="heading-weights-result">')
    e = dom.find('</div>', s)
    results = json.loads(dom[s:e])
    print("\n=== COMPUTED FONT-WEIGHT OF ALL HEADINGS (TOP TO BOTTOM) ===")
    print(f"{'Heading Name':<25} | {'Font Family':<25} | {'Weight':<8} | {'Text Preview'}")
    print("-" * 90)
    for r in results:
        ff = r.get('fontFamily', '')[:23]
        fw = r.get('fontWeight', '')
        txt = r.get('text', '')
        print(f"{r['name']:<25} | {ff:<25} | {fw:<8} | {txt}")
        assert fw == '600', f"Heading {r['name']} does not have font-weight 600! Got: {fw}"
    print("\nSUCCESS: ALL HEADINGS FROM TOP TO BOTTOM ARE STRICTLY FONT-WEIGHT 600!")

if os.path.exists('temp_heading_weights.html'):
    os.remove('temp_heading_weights.html')
