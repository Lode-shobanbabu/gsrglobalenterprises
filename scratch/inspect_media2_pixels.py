from PIL import Image

img = Image.open(r'C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795772783976_42f6c95f.png')
w, h = img.size
non_white = []
for y in range(h):
    for x in range(w):
        p = img.getpixel((x, y))
        if p[0] < 200 or p[1] < 200 or p[2] < 200:
            non_white.append((x, y, p))

print("Total non-white pixels in media 2:", len(non_white))
if non_white:
    print("Sample:", non_white[len(non_white)//2])
