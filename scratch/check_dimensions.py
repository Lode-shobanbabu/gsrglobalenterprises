import os
from PIL import Image

for i in range(1, 6):
    names = [
        "service-pro-medical.webp",
        "service-pro-it.webp",
        "service-pro-education.webp",
        "service-pro-industrial.webp",
        "service-pro-automotive.webp"
    ]
    p = os.path.join("assets", "images", names[i-1])
    im = Image.open(p)
    print(f"{names[i-1]}: {im.size} px, {os.path.getsize(p) // 1024} KB")
