from PIL import Image

img = Image.open('C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795763852812_91cd05fa.png')
print("Image size:", img.size)
print("Image mode:", img.mode)

# Save to scratch for reference
img.save('scratch/ref_procurement_process.png')
print("Saved to scratch/ref_procurement_process.png")
