from PIL import Image

for name in ["hero-corporate-meeting.webp", "hero-boardroom.webp", "hero-executives.webp", "about-warehouse-logistics.webp"]:
    im = Image.open(f"assets/images/{name}")
    print(f"{name}: {im.size}, {im.mode}")
