from PIL import Image

topbar = Image.open("scratch/ref_topbar.png")
print("Topbar size:", topbar.size)

# Sample background at multiple points
print("Topbar bg at (100, 5):", topbar.getpixel((100, 5)))
print("Topbar bg at (500, 5):", topbar.getpixel((500, 5)))
print("Topbar bg at (900, 5):", topbar.getpixel((900, 5)))

# Social icon size
icons = Image.open("scratch/ref_social_icons.png")
print("Social icons crop size:", icons.size)
