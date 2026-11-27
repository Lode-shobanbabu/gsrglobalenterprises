from PIL import Image

for name in ['hero-procurement.webp', 'about-procurement-facility.webp', 'about-steel-infrastructure.webp']:
    im = Image.open(f'assets/images/{name}')
    print(f"{name}: size={im.size}, aspect_ratio={im.width/im.height:.2f}")
