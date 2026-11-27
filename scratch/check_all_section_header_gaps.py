import os
import subprocess
import json

# HTML to measure rendered positions of header elements in each section
runner_html = """<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <link rel="stylesheet" href="css/style.css">
  <style>
    .fade-up-element { opacity: 1 !important; transform: none !important; }
  </style>
</head>
<body>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    full_html = f.read()

# Replace body contents
body_start = full_html.find('<body')
body_tag_end = full_html.find('>', body_start) + 1
body_end = full_html.rfind('</body>')
body_content = full_html[body_tag_end:body_end]

measure_script = """
<script>
window.addEventListener('load', () => {
  const sections = Array.from(document.querySelectorAll('section'));
  const results = [];
  
  sections.forEach(sec => {
    const id = sec.id;
    // Eyebrow
    const eb = sec.querySelector('[class*="eyebrow"], .contact-panel-tag');
    // Heading
    const h = sec.querySelector('h1, h2, [class*="section-title"], [class*="title"]');
    // Subtitle
    const sub = sec.querySelector('[class*="subtitle"], .contact-panel-desc, .commitment-text');
    // Content after header
    // In centered sections, the header container is usually .text-center or similar
    const headerContainer = sec.querySelector('.text-center');
    let contentEl = null;
    if (headerContainer) {
      contentEl = headerContainer.nextElementSibling;
    } else {
      // For 2-col sections
      contentEl = sec.querySelector('.row, .commitment-content-wrap');
    }
    
    const ebBox = eb ? eb.getBoundingClientRect() : null;
    const hBox = h ? h.getBoundingClientRect() : null;
    const subBox = sub ? sub.getBoundingClientRect() : null;
    const headerBox = headerContainer ? headerContainer.getBoundingClientRect() : null;
    const contentBox = contentEl ? contentEl.getBoundingClientRect() : null;
    
    results.push({
      id: id,
      eyebrowBottom: ebBox ? Math.round(ebBox.bottom) : null,
      headingTop: hBox ? Math.round(hBox.top) : null,
      headingBottom: hBox ? Math.round(hBox.bottom) : null,
      subtitleTop: subBox ? Math.round(subBox.top) : null,
      subtitleBottom: subBox ? Math.round(subBox.bottom) : null,
      gapEyebrowToHeading: (ebBox && hBox) ? Math.round(hBox.top - ebBox.bottom) : null,
      gapHeadingToSubtitle: (hBox && subBox) ? Math.round(subBox.top - hBox.bottom) : null,
      gapSubtitleToContent: (subBox && contentBox) ? Math.round(contentBox.top - subBox.bottom) : null,
      gapHeaderContainerToContent: (headerBox && contentBox) ? Math.round(contentBox.top - headerBox.bottom) : null,
      headerContainerMb: headerContainer ? window.getComputedStyle(headerContainer).marginBottom : null
    });
  });
  
  const div = document.createElement('div');
  div.id = 'measure-output';
  div.textContent = JSON.stringify(results, null, 2);
  document.body.appendChild(div);
});
</script>
"""

test_html = full_html.replace('</body>', measure_script + '\n</body>')
with open('temp_gap_measure.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_abs = os.path.abspath('temp_gap_measure.html').replace('\\', '/')
url = f"file:///{temp_abs}"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,6000",
    "--virtual-time-budget=3000",
    "--dump-dom",
    url
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
dom = res.stdout

if '<div id="measure-output">' in dom:
    start = dom.find('<div id="measure-output">') + len('<div id="measure-output">')
    end = dom.find('</div>', start)
    json_text = dom[start:end]
    print(json_text)
else:
    print("Could not find measure-output div in rendered DOM")

if os.path.exists('temp_gap_measure.html'):
    os.remove('temp_gap_measure.html')
