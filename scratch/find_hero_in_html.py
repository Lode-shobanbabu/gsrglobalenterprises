with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[:210]):
    if 'hero-section' in l or 'about-section' in l or 'HOME' in l:
        print(f"L{i+1}: {repr(l[:60])}")
