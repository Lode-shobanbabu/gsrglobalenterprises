with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="about"' in line:
        print(f"Line {i+1}: {line.rstrip()}")
        for j in range(i, min(len(lines), i+80)):
            print(f"  {j+1}: {lines[j].rstrip()}")
        break
