from PIL import Image

ref = Image.open(r'C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795602918218_ab4796e1.jpg')

# Let's crop x=10..100, y=10..60 and check non-background pixels
for y in range(15, 55):
    for x in range(15, 100):
        p = ref.getpixel((x, y))[:3]
        # if not background (242, 241, 246)
        if abs(p[0] - 242) + abs(p[1] - 241) + abs(p[2] - 246) > 40:
            print(f"Non-bg at ({x},{y}): RGB{p} -> #{p[0]:02x}{p[1]:02x}{p[2]:02x}")
