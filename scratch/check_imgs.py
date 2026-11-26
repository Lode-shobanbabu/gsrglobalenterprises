import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

s_idx = html.find('id="services"')
c_idx = html.find('id="clients"')
sec = html[s_idx:c_idx]

imgs = re.findall(r'<img\s+src="([^"]+)"', sec)
for i, img in enumerate(imgs, 1):
    print(f'Card {i} img:', img)
