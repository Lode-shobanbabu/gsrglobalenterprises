import subprocess
import os
import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

measure_script = """
<script>
window.addEventListener('load', () => {
  const sections = ['services', 'Industries', 'why-us', 'clients', 'process'];
  const res = sections.map(id => {
    const sec = document.getElementById(id);
    const sub = sec.querySelector('[class*="subtitle"]');
    
    // Find the first actual visual item or card
    const firstVisual = sec.querySelector('.service-pro-card, .industry-support-card, .why-ref-card, .clients-carousel-viewport, .procurement-image-card');
    
    const subBox = sub.getBoundingClientRect();
    const visBox = firstVisual ? firstVisual.getBoundingClientRect() : null;
    
    return {
      id: id,
      subtitleBottom: Math.round(subBox.bottom),
      firstCardTop: visBox ? Math.round(visBox.top) : null,
      realVisualGap: visBox ? Math.round(visBox.top - subBox.bottom) : null
    };
  });
  
  const d = document.createElement('div');
  d.id = 'visual-gaps';
  d.textContent = JSON.stringify(res, null, 2);
  document.body.appendChild(d);
});
</script>
"""

with open('temp_vis_gaps.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', measure_script + '\n</body>'))

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_abs = os.path.abspath('temp_vis_gaps.html').replace('\\', '/')

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

if '<div id="visual-gaps">' in dom:
    s = dom.find('<div id="visual-gaps">') + len('<div id="visual-gaps">')
    e = dom.find('</div>', s)
    results = json.loads(dom[s:e])
    print(json.dumps(results, indent=2))

if os.path.exists('temp_vis_gaps.html'):
    os.remove('temp_vis_gaps.html')
