from PIL import Image

nav = Image.open("scratch/ref_navbar.png")
w, h = nav.size
for x in range(350, 500):
    for y in range(40, h):
        r, g, b = nav.getpixel((x, y))[:3]
        if r > 200 and g > 80 and b < 60:
            print(f"Orange under nav at x={x}, y={y}: ({r}, {g}, {b})")
