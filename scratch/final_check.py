import shutil
import re

shutil.copyfile(r"scratch\about_equal_height_perfect.png", r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\about_equal_height_perfect.png")
print("Copied preview image to brain.")

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

open_b = css.count('{')
close_b = css.count('}')
print(f"CSS Braces: {open_b} open, {close_b} close (diff = {open_b - close_b})")
assert open_b == close_b

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

div_o = len(re.findall(r'<div\b', html))
div_c = html.count('</div>')
sec_o = len(re.findall(r'<section\b', html))
sec_c = html.count('</section>')
print(f"HTML <div>: {div_o} vs {div_c} (diff = {div_o - div_c})")
print(f"HTML <section>: {sec_o} vs {sec_c} (diff = {sec_o - sec_c})")
assert div_o == div_c
assert sec_o == sec_c

sections = re.findall(r'<section[^>]+id=[\"\']([^\"\']+)[\"\']', html)
expected = ['hero', 'sectors', 'about', 'services', 'Industries', 'why-us', 'clients', 'process', 'commitment', 'contact']
print(f"HTML Sections: {sections}")
assert sections == expected
print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY!")
