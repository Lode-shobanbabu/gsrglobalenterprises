from PIL import Image

path = r'C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795602424527_c9d3202d.png'
im = Image.open(path)
w, h = im.size

min_x, max_x = w, 0
min_y, max_y = h, 0

for y in range(h):
    for x in range(w):
        a = im.getpixel((x, y))[3]
        if a > 20:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

print(f"Actual content bounding box: X=[{min_x}..{max_x}] (w={max_x-min_x+1}), Y=[{min_y}..{max_y}] (h={max_y-min_y+1})")
crop_tight = im.crop((min_x, min_y, max_x + 1, max_y + 1))
print("Crop tight size:", crop_tight.size)
crop_tight.save('scratch/logo_actual_tight.png')
