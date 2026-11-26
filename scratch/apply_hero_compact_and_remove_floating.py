# apply_hero_compact_and_remove_floating.py

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove floating quick contact aside
floating_widget_start = '<!-- ==========================================================================\n       FLOATING QUICK CONTACT WIDGET'
floating_widget_end = '</aside>'

f_idx1 = html.find(floating_widget_start)
if f_idx1 != -1:
    f_idx2 = html.find(floating_widget_end, f_idx1)
    if f_idx2 != -1:
        f_idx2 += len(floating_widget_end)
        html = html[:f_idx1] + html[f_idx2:]
        print("Successfully removed floating quick contact widget (WhatsApp & Call icons) from index.html!")
    else:
        print("Warning: could not find floating_widget_end")
else:
    print("Warning: could not find floating_widget_start")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_start = '/* ==========================================================================\n   A. Hero Section'
css_end = '/* ==========================================================================\n   B. About Us Section'

c_idx1 = css.find(css_start)
c_idx2 = css.find(css_end)

if c_idx1 == -1 or c_idx2 == -1:
    print(f"Error finding CSS markers: c_idx1={c_idx1}, c_idx2={c_idx2}")
    exit(1)

new_hero_css = '''/* ==========================================================================
   A. Hero Section - Exact User Design Reference (Compact & Proportional)
   ========================================================================== */
.hero-section {
  position: relative;
  min-height: clamp(400px, 34vw, 470px);
  background: url('../assets/images/hero-logistics-global.webp') right top / cover no-repeat;
  background-color: #e5f1fd;
  padding: clamp(2.4rem, 4.5vh, 3.2rem) 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
}

.hero-container {
  position: relative;
  z-index: 2;
}

.hero-content-col {
  position: relative;
  z-index: 3;
}

.hero-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 0.75rem;
}

.hero-eyebrow-dash {
  width: 26px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.hero-eyebrow-text {
  font-family: var(--font-heading);
  font-size: 0.80rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--primary-navy);
}

/* Exact 3-Line Headline (Compact & Balanced Proportions) */
.hero-main-title {
  font-family: var(--font-heading);
  font-size: clamp(1.75rem, 2.45vw, 2.2rem);
  font-weight: 700;
  line-height: 1.20;
  letter-spacing: -0.02em;
  color: var(--primary-navy);
  margin-bottom: 0.85rem;
  max-width: 580px;
  white-space: normal;
}

.hero-title-line {
  display: inline-block;
  white-space: nowrap;
}

.hero-lead-desc {
  font-family: var(--font-body);
  font-size: clamp(0.88rem, 0.96vw, 0.94rem);
  font-weight: 400;
  color: var(--text-grey);
  line-height: 1.56;
  max-width: 510px;
  margin-bottom: 0.5rem;
}

.hero-sub-desc {
  font-family: var(--font-body);
  font-size: clamp(0.86rem, 0.92vw, 0.91rem);
  font-weight: 400;
  color: var(--text-grey);
  line-height: 1.54;
  max-width: 510px;
  margin-bottom: 1.5rem;
}

.hero-action-row {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  flex-wrap: wrap;
}

/* Primary CTA Button: Explore Our Services -> */
.btn-hero-primary {
  background-color: var(--accent-orange);
  color: #ffffff;
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 0.88rem;
  padding: 0.65rem 1.6rem;
  border-radius: 50px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 14px rgba(255, 121, 0, 0.35);
  border: none;
}

.btn-hero-primary:hover {
  background-color: var(--brand-orange-hover);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 121, 0, 0.45);
}

.btn-hero-primary i {
  transition: transform 0.2s ease;
}

.btn-hero-primary:hover i {
  transform: translateX(3px);
}

/* Secondary CTA Button: Circular Chat Badge with Text */
.btn-hero-secondary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  color: var(--primary-navy);
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 0.88rem;
  text-decoration: none;
  transition: color 0.2s ease;
}

.btn-hero-secondary .btn-icon-circle {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  border: 1.5px solid rgba(6, 43, 85, 0.35);
  background-color: #d2e4f7;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--primary-navy);
  font-size: 0.90rem;
  transition: all 0.25s ease;
}

.btn-hero-secondary:hover {
  color: var(--accent-orange);
}

.btn-hero-secondary:hover .btn-icon-circle {
  border-color: var(--accent-orange);
  background-color: var(--accent-orange);
  color: #ffffff;
  transform: scale(1.06);
}

/* Clean spacing for About Section */
.about-section {
  padding-top: 4.5rem !important;
}

.text-orange {
  color: var(--brand-orange) !important;
}

.bg-orange {
  background-color: var(--brand-orange) !important;
}

/* Hide floating contact buttons */
.floating-quick-contact {
  display: none !important;
}

@media (max-width: 991.98px) {
  .hero-section {
    padding: 2.8rem 0;
    min-height: auto;
    background-position: right 15% top;
  }

  .about-section {
    padding-top: 3.5rem !important;
  }
}

@media (max-width: 767.98px) {
  .hero-title-line {
    white-space: normal;
  }
}

@media (max-width: 575.98px) {
  .hero-main-title {
    font-size: 1.6rem;
  }

  .hero-action-row {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.85rem;
  }
}

'''

css = css[:c_idx1] + new_hero_css + css[c_idx2:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/style.css: Hero section height reduced, globe placed cleanly with top sky, floating widgets hidden!")
