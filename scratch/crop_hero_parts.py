from PIL import Image

img = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795677832868_afa5e5b5.jpg")
w, h = img.size

# Let's crop right half
right_bg = img.crop((int(w * 0.42), 0, w, h))
right_bg.save("scratch/hero_right_bg.png")

# Let's also crop the services bar from image 3
img3 = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795677933374_49373d0b.jpg")
w3, h3 = img3.size
# Find where the white card starts (around y=310)
services_bar = img3.crop((0, 310, w3, h3))
services_bar.save("scratch/services_bar_crop.png")

print("Cropped right_bg and services_bar")
