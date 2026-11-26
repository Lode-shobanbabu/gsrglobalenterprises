from PIL import Image

topbar = Image.open("scratch/ref_topbar.png")
w, h = topbar.size
# Crop rightmost 200px
icons = topbar.crop((w - 180, 0, w, h))
icons.save("scratch/ref_social_icons.png")
print("Saved ref_social_icons.png")
