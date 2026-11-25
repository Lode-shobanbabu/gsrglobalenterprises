from PIL import Image

ref = Image.open(r'C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795602918218_ab4796e1.jpg')
w, h = ref.size

# Let's inspect background color around (10, 10)
bg = ref.getpixel((10, 10))
print("Page background color:", bg)

# The photo has dark pixels (r < 100, g < 100, b < 100)
min_x, max_x = w, 0
min_y, max_y = h, 0

for y in range(160, h):
    for x in range(10, 500):
        p = ref.getpixel((x, y))
        diff = abs(p[0] - bg[0]) + abs(p[1] - bg[1]) + abs(p[2] - bg[2])
        if diff > 40:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

print(f"Photo bbox in ref: X=[{min_x}..{max_x}] (w={max_x-min_x+1}), Y=[{min_y}..{max_y}] (h={max_y-min_y+1})")
photo = ref.crop((min_x, min_y, max_x + 1, max_y + 1))
photo.save('assets/images/faq-specialist.jpg')
photo.save('assets/images/faq-specialist.webp', quality=95)
print("Saved assets/images/faq-specialist.webp!")
