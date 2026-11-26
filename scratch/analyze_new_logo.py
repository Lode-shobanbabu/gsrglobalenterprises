import os
from PIL import Image

src_path = r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795675948188_7896240d.webp"
img = Image.open(src_path)
print("Format:", img.format)
print("Mode:", img.mode)
print("Size:", img.size)

# Check alpha channel bounding box
if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
    alpha = img.convert('RGBA').split()[-1]
    bbox = alpha.getbbox()
    print("Non-transparent bbox:", bbox)
else:
    print("No alpha channel directly")
