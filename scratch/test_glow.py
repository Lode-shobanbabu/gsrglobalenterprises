from PIL import Image, ImageFilter

orig = Image.open('assets/images/gsr-logo.png') # 919 x 470, RGBA
w, h = orig.size

# Let's create a version of the original logo with a soft bright rim/glow for dark backgrounds:
# 1. Extract alpha mask
alpha = orig.split()[3]
# 2. Expand/dilate alpha mask to create a soft white backlight glow
glow_mask = alpha.filter(ImageFilter.GaussianBlur(radius=4))

# Create white glow image
glow_im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
for y in range(h):
    for x in range(w):
        a = glow_mask.getpixel((x, y))
        if a > 15:
            # Subtle white glow
            glow_im.putpixel((x, y), (255, 255, 255, min(180, int(a * 0.9))))

# Paste original on top of glow
with_glow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
with_glow.paste(glow_im, (0, 0), glow_im)
with_glow.paste(orig, (0, 0), orig)

with_glow.save('assets/images/gsr-logo-orig-glow.png')
with_glow.save('assets/images/gsr-logo-orig-glow.webp', quality=95)

# Also test on #020612 dark background
bg = Image.new('RGBA', (w + 40, h + 40), (2, 6, 18, 255))
bg.paste(with_glow, (20, 20), with_glow)
bg.save('scratch/orig_with_glow_on_dark.png')
print("Saved assets/images/gsr-logo-orig-glow.webp!")
