with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace justify-content-center with flex-column justify-content-between or clean flex
old_right = """          <!-- Right Column: Exact Reference Content Layout (Equal Height) -->
          <div class="col-lg-6 d-flex flex-column justify-content-center fade-up-element">
            <div class="about-ref-content h-100 d-flex flex-column justify-content-center">"""

new_right = """          <!-- Right Column: Exact Reference Content Layout (Equal Height) -->
          <div class="col-lg-6 d-flex flex-column fade-up-element">
            <div class="about-ref-content h-100 d-flex flex-column justify-content-between">"""

if old_right in html:
    html = html.replace(old_right, new_right, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated index.html to justify-content-between!")

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure .about-ref-content uses flexbox properly
target_content_css = """.about-ref-content {
  padding-left: 0.85rem;
}"""

replacement_content_css = """.about-ref-content {
  padding-left: 0.85rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}"""

if target_content_css in css:
    css = css.replace(target_content_css, replacement_content_css, 1)
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated css/style.css for .about-ref-content!")
