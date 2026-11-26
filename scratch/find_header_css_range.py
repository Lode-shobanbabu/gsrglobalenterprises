with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

start_marker = '/* ==========================================================================\n   Top Corporate Utility Bar'
end_marker = '/* ==========================================================================\n   A. HOME / HERO SECTION'

idx1 = css.find(start_marker)
idx2 = css.find(end_marker)

print(f"Top/Header section in CSS: start={idx1}, end={idx2}")
