from PIL import Image

im = Image.open('scratch/logo_actual_tight.png')
w, h = im.size
print(f"Logo actual tight: {w} x {h}")

# Scan row non-zero count
row_counts = [sum(1 for x in range(w) if im.getpixel((x, y))[3] > 30) for y in range(h)]

# Find horizontal divider lines (rows where count is 0 or very low)
for y in range(h):
    if row_counts[y] == 0:
        print(f"Empty row at y={y}")
