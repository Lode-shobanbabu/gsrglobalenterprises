# scratch/verify_new_about.py

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

print("About section exists:", s_idx != -1)
print("Laptop or meeting images in about:", "meeting" in about_part or "laptop" in about_part)
print("User exact text in about:", "From medical equipment and IT infrastructure to industrial materials, automotive components and renewable energy solutions" in about_part)
print("Sectors panel in about:", "about-corp-sectors-panel" in about_part)
