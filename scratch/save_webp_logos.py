from PIL import Image

cp = Image.open('assets/images/client-central-prison-emblem@2x.png')
cp.save('assets/images/client-central-prison-emblem@2x.webp', 'WEBP', quality=95)

ap = Image.open('assets/images/client-apsrtc-logo@2x.png')
ap.save('assets/images/client-apsrtc-logo@2x.webp', 'WEBP', quality=95)

print("Saved WebP versions")
