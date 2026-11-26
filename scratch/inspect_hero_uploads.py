from PIL import Image

img1 = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795677832868_afa5e5b5.jpg")
print("Image 1 (Hero):", img1.size, img1.mode)

img2 = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795677871565_f2aef860.png")
print("Image 2 (Content):", img2.size, img2.mode)

img3 = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795677933374_49373d0b.jpg")
print("Image 3 (Hero + Floating Services Bar):", img3.size, img3.mode)
