import os
from PIL import Image

for name in [
    "about-warehouse-logistics.webp",
    "about-steel-infrastructure.webp",
    "about-hospital-facility.webp",
    "service-pro-industrial.webp",
    "service-pro-medical.webp"
]:
    p = os.path.join("assets", "images", name)
    if os.path.exists(p):
        im = Image.open(p)
        print(f"{name}: {im.size}, {im.mode}")
