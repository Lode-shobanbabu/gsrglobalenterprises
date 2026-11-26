with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

open_b = css.count('{')
close_b = css.count('}')
print(f'CSS Braces: {open_b} open, {close_b} close (Balanced: {open_b == close_b})')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("About section exists in HTML:", 'id="about"' in html)
print("about-corp-media-wrap in HTML:", 'about-corp-media-wrap' in html)
print("about-corp-title in HTML:", 'about-corp-title' in html)
print("about-corp-stats-bar in HTML:", 'about-corp-stats-bar' in html)
print("about-ref in HTML:", 'about-ref' in html)
print("about-ref in CSS:", 'about-ref' in css)
