with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for j in range(2350, min(len(lines), 2600)):
    if '/* ==========================================================================' in lines[j] and 'G.' in lines[j+1]:
        print(f"Section F ends before line {j+1}")
        break
