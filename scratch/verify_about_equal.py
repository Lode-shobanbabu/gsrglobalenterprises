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
print("Small heading 'WHO WE ARE':", "WHO WE ARE" in about_part)
print("Main title 'Your Partner in Smarter Sourcing and Reliable Procurement':", "Your Partner in Smarter Sourcing and Reliable Procurement" in about_part)
print("CTA 'Know More About Our Capabilities':", "Know More About Our Capabilities" in about_part)
print("Equal media container:", "about-equal-media h-100" in about_part)
print("Equal content container:", "about-equal-content h-100" in about_part)
