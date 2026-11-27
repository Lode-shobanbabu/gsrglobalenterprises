from PIL import Image

im = Image.open('scratch/ref_commitment_banner.jpg')
print("Corner pixels:")
print("0,0:", im.getpixel((0, 0)))
print("10,10:", im.getpixel((10, 10)))
print("w-1,0:", im.getpixel((im.width - 1, 0)))
print("w-10,10:", im.getpixel((im.width - 10, 10)))
