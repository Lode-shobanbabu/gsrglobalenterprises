# scratch/verify_testimonials_cleanup.py

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

open_b = css.count('{')
close_b = css.count('}')
print(f'CSS Braces: {open_b} open, {close_b} close (Balanced: {open_b == close_b})')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
print("Testimonial in HTML:", "testimonial" in html.lower())

with open('js/script.js', 'r', encoding='utf-8') as f:
    js = f.read()
print("Testimonial in JS:", "testimonial" in js.lower())

print("Testimonial in CSS:", "testimonial" in css.lower())
print("Coverflow in CSS:", "coverflow" in css.lower())
print("Coverflow in JS:", "coverflow" in js.lower())
