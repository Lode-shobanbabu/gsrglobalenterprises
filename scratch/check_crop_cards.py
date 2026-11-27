from PIL import Image

cp = Image.open('scratch/cp_emblem.png')
print("cp:", cp.size)

ap = Image.open('scratch/apsrtc_logo_crop.png')
print("ap:", ap.size)

# Also let's inspect the entire card in img1:
# The left card has a background and rounded borders
img1 = Image.open('C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795760749412_4206333d.png')
# Let's crop the entire Central Prison item:
# x from roughly 10 to 240, y from 0 to 103
card1 = img1.crop((10, 5, 250, 98))
card1.save('scratch/card_central_prison.png')

# And APSRTC item:
card2 = img1.crop((280, 5, 510, 98))
card2.save('scratch/card_apsrtc.png')
print("Saved card1 and card2")
