with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '.nav-link' in line or '.navbar-nav' in line or 'header' in line and '{' in line:
        print(f"Line {i+1}: {line.rstrip()}")
        for j in range(max(0, i-1), min(len(lines), i+15)):
            print(f"  {j+1}: {lines[j].rstrip()}")
        print("="*40)
