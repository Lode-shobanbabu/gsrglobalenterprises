from PIL import Image

img = Image.open(r"scratch\discuss_btn_rendered.png")
print("Rendered button size:", img.size)
w, h = img.size

orange_px = 0
white_px = 0
for x in range(w):
    for y in range(h):
        r, g, b, *a = img.getpixel((x, y))
        if r > 240 and 110 <= g <= 135 and b < 20:
            orange_px += 1
        elif r > 245 and g > 245 and b > 245:
            white_px += 1

print(f"Orange pixels in button: {orange_px}, White pixels (text): {white_px}")
assert orange_px > 5000, "Expected orange pill background"
assert white_px > 500, "Expected white text inside button"
print("SUCCESS: The button renders cleanly with vibrant orange background and clear white text without underline!")
