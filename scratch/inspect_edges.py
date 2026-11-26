from PIL import Image

src_path = r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795675948188_7896240d.webp"
img = Image.open(src_path).convert('RGBA')
w, h = img.size
pixels = img.load()

# Let's inspect edges and colors
semitrans = []
for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        if 0 < a < 255:
            semitrans.append((r, g, b, a))

print(f"Total semi-transparent pixels: {len(semitrans)}")
if semitrans:
    print("Sample semi-transparent pixels:", semitrans[:15])

# Also check fully opaque pixels: what are the background pixels?
transparent_count = sum(1 for y in range(h) for x in range(w) if pixels[x, y][3] == 0)
opaque_count = sum(1 for y in range(h) for x in range(w) if pixels[x, y][3] == 255)
print(f"Total pixels: {w*h}, Transparent: {transparent_count}, Semi-trans: {len(semitrans)}, Opaque: {opaque_count}")
