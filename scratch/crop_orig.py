from PIL import Image

im = Image.open('assets/images/gsr-logo.png')
print("Size:", im.size)
# Let's save a smaller preview with text info
# What is in the emblem?
# Let's crop the emblem from gsr-logo.png
emblem_orig = im.crop((55, 8, 842, 397))
emblem_orig.save('scratch/emblem_orig.png')

text_orig = im.crop((9, 407, 939, 471))
text_orig.save('scratch/text_orig.png')

tagline_orig = im.crop((10, 487, 940, 524))
tagline_orig.save('scratch/tagline_orig.png')

print("Saved scratch/emblem_orig.png, text_orig.png, tagline_orig.png")
