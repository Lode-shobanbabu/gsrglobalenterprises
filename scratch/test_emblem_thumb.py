from PIL import Image

im = Image.open('scratch/emblem_white_transparent.png')
print("Size:", im.size)

# Let's see how dense it is
w, h = im.size
print("Width:", w, "Height:", h)

# Let's count alpha > 50
visible_pixels = sum(1 for y in range(h) for x in range(w) if im.getpixel((x, y))[3] > 50)
print(f"Visible pixels: {visible_pixels} / {w*h} ({visible_pixels/(w*h)*100:.1f}%)")

# Let's resize it to standard header emblem height (e.g., 50px tall, 102px wide)
# and save to see if it's sharp
thumb = im.resize((int(w * (52 / h)), 52), Image.Resampling.LANCZOS)
thumb.save('scratch/emblem_thumb.png')
print(f"Thumb size: {thumb.size}")
