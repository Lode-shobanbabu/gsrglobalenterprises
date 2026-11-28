import subprocess, json, os

script = """<script>
window.addEventListener('load', () => {
  const all = Array.from(document.querySelectorAll('*'));
  const list = all.map(el => {
    return {
      tag: el.tagName,
      cls: (el.className || '').toString().substring(0, 35),
      id: el.id,
      width: Math.round(el.scrollWidth)
    };
  }).filter(x => x.width > 390);
  list.sort((a,b) => b.width - a.width);
  const d = document.createElement('div');
  d.id = 'wide-out';
  d.textContent = JSON.stringify(list.slice(0, 20));
  document.body.appendChild(d);
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read().replace('</body>', script + '\n</body>')
with open('debug_wide.html', 'w', encoding='utf-8') as f:
    f.write(h)

cmd = [r'C:\Program Files\Google\Chrome\Application\chrome.exe', '--headless=new', '--disable-gpu', '--no-sandbox', '--window-size=390,1000', '--dump-dom', 'file:///' + os.path.abspath('debug_wide.html').replace('\\', '/')]
dom = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8').stdout
s = dom.find('<div id="wide-out">') + len('<div id="wide-out">')
e = dom.find('</div>', s)
print(dom[s:e])
if os.path.exists('debug_wide.html'):
    os.remove('debug_wide.html')
