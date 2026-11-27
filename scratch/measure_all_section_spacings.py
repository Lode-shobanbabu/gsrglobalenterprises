import subprocess
import os

script = """
const sections = Array.from(document.querySelectorAll('section'));
const data = sections.map(sec => {
    const s = window.getComputedStyle(sec);
    const id = sec.id;
    const header = sec.querySelector('.text-center, .section-header, .about-ref-content, .contact-info-panel, .commitment-content-wrap');
    
    let headerInfo = null;
    if (header) {
        const hs = window.getComputedStyle(header);
        const eyebrow = header.querySelector('[class*="eyebrow"]');
        const h2 = header.querySelector('h2, h1, .section-title, [class*="title"]');
        const p = header.querySelector('p, [class*="subtitle"], [class*="desc"]');
        
        const ebRect = eyebrow ? eyebrow.getBoundingClientRect() : null;
        const h2Rect = h2 ? h2.getBoundingClientRect() : null;
        const pRect = p ? p.getBoundingClientRect() : null;
        const headerRect = header.getBoundingClientRect();
        
        // Find next sibling or content after header
        const nextContent = header.nextElementSibling || sec.querySelector('.row, .grid, .clients-carousel-container, .contact-quote-card');
        const nextRect = nextContent ? nextContent.getBoundingClientRect() : null;
        
        headerInfo = {
            headerMarginBottom: hs.marginBottom,
            gapHeaderToContent: nextRect && pRect ? Math.round(nextRect.top - pRect.bottom) : null,
            gapHeaderTagToContent: nextRect ? Math.round(nextRect.top - headerRect.bottom) : null,
            eyebrowToTitle: ebRect && h2Rect ? Math.round(h2Rect.top - ebRect.bottom) : null,
            titleToSubtitle: h2Rect && pRect ? Math.round(pRect.top - h2Rect.bottom) : null,
        };
    }
    
    return {
        id: id,
        paddingTop: s.paddingTop,
        paddingBottom: s.paddingBottom,
        marginTop: s.marginTop,
        marginBottom: s.marginBottom,
        headerInfo: headerInfo
    };
});
console.log(JSON.stringify(data, null, 2));
"""

with open('scratch/eval_spacings.js', 'w', encoding='utf-8') as f:
    f.write(script)

# Run a python script using playwright or selenium, or write an html with this script and run chrome
runner = """
import subprocess
import json
import os

with open('scratch/eval_spacings.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

# Inject into index.html temporarily
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

inject = f'<script>\\nwindow.addEventListener("DOMContentLoaded", () => {{\\n{js_code}\\n}});\\n</script>'
temp_html = html.replace('</body>', inject + '\\n</body>')

with open('temp_measure.html', 'w', encoding='utf-8') as f:
    f.write(temp_html)

chrome_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
temp_abs = os.path.abspath('temp_measure.html').replace('\\\\', '/')
url = f"file:///{temp_abs}"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,1000",
    "--virtual-time-budget=3000",
    "--enable-logging=stderr",
    "--v=1",
    url
]

res = subprocess.run(cmd, capture_output=True, text=True)
# Find JSON in output
output = res.stderr + "\\n" + res.stdout
for line in output.splitlines():
    if line.strip().startswith('[') or line.strip().startswith('{'):
        print(line)

if os.path.exists('temp_measure.html'):
    os.remove('temp_measure.html')
"""

with open('scratch/run_measure.py', 'w', encoding='utf-8') as f:
    f.write(runner)
