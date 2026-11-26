from PIL import Image

# Let's inspect ref_hero_clean.png
img = Image.open("scratch/ref_hero_clean.png")
w, h = img.size
print(f"Ref hero dimensions: {w}x{h}")

# In ref_hero_clean.png:
# Where does the right artwork start?
# At x=480, we have the ship's bow and the water.
# The airplane is at x=530 to 670, y=30 to 110.
# The cranes and ship are at x=500 to 1020, y=100 to 318.
# The globe is at x=680 to 1020, y=0 to 280.

# Notice that the left half has the text from the mockup:
# "Your Trusted Partner for Global Solutions..."
# What if we inpaint/erase the text on the left of ref_hero_clean.png using the clean sky gradient?
# Let's see: at x=20, the entire column is clean sky/water gradient.
# Let's inpaint x=0 to 480 by filling it with the clean sky gradient,
# and feathering it smoothly into x=480 to 520!

clean_hero = img.copy()
pix = clean_hero.load()

# Sample clean column at x=25
clean_col = [img.getpixel((25, y)) for y in range(h)]

# Feather blend from x=380 to x=510
blend_start = 360
blend_end = 510

for y in range(h):
    base_color = clean_col[y]
    for x in range(w):
        if x < blend_start:
            pix[x, y] = base_color
        elif x < blend_end:
            alpha = (x - blend_start) / (blend_end - blend_start)
            orig = img.getpixel((x, y))
            r = int((1 - alpha) * base_color[0] + alpha * orig[0])
            g = int((1 - alpha) * base_color[1] + alpha * orig[1])
            b = int((1 - alpha) * base_color[2] + alpha * orig[2])
            pix[x, y] = (r, g, b)

clean_hero.save("scratch/clean_hero_inpainted.png")
print("Saved scratch/clean_hero_inpainted.png")
