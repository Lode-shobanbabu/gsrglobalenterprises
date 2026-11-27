from PIL import Image

img1 = Image.open('C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795760749412_4206333d.png')
w, h = img1.size
print("Size:", w, h)

# Let's crop the Ashoka emblem from Central Prison:
# Looking at the image, emblem is on the left
emblem_crop = img1.crop((20, 10, 85, 95))
emblem_crop.save('scratch/cp_emblem.png')

# Let's crop the APSRTC circular logo:
# Looking at the image, APSRTC circular logo is around x=310 to 380
apsrtc_logo_crop = img1.crop((310, 10, 385, 95))
apsrtc_logo_crop.save('scratch/apsrtc_logo_crop.png')

print("Cropped emblem and apsrtc logo")
