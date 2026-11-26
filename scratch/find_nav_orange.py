from PIL import Image

nav = Image.open("scratch/ref_navbar.png")
w, h = nav.size
for x in range(w):
    for y in range(h):
        r, g, b = nav.getpixel((x, y))[:3]
        if r > 200 and g > 80 and b < 60:
            if x < 600: # not CTA button
                print(f"Orange pixel at x={x}, y={y}: ({r}, {g}, {b})")
