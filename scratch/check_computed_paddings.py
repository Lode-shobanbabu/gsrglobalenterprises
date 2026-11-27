import subprocess
import os
import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

script = """
<script>
window.addEventListener('load', () => {
  const ids = ['sectors', 'about', 'services', 'Industries', 'why-us', 'clients', 'process', 'commitment', 'contact'];
  const res = ids.map(id => {
    const el = document.getElementById(id);
    if (!el) return { id, error: 'not found' };
    const s = window.getComputedStyle(el);
    return {
      id: id,
      className: el.className,
      paddingTop: s.paddingTop,
      paddingBottom: s.paddingBottom,
      marginTop: s.marginTop,
      marginBottom: s.marginBottom
    };
  });
  const d = document.createElement('div');
  d.id = 'paddings-result';
  d.textContent = JSON.stringify(res, null, 2);
  document.body.appendChild(d);
});
</script>
"""

with open('temp_paddings.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', script + '\n</body>'))

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_abs = os.path.abspath('temp_paddings.html').replace('\\', '/')

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--dump-dom",
    f"file:///{temp_abs}"
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
dom = res.stdout

if '<div id="paddings-result">' in dom:
    s = dom.find('<div id="paddings-result">') + len('<div id="paddings-result">')
    e = dom.find('</div>', s)
    print(dom[s:e])

if os.path.exists('temp_paddings.html'):
    os.remove('temp_paddings.html')
