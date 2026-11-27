from PIL import Image

img = Image.open('scratch/ref_navbar.png')
w, h = img.size
nav_crop = img.crop((300, 0, min(w, 850), h))
nav_crop.save('scratch/ref_nav_links.png')
print("Saved ref_nav_links.png, size:", nav_crop.size)
