from PIL import Image

im = Image.open('assets/images/gsr-logo-white.webp')
crest = Image.open('scratch/crest.png')
print("Crest size:", crest.size)

# Find bounding box of actual visible pixels in crest.png
bbox = crest.getbbox()
print("Crest bbox:", bbox)
cropped_crest = crest.crop(bbox)
print("Cropped crest size:", cropped_crest.size)
cropped_crest.save('scratch/crest_tight.png')
