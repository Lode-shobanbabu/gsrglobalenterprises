from PIL import Image

img1 = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795676728974_3476531f.jpg")
print("Screenshot 1 (Header mockup):", img1.size)

img2 = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795676901653_8c2d2164.png")
print("Screenshot 2 (Navigation list):", img2.size)

img3 = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795676978289_6a14f001.webp")
print("Logo 3 (White logo):", img3.size, img3.mode)

img4 = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795677023323_06887d01.webp")
print("Logo 4 (Color logo):", img4.size, img4.mode)
