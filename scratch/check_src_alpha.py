from PIL import Image

src_path = r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795675948188_7896240d.webp"
img = Image.open(src_path).convert('RGBA')
print("Original at (10, 70):", img.getpixel((10, 70)))
print("Original at (0, 0):", img.getpixel((0, 0)))
print("Original at (5, 5):", img.getpixel((5, 5)))
print("Original min/max alpha:", img.getextrema()[3])
