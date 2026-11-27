from PIL import Image

full = Image.open('scratch/about_perfect_equal.png')
# Search for orange pixels of the eyebrow dash in x in [700, 1100]
dash_pts = []
for x in range(700, 1100):
    for y in range(50, 400):
        r, g, b, *a = full.getpixel((x, y))
        if r > 240 and 110 <= g <= 135 and b < 20:
            dash_pts.append((x, y))

if dash_pts:
    min_dy = min(p[1] for p in dash_pts)
    max_dy = max(p[1] for p in dash_pts)
    print(f"Eyebrow dash Y in full screenshot: {min_dy} to {max_dy}")
else:
    print("No orange dash found in [700, 1100], y in [50, 400]")
