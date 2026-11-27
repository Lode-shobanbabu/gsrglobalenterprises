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
    const container = sec.querySelector('.container');
    const header = container.querySelector('.text-center');
    const content = header.nextElementSibling;
    
    const subBox = sub.getBoundingClientRect();
    const headerBox = header.getBoundingClientRect();
    const contentBox = content.getBoundingClientRect();
    
    return {
      id: id,
      subtitleBottom: Math.round(subBox.bottom),
      headerBottom: Math.round(headerBox.bottom),
      contentTop: Math.round(contentBox.top),
      gapSubtitleToContent: Math.round(contentBox.top - subBox.bottom),
      gapHeaderToContent: Math.round(contentBox.top - headerBox.bottom),
      headerMarginBottom: window.getComputedStyle(header).marginBottom
    };
  });
  
  const d = document.createElement('div');
  d.id = 'real-gaps';
  d.textContent = JSON.stringify(res, null, 2);
  document.body.appendChild(d);
});
</script>
"""

with open('temp_real_gaps.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', measure_script + '\n</body>'))

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_abs = os.path.abspath('temp_real_gaps.html').replace('\\', '/')

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

if '<div id="real-gaps">' in dom:
    s = dom.find('<div id="real-gaps">') + len('<div id="real-gaps">')
    e = dom.find('</div>', s)
    results = json.loads(dom[s:e])
    print(json.dumps(results, indent=2))

if os.path.exists('temp_real_gaps.html'):
    os.remove('temp_real_gaps.html')
