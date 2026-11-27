import subprocess, json, os

script = """<script>
window.addEventListener('load', () => {
  const el1 = document.querySelector('#Industries');
  const el2 = document.querySelector('.industries-section');
  const el3 = document.querySelector('.industries-section-title');
  const el4 = document.querySelector('.industries-grid');
  
  const getR = el => el ? {
    top: Math.round(el.getBoundingClientRect().top + window.scrollY),
    bottom: Math.round(el.getBoundingClientRect().bottom + window.scrollY),
    left: Math.round(el.getBoundingClientRect().left),
    right: Math.round(el.getBoundingClientRect().right),
    height: Math.round(el.getBoundingClientRect().height)
  } : null;

  const res = {
    '#Industries': getR(el1),
    '.industries-section': getR(el2),
    '.industries-section-title': getR(el3),
    '.industries-grid': getR(el4),
  };
  const d = document.createElement('div');
  d.id = 'rects-out';
  d.textContent = JSON.stringify(res);
  document.body.appendChild(d);
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read().replace('</body>', script + '\n</body>')
with open('test_r.html', 'w', encoding='utf-8') as f:
    f.write(h)

cmd = [r'C:\Program Files\Google\Chrome\Application\chrome.exe', '--headless=new', '--disable-gpu', '--no-sandbox', '--window-size=1400,8000', '--virtual-time-budget=3000', '--dump-dom', 'file:///' + os.path.abspath('test_r.html').replace('\\', '/')]
out = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8').stdout
s = out.find('<div id="rects-out">') + len('<div id="rects-out">')
e = out.find('</div>', s)
print(out[s:e])
if os.path.exists('test_r.html'):
    os.remove('test_r.html')
