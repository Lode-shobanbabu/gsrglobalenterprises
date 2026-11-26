import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

open_b = css.count('{')
close_b = css.count('}')
print(f'CSS Braces: open={open_b}, close={close_b}, diff={open_b - close_b}')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

div_open = html.count('<div')
div_close = html.count('</div')
print(f'HTML Divs: open={div_open}, close={div_close}, diff={div_open - div_close}')

section_open = html.count('<section')
section_close = html.count('</section')
print(f'HTML Sections: open={section_open}, close={section_close}, diff={section_open - section_close}')

more_count = len(re.findall(r'class=[\"\']dock-card-more[\"\']', html))
print('dock-card-more count:', more_count)

print('about-eyebrow present:', 'about-eyebrow' in html)
