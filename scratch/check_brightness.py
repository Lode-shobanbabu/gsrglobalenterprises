from PIL import Image

uploaded = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795679056548_41604df5.jpg")
ref1 = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795677832868_afa5e5b5.jpg")

print("User screenshot size:", uploaded.size)
print("Reference 1 size:", ref1.size)

# Sample background brightness in ref1 vs uploaded in the sky and port area
# In ref1, look at the sky at (800, 50), (600, 50)
print("Ref1 sky at (600, 50):", ref1.getpixel((600, 50)))
print("Ref1 harbor at (600, 200):", ref1.getpixel((600, 200)))
print("Ref1 water at (600, 300):", ref1.getpixel((600, 300)))
