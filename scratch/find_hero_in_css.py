with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[:600]):
    if 'Hero Section' in l or 'About Section' in l or 'about-section' in l:
        print(f"L{i+1}: {repr(l[:60])}")
