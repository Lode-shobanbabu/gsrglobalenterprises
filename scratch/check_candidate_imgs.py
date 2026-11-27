from PIL import Image

for name in ['about-procurement-facility.webp', 'about-warehouse-logistics.webp', 'hero-logistics-global.webp', 'hero-procurement.webp', 'about-corporate-team-meeting.webp']:
    path = f'assets/images/{name}'
    try:
        im = Image.open(path)
        print(f"{name}: size={im.size}, mode={im.mode}")
    except Exception as e:
        print(f"Error {name}: {e}")
