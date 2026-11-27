from PIL import Image

cp = Image.open('assets/images/client-central-prison-emblem-clean.png')
ap = Image.open('assets/images/client-apsrtc-logo-clean.png')

# Let's upscale with high-quality Lanczos resampling to 2x (e.g. height=160)
cp_2x = cp.resize((int(cp.width * 2), int(cp.height * 2)), Image.Resampling.LANCZOS)
cp_2x.save('assets/images/client-central-prison-emblem@2x.png')

ap_2x = ap.resize((int(ap.width * 2), int(ap.height * 2)), Image.Resampling.LANCZOS)
ap_2x.save('assets/images/client-apsrtc-logo@2x.png')

print("Saved 2x crisp assets for Retina screens")
