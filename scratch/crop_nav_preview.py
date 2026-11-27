from PIL import Image

nav = Image.open('scratch/navbar_capitalized.png')
w, h = nav.size
# Crop around the central nav links
# Navbar links are in the center roughly x=400 to 1000, y=40 to 110
links_crop = nav.crop((380, 40, 1050, 110))
links_crop.save('scratch/nav_links_preview.png')
print("Saved nav links preview, size:", links_crop.size)
