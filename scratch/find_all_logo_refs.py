with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if any(k in l.lower() for k in ['logo', 'brand-logo', 'gsr-logo']):
        print(f"L{i+1}: {l.strip()}")
