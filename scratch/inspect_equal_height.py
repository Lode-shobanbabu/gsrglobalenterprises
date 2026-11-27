from PIL import Image

img = Image.open('scratch/about_equal_crop.png')
print("Crop dimensions:", img.size)
w, h = img.size

# Let's find the bounds of the image (left side: x from 0 to w//2)
# The image has rich colors, not white background (#ffffff)
img_y_pixels = []
for y in range(h):
    # sample at x=250 (inside left column)
    p = img.getpixel((250, y))
    if p[0] < 240 or p[1] < 240 or p[2] < 240:
        img_y_pixels.append(y)

if img_y_pixels:
    print(f"Left Image vertical span: y={min(img_y_pixels)} to y={max(img_y_pixels)} (height: {max(img_y_pixels) - min(img_y_pixels)}px)")

# Let's find the bounds of right content (right side: x from w//2 to w)
text_y_pixels = []
for y in range(h):
    # check if any non-white pixel in x from 750 to 1250
    has_content = False
    for x in range(750, 1250, 10):
        p = img.getpixel((x, y))
        if p[0] < 240 or p[1] < 240 or p[2] < 240:
            has_content = True
            break
    if has_content:
        text_y_pixels.append(y)

if text_y_pixels:
    print(f"Right Content vertical span: y={min(text_y_pixels)} to y={max(text_y_pixels)} (height: {max(text_y_pixels) - min(text_y_pixels)}px)")
