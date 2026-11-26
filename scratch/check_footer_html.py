with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'footer-brand' in l or 'footer-logo' in l or 'gsr-logo-official-white' in l:
        print(f"L{i+1}: {l.strip()}")
