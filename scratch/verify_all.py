with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('=== CSS VALIDATION ===')
open_b = css.count('{')
close_b = css.count('}')
print(f'CSS Braces: {open_b} open, {close_b} close (Balanced: {open_b == close_b})')

print('\n=== HTML VALIDATION ===')
for tag in ['div', 'section', 'span', 'h2', 'h3', 'p']:
    o = html.count(f'<{tag}')
    c = html.count(f'</{tag}>')
    print(f'<{tag}>: {o} open, {c} close (Balanced: {o == c})')

print('\n=== SECTION 8 DATA VERIFICATION ===')
proc_idx = html.find('id="process"')
comm_idx = html.find('id="commitment"')
proc_html = html[proc_idx:comm_idx]

checks = [
    'HOW WE WORK',
    'A Straightforward Approach to Reliable Procurement',
    'We make the procurement process easier through structured coordination and a clear understanding of your requirements.',
    'STEP 01',
    'Understand Your Requirements',
    'We understand your product specifications, quantities, budget expectations and project needs.',
    'STEP 02',
    'Source the Right Products',
    'We coordinate sourcing based on your technical, commercial and quality requirements.',
    'STEP 03',
    'Coordinate Procurement',
    'We coordinate quotations, product details, availability and procurement arrangements.',
    'STEP 04',
    'Support Supply & Delivery',
    'We coordinate supply arrangements to support your purchasing and project timelines.',
    'about-procurement-facility.webp'
]

for c in checks:
    status = 'PASS' if c in proc_html else 'FAIL'
    print(f'[{status}] {c[:50]}...')

print('Section 8 <p> open:', proc_html.count('<p'))
print('Section 8 </p> close:', proc_html.count('</p>'))

clean_proc = ' '.join(proc_html.split())
print("Clean subtitle match:", 'We make the procurement process easier through structured coordination and a clear understanding of your requirements.' in clean_proc)
print("Clean Support Supply & Delivery match:", 'Support Supply &amp; Delivery' in clean_proc)
import re
section_ids = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', html)
print('Section count:', len(section_ids))
print('Sections:', section_ids)
