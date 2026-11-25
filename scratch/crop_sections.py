from PIL import Image

im = Image.open('assets/images/gsr-logo-white.webp')

# Let's crop Section 1 (Crest), Section 2 (GSR GLOBAL ENTERPRISES), Section 3 (Tagline)
crest = im.crop((55, 8, 842, 397))
crest.save('scratch/crest.png')

text_name = im.crop((9, 407, 939, 471))
text_name.save('scratch/text_name.png')

text_tagline = im.crop((10, 487, 940, 524))
text_tagline.save('scratch/text_tagline.png')

print("Crest size:", crest.size)
print("Text name size:", text_name.size)
print("Tagline size:", text_tagline.size)
