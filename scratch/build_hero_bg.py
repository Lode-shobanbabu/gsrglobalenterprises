from PIL import Image

src = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795677832868_afa5e5b5.jpg")
w, h = src.size

# The text on the left is roughly from x=50 to x=460.
# The right side artwork (ship bow, crane, airplane, globe) starts around x=480.
# At x=470-490, what are the pixels?
# Let's inspect column x=470, x=480, x=490
print(f"Image dimensions: {w}x{h}")
col_samples = [src.getpixel((480, y)) for y in range(0, h, 30)]
print("Sample at x=480:", col_samples)

# Let's create a clean background by synthesizing the smooth left sky/water gradient
# and blending it into the right side artwork starting at x=460.
clean_bg = Image.new("RGB", (w, h))

# Sample gradient column at x=20 (clean column with no text)
left_grad = [src.getpixel((20, y)) for y in range(h)]

# Fill clean_bg
pixels = clean_bg.load()
src_pix = src.load()

blend_start = 380
blend_end = 480

for y in range(h):
    base_color = left_grad[y]
    for x in range(w):
        if x < blend_start:
            pixels[x, y] = base_color
        elif x < blend_end:
            alpha = (x - blend_start) / (blend_end - blend_start)
            # Blend base_color with right-side src_pix
            r = int((1 - alpha) * base_color[0] + alpha * src_pix[x, y][0])
            g = int((1 - alpha) * base_color[1] + alpha * src_pix[x, y][1])
            b = int((1 - alpha) * base_color[2] + alpha * src_pix[x, y][2])
            pixels[x, y] = (r, g, b)
        else:
            pixels[x, y] = src_pix[x, y]

# Upscale nicely to 1920 width for crisp high-res desktop display
clean_bg_1920 = clean_bg.resize((1920, int(1920 * h / w)), Image.Resampling.LANCZOS)
clean_bg_1920.save("assets/images/hero-logistics-global.webp", "WEBP", quality=95)
clean_bg_1920.save("assets/images/hero-logistics-global.jpg", "JPEG", quality=95)
clean_bg.save("scratch/test_clean_bg.jpg")

print("Created assets/images/hero-logistics-global.webp successfully!")
