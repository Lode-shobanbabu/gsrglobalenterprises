import os
from PIL import Image

for name in [
    "hero-corporate-team.jpg",
    "hero-corporate-meeting.webp",
    "hero-boardroom.webp",
    "hero-executives.webp"
]:
    p = os.path.join("assets", "images", name)
    if os.path.exists(p):
        im = Image.open(p)
        print(f"{name}: {im.size}, {im.mode}")
