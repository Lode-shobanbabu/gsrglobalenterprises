from PIL import Image

img = Image.open(r"D:\shoban\GSR GLOBAL ENTERPRISES\scratch\services_rendered.png")
print("Image size:", img.size)

# The total height is 2200. Let's see what parts correspond to hero, about, services
# Let's crop slices to see where services section is
# Slice 1: 0 to 800 (hero & docked bar)
# Slice 2: 800 to 1600 (about & services)
# Slice 3: 1400 to 2200 (services & client/footer)

img.crop((0, 700, 1400, 1700)).save(r"D:\shoban\GSR GLOBAL ENTERPRISES\scratch\services_crop_1.png")
img.crop((0, 1300, 1400, 2200)).save(r"D:\shoban\GSR GLOBAL ENTERPRISES\scratch\services_crop_2.png")
print("Saved crops!")
