from PIL import Image

src = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795677832868_afa5e5b5.jpg")
w, h = src.size

# Find dark pixels in upper half between x=400 and x=700 (airplane is white with grey shadows)
# Airplane is around x=500 to 650, y=50 to 120
crop_plane = src.crop((450, 20, 680, 150))
crop_plane.save("scratch/plane_crop.png")
print("Cropped airplane region to scratch/plane_crop.png")
