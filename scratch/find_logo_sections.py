from PIL import Image

im = Image.open('assets/images/gsr-logo-new-original.png')
w, h = im.size
print("Size:", w, h)

# Let's find vertical segments:
row_alphas = [sum(1 for x in range(w) if im.getpixel((x, y))[3] > 30) for y in range(h)]

# Let's find vertical gaps
for y in range(0, h, 20):
    print(f"y={y:3d}: non-empty pixels={row_alphas[y]}")
