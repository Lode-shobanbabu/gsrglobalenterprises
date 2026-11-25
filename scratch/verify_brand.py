import re, os

# Check CSS brace balance
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

open_braces = css.count('{')
close_braces = css.count('}')
print(f"CSS braces: open={open_braces}, close={close_braces}, balanced={open_braces == close_braces}")

# Check HTML tag balance for brand-container
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check image references in brand-container
brand_imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*class=["\'][^"\']*brand-[^"\']*["\']', html)
print(f"Brand images in HTML: {brand_imgs}")
for img in brand_imgs:
    exists = os.path.exists(img)
    print(f"  {img}: exists={exists}")

footer_imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*class=["\'][^"\']*footer-[^"\']*["\']', html)
print(f"Footer images in HTML: {footer_imgs}")
for img in footer_imgs:
    exists = os.path.exists(img)
    print(f"  {img}: exists={exists}")
