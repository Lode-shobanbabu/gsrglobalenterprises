with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for j in range(2318, min(len(lines), 2360)):
    print(f"{j+1}: {lines[j]}", end='')
