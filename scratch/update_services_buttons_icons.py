import re

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace check-circle-fill with chevron-right in service-pro-checklist
def replace_service_checklist(match):
    block = match.group(0)
    block = block.replace("bi-check-circle-fill", "bi-chevron-right")
    return block

html_updated = re.sub(r'<ul class="service-pro-checklist">.*?</ul>', replace_service_checklist, html, flags=re.DOTALL)

# Replace the footer in all 5 cards
def replace_footer(match):
    block = match.group(0)
    key_match = re.search(r'data-service-key="([^"]+)"', block)
    if key_match:
        key = key_match.group(1)
        new_footer = f'''<div class="service-pro-footer">
                  <button type="button" class="btn-pro-readmore" data-service-key="{key}">
                    <span>Read More</span>
                    <i class="bi bi-arrow-right"></i>
                  </button>
                </div>'''
        return new_footer
    return block

html_updated = re.sub(r'<div class="service-pro-footer">.*?</div>', replace_footer, html_updated, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_updated)

print("Updated index.html successfully.")

# 2. Update css/style.css
with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Target block to replace in css/style.css
old_css_target = """/* Checklist (Exactly 3 Items - Compact) */
.service-pro-checklist {
  list-style: none;
  padding: 0;
  margin: 0 0 1rem 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.service-pro-checklist li {
  display: flex;
  align-items: flex-start;
  gap: 7px;
  font-family: var(--font-body);
  font-size: 0.82rem;
  color: #2c3e50;
  line-height: 1.38;
  font-weight: 500;
}

.service-pro-checklist li i {
  color: var(--accent-orange);
  font-size: 0.88rem;
  flex-shrink: 0;
  margin-top: 1px;
}

/* Card Footer (Compact) */
.service-pro-footer {
  margin-top: auto;
  padding-top: 0.8rem;
  border-top: 1px solid rgba(6, 43, 85, 0.06);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.btn-pro-readmore {
  background: transparent;
  color: var(--primary-navy);
  border: 1.5px solid rgba(6, 43, 85, 0.28);
  border-radius: 50px;
  padding: 0.38rem 0.85rem;
  font-family: var(--font-heading);
  font-size: 0.78rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  transition: all 0.25s ease;
  cursor: pointer;
}

.btn-pro-readmore:hover {
  background: var(--primary-navy);
  color: #ffffff;
  border-color: var(--primary-navy);
  transform: translateY(-1px);
}

.btn-pro-enquire {
  background: var(--accent-orange);
  color: #ffffff;
  border-radius: 50px;
  padding: 0.40rem 0.95rem;
  font-family: var(--font-heading);
  font-size: 0.78rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  text-decoration: none;
  box-shadow: 0 3px 8px rgba(255, 121, 0, 0.25);
  transition: all 0.25s ease;
}

.btn-pro-enquire:hover {
  background: var(--brand-orange-hover);
  color: #ffffff;
  transform: translateY(-1px);
  box-shadow: 0 5px 12px rgba(255, 121, 0, 0.35);
}"""

new_css_replacement = """/* Checklist (Simple Right Arrows) */
.service-pro-checklist {
  list-style: none;
  padding: 0;
  margin: 0 0 1.1rem 0;
  display: flex;
  flex-direction: column;
  gap: 7px;
}

.service-pro-checklist li {
  display: flex;
  align-items: flex-start;
  gap: 9px;
  font-family: var(--font-body);
  font-size: 0.83rem;
  color: #2c3e50;
  line-height: 1.42;
  font-weight: 500;
}

.service-pro-checklist li i {
  color: var(--accent-orange);
  font-size: 0.72rem;
  font-weight: 700;
  flex-shrink: 0;
  margin-top: 3px;
  transition: transform 0.22s ease, color 0.22s ease;
}

.service-pro-card:hover .service-pro-checklist li i {
  transform: translateX(3px);
  color: var(--brand-orange-hover);
}

/* Card Footer (Single Full-Width Sleek Button) */
.service-pro-footer {
  margin-top: auto;
  padding-top: 0.95rem;
  border-top: 1px solid rgba(6, 43, 85, 0.08);
}

.btn-pro-readmore {
  width: 100%;
  background: var(--primary-navy);
  color: #ffffff;
  border: 1.5px solid var(--primary-navy);
  border-radius: 50px;
  padding: 0.65rem 1.25rem;
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: 0.03em;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.28s ease;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(6, 43, 85, 0.12);
}

.btn-pro-readmore i {
  font-size: 0.85rem;
  transition: transform 0.25s ease;
}

.btn-pro-readmore:hover {
  background: var(--accent-orange);
  border-color: var(--accent-orange);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(255, 121, 0, 0.32);
}

.btn-pro-readmore:hover i {
  transform: translateX(4px);
}"""

# Normalize line endings before comparison
css_norm = css.replace("\r\n", "\n")
target_norm = old_css_target.replace("\r\n", "\n")
replacement_norm = new_css_replacement.replace("\r\n", "\n")

if target_norm in css_norm:
    css_updated = css_norm.replace(target_norm, replacement_norm)
    with open("css/style.css", "w", encoding="utf-8") as f:
        f.write(css_updated)
    print("Updated css/style.css successfully.")
else:
    print("WARNING: Could not find exact old_css_target in css/style.css!")
