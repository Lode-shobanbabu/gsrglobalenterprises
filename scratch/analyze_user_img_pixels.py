from PIL import Image

im = Image.open(r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\.user_uploaded\media_1795782454230_42e164c9.png").convert('RGB')
w, h = im.size

non_white_rows = []
for y in range(h):
    is_non_white = False
    for x in range(w):
        r, g, b = im.getpixel((x, y))
        if r < 240 or g < 240 or b < 240:
            is_non_white = True
            break
    if is_non_white:
        non_white_rows.append(y)

print(f"Total height: {h}")
print(f"First non-white row: {non_white_rows[0]}")
print(f"Last non-white row: {non_white_rows[-1]}")

white_bands = []
in_white = False
start = 0
for y in range(h):
    if y not in non_white_rows:
        if not in_white:
            in_white = True
            start = y
    else:
        if in_white:
            in_white = False
            white_bands.append((start, y - 1, y - start))
if in_white:
    white_bands.append((start, h - 1, h - start))

print("White bands (start, end, height):")
for b in white_bands:
    print(f"  Rows {b[0]} to {b[1]}: height = {b[2]}px")
