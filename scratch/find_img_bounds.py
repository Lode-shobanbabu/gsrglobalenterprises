from PIL import Image

full = Image.open('scratch/about_equal_height_preview.png')
print("Full preview size:", full.size)
w, h = full.size

# Search for the image bounding box in the left half (x < w/2)
# The image top pixel has color around (176, 180, 183)
# Let's find all pixels matching the image border or colors in x in [100, 600]
img_pts = []
for x in range(120, 600, 5):
    for y in range(100, 900, 5):
        p = full.getpixel((x, y))
        # Image background is not pure white
        if p != (255, 255, 255):
            img_pts.append((x, y))

if img_pts:
    min_x = min(p[0] for p in img_pts)
    max_x = max(p[0] for p in img_pts)
    min_y = min(p[1] for p in img_pts)
    max_y = max(p[1] for p in img_pts)
    print(f"Left Image frame in full preview: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}], height={max_y - min_y}px")

# Search for the right content bounding box in x in [700, 1300]
content_pts = []
for x in range(700, 1300, 5):
    for y in range(100, 900, 5):
        p = full.getpixel((x, y))
        if p != (255, 255, 255):
            content_pts.append((x, y))

if content_pts:
    min_cx = min(p[0] for p in content_pts)
    max_cx = max(p[0] for p in content_pts)
    min_cy = min(p[1] for p in content_pts)
    max_cy = max(p[1] for p in content_pts)
    print(f"Right Content in full preview: x=[{min_cx}, {max_cx}], y=[{min_cy}, {max_cy}], height={max_cy - min_cy}px")
