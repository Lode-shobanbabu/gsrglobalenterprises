from PIL import Image

src = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795677832868_afa5e5b5.jpg")
w, h = src.size

# Let's crop the right-hand artwork from x=455 to w (1024)
# In this region (455 to 1024), there is NO text at all!
artwork = src.crop((455, 0, w, h))
aw, ah = artwork.size
print(f"Clean artwork size: {aw}x{ah}")

# Now let's create a bright, clean, premium widescreen hero background
# Canvas: 2000 x 550 (or 2200 x 550)
target_h = 550
scale = target_h / ah
target_aw = int(aw * scale)
scaled_art = artwork.resize((target_aw, target_h), Image.Resampling.LANCZOS)

target_w = 2000
canvas = Image.new("RGB", (target_w, target_h), (255, 255, 255))

# Paste artwork on the right edge
art_x = target_w - target_aw
canvas.paste(scaled_art, (art_x, 0))

# Now create a smooth, bright feather blend on the left edge of the artwork (first 120px of artwork)
# The artwork's left edge (art_x to art_x + 120) should fade smoothly into pure white (255, 255, 255)
# or soft bright sky!
canvas_pix = canvas.load()
art_pix = scaled_art.load()

fade_width = 140
for y in range(target_h):
    # Sample sky color at top vs water at bottom
    # Top sky at x=art_x + fade_width:
    target_sky = scaled_art.getpixel((fade_width, y))
    for x in range(art_x, art_x + fade_width):
        factor = (x - art_x) / fade_width # 0 to 1
        orig_p = art_pix[x - art_x, y]
        # Smooth ease-in-out factor
        factor = factor * factor * (3 - 2 * factor)
        # Blend with pure white (255, 255, 255) on far left
        r = int((1 - factor) * 255 + factor * orig_p[0])
        g = int((1 - factor) * 255 + factor * orig_p[1])
        b = int((1 - factor) * 255 + factor * orig_p[2])
        canvas_pix[x, y] = (r, g, b)

# Fill the left area (0 to art_x) with pure bright white (#FFFFFF)
for y in range(target_h):
    for x in range(art_x):
        canvas_pix[x, y] = (255, 255, 255)

canvas.save("assets/images/hero-logistics-global.webp", "WEBP", quality=98)
canvas.save("assets/images/hero-logistics-global.jpg", "JPEG", quality=98)
canvas.save("scratch/bright_hero_preview.jpg")

print("Created ultra-bright clean background with ZERO ghost text and pure white left half!")
