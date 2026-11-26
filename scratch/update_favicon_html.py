with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update favicon links
old_fav = """  <!-- Favicon Monogram (Brand Navy & Accent Orange) -->
  <link rel="icon" type="image/svg+xml"
    href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='16' fill='%23062B55'/><path d='M28 68V32h24c8 0 14 5 14 13s-6 13-14 13H42v10H28zm14-20h10c3 0 5-2 5-5s-2-5-5-5H42v10z' fill='%23FF7900'/><circle cx='72' cy='68' r='6' fill='%23FF7900'/></svg>">"""

new_fav = """  <!-- Official Brand Favicons (Cropped from Official Client Emblem) -->
  <link rel="icon" type="image/png" sizes="32x32" href="assets/images/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="assets/images/favicon-16.png">
  <link rel="apple-touch-icon" sizes="128x128" href="assets/images/favicon-128.png">"""

if old_fav in html:
    html = html.replace(old_fav, new_fav)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated favicon links in index.html!")
else:
    print("Old favicon marker not found directly, checking partial...")
    idx = html.find('<!-- Favicon')
    if idx != -1:
        end_idx = html.find('<!-- Google Fonts', idx)
        print("Existing favicon block:\n", html[idx:end_idx])
