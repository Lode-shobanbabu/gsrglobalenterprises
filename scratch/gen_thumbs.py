from PIL import Image

im = Image.open('assets/images/hero-procurement.webp')
# Save a thumbnail to scratch
im.thumbnail((600, 400))
im.save('scratch/thumb_hero_procurement.jpg')

im2 = Image.open('assets/images/about-procurement-facility.webp')
im2.thumbnail((600, 400))
im2.save('scratch/thumb_about_facility.jpg')

im3 = Image.open('assets/images/hero-logistics-global.webp')
im3.thumbnail((600, 400))
im3.save('scratch/thumb_hero_logistics.jpg')

print("Thumbnails generated")
