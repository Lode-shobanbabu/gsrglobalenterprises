with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="services"' in line:
        for j in range(i, min(len(lines), i+180)):
            print(f"{j+1}: {lines[j].rstrip()}")
        break
