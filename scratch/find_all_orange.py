from PIL import Image

full = Image.open(r"scratch\tall_page_preview.png")
w, h = full.size

orange_pts = []
for x in range(0, w, 4):
    for y in range(0, h, 4):
        r, g, b, *a = full.getpixel((x, y))
        if r > 230 and 100 <= g <= 145 and b < 30:
            orange_pts.append((x, y))

print("Total orange pixels in entire 1400x3600:", len(orange_pts))
if orange_pts:
    y_vals = [p[1] for p in orange_pts]
    print(f"Y range of all orange pixels: {min(y_vals)} to {max(y_vals)}")
    clusters = {}
    for p in orange_pts:
        k = p[1] // 100 * 100
        clusters[k] = clusters.get(k, 0) + 1
    for k in sorted(clusters.keys()):
        print(f"y ~ {k}: {clusters[k]} pixels")
