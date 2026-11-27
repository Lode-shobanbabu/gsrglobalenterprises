from PIL import Image

img = Image.open('scratch/about_equal_crop.png')
w, h = img.size

# Let's check a column of pixels down the center of the left image (around x=350)
print("Sampling x=350 from y=0 to y=300:")
for y in range(0, 300, 10):
    p = img.getpixel((350, y))
    print(f"y={y}: {p}")
