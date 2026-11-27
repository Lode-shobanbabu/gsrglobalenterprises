with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if any(k in line for k in [
        '.hero-main-title {',
        '.about-ref-title {',
        '.services-section-title {',
        '.industries-section-title {',
        '.why-section-title {',
        '.clients-section-title {',
        '.process-section-title {',
        '.commitment-title {',
        '.contact-panel-title {',
        '.quote-card-title {'
    ]):
        start = max(0, idx - 1)
        end = min(len(lines), idx + 15)
        print(f"--- Line {idx+1} ---")
        print(''.join(lines[start:end]))
