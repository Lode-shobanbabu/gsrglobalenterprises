from PIL import Image

src_path = r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795675948188_7896240d.webp"
img = Image.open(src_path).convert('RGBA')

# High-resolution 2x version (800x164)
img_2x = img.resize((img.width * 2, img.height * 2), Image.Resampling.LANCZOS)
img_2x.save("assets/images/gsr-logo-official-transparent@2x.png", "PNG")
img_2x.save("assets/images/gsr-logo-official-transparent@2x.webp", "WEBP", quality=100)

# Check white version at 2x as well
white_img = Image.open("assets/images/gsr-logo-official-white.png").convert('RGBA')
white_2x = white_img.resize((white_img.width * 2, white_img.height * 2), Image.Resampling.LANCZOS)
white_2x.save("assets/images/gsr-logo-official-white@2x.png", "PNG")
white_2x.save("assets/images/gsr-logo-official-white@2x.webp", "WEBP", quality=100)

print("Created 2x high-resolution versions!")
