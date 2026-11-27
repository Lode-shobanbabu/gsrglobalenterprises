from PIL import Image

img2 = Image.open('C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795760839820_b5c39bc8.png')
# Save crop of img2
img2.save('scratch/img2_view.png')
img1 = Image.open('C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795760749412_4206333d.png')
img1.save('scratch/img1_view.png')
print("Saved preview crops")
