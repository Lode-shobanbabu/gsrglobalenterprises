from PIL import Image

img = Image.open('assets/images/about-corporate-team-meeting.webp')
print("Image size:", img.size)
for y in range(0, 100, 10):
    print(f"Image y={y}:", img.getpixel((img.size[0]//2, y)))
