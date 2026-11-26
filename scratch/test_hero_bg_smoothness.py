from PIL import Image

bg = Image.open("assets/images/hero-logistics-global.webp")
print("Hero bg size:", bg.size)
# Sample across horizontal line at y = 150 (mid-height)
w, h = bg.size
y_test = int(h * 0.4)
samples = [bg.getpixel((x, y_test)) for x in range(0, w, 100)]
print("Mid-height horizontal pixel samples (every 100px):")
for i, s in enumerate(samples):
    print(f"x={i*100:4d}: {s}")
