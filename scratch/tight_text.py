from PIL import Image

# Let's check text_orig.png which is the original text from gsr-logo.png
im_text = Image.open('scratch/text_orig.png')
print("im_text size:", im_text.size)

# Find content bbox in text_orig
w, h = im_text.size
min_x, max_x = w, 0
min_y, max_y = h, 0

for y in range(h):
    for x in range(w):
        r, g, b = im_text.getpixel((x, y))
        if r < 240 or g < 240 or b < 240:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

print(f"Text orig bbox: X=[{min_x}..{max_x}] (w={max_x-min_x+1}), Y=[{min_y}..{max_y}] (h={max_y-min_y+1})")

# Let's crop it tightly
text_tight = im_text.crop((min_x, min_y, max_x + 1, max_y + 1))
print("text_tight size:", text_tight.size)

# Check tagline bbox as well
im_tag = Image.open('scratch/tagline_orig.png')
w, h = im_tag.size
min_x, max_x = w, 0
min_y, max_y = h, 0
for y in range(h):
    for x in range(w):
        r, g, b = im_tag.getpixel((x, y))
        if r < 240 or g < 240 or b < 240:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

tag_tight = im_tag.crop((min_x, min_y, max_x + 1, max_y + 1))
print(f"Tagline tight size: {tag_tight.size}")
