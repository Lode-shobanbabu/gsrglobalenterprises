from PIL import Image

c1 = Image.open('scratch/card_central_prison.png')
print("c1 size:", c1.size, "colors:", c1.getextrema())

c2 = Image.open('scratch/card_apsrtc.png')
print("c2 size:", c2.size, "colors:", c2.getextrema())
