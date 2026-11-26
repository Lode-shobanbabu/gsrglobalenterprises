with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

open_b = css.count('{')
close_b = css.count('}')
print(f'CSS Braces: {open_b} open, {close_b} close (Balanced: {open_b == close_b})')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

s_idx = html.find('id="about"')
c_idx = html.find('id="services"')
about_part = html[s_idx:c_idx]

print("align-items-center in about:", "align-items-center" in about_part)
print("about-corporate-team.webp in about:", "about-corporate-team.webp" in about_part)
print("h-100 on image container:", "about-equal-media h-100" in about_part)
