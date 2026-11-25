from PIL import Image

im = Image.open('scratch/text_name.png')
w, h = im.size
print(f"text_name size: {w} x {h}")

# Find blank columns
col_pixels = []
for x in range(w):
    count = sum(1 for y in range(h) if im.getpixel((x, y))[3] > 30)
    col_pixels.append(count)

spaces = []
current_space = None
for x, c in enumerate(col_pixels):
    if c == 0:
        if current_space is None:
            current_space = [x, x]
        else:
            current_space[1] = x
    else:
        if current_space is not None:
            spaces.append(current_space)
            current_space = None
if current_space is not None:
    spaces.append(current_space)

print("Spaces found:")
for s in spaces:
    if s[1] - s[0] >= 5: # significant spaces
        print(f"  Range [{s[0]}..{s[1]}], width={s[1]-s[0]+1}")
