from PIL import Image

for name in ["about-warehouse-logistics.webp", "about-medical.webp", "about-steel.webp", "about-solar.webp", "hero-corporate-meeting.webp"]:
    try:
        im = Image.open(f"assets/images/{name}")
        print(f"{name}: {im.size}, {im.mode}")
    except Exception as e:
        print(f"{name}: {e}")
