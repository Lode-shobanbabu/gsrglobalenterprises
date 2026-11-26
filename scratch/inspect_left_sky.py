from PIL import Image

img = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795677832868_afa5e5b5.jpg")
w, h = img.size

# Let's inspect rows at x=20, x=50, x=100
for y in range(0, h, 20):
    p = img.getpixel((20, y))
    p2 = img.getpixel((300, y))
    print(f"y={y:3d} | (20, y)={p} | (300, y)={p2}")
