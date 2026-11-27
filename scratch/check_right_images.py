from PIL import Image

f1 = Image.open('assets/images/about-procurement-facility.webp')
print("about-procurement-facility:", f1.size)

f2 = Image.open('assets/images/hero-procurement.webp')
print("hero-procurement:", f2.size)

f3 = Image.open('assets/images/about-warehouse-logistics.webp')
print("about-warehouse-logistics:", f3.size)
