from PIL import Image

src_path = r'C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795772008054_d64f5bd1.webp'
img = Image.open(src_path)
print("Uploaded image format:", img.format, "size:", img.size, "mode:", img.mode)

# Save as assets/images/about-corporate-team-meeting.webp
img.save('assets/images/about-corporate-team-meeting.webp', 'WEBP', quality=92)
print("Saved assets/images/about-corporate-team-meeting.webp")

# Also save as jpg
if img.mode != 'RGB':
    rgb_img = img.convert('RGB')
else:
    rgb_img = img
rgb_img.save('assets/images/about-corporate-team-meeting.jpg', 'JPEG', quality=92)
print("Saved assets/images/about-corporate-team-meeting.jpg")
