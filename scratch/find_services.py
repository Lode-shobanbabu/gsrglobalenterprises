# find_services.py
with open('index.html', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 'id="services"' in line or 'SERVICES' in line:
            print(f'{i}: {line.strip()[:80]}')
