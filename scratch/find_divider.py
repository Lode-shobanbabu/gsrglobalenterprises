from PIL import Image

img = Image.open("assets/images/gsr-logo-official-transparent.png").convert("RGBA")
w, h = img.size
pixels = img.load()

# Let's inspect columns from x=250 to 450 (image is 800 wide)
col_dark_counts = []
for x in range(int(w * 0.3), int(w * 0.6)):
    cnt = sum(1 for y in range(h) if pixels[x, y][3] > 100)
    col_dark_counts.append((x, cnt))

# Print local minimums / spikes
for x, cnt in col_dark_counts:
    if cnt > 40:
        print(f"x={x}: cnt={cnt}")
