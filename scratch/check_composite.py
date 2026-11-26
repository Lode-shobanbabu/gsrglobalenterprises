from PIL import Image

comp = Image.open("scratch/composite_dark_navy.png")
print("Composite size:", comp.size)
# Sample pixels at specific regions:
# Region around GSR (x: 40-100, y: 30-50)
print("Sample pixel at x=50, y=40 (inside G):", comp.getpixel((50, 40)))
print("Sample pixel at x=20, y=10 (inside Orange arc):", comp.getpixel((20, 10)))
print("Sample pixel at x=250, y=65 (inside ENTERPRISES):", comp.getpixel((250, 65)))
print("Sample pixel at x=10, y=70 (background):", comp.getpixel((10, 70)))
