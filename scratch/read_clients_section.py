with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="clients"' in line or 'class="clients-section"' in line:
        start = max(0, i - 5)
        end = min(len(lines), i + 75)
        for j in range(start, end):
            print(f"{j+1}: {lines[j]}", end='')
        break
