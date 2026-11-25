from PIL import Image

im = Image.open('assets/images/gsr-logo.png')
print("gsr-logo.png format:", im.format, "size:", im.size, "mode:", im.mode)

# Check colors in text region Y=[407..470]
colors = set()
for y in range(407, 471):
    for x in range(9, 939):
        colors.add(im.getpixel((x, y)))

print("Number of distinct colors in text area:", len(colors))
# Find non-white/non-black dominant colors
from collections import Counter
c = Counter()
for y in range(407, 471):
    for x in range(9, 939):
        c[im.getpixel((x, y))] += 1

print("Top 10 most common colors in text area:")
for col, cnt in c.most_common(10):
    print(f"  {col}: {cnt}")
