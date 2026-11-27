from PIL import Image

img2 = Image.open('C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795760839820_b5c39bc8.png')
w2, h2 = img2.size
print("img2 dimensions:", w2, h2)

# There are 3 cards roughly separated horizontally
# Let's crop each of the 3 cards:
# card 1: 0 to ~200
# card 2: ~200 to ~410
# card 3: ~410 to w2
c1 = img2.crop((10, 10, 205, h2-10))
c2 = img2.crop((215, 10, 410, h2-10))
c3 = img2.crop((415, 10, 610, h2-10))

c1.save('scratch/crop_airtel.png')
c2.save('scratch/crop_jio.png')
c3.save('scratch/crop_vi.png')
print("Saved 3 cards from img2")
