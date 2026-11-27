with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(105, 145):
    print(f"{i+1}: {lines[i].rstrip()}")
