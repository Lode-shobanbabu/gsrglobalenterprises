from PIL import Image

ref = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795678580651_7b73262f.jpg")
print("Ref dimensions:", ref.size)

# The hero section in ref is from y=0 to y=318 (where the cards start)
hero_only = ref.crop((0, 0, ref.width, 318))
hero_only.save("scratch/ref_hero_clean.png")

# Let's inspect where key elements are in ref_hero_clean.png:
# Airplane:
# Globe:
# Ship:
print("Saved scratch/ref_hero_clean.png (dimensions: 1020 x 318)")
