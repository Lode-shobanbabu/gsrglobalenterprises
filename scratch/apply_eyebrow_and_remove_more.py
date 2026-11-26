# scratch/apply_eyebrow_and_remove_more.py
import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# A. Remove "MORE" links from the 5 hero dock cards
# Each card has:
# <a href="#services" class="dock-card-more".*?</a>
more_pattern = r'\s*<a href="#services" class="dock-card-more"[^>]*>.*?</a>'
html_after_more_removal = re.sub(more_pattern, '', html, flags=re.DOTALL)

# B. Replace the pill in About Us with the unified brand eyebrow style:
# <div class="about-ref-pill mb-3">\s*<span>Who we Are</span>\s*</div>
eyebrow_pattern = r'<div class="about-ref-pill mb-3">\s*<span>Who we Are</span>\s*</div>'
replacement_eyebrow = '''<div class="about-eyebrow mb-3">
                <span class="about-eyebrow-dash"></span>
                <span class="about-eyebrow-text">WHO WE ARE</span>
                <span class="about-eyebrow-dash"></span>
              </div>'''

if re.search(eyebrow_pattern, html_after_more_removal, re.IGNORECASE):
    html_final = re.sub(eyebrow_pattern, replacement_eyebrow, html_after_more_removal, flags=re.IGNORECASE)
    print("Replaced about-ref-pill with about-eyebrow!")
else:
    # Try broader pattern if text varies
    broader_pattern = r'<div class="about-ref-pill[^"]*">.*?</div>'
    html_final = re.sub(broader_pattern, replacement_eyebrow, html_after_more_removal, count=1, flags=re.DOTALL)
    print("Replaced with broader pattern!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_final)

print("Updated index.html successfully!")

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update .dock-card-desc margin-bottom to 0
css = css.replace(
'''/* Bottom Action: MORE -> (Exact Reference Style) */
.dock-card-more {
  font-family: var(--font-heading);
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.10em;
  text-transform: uppercase;
  color: var(--primary-navy);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: auto;
  transition: all 0.25s ease;
}

.dock-card-more i {
  font-size: 0.82rem;
  transition: transform 0.25s ease;
}

.hero-dock-card:hover .dock-card-more {
  color: var(--accent-orange);
}

.hero-dock-card:hover .dock-card-more i {
  transform: translateX(4px);
}''',
'''/* Bottom margin adjusted as MORE link was removed */
.dock-card-desc {
  margin-bottom: 0;
}'''
)

# Add .about-eyebrow styles
about_eyebrow_css = '''/* Top Section Eyebrow: WHO WE ARE (Unified Brand Dash Style) */
.about-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 0.85rem;
}

.about-eyebrow-dash {
  width: 24px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.about-eyebrow-text {
  font-family: var(--font-heading);
  font-size: 0.80rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--primary-navy);
}
'''

# Replace .about-ref-pill CSS with .about-eyebrow CSS
old_pill_css = '''/* Top Outlined Pill: ABOUT US / WHO WE ARE (Exact Reference Style) */
.about-ref-pill {
  display: inline-block;
  border: 1.5px solid rgba(6, 43, 85, 0.18);
  background-color: #ffffff;
  border-radius: 50px;
  padding: 0.35rem 1.25rem;
  box-shadow: 0 2px 6px rgba(6, 43, 85, 0.04);
}

.about-ref-pill span {
  font-family: var(--font-heading);
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--primary-navy);
}'''

if old_pill_css in css:
    css = css.replace(old_pill_css, about_eyebrow_css)
    print("Replaced .about-ref-pill CSS with .about-eyebrow CSS!")
else:
    print("Warning: old_pill_css not found exactly, will check.")

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/style.css successfully!")
