from PIL import Image

im = Image.open('scratch/ref_procurement_process.png')
w, h = im.size

# Crop step 01 card and circle
step1_crop = im.crop((120, 180, 480, 310))
step1_crop.save('scratch/crop_step1.png')

# Crop step 02 card and circle
step2_crop = im.crop((400, 290, 750, 420))
step2_crop.save('scratch/crop_step2.png')

print("Cropped step1 and step2")
