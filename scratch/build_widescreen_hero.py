from PIL import Image

src = Image.open("scratch/clean_hero_inpainted.png")
sw, sh = src.size

# Target widescreen: width = 2000, height = 550
# We want the right artwork (airplane, ship, globe) to take the right ~950px
# and the left ~1050px to be clean sky gradient.
scale_factor = 550 / sh
new_sh = 550
new_sw = int(sw * scale_factor) # approx 1762px

scaled_src = src.resize((new_sw, new_sh), Image.Resampling.LANCZOS)

# Create 2200 x 550 canvas
canvas_w = 2200
canvas_h = 550
wide_canvas = Image.new("RGB", (canvas_w, canvas_h))

# Paste scaled_src on the right side
paste_x = canvas_w - new_sw
wide_canvas.paste(scaled_src, (paste_x, 0))

# Fill the left area (from x=0 to paste_x + 100) with the left sky/water gradient
left_col = [scaled_src.getpixel((10, y)) for y in range(new_sh)]
pix = wide_canvas.load()

for y in range(new_sh):
    col = left_col[y]
    for x in range(paste_x + 80):
        pix[x, y] = col

wide_canvas.save("assets/images/hero-logistics-global.webp", "WEBP", quality=96)
wide_canvas.save("assets/images/hero-logistics-global.jpg", "JPEG", quality=96)

print(f"Created wide canvas assets/images/hero-logistics-global.webp ({canvas_w}x{canvas_h})")
