from PIL import Image

img = Image.open('assets/images/service-solar.webp')
print("service-solar.webp size:", img.size, "format:", img.format)

# Check dimensions of service-pro-medical.webp for comparison
pro_med = Image.open('assets/images/service-pro-medical.webp')
print("service-pro-medical.webp size:", pro_med.size)

# Resize or save service-pro-solar.webp matching the aspect ratio and quality
img_resized = img.resize(pro_med.size, Image.Resampling.LANCZOS)
img_resized.save('assets/images/service-pro-solar.webp', 'WEBP', quality=90)
print("Saved assets/images/service-pro-solar.webp with size:", img_resized.size)
