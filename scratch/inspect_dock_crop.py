from PIL import Image

img = Image.open('scratch/dock_cards_rendered.png')
print("Dock cards crop size:", img.size)
# Sample points inside the cards and background
w, h = img.size
# Card 1 center
card1_x = int(w * 0.2)
card1_y = int(h * 0.6)
print("Card 1 center pixel:", img.getpixel((card1_x, card1_y)))
# Between cards (background)
bg_x = int(w * 0.32)
bg_y = int(h * 0.6)
print("Background between cards:", img.getpixel((bg_x, bg_y)))
