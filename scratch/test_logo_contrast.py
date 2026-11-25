from PIL import Image

path = r'C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795602424527_c9d3202d.png'
im = Image.open(path)

# Crop to tight bounding box
bbox = im.getbbox()
im_tight = im.crop(bbox)
print("Tight size:", im_tight.size)

# Let's save a copy on dark background (#020612) to see how it looks
bg = Image.new('RGBA', (im_tight.size[0] + 60, im_tight.size[1] + 60), (2, 6, 18, 255))
bg.paste(im_tight, (30, 30), im_tight)
bg.save('scratch/logo_on_dark_raw.png')

# Let's analyze pixel colors: what are the navy colors?
colors = set()
for y in range(im_tight.size[1]):
    for x in range(im_tight.size[0]):
        r, g, b, a = im_tight.getpixel((x, y))
        if a > 100:
            colors.add((r, g, b))

print(f"Total non-transparent colors: {len(colors)}")
# Find most common dark colors
from collections import Counter
c = Counter()
for y in range(im_tight.size[1]):
    for x in range(im_tight.size[0]):
        r, g, b, a = im_tight.getpixel((x, y))
        if a > 150:
            c[(r, g, b)] += 1

print("Top 10 dominant colors:")
for col, cnt in c.most_common(10):
    print(f"  RGB{col}: {cnt} pixels")
