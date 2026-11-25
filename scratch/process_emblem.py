from PIL import Image

im = Image.open('scratch/emblem_tight.png')
print("Emblem tight size:", im.size)

# Create a transparent version where white background is removed
# and the emblem is crisp white/gold for dark backgrounds!
rgba = im.convert('RGBA')
w, h = rgba.size

# Emblem on white background: white pixels are background (r > 230, g > 230, b > 230)
# Dark pixels (navy) are foreground.
# For dark navbar, foreground should be bright (white / gold)!
out_white = Image.new('RGBA', (w, h), (0, 0, 0, 0))
out_gold = Image.new('RGBA', (w, h), (0, 0, 0, 0))

for y in range(h):
    for x in range(w):
        r, g, b, a = rgba.getpixel((x, y))
        # Compute darkness of original pixel (0 is black, 255 is white)
        luminance = 0.299 * r + 0.587 * g + 0.114 * b
        if luminance < 235:
            # Foreground pixel!
            # The darker the pixel was, the more opaque it is
            alpha = int(255 * (1.0 - (luminance / 235.0)))
            # White version
            out_white.putpixel((x, y), (255, 255, 255, alpha))
            # Gold version (#f1a03c / #e5a93c)
            out_gold.putpixel((x, y), (241, 160, 60, alpha))

out_white.save('scratch/emblem_white_transparent.png')
out_gold.save('scratch/emblem_gold_transparent.png')
print("Saved transparent emblems!")
