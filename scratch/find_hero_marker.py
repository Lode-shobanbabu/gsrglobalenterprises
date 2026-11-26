with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[:450]):
    if '/* =====' in l or 'HERO' in l or 'hero-section' in l:
        print(f"L{i+1}: {l.strip()[:80]}")
