from PIL import Image, ImageFilter, ImageEnhance

# Let's inspect emblem_orig.png which is the original high-res emblem from gsr-logo.png
orig = Image.open('scratch/emblem_orig.png') # 787 x 389, RGB
w, h = orig.size

# The original has a white background (around 254,254,254) and dark navy lines
# Let's make an ultra-clean RGBA emblem for dark backgrounds:
# Foreground should be crisp white (#ffffff) with subtle gold edge or pure white
clean_white = Image.new('RGBA', (w, h), (0, 0, 0, 0))
clean_gold = Image.new('RGBA', (w, h), (0, 0, 0, 0))

for y in range(h):
    for x in range(w):
        r, g, b = orig.getpixel((x, y))
        # Compute darkness
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        if lum < 225:
            # Alpha gradient for smooth anti-aliasing
            alpha = int(255 * (1.0 - (lum / 225.0)))
            # Boost alpha slightly for stronger solid presence
            alpha = min(255, int(alpha * 1.35))
            clean_white.putpixel((x, y), (255, 255, 255, alpha))
            clean_gold.putpixel((x, y), (241, 160, 50, alpha))

# Crop tightly
bbox = clean_white.getbbox()
tight_white = clean_white.crop(bbox)
tight_gold = clean_gold.crop(bbox)

print("Tight white emblem size:", tight_white.size)

# Save high-res master
tight_white.save('assets/images/gsr-emblem-white.png')
tight_white.save('assets/images/gsr-emblem-white.webp', quality=95)

tight_gold.save('assets/images/gsr-emblem-gold.png')
tight_gold.save('assets/images/gsr-emblem-gold.webp', quality=95)

# Also create a composite version: white emblem with subtle gold accent or glow!
print("Successfully generated assets/images/gsr-emblem-white.webp and .png!")
