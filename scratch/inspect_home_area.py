from PIL import Image

nav = Image.open("scratch/ref_navbar.png")
# Let's crop the text area of the navbar: x: 380 to 800, y: 0 to h
crop_links = nav.crop((380, 0, 800, nav.height))
crop_links.save("scratch/crop_links.png")

# Let's find any non-white pixels near the bottom of crop_links
for y in range(35, nav.height):
    for x in range(380, 500):
        p = nav.getpixel((x, y))
        if p[0] < 240 or p[1] < 240 or p[2] < 240:
            print(f"Non-white at x={x}, y={y}: {p}")
