from PIL import Image

src = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795677832868_afa5e5b5.jpg")
w, h = src.size
pixels = src.load()

# Find orange pixels in lower left
orange_cols = [x for x in range(w) for y in range(h) if pixels[x, y][0] > 200 and pixels[x, y][1] > 80 and pixels[x, y][2] < 50 and x < 500]
print(f"Orange button x range: {min(orange_cols)} to {max(orange_cols)}")

# Also find where "Watch Overview" play button was
# It has a circle around x=240 to 300
crop_btn = src.crop((0, 220, 480, 317))
crop_btn.save("scratch/btn_area.png")
print("Saved scratch/btn_area.png")
