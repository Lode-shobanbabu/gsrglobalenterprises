from PIL import Image

img1 = Image.open('C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795760749412_4206333d.png')
w, h = img1.size

# Let's crop central prison (left) and apsrtc (right)
# The image is 520x103
# Let's inspect where the vertical divider is
# Let's find vertical lines around x=240..280
for x in range(200, 300):
    col = [img1.getpixel((x, y)) for y in range(20, 80)]
    # check if dark or blueish line
    dark_count = sum(1 for p in col if p[0] < 100 and p[1] < 100)
    if dark_count > 30:
        print(f"Vertical line near x={x}, dark_count={dark_count}")

# Central prison crop
crop_cp = img1.crop((0, 0, 260, h))
crop_cp.save('scratch/crop_central_prison.png')

# APSRTC crop
crop_apsrtc = img1.crop((260, 0, w, h))
crop_apsrtc.save('scratch/crop_apsrtc.png')

print("Cropped both successfully")
