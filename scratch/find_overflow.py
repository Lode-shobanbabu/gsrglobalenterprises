import subprocess, json, os

script = """<script>
window.addEventListener('load', () => {
  const all = Array.from(document.querySelectorAll('*'));
  const overflowing = [];
  all.forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.right > 390) {
      overflowing.push({
        tag: el.tagName,
        cls: el.className,
        id: el.id,
        right: Math.round(r.right),
        width: Math.round(r.width)
      });
    }
  });
  const d = document.createElement('div');
  d.id = 'overflow-out';
  d.textContent = JSON.stringify(overflowing.slice(0, 15));
  document.body.appendChild(d);
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read().replace('</body>', script + '\n</body>')
with open('debug_overflow.html', 'w', encoding='utf-8') as f:
    f.write(h)

cmd = [r'C:\Program Files\Google\Chrome\Application\chrome.exe', '--headless=new', '--disable-gpu', '--no-sandbox', '--window-size=390,1000', '--dump-dom', 'file:///' + os.path.abspath('debug_overflow.html').replace('\\', '/')]
dom = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8').stdout
s = dom.find('<div id="overflow-out">') + len('<div id="overflow-out">')
e = dom.find('</div>', s)
print(dom[s:e])
if os.path.exists('debug_overflow.html'):
    os.remove('debug_overflow.html')
