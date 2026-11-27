from PIL import Image

im = Image.open('assets/images/hero-procurement.webp')
print("hero-procurement size:", im.size)

im2 = Image.open('assets/images/hero-logistics-global.webp')
print("hero-logistics-global size:", im2.size)
