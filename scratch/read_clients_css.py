with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '.clients-section' in line or 'E. Our Clients' in line:
        start = max(0, i - 5)
        end = min(len(lines), i + 100)
        for j in range(start, end):
            print(f"{j+1}: {lines[j]}", end='')
        break
