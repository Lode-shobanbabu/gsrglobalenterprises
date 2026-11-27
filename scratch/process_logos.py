from PIL import Image

# Let's inspect the emblem crop and see if we can remove background or make transparent
emblem = Image.open('scratch/cp_emblem.png').convert('RGBA')
w, h = emblem.size

# Let's see background color around corners
bg_color = emblem.getpixel((2, 2))
print("Emblem bg color:", bg_color)

# For APSRTC:
apsrtc_logo = Image.open('scratch/apsrtc_logo_crop.png').convert('RGBA')
print("APSRTC bg color:", apsrtc_logo.getpixel((2, 2)))
