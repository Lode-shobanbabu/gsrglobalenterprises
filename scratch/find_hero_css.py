with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '.hero-section' in line:
        print(f"Line {i+1}: {line.strip()}")
        for j in range(max(0, i-2), min(len(lines), i+35)):
            print(f"  {j+1}: {lines[j].rstrip()}")
        print("="*40)
        break
