from PIL import Image

# Let's inspect the cropped logos
img1 = Image.open('C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795760749412_4206333d.png')
print("Image 1 format:", img1.format, img1.size)

# Let's save clean high quality assets into assets/images/
# Let's crop tight logo symbols:
# Emblem for Central Prison: x: 15 to 88, y: 8 to 96
emblem = img1.crop((15, 8, 88, 96))
emblem.save('assets/images/client-central-prison-emblem.png')

# APSRTC circular logo: x: 308 to 386, y: 8 to 96
apsrtc_logo = img1.crop((308, 8, 386, 96))
apsrtc_logo.save('assets/images/client-apsrtc-logo.png')

# Also let's crop the full lockups (emblem + text):
# Central prison lockup: x: 10 to 255, y: 5 to 98
cp_full = img1.crop((10, 5, 255, 98))
cp_full.save('assets/images/client-central-prison-full.png')

# APSRTC lockup: x: 295 to 500, y: 5 to 98
apsrtc_full = img1.crop((295, 5, 500, 98))
apsrtc_full.save('assets/images/client-apsrtc-full.png')

print("Saved all client logo assets into assets/images/")
