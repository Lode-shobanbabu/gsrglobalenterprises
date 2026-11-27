from PIL import Image, ImageDraw, ImageFilter

# Let's see hero-procurement and about-procurement-facility
img_proc = Image.open('assets/images/hero-procurement.webp')
print("hero-procurement:", img_proc.size)

img_wh = Image.open('assets/images/about-procurement-facility.webp')
print("about-procurement-facility:", img_wh.size)

img_log = Image.open('assets/images/hero-logistics-global.webp')
print("hero-logistics-global:", img_log.size)

img_team = Image.open('assets/images/about-corporate-team-meeting.webp')
print("about-corporate-team-meeting:", img_team.size)
