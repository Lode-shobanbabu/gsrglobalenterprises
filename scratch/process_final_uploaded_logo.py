from PIL import Image

src_path = r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795675948188_7896240d.webp"
img = Image.open(src_path).convert('RGBA')
width, height = img.size

# Let's save a clean copy to assets/images
# 1. Main light version (for white navbar and light backgrounds)
img.save("assets/images/gsr-logo-official-transparent.webp", "WEBP", quality=100)
img.save("assets/images/gsr-logo-official-transparent.png", "PNG")
img.save("assets/images/gsr-logo-official.png", "PNG")

# 2. Inverted / White version for dark backgrounds (like the footer)
# In the footer, navy text (#062B55) and grey text become white/bright (#FFFFFF and #E2E8F0),
# while orange arc (#FF7900) and the globe remain vibrant!
white_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
white_pixels = white_img.load()
src_pixels = img.load()

for y in range(height):
    for x in range(width):
        r, g, b, a = src_pixels[x, y]
        if a < 10:
            white_pixels[x, y] = (0, 0, 0, 0)
            continue
        
        # Check if pixel is part of the orange arc/orbit:
        # Orange has high red and low blue
        is_orange = (r > 160 and r > b + 60 and g > 50)
        is_globe = (b > r + 30 and g > r + 20 and b > 100) # light blue/cyan in globe
        
        if is_orange:
            # Keep orange vibrant
            white_pixels[x, y] = (r, g, b, a)
        elif is_globe:
            # Keep globe vibrant / slightly brighter
            white_pixels[x, y] = (min(255, r + 40), min(255, g + 40), min(255, b + 40), a)
        else:
            # Navy and grey letters -> make crisp white or silver
            # Calculate perceived lightness or preserve alpha antialiasing
            # The darker the original, the more solid white
            # If it's grey (ENTERPRISES), make it a bright silver #E2E8F0
            is_grey = (abs(r - g) < 20 and abs(g - b) < 20 and r > 70)
            if is_grey:
                white_pixels[x, y] = (226, 232, 240, a)
            else:
                # Navy Blue letters (GSR, GLOBAL, vertical bar) -> Pure White
                white_pixels[x, y] = (255, 255, 255, a)

white_img.save("assets/images/gsr-logo-official-white.webp", "WEBP", quality=100)
white_img.save("assets/images/gsr-logo-official-white.png", "PNG")

print("Successfully generated all logo variants from newly uploaded final logo!")
print("Saved assets/images/gsr-logo-official-transparent.webp")
print("Saved assets/images/gsr-logo-official-transparent.png")
print("Saved assets/images/gsr-logo-official.png")
print("Saved assets/images/gsr-logo-official-white.webp")
print("Saved assets/images/gsr-logo-official-white.png")
