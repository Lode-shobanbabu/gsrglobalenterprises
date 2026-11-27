with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '.about-section' in line:
        print(f"Line {i+1}: {line.strip()}")
        for j in range(i, min(len(lines), i+80)):
            print(f"  {j+1}: {lines[j].rstrip()}")
        break
