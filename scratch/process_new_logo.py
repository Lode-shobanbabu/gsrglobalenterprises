from PIL import Image

path = r'C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795602424527_c9d3202d.png'
im = Image.open(path)
w, h = im.size

# Let's crop tight bbox
bbox = im.getbbox()
im_tight = im.crop(bbox)
tw, th = im_tight.size

# Save original cropped transparent
im_tight.save('assets/images/gsr-logo-new-original.png')
im_tight.save('assets/images/gsr-logo-new-original.webp', quality=95)

# Now let's create a version optimized for Dark Backgrounds:
# In the original, the navy color is around RGB(0..10, 30..45, 80..95) - high blue, low red/green
# Gold is around R > 150, G > 100, B < 80.
# Globe has lighter blues (R: 20..100, G: 60..150, B: 120..220) and white lines (R>200, G>200, B>200).
# Let's inspect the colors carefully:
dark_mode = Image.new('RGBA', (tw, th), (0, 0, 0, 0))

for y in range(th):
    for x in range(tw):
        r, g, b, a = im_tight.getpixel((x, y))
        if a < 15:
            continue
        
        # Check if it's the deep navy blue:
        # Deep navy has r < 35, g < 60, b between 50 and 120
        # and specifically lum is low (lum < 50)
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        
        is_navy = (r < 40 and g < 65 and b > 40 and b < 130 and lum < 55)
        # Also anti-aliased edges of navy:
        is_navy_edge = (r < 70 and g < 90 and b > 70 and b < 160 and lum < 80 and (b - r > 40) and (b - g > 25))
        
        # Check if it's gold (r > 130, g > 80, b < 90 or r > g > b)
        is_gold = (r > 120 and g > 75 and r > b + 30)
        
        # Globe blue (has higher green and brighter blue: g > 60 or lum > 70)
        # We only want to turn the NAVY text and icons to white!
        # Notice: the globe is located at X < 350 and Y < 360!
        # The text "GSR" is at X > 280, Y < 360
        # "GLOBAL ENTERPRISES" is at Y > 330, Y < 450
        # Tagline is at Y > 430, Y < 530
        # Icons are at Y > 500
        
        # In the globe area (X < 340, Y < 340):
        # We want to keep the globe blue as it is!
        in_globe = (x < 330 and y < 335)
        
        if is_gold:
            # Keep gold!
            dark_mode.putpixel((x, y), (r, g, b, a))
        elif in_globe:
            # In globe: keep original globe colors
            dark_mode.putpixel((x, y), (r, g, b, a))
        elif is_navy or is_navy_edge:
            # Turn navy to bright white for dark backgrounds!
            # Preserve original alpha
            dark_mode.putpixel((x, y), (255, 255, 255, a))
        else:
            # Other pixels (anti-aliasing, etc.)
            dark_mode.putpixel((x, y), (r, g, b, a))

dark_mode.save('assets/images/gsr-logo-new-darkmode.png')
dark_mode.save('assets/images/gsr-logo-new-darkmode.webp', quality=95)

# Also let's paste on dark background (#020612) to test
bg = Image.new('RGBA', (tw + 40, th + 40), (2, 6, 18, 255))
bg.paste(dark_mode, (20, 20), dark_mode)
bg.save('scratch/logo_darkmode_preview.png')

print("Saved assets/images/gsr-logo-new-darkmode.webp and preview!")
