from PIL import Image

cp = Image.open('scratch/crop_central_prison.png')
print("CP size:", cp.size)

apsrtc = Image.open('scratch/crop_apsrtc.png')
print("APSRTC size:", apsrtc.size)
