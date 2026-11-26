with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '<section' in l or 'class="section-' in l:
        print(f"L{i+1}: {l.strip()[:90]}")
