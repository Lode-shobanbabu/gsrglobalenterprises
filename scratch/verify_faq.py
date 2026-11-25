import re, os

# Check CSS brace balance
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

open_braces = css.count('{')
close_braces = css.count('}')
print(f"CSS braces: open={open_braces}, close={close_braces}, balanced={open_braces == close_braces}")

# Check HTML tag balance
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check faq-specialist image exists
img_match = re.search(r'assets/images/faq-specialist\.[a-z]+', html)
if img_match:
    img_path = img_match.group(0)
    print(f"Found image: {img_path}, exists={os.path.exists(img_path)}")
else:
    print("No faq-specialist image found in index.html!")

# Check faq section open/close tags
div_open = html.count('<div')
div_close = html.count('</div>')
print(f"HTML divs: open={div_open}, close={div_close}, balanced={div_open == div_close}")

section_open = html.count('<section')
section_close = html.count('</section>')
print(f"HTML sections: open={section_open}, close={section_close}, balanced={section_open == section_close}")
