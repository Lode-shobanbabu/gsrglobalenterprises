from PIL import Image

im = Image.open('scratch/text_name.png')
# resize to 90x14 for ascii art
small = im.resize((90, 14), Image.Resampling.BILINEAR)

w, h = small.size
chars = " .:-=+*#%@"

print("-" * 92)
for y in range(h):
    line = ""
    for x in range(w):
        a = small.getpixel((x, y))[3]
        idx = int(a / 256 * len(chars))
        idx = min(idx, len(chars) - 1)
        line += chars[idx]
    print(line)
print("-" * 92)
