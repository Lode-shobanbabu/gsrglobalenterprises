from PIL import Image

white_logo = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795676978289_6a14f001.webp")
color_logo = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795677023323_06887d01.webp")

print("White logo format:", white_logo.format, white_logo.size, white_logo.mode)
print("Color logo format:", color_logo.format, color_logo.size, color_logo.mode)

# Save the exact white logo as assets/images/gsr-logo-official-white.webp and .png
white_logo.save("assets/images/gsr-logo-official-white.webp", "WEBP", quality=100)
white_logo.save("assets/images/gsr-logo-official-white.png", "PNG")

# Also save high-DPI 2x
w, h = white_logo.size
white_2x = white_logo.resize((w * 2, h * 2), Image.Resampling.LANCZOS)
white_2x.save("assets/images/gsr-logo-official-white@2x.webp", "WEBP", quality=100)
white_2x.save("assets/images/gsr-logo-official-white@2x.png", "PNG")

# Save the exact color logo as assets/images/gsr-logo-official-transparent.webp and .png
color_logo.save("assets/images/gsr-logo-official-transparent.webp", "WEBP", quality=100)
color_logo.save("assets/images/gsr-logo-official-transparent.png", "PNG")

w_c, h_c = color_logo.size
color_2x = color_logo.resize((w_c * 2, h_c * 2), Image.Resampling.LANCZOS)
color_2x.save("assets/images/gsr-logo-official-transparent@2x.webp", "WEBP", quality=100)
color_2x.save("assets/images/gsr-logo-official-transparent@2x.png", "PNG")

print("Deployed exact user-uploaded logos directly into assets/images/!")
