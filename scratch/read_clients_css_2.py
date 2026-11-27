with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for j in range(1460, min(len(lines), 1510)):
    print(f"{j+1}: {lines[j]}", end='')
