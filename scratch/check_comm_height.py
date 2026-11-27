import os
import subprocess

html_file = os.path.abspath('index.html').replace('\\', '/')

# We can append a tiny script at the end of a temp copy of index.html to output document.title with height
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

snippet = """
<script>
window.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    const el = document.getElementById('commitment');
    const wrap = document.querySelector('.commitment-content-wrap');
    if (el) {
      const r = el.getBoundingClientRect();
      const wr = wrap ? wrap.getBoundingClientRect() : {};
      document.title = 'COMM_HEIGHT:' + JSON.stringify({el_height: r.height, wrap_height: wr.height, top: r.top, bottom: r.bottom});
    }
  }, 400);
});
</script>
"""

temp_html = os.path.abspath('scratch/temp_comm_measure.html').replace('\\', '/')
with open(temp_html, 'w', encoding='utf-8') as f:
    f.write(content.replace('</body>', snippet + '</body>'))

cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1440,1200",
    "--virtual-time-budget=2000",
    "--dump-dom",
    f"file:///{temp_html}"
]

res = subprocess.run(cmd, capture_output=True, text=True)
for line in res.stdout.splitlines():
    if "COMM_HEIGHT:" in line:
        print(line)
