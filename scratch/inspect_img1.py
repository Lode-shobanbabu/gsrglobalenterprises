from PIL import Image

img1 = Image.open('C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795760749412_4206333d.png')
print("img1 size:", img1.size)
print("Pixel at 5,5:", img1.getpixel((5, 5)))
print("Pixel at 100,50:", img1.getpixel((100, 50)))
print("Pixel at 300,50:", img1.getpixel((300, 50)))

img2 = Image.open('C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795760839820_b5c39bc8.png')
print("img2 size:", img2.size)
print("Pixel at 5,5:", img2.getpixel((5, 5)))
print("Pixel at 100,50:", img2.getpixel((100, 50)))
