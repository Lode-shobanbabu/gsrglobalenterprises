from PIL import Image

im = Image.open('scratch/emblem_orig.png')
print("Emblem orig size:", im.size)

# Find bounding box of content inside emblem_orig
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

print(f"Emblem bbox: X=[{min_x}..{max_x}] (w={max_x-min_x+1}), Y=[{min_y}..{max_y}] (h={max_y-min_y+1})")
crop_emblem = im.crop((min_x, min_y, max_x + 1, max_y + 1))
crop_emblem.save('scratch/emblem_tight.png')
print(f"Saved scratch/emblem_tight.png of size {crop_emblem.size}")
