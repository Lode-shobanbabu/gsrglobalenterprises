from PIL import Image

ref = Image.open(r'C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795602918218_ab4796e1.jpg')
w, h = ref.size
print(f"Ref size: {w} x {h}")

# In media_1795602918218_ab4796e1.jpg:
# Where is 'FAQ'? (around y=15..50, x=15..80)
# Where is 'Cybersecurity questions'? (around y=60..105, x=15..450)
# Where is 'answered clearly'? (around y=105..150, x=15..350)
# Where is the background? (around x=5, y=5)

bg_color = ref.getpixel((5, 5))
print(f"Background color: RGB{bg_color[:3]} -> #{bg_color[0]:02x}{bg_color[1]:02x}{bg_color[2]:02x}")

# Sample colors in 'FAQ' area
from collections import Counter
faq_colors = Counter()
for y in range(20, 50):
    for x in range(15, 80):
        faq_colors[ref.getpixel((x, y))[:3]] += 1

print("\nTop colors in FAQ badge area:")
for c, cnt in faq_colors.most_common(5):
    print(f"  RGB{c} -> #{c[0]:02x}{c[1]:02x}{c[2]:02x} ({cnt})")

# Sample colors in 'Cybersecurity questions'
h1_colors = Counter()
for y in range(65, 105):
    for x in range(15, 450):
        p = ref.getpixel((x, y))[:3]
        if p[0] < 100 and p[1] < 100: # non-background
            h1_colors[p] += 1

print("\nTop darkest colors in 'Cybersecurity questions':")
for c, cnt in h1_colors.most_common(8):
    print(f"  RGB{c} -> #{c[0]:02x}{c[1]:02x}{c[2]:02x} ({cnt})")

# Sample colors in 'answered clearly'
h2_colors = Counter()
for y in range(110, 155):
    for x in range(15, 350):
        p = ref.getpixel((x, y))[:3]
        # look for cyan/blue (b > 150, g > 100)
        if p[2] > 140 and p[0] < 150:
            h2_colors[p] += 1

print("\nTop colors in 'answered clearly':")
for c, cnt in h2_colors.most_common(8):
    print(f"  RGB{c} -> #{c[0]:02x}{c[1]:02x}{c[2]:02x} ({cnt})")
