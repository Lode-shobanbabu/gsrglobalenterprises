with open('js/script.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for j in range(max(0, len(lines) - 40), len(lines)):
    print(f"{j+1}: {lines[j]}", end='')
