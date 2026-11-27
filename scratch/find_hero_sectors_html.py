with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="hero"' in line or 'id="sectors"' in line or 'class="hero-dock' in line:
        print(f"Line {i+1}: {line.rstrip()}")
        for j in range(max(0, i-2), min(len(lines), i+30)):
            print(f"  {j+1}: {lines[j].rstrip()}")
        print("="*40)
