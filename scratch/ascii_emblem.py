from PIL import Image

im = Image.open('scratch/emblem_white_transparent.png')
# resize to 80x30 for ascii art
small = im.resize((80, 30), Image.Resampling.BILINEAR)

w, h = small.size
chars = " .:-=+*#%@"

print("-" * 82)
for y in range(h):
    line = ""
    for x in range(w):
        a = small.getpixel((x, y))[3]
        idx = int(a / 256 * len(chars))
        idx = min(idx, len(chars) - 1)
        line += chars[idx]
    print(line)
print("-" * 82)
