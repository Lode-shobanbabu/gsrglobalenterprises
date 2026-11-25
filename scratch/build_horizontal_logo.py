from PIL import Image, ImageDraw, ImageFont

# Load cropped high-res parts
emblem = Image.open('scratch/emblem_white_transparent.png') # 784 x 386
text_name = Image.open('scratch/text_name.png') # 930 x 64
text_tag = Image.open('scratch/tagline_orig.png') # 930 x 37

# Let's clean text_name and text_tag to make them bright white and bright gold
# In text_orig (which has white background and dark navy text):
im_text_orig = Image.open('scratch/text_orig.png')
w_t, h_t = im_text_orig.size
clean_name = Image.new('RGBA', (w_t, h_t), (0, 0, 0, 0))
for y in range(h_t):
    for x in range(w_t):
        r, g, b = im_text_orig.getpixel((x, y))
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        if lum < 220:
            # Alpha based on darkness
            alpha = int(255 * (1.0 - (lum / 220.0)))
            clean_name.putpixel((x, y), (255, 255, 255, min(255, int(alpha * 1.3))))

# Crop clean_name tightly
bbox_name = clean_name.getbbox()
clean_name = clean_name.crop(bbox_name)
print("Clean name tight size:", clean_name.size)

# Clean tagline
im_tag_orig = Image.open('scratch/tagline_orig.png')
w_tg, h_tg = im_tag_orig.size
clean_tag = Image.new('RGBA', (w_tg, h_tg), (0, 0, 0, 0))
# Let's use gold #f1811b / #e5a93c
for y in range(h_tg):
    for x in range(w_tg):
        r, g, b = im_tag_orig.getpixel((x, y))
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        if lum < 220:
            alpha = int(255 * (1.0 - (lum / 220.0)))
            # Amber gold color: RGB (241, 145, 45)
            clean_tag.putpixel((x, y), (241, 150, 48, min(255, int(alpha * 1.4))))

bbox_tag = clean_tag.getbbox()
clean_tag = clean_tag.crop(bbox_tag)
print("Clean tag tight size:", clean_tag.size)

# Emblem tight
bbox_emb = emblem.getbbox()
clean_emb = emblem.crop(bbox_emb)
print("Clean emblem tight size:", clean_emb.size)

# Now, let's create a horizontal layout at 2x retina resolution!
# Target canvas height = 140px (which renders at 70px height in browser)
# Emblem height: 130px. Aspect ratio of emblem is 784 / 386 = 2.03.
# So emblem width = 130 * 2.03 = 264px.
target_emb_h = 130
target_emb_w = int(clean_emb.size[0] * (target_emb_h / clean_emb.size[1]))
scaled_emb = clean_emb.resize((target_emb_w, target_emb_h), Image.Resampling.LANCZOS)

# Now text:
# In the horizontal layout beside the emblem:
# We want "GSR GLOBAL ENTERPRISES" to be prominent!
# Height of name: ~56px (renders at 28px in browser).
target_name_h = 56
target_name_w = int(clean_name.size[0] * (target_name_h / clean_name.size[1]))
scaled_name = clean_name.resize((target_name_w, target_name_h), Image.Resampling.LANCZOS)

# Height of tagline: ~26px (renders at 13px in browser).
target_tag_h = 24
target_tag_w = int(clean_tag.size[0] * (target_tag_h / clean_tag.size[1]))
scaled_tag = clean_tag.resize((target_tag_w, target_tag_h), Image.Resampling.LANCZOS)

gap = 36 # gap between emblem and text
margin_x = 10
margin_y = 10

total_w = margin_x * 2 + target_emb_w + gap + max(target_name_w, target_tag_w)
total_h = 140

canvas = Image.new('RGBA', (total_w, total_h), (0, 0, 0, 0))

# Paste emblem vertically centered
emb_y = (total_h - target_emb_h) // 2
canvas.paste(scaled_emb, (margin_x, emb_y), scaled_emb)

# Paste name and tagline
text_x = margin_x + target_emb_w + gap
text_block_h = target_name_h + 12 + target_tag_h
start_text_y = (total_h - text_block_h) // 2

canvas.paste(scaled_name, (text_x, start_text_y), scaled_name)
canvas.paste(scaled_tag, (text_x, start_text_y + target_name_h + 12), scaled_tag)

print(f"Generated horizontal canvas: {total_w} x {total_h}")
canvas.save('assets/images/gsr-logo-horizontal.png')
canvas.save('assets/images/gsr-logo-horizontal.webp', quality=95)

# Also save standalone emblem
scaled_emb.save('assets/images/gsr-emblem-white.webp', quality=95)
scaled_emb.save('assets/images/gsr-emblem-white.png')

print("Saved assets/images/gsr-logo-horizontal.png and .webp!")
