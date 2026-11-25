from PIL import Image
import os

files = [
    'gsr-logo.png',
    'gsr-logo.jpg',
    'gsr-logo-cropped.png',
    'gsr-logo-transparent.png',
    'gsr-logo-white.png',
    'gsr-logo-white.webp',
    'gsr-logo-dark-bg.png'
]

for f in files:
    path = os.path.join('assets/images', f)
    if os.path.exists(path):
        im = Image.open(path)
        print(f"{f}: size={im.size}, mode={im.mode}")
