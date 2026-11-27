from PIL import Image

img = Image.open('scratch/right_content_test.png')
w, h = img.size

# Find the very first row with non-white pixels
first_y = None
last_y = None
for y in range(h):
    row_pixels = [img.getpixel((x, y)) for x in range(0, w, 5)]
    if any(p != (255, 255, 255) for p in row_pixels):
        if first_y is None:
            first_y = y
        last_y = y

print(f"Right content active Y range in crop: {first_y} to {last_y} (offset +50 = {first_y + 50} to {last_y + 50})")

# Sample pixels around first_y
if first_y is not None:
    for x in range(0, 200, 20):
        print(f"x={x}, y={first_y}: {img.getpixel((x, first_y))}")
