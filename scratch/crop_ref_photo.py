from PIL import Image

ref = Image.open(r'C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795602918218_ab4796e1.jpg')
w, h = ref.size
print(f"Ref size: {w} x {h}")

# In media_1795602918218_ab4796e1.jpg:
# The photo is on the bottom left!
# Let's inspect where the photo begins and ends:
# Background of the page in the ref image is very light grey/lavender: around (245, 245, 250)
# Photo has dark blue / teal / cyan pixels
# Let's find bounding box of the photo inside the bottom-left quadrant (x < 500, y > 150)
for y in range(160, h, 20):
    for x in range(10, 480, 40):
        pass

# Let's crop candidate region [15, 175, 475, 445]
photo_crop = ref.crop((18, 175, 475, 444))
photo_crop.save('scratch/ref_photo_crop.png')
print("Cropped photo size:", photo_crop.size)
