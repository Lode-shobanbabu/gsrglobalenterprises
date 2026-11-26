# scratch/verify_services.py

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()
open_b = css.count('{')
close_b = css.count('}')
print(f'CSS Braces: {open_b} open, {close_b} close (Balanced: {open_b == close_b})')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('Services section present:', 'id="services"' in html)
print('Card 1 present:', 'Medical &amp; Healthcare Supplies' in html or 'Medical & Healthcare Supplies' in html)
print('Card 2 present:', 'GCC &amp; IT Infrastructure' in html or 'GCC & IT Infrastructure' in html)
print('Card 3 present:', 'Government &amp; Education Projects' in html or 'Government & Education Projects' in html)
print('Card 4 present:', 'Industrial &amp; Manufacturing Supplies' in html or 'Industrial & Manufacturing Supplies' in html)
print('Card 5 present:', 'Automobile &amp; Transportation Supplies' in html or 'Automobile & Transportation Supplies' in html)
print('Carousel tracks/buttons in html:', 'services-carousel-track' in html or 'services-prev-btn' in html)

# Check modal trigger selectors in js/script.js
with open('js/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

print('script.js has btn-pro-readmore:', 'btn-pro-readmore' in js or 'data-service-key' in js)
