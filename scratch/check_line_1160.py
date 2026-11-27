with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(max(0, 1140), min(len(lines), 1180)):
    print(f"{i+1}: {lines[i].rstrip()}")
