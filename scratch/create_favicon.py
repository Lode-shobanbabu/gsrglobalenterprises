from PIL import Image

img = Image.open("assets/images/gsr-logo-official-transparent.png").convert("RGBA")
w, h = img.size

# Look at the horizontal layout:
# The vertical divider is between GSR and GSR GLOBAL
# Let's find the vertical divider column
# The vertical divider has dark pixels around height 15 to 65
pixels = img.load()
divider_x = None

for x in range(int(w * 0.3), int(w * 0.5)):
    # count pixels in this column that are dark
    dark_in_col = sum(1 for y in range(h) if pixels[x, y][3] > 150 and pixels[x, y][0] < 50)
    # The divider is a thin line with many vertical pixels and empty on sides
    if dark_in_col > h * 0.6:
        divider_x = x
        break

print("Divider detected at x =", divider_x)
if divider_x:
    # Emblem is from x=0 to divider_x - 10
    emblem = img.crop((0, 0, divider_x - 8, h))
    # Trim transparency
    alpha = emblem.split()[-1]
    bbox = alpha.getbbox()
    if bbox:
        emblem_tight = emblem.crop(bbox)
        # Pad slightly to square
        ew, eh = emblem_tight.size
        side = max(ew, eh) + 16
        fav = Image.new("RGBA", (side, side), (0, 0, 0, 0))
        fav.paste(emblem_tight, ((side - ew) // 2, (side - eh) // 2), emblem_tight)
        fav_64 = fav.resize((64, 64), Image.Resampling.LANCZOS)
        fav_32 = fav.resize((32, 32), Image.Resampling.LANCZOS)
        fav_64.save("assets/images/favicon-64.png", "PNG")
        fav_32.save("assets/images/favicon-32.png", "PNG")
        fav_32.save("assets/images/favicon.ico")
        fav_64.save("assets/images/favicon.png", "PNG")
        print("Generated official emblem favicons (32px, 64px, .ico)!")
