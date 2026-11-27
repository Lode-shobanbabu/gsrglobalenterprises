with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'about' in line.lower() and ('btn' in line.lower() or 'capabilities' in line.lower() or 'know more' in line.lower()):
        print(f"HTML Line {i+1}: {line.strip()}")
        for j in range(max(0, i-3), min(len(lines), i+6)):
            print(f"  {j+1}: {lines[j].rstrip()}")
        print("="*40)

with open('css/style.css', 'r', encoding='utf-8') as f:
    css_lines = f.readlines()

for i, line in enumerate(css_lines):
    if 'capabilities' in line.lower() or ('about' in line.lower() and 'btn' in line.lower()):
        print(f"CSS Line {i+1}: {line.strip()}")
        for j in range(max(0, i-2), min(len(css_lines), i+15)):
            print(f"  {j+1}: {css_lines[j].rstrip()}")
        print("="*40)
