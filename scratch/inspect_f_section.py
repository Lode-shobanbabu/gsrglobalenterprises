with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for j in range(2140, min(len(lines), 2320)):
    if 'G. Contact' in lines[j] or 'contact-quote-section' in lines[j]:
        print(f"Reached G at line {j+1}")
        break
    if j < 2185 or j > 2290:
        print(f"{j+1}: {lines[j]}", end='')
