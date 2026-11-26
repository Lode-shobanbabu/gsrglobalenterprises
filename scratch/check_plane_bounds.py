from PIL import Image

plane = Image.open("scratch/plane_crop.png")
print("Plane crop size:", plane.size)
# The plane starts at x=520 (which is 450 + 70 in original image)
# So blend_start = 420 and blend_end = 510 keeps the entire airplane intact!
