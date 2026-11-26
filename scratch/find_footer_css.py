with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'footer-logo-img' in l:
        print(f"L{i+1}:")
        print(''.join(lines[i:i+20]))
        break
