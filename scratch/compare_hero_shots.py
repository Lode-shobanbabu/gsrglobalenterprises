from PIL import Image

ref = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795678580651_7b73262f.jpg")
current = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795678645868_4ca7bf5d.jpg")

print("Ref size:", ref.size)
print("Current screenshot size:", current.size)
