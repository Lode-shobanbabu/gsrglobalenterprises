from PIL import Image

im = Image.open('assets/images/gsr-logo.jpg')
w, h = im.size

min_x, max_x = w, 0
min_y, max_y = h, 0

for y in range(h):
    for x in range(w):
        r, g, b = im.getpixel((x, y))
        if r < 240 or g < 240 or b < 240:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

print(f"Content bbox in gsr-logo.jpg: X=[{min_x}..{max_x}] (w={max_x-min_x+1}), Y=[{min_y}..{max_y}] (h={max_y-min_y+1})")
