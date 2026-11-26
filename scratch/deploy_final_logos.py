from PIL import Image

src_path = r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795675948188_7896240d.webp"
img = Image.open(src_path).convert('RGBA')

# 1. Save pristine 1x original
img.save("assets/images/gsr-logo-original-upload.webp", "WEBP", quality=100)
img.save("assets/images/gsr-logo-original-upload.png", "PNG")

# 2. High-DPI 2x version for crisp rendering on all screens (800 x 164)
img_2x = img.resize((img.width * 2, img.height * 2), Image.Resampling.LANCZOS)
# Save as the main transparent logo
img_2x.save("assets/images/gsr-logo-official-transparent.webp", "WEBP", quality=100)
img_2x.save("assets/images/gsr-logo-official-transparent.png", "PNG")
img_2x.save("assets/images/gsr-logo-official.png", "PNG")

# 3. Create high-DPI 2x white version for dark footer
w, h = img_2x.size
white_2x = Image.new("RGBA", (w, h), (0, 0, 0, 0))
src_pix = img_2x.load()
dest_pix = white_2x.load()

for y in range(h):
    for x in range(w):
        r, g, b, a = src_pix[x, y]
        if a < 8:
            dest_pix[x, y] = (0, 0, 0, 0)
            continue
        
        # Orange arc / orbit
        is_orange = (r > 160 and r > b + 60 and g > 50)
        # Blue / cyan globe inside "GLOBAL"
        is_globe = (b > r + 30 and g > r + 20 and b > 100)
        
        if is_orange:
            dest_pix[x, y] = (r, g, b, a)
        elif is_globe:
            dest_pix[x, y] = (min(255, r + 40), min(255, g + 40), min(255, b + 40), a)
        else:
            # Grey text ("ENTERPRISES") vs Navy text ("GSR", "GLOBAL", divider)
            is_grey = (abs(r - g) < 20 and abs(g - b) < 20 and r > 70)
            if is_grey:
                dest_pix[x, y] = (226, 232, 240, a) # Crisp silver
            else:
                dest_pix[x, y] = (255, 255, 255, a) # Pure white

white_2x.save("assets/images/gsr-logo-official-white.webp", "WEBP", quality=100)
white_2x.save("assets/images/gsr-logo-official-white.png", "PNG")

print("Generated and deployed all assets successfully!")
