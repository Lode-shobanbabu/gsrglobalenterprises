from PIL import Image

full = Image.open('scratch/nav_about_preview.png')
w, h = full.size

# Let's crop from y=750 to 1600
section_crop = full.crop((0, 700, w, 1600))
section_crop.save('scratch/preview_700_1600.png')
print("Saved preview_700_1600.png")

# Let's see what colors are present around y=1000..1500
# Look for button text: "KNOW MORE ABOUT OUR CAPABILITIES"
# If the button is navy or orange or something else, let's sample non-white pixels
non_white = []
for x in range(100, w-100, 5):
    for y in range(750, 1600, 5):
        p = full.getpixel((x, y))
        if p[0] < 240 or p[1] < 240 or p[2] < 240:
            non_white.append((x, y, p))

print("Total non-white pixels sampled:", len(non_white))
# Check if there are dark navy pixels (like rgb(6, 43, 85))
navy_px = [p for p in non_white if p[2][0] < 20 and p[2][1] < 60 and p[2][2] > 60]
print("Dark navy pixels:", len(navy_px))
if navy_px:
    print("Navy sample:", navy_px[0])
    print("Navy Y range:", min(p[1] for p in navy_px), "to", max(p[1] for p in navy_px))
