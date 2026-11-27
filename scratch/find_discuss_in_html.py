with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'services-discuss-btn' in line or 'services-bottom-cta' in line:
        for j in range(max(0, i-5), min(len(lines), i+15)):
            print(f"{j+1}: {lines[j].rstrip()}")
        break
