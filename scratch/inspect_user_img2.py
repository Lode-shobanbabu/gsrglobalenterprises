from PIL import Image

img = Image.open(r'C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795772783976_42f6c95f.png')
print("Image size:", img.size)
print("Color samples:")
w, h = img.size
for y in range(0, h, 5):
    for x in range(0, w, 20):
        p = img.getpixel((x, y))
        if p != (255, 255, 255):
            print(f"({x}, {y}): {p}")
            break
