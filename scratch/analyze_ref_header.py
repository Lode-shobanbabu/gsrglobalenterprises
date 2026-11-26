from PIL import Image

img = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795676728974_3476531f.jpg")
w, h = img.size

# The image height is 103px.
# Top bar appears to be around y=0 to y=35.
# Main navbar appears to be around y=35 to y=103.
topbar = img.crop((0, 0, w, 36))
navbar = img.crop((0, 36, w, h))

topbar.save("scratch/ref_topbar.png")
navbar.save("scratch/ref_navbar.png")

# Let's inspect colors
# Sample topbar background color
print("Topbar background color at (500, 15):", topbar.getpixel((500, 15)))

# Sample right-side social icon at (900, 15)
for x in [890, 915, 940]:
    print(f"Topbar pixel at ({x}, 18):", topbar.getpixel((x, 18)))

# Sample CTA button color in navbar
# CTA is on the right side around x=850 to 980
cta_sample = None
for x in range(850, 950):
    for y in range(20, 60):
        p = navbar.getpixel((x, y))
        if p[0] > 200 and p[1] > 80 and p[2] < 50:
            cta_sample = p
            break
    if cta_sample:
        break
print("Navbar CTA button color sample:", cta_sample)

# Sample active nav link underline color under "Home"
# "Home" is around x=400 to 450
home_sample = None
for x in range(400, 480):
    for y in range(45, 65):
        p = navbar.getpixel((x, y))
        if p[0] > 200 and p[1] > 80 and p[2] < 50:
            home_sample = p
            break
    if home_sample:
        break
print("Navbar Home underline color sample:", home_sample)
