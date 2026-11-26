# scratch/verify_about_exact.py

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

user_text = "From medical equipment and IT infrastructure to industrial materials, automotive components and renewable energy solutions, GSR Global Enterprises delivers reliable procurement and supply services tailored to diverse industry requirements."

print("User exact text in HTML:", user_text in html or "From medical equipment and IT infrastructure to industrial materials, automotive components and renewable energy solutions" in html)
print("Mission in HTML:", "mission" in html.lower())
print("Vision in HTML:", "vision" in html.lower())
print("About section exists:", 'id="about"' in html)

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

open_b = css.count('{')
close_b = css.count('}')
print(f'CSS Braces: {open_b} open, {close_b} close (Balanced: {open_b == close_b})')
