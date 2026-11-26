# update_hero_css_compact.py

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

target = '''.hero-section {
  position: relative;
  min-height: clamp(400px, 34vw, 470px);
  background: url('../assets/images/hero-logistics-global.webp') right top / cover no-repeat;
  background-color: #e5f1fd;
  padding: clamp(2.4rem, 4.5vh, 3.2rem) 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
}'''

replacement = '''.hero-section {
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

if target in css:
    css = css.replace(target, replacement)
    print("Updated hero-section height and padding to sleek compact dimensions!")
else:
    print("Target not found in style.css!")

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
