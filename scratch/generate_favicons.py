from PIL import Image

img = Image.open("assets/images/gsr-logo-official-transparent.png").convert("RGBA")
w, h = img.size

# Crop GSR emblem (x: 0 to 315)
emblem = img.crop((0, 0, 315, h))
bbox = emblem.split()[-1].getbbox()
emblem_tight = emblem.crop(bbox)

ew, eh = emblem_tight.size
side = max(ew, eh) + 12
fav = Image.new("RGBA", (side, side), (0, 0, 0, 0))
fav.paste(emblem_tight, ((side - ew) // 2, (side - eh) // 2), emblem_tight)

fav_128 = fav.resize((128, 128), Image.Resampling.LANCZOS)
fav_64 = fav.resize((64, 64), Image.Resampling.LANCZOS)
fav_32 = fav.resize((32, 32), Image.Resampling.LANCZOS)
fav_16 = fav.resize((16, 16), Image.Resampling.LANCZOS)

fav_128.save("assets/images/favicon-128.png", "PNG")
fav_64.save("assets/images/favicon-64.png", "PNG")
fav_32.save("assets/images/favicon-32.png", "PNG")
fav_16.save("assets/images/favicon-16.png", "PNG")
fav_32.save("assets/images/favicon.ico")

print("Emblem size:", emblem_tight.size)
print("Saved official favicon suite (16, 32, 64, 128 px)!")
