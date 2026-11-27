import os

imgs = os.listdir('assets/images')
for img in imgs:
    if 'solar' in img.lower() or 'energy' in img.lower() or 'renewable' in img.lower() or 'service' in img.lower():
        print(img)
