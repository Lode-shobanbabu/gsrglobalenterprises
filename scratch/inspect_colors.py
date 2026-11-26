from PIL import Image

src_path = r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795675948188_7896240d.webp"
img = Image.open(src_path).convert('RGBA')
pixels = img.load()
w, h = img.size

navy_samples = []
grey_samples = []
orange_samples = []

for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        if a > 200:
            if r > 180 and g > 80 and b < 80:
                orange_samples.append((r, g, b, a))
            elif b > r + 15 and b < 100:
                navy_samples.append((r, g, b, a))
            elif abs(r - g) < 15 and abs(g - b) < 15 and 80 < r < 180:
                grey_samples.append((r, g, b, a))

print("Navy samples count:", len(navy_samples), "Sample:", navy_samples[:5])
print("Orange samples count:", len(orange_samples), "Sample:", orange_samples[:5])
print("Grey samples count:", len(grey_samples), "Sample:", grey_samples[:5])
