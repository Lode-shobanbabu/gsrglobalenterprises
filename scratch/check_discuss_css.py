with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '.services-discuss-btn' in line:
        for j in range(max(0, i-5), min(len(lines), i+35)):
            print(f"{j+1}: {lines[j].rstrip()}")
        break
