from PIL import Image
import numpy as np

img1 = Image.open('C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795760749412_4206333d.png')
img2 = Image.open('C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795760839820_b5c39bc8.png')

print("Image 1 mode:", img1.mode, "size:", img1.size)
print("Image 2 mode:", img2.mode, "size:", img2.size)
