with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[:350]):
    if 'navbar' in line or 'brand-logo' in line:
        print(f"L{i+1}: {line.strip()[:80]}")
