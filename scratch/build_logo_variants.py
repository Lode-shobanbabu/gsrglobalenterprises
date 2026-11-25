from PIL import Image

tight = Image.open('scratch/logo_actual_tight.png') # 919 x 470
w, h = tight.size

# Let's save original cropped as assets/images/gsr-logo-original.png and webp
tight.save('assets/images/gsr-logo.png')
tight.save('assets/images/gsr-logo.webp', quality=95)

# Now, let's create a perfect Dark Mode version:
# Where the deep navy parts (#002457) are brightened to crisp white (#ffffff)
# The globe blue stays rich blue
# The gold swoosh & R-leg stay gold (#caa24d to #f0b84c)
# Let's inspect each pixel:
dark_im = Image.new('RGBA', (w, h), (0, 0, 0, 0))

for y in range(h):
    for x in range(w):
        r, g, b, a = tight.getpixel((x, y))
        if a < 10:
            continue
        
        # Is it in the globe? (x < 320 and y < 255)
        in_globe = (x < 315 and y < 255)
        
        # Is it gold?
        is_gold = (r > 130 and g > 80 and r > b + 25)
        
        # Is it navy?
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        is_navy = (r < 50 and g < 75 and b > 40 and lum < 70)
        
        if is_gold:
            dark_im.putpixel((x, y), (r, g, b, a))
        elif in_globe:
            # Keep globe blue & white lines!
            dark_im.putpixel((x, y), (r, g, b, a))
        elif is_navy:
            # Navy text & icons -> White with same alpha!
            dark_im.putpixel((x, y), (255, 255, 255, a))
        else:
            # Anti-aliased transition pixels
            if lum < 100 and (b > r):
                # Navy edge -> white with adjusted alpha
                dark_im.putpixel((x, y), (255, 255, 255, a))
            else:
                dark_im.putpixel((x, y), (r, g, b, a))

dark_im.save('assets/images/gsr-logo-darkmode.png')
dark_im.save('assets/images/gsr-logo-darkmode.webp', quality=95)
dark_im.save('assets/images/gsr-logo-white.webp', quality=95)

# Also let's create a version on a crisp white / frosted-glass pill badge:
# Sized around the logo with rounded corners
pill_w = w + 40
pill_h = h + 30
pill = Image.new('RGBA', (pill_w, pill_h), (0, 0, 0, 0))
from PIL import ImageDraw
draw = ImageDraw.Draw(pill)
# Draw rounded white rectangle with subtle border
draw.rounded_rectangle([0, 0, pill_w-1, pill_h-1], radius=24, fill=(255, 255, 255, 240), outline=(220, 180, 100, 200), width=2)
pill.paste(tight, (20, 15), tight)
pill.save('assets/images/gsr-logo-badge.webp', quality=95)
pill.save('assets/images/gsr-logo-badge.png')

print("Saved all variants successfully!")
