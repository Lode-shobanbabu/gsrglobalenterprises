with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update brand-logo-img
old_brand_css = """.brand-logo-img {
  height: 52px;
  width: auto;
  max-width: 250px;
  object-fit: contain;
  display: block;
  transition: transform 0.25s ease, height 0.25s ease;
}

.navbar-corporate.scrolled .brand-logo-img {
  height: 46px;
}"""

new_brand_css = """.brand-logo-img {
  height: 52px;
  width: auto;
  max-width: 255px;
  object-fit: contain;
  display: block;
  transition: transform 0.25s ease, height 0.25s ease;
}

.navbar-corporate.scrolled .brand-logo-img {
  height: 46px;
}

@media (max-width: 575.98px) {
  .brand-logo-img {
    height: 42px;
    max-width: 200px;
  }
}"""

# Update footer-logo-img
old_footer_css = """.footer-logo-img {
  height: 74px;
  width: auto;
  max-width: 260px;
  object-fit: contain;
  display: block;
  filter: drop-shadow(0 2px 10px rgba(0, 0, 0, 0.45));
  transition: transform 0.25s ease, filter 0.25s ease;
}

.footer-brand:hover .footer-logo-img {
  transform: translateY(-2px);
  filter: drop-shadow(0 4px 16px rgba(241, 129, 27, 0.3));
}"""

new_footer_css = """.footer-logo-img {
  height: 60px;
  width: auto;
  max-width: 285px;
  object-fit: contain;
  display: block;
  filter: drop-shadow(0 2px 10px rgba(0, 0, 0, 0.45));
  transition: transform 0.25s ease, filter 0.25s ease;
}

.footer-brand:hover .footer-logo-img {
  transform: translateY(-2px);
  filter: drop-shadow(0 4px 16px rgba(255, 121, 0, 0.4));
}"""

if old_brand_css in css:
    css = css.replace(old_brand_css, new_brand_css)
    print("Replaced brand logo CSS!")
else:
    print("WARNING: old_brand_css not found directly")

if old_footer_css in css:
    css = css.replace(old_footer_css, new_footer_css)
    print("Replaced footer logo CSS!")
else:
    print("WARNING: old_footer_css not found directly")

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS saved!")
