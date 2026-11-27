from PIL import Image

# Let's crop individual parts of img1 and img2
img1 = Image.open('C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795760749412_4206333d.png')
img2 = Image.open('C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795760839820_b5c39bc8.png')

# In img1:
# Let's see the width and height
w1, h1 = img1.size
print("img1:", w1, h1)
# left is central prison: roughly 0 to 260
# right is apsrtc: roughly 260 to 520

# In img2:
w2, h2 = img2.size
print("img2:", w2, h2)
# 3 cards across w2
