from PIL import Image

img = Image.open(r"scratch\chevrons_crop.png")
w, h = img.size
print("Crop size:", w, h)

# Check if there is any black outline or text stroke in the crop around orange pixels
black_stroke_px = []
for x in range(w):
    for y in range(h):
        r, g, b, *a = img.getpixel((x, y))
        # If dark black (r < 30, g < 30, b < 30) near an orange pixel
        if r < 30 and g < 30 and b < 30:
            black_stroke_px.append((x, y))

print("Dark black text/border pixels in crop:", len(black_stroke_px))
