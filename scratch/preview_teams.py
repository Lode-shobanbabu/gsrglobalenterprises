from PIL import Image

im1 = Image.open('assets/images/hero-corporate-team.jpg')
im1.resize((480, 320)).save('scratch/team_preview.jpg')

im2 = Image.open('assets/images/hero-executives.webp')
im2.resize((480, 320)).save('scratch/executives_preview.jpg')

print("Saved previews!")
