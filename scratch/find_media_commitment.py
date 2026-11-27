with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '.commitment-mockup-section' in line and i > 2500:
        print(f"Line {i+1}: {line.strip()}")
        for j in range(max(0, i-5), min(len(lines), i+15)):
            print(f"{j+1}: {lines[j]}", end='')
