from PIL import Image

im = Image.open('assets/images/gsr-logo-white.webp')
width, height = im.size
print(f"Total size: {width} x {height}")

# Scan non-zero alpha rows and cols
non_empty_rows = []
for y in range(height):
    has_pixel = False
    for x in range(width):
        r, g, b, a = im.getpixel((x, y))
        if a > 20:
            has_pixel = True
            break
    if has_pixel:
        non_empty_rows.append(y)

print(f"Non-empty rows: {min(non_empty_rows)} to {max(non_empty_rows)} (height={max(non_empty_rows) - min(non_empty_rows) + 1})")

# Let's find vertical gaps (empty rows) to see sections of the logo
sections = []
current_start = None
for y in range(min(non_empty_rows), max(non_empty_rows) + 1):
    row_pixels = sum(1 for x in range(width) if im.getpixel((x, y))[3] > 20)
    if row_pixels > 0:
        if current_start is None:
            current_start = y
    else:
        if current_start is not None:
            sections.append((current_start, y - 1))
            current_start = None
if current_start is not None:
    sections.append((current_start, max(non_empty_rows)))

print(f"Vertical sections found: {len(sections)}")
for i, (sy, ey) in enumerate(sections):
    # Find x bounds for this section
    min_x = width
    max_x = 0
    for y in range(sy, ey + 1):
        for x in range(width):
            if im.getpixel((x, y))[3] > 20:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
    print(f"Section {i}: Y=[{sy}..{ey}] (h={ey-sy+1}), X=[{min_x}..{max_x}] (w={max_x-min_x+1})")
