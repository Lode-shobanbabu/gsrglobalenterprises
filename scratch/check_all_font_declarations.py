with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

for i, line in enumerate(css.splitlines()):
    if '--font' in line or ('font-family' in line and not 'var(--font' in line):
        print(f"Line {i+1}: {line.strip()}")
