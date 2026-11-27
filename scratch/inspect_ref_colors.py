from PIL import Image

im = Image.open('C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795761876451_5baf8609.jpg')
w, h = im.size
print("Width:", w, "Height:", h)

# Sample colors along horizontal line at y = h // 2
for x in [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]:
    p = im.getpixel((x, h // 2))
    print(f"x={x}: RGB={p}")
