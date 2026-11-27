import subprocess
import os
import json
import re

# 1. CSS Syntax check
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()
open_b = css.count('{')
close_b = css.count('}')
print(f"CSS Braces: open={open_b}, close={close_b}, diff={open_b - close_b}")
assert open_b == close_b, "Mismatched braces in css/style.css"

# 2. HTML Tag Balance
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for tag in ['div', 'section', 'span', 'h2', 'h3', 'p']:
    o = len(re.findall(rf'<{tag}\b', html))
    c = html.count(f'</{tag}>')
    print(f"<{tag}>: {o} open, {c} close (Balanced: {o == c})")
    assert o == c, f"Mismatched tag: <{tag}>"

# 3. Measurement in Headless Chrome
measure_script = """
<script>
window.addEventListener('load', () => {
  const sections = ['about', 'services', 'Industries', 'why-us', 'clients', 'process', 'commitment', 'contact'];
  const res = sections.map(id => {
    const sec = document.getElementById(id);
    if (!sec) return { id, error: 'not found' };
    const s = window.getComputedStyle(sec);
    
    const eb = sec.querySelector('[class*="eyebrow"], .contact-panel-tag');
    const h = sec.querySelector('h1, h2, [class*="section-title"], [class*="title"]');
    const sub = sec.querySelector('[class*="subtitle"], .contact-panel-desc, .commitment-text');
    const headerContainer = sec.querySelector('.text-center');
    let content = null;
    if (headerContainer) {
      content = headerContainer.nextElementSibling;
    } else {
      content = sec.querySelector('.row, .commitment-content-wrap');
    }
    
    const ebBox = eb ? eb.getBoundingClientRect() : null;
    const hBox = h ? h.getBoundingClientRect() : null;
    const subBox = sub ? sub.getBoundingClientRect() : null;
    const headerBox = headerContainer ? headerContainer.getBoundingClientRect() : null;
    const contentBox = content ? content.getBoundingClientRect() : null;
    
    return {
      id: id,
      paddingTop: s.paddingTop,
      paddingBottom: s.paddingBottom,
      gapEyebrowToHeading: (ebBox && hBox) ? Math.round(hBox.top - ebBox.bottom) : null,
      gapHeadingToSubtitle: (hBox && subBox) ? Math.round(subBox.top - hBox.bottom) : null,
      gapSubtitleToContent: (subBox && contentBox) ? Math.round(contentBox.top - subBox.bottom) : null,
      gapHeaderToContent: (headerBox && contentBox) ? Math.round(contentBox.top - headerBox.bottom) : null,
    };
  });
  
  const d = document.createElement('div');
  d.id = 'gap-results';
  d.textContent = JSON.stringify(res, null, 2);
  document.body.appendChild(d);
});
</script>
"""

with open('temp_gap_test.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', measure_script + '\n</body>'))

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_abs = os.path.abspath('temp_gap_test.html').replace('\\', '/')

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

if '<div id="gap-results">' in dom:
    s = dom.find('<div id="gap-results">') + len('<div id="gap-results">')
    e = dom.find('</div>', s)
    results = json.loads(dom[s:e])
    print("\n=== MEASURED GAPS ACROSS ALL SECTIONS ===")
    print(f"{'Section':<15} | {'PT':<6} | {'PB':<6} | {'Eb->Head':<9} | {'Head->Sub':<10} | {'Sub->Content':<12}")
    print("-" * 75)
    for r in results:
        pt = r['paddingTop']
        pb = r['paddingBottom']
        eb_h = str(r['gapEyebrowToHeading'])
        h_sub = str(r['gapHeadingToSubtitle'])
        sub_c = str(r['gapSubtitleToContent'])
        print(f"{r['id']:<15} | {pt:<6} | {pb:<6} | {eb_h:<9} | {h_sub:<10} | {sub_c:<12}")

if os.path.exists('temp_gap_test.html'):
    os.remove('temp_gap_test.html')
