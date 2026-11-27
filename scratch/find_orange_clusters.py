from PIL import Image

full = Image.open('scratch/nav_about_preview.png')
print("Full screenshot size:", full.size)
w, h = full.size

# Let's search for orange pixels across the entire screenshot
orange_pixels = []
for x in range(0, w, 2):
    for y in range(0, h, 2):
        r, g, b, *a = full.getpixel((x, y))
        # Orange has high R, medium G, low B
        if r > 230 and 100 <= g <= 150 and b < 40:
            orange_pixels.append((x, y, r, g, b))

print("Total orange pixels found in full screenshot:", len(orange_pixels))

# Group by y regions
y_vals = [p[1] for p in orange_pixels]
if y_vals:
    print(f"Y range of orange pixels: {min(y_vals)} to {max(y_vals)}")
    
    # Check distinct clusters in Y
    clusters = {}
    for x, y, r, g, b in orange_pixels:
        bucket = y // 100 * 100
        clusters[bucket] = clusters.get(bucket, 0) + 1
    
    for bucket in sorted(clusters.keys()):
        print(f"Y ~ {bucket}: {clusters[bucket]} orange pixels")
