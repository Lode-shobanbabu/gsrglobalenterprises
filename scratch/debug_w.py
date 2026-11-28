import subprocess, json, os

script = """<script>
window.addEventListener('load', () => {
  const container = document.querySelector('.hero-section .container');
  const h1 = document.querySelector('.hero-main-title');
  const s1 = window.getComputedStyle(container);
  const s2 = window.getComputedStyle(h1);
  const r1 = container.getBoundingClientRect();
  const r2 = h1.getBoundingClientRect();
  const d = document.createElement('div');
  d.id = 'debug-widths';
  d.textContent = JSON.stringify({
    container: { width: r1.width, left: r1.left, right: r1.right, paddingLeft: s1.paddingLeft, paddingRight: s1.paddingRight },
    h1: { width: r2.width, left: r2.left, right: r2.right, fontSize: s2.fontSize, whiteSpace: s2.whiteSpace }
  });
  document.body.appendChild(d);
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read().replace('</body>', script + '\n</body>')
with open('debug_w.html', 'w', encoding='utf-8') as f:
    f.write(h)

cmd = [r'C:\Program Files\Google\Chrome\Application\chrome.exe', '--headless=new', '--disable-gpu', '--no-sandbox', '--window-size=390,1000', '--dump-dom', 'file:///' + os.path.abspath('debug_w.html').replace('\\', '/')]
dom = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8').stdout
s = dom.find('<div id="debug-widths">') + len('<div id="debug-widths">')
e = dom.find('</div>', s)
print(dom[s:e])
if os.path.exists('debug_w.html'):
    os.remove('debug_w.html')
