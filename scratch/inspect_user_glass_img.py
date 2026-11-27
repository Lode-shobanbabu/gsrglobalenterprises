from PIL import Image

img = Image.open(r'C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795768083618_0589b743.png')
print("Image size:", img.size)

# Sample some pixel colors across the vertical slices of the image
# to see where the cards are located and what background is behind them
w, h = img.size
print("Top background (w//2, 10):", img.getpixel((w//2, 10)))
print("Upper card (w//2, h//3):", img.getpixel((w//2, h//3)))
print("Lower card (w//2, 2*h//3):", img.getpixel((w//2, 2*h//3)))
print("Bottom background (w//2, h-10):", img.getpixel((w//2, h-10)))
