# fix_cards_covering_buttons.py

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .hero-section padding to give ample bottom clearance
old_hero = '''.hero-section {
  position: relative;
  min-height: clamp(380px, 30vw, 440px);
  background: url('../assets/images/hero-logistics-global.webp') right top / cover no-repeat;
  background-color: #e5f1fd;
  padding: clamp(2.2rem, 3.8vh, 2.8rem) 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
}'''

new_hero = '''.hero-section {
  position: relative;
  min-height: clamp(400px, 32vw, 460px);
  background: url('../assets/images/hero-logistics-global.webp') right top / cover no-repeat;
  background-color: #e5f1fd;
  padding: 2.2rem 0 3.6rem 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
}'''

if old_hero in css:
    css = css.replace(old_hero, new_hero)
    print("Updated .hero-section padding-bottom to 3.6rem!")
else:
    print("Warning: old_hero not found")

# 2. Update .sectors-cards-bar-section margin-top from -2.8rem down to -0.9rem
old_sectors_bar = '''.sectors-cards-bar-section {
  position: relative;
  z-index: 10;
  margin-top: -2.8rem;
  margin-bottom: 0.5rem;
  padding: 0;
}'''

new_sectors_bar = '''.sectors-cards-bar-section {
  position: relative;
  z-index: 10;
  margin-top: -0.9rem;
  margin-bottom: 0.5rem;
  padding: 0;
}'''

if old_sectors_bar in css:
    css = css.replace(old_sectors_bar, new_sectors_bar)
    print("Updated .sectors-cards-bar-section margin-top to -0.9rem (moved down by ~30px)!")
else:
    print("Warning: old_sectors_bar not found")

# 3. Update .about-section padding-top
old_about = '.about-section {\n  padding-top: 5.5rem !important;\n}'
new_about = '.about-section {\n  padding-top: 4.8rem !important;\n}'

if old_about in css:
    css = css.replace(old_about, new_about)
    print("Updated .about-section padding-top to 4.8rem!")
else:
    print("Warning: old_about not found")

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("All card spacing adjustments applied!")
