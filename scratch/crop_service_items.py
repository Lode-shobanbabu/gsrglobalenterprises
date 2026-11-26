from PIL import Image

bar = Image.open("scratch/services_bar_crop.png")
w, h = bar.size

# The 5 items are spaced across w (approx w/5 each)
item_w = w / 5
for i in range(5):
    x1 = int(i * item_w)
    x2 = int((i + 1) * item_w)
    item_crop = bar.crop((x1, 0, x2, h))
    item_crop.save(f"scratch/service_item_{i+1}.png")
    print(f"Saved service_item_{i+1}.png")
