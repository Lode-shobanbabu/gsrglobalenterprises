with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[:170]):
    if '<nav' in line or '<header' in line or 'nav-link' in line or 'navbar' in line:
        print(f"{i+1}: {line.rstrip()}")
