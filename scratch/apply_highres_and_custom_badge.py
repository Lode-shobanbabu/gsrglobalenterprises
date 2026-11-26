# scratch/apply_highres_and_custom_badge.py

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_html = '''          <!-- Left Column: Exact Reference Geometric Cutout Image with Experience Badge -->
          <div class="col-lg-6 fade-up-element">
            <div class="about-ref-media-box">
              <picture>
                <source srcset="assets/images/about-reference-exact.webp" type="image/webp">
                <img src="assets/images/about-reference-exact.png"
                  alt="GSR Global Enterprises Corporate Team Consultation and Procurement Strategy"
                  class="about-ref-img" width="732" height="568" loading="lazy">
              </picture>
            </div>
          </div>'''

replacement_html = '''          <!-- Left Column: High-Resolution Geometric Cutout Image with Customizable Experience Badge -->
          <div class="col-lg-6 fade-up-element">
            <div class="about-ref-media-box">
              <!-- Geometric Framed Image Container -->
              <div class="about-ref-img-frame-wrap">
                <div class="about-ref-img-frame">
                  <picture>
                    <source srcset="assets/images/about-corporate-team-meeting.webp" type="image/webp">
                    <img src="assets/images/about-corporate-team-meeting.jpg"
                      alt="GSR Global Enterprises Corporate Team Consultation and Procurement Strategy"
                      class="about-ref-img" width="1200" height="896" loading="lazy">
                  </picture>
                </div>
              </div>

              <!-- Customizable Experience Badge (Directly editable in HTML) -->
              <div class="about-ref-exp-badge" aria-label="Company Experience Badge">
                <span class="exp-badge-number">30+</span>
                <div class="exp-badge-labels">
                  <span class="exp-badge-line">Years</span>
                  <span class="exp-badge-line">Experience</span>
                </div>
              </div>
            </div>
          </div>'''

if target_html in html:
    html = html.replace(target_html, replacement_html)
    print("Found exact target_html in index.html and replaced!")
else:
    # Try finding with regex or markers
    import re
    pattern = r'<!-- Left Column:.*?<div class="col-lg-6 fade-up-element">\s*<div class="about-ref-media-box">.*?</div>\s*</div>'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        html = html[:match.start()] + replacement_html + html[match.end():]
        print("Replaced via regex in index.html!")
    else:
        print("Error: Could not locate left column in index.html!")
        exit(1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

c_start = '/* ==========================================================================\n   B. About Us Section - Exact Reference Design Style (Corporate Consulting)'
c_end = '/* ==========================================================================\n   C. Services Section - Compact 3 Cards Per Row'

c_idx1 = css.find(c_start)
c_idx2 = css.find(c_end)

if c_idx1 == -1 or c_idx2 == -1:
    print(f"Error finding CSS markers: c_idx1={c_idx1}, c_idx2={c_idx2}")
    exit(1)

new_about_css = '''/* ==========================================================================
   B. About Us Section - Exact Reference Design Style (Corporate Consulting)
   ========================================================================== */
.about-section {
  padding: 3.5rem 0 3.8rem;
  background-color: #ffffff;
  position: relative;
  border-bottom: 1px solid rgba(6, 43, 85, 0.06);
}

/* Left Column: Geometric Cutout Frame & Customizable Floating Badge */
.about-ref-media-box {
  position: relative;
  display: block;
  width: 100%;
  max-width: 530px;
  margin: 0 auto;
}

/* Shadow Wrapper for Polygon Clip-Path */
.about-ref-img-frame-wrap {
  filter: drop-shadow(0 16px 36px rgba(6, 43, 85, 0.12));
  transition: filter 0.4s ease;
}

.about-ref-media-box:hover .about-ref-img-frame-wrap {
  filter: drop-shadow(0 22px 46px rgba(6, 43, 85, 0.18));
}

/* Geometric Cutout Frame (Exact Reference Polygon) */
.about-ref-img-frame {
  position: relative;
  width: 100%;
  aspect-ratio: 4 / 3;
  overflow: hidden;
  clip-path: polygon(
    0% 28px,
    28px 0%,
    50% 0%,
    58% 13%,
    66% 0%,
    calc(100% - 24px) 0%,
    100% 24px,
    100% 100%,
    75px 100%,
    0% calc(100% - 75px)
  );
  background-color: var(--primary-navy);
}

.about-ref-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 25%;
  display: block;
  transition: transform 0.65s cubic-bezier(0.16, 1, 0.3, 1);
}

.about-ref-media-box:hover .about-ref-img {
  transform: scale(1.04);
}

/* Customizable Experience Badge (Code-Based, HTML Editable) */
.about-ref-exp-badge {
  position: absolute;
  bottom: 14px;
  right: 14px;
  background-color: var(--primary-navy);
  color: #ffffff;
  padding: 0.95rem 1.45rem;
  border-radius: 14px;
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  box-shadow: 0 10px 26px rgba(6, 43, 85, 0.38);
  border: 1.5px solid rgba(255, 255, 255, 0.18);
  backdrop-filter: blur(8px);
  z-index: 5;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.about-ref-media-box:hover .about-ref-exp-badge {
  transform: translateY(-4px) scale(1.03);
  box-shadow: 0 14px 32px rgba(6, 43, 85, 0.45);
  border-color: rgba(255, 121, 0, 0.45);
}

.exp-badge-number {
  font-family: var(--font-heading);
  font-size: 2.15rem;
  font-weight: 800;
  line-height: 1;
  color: #ffffff;
  letter-spacing: -0.02em;
  margin-bottom: 0.25rem;
}

.exp-badge-labels {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.exp-badge-line {
  font-family: var(--font-heading);
  font-size: 0.76rem;
  font-weight: 600;
  line-height: 1.25;
  color: rgba(255, 255, 255, 0.92);
  letter-spacing: 0.02em;
}

/* Right Column Content */
.about-ref-content {
  padding-left: 0.85rem;
}

/* Top Outlined Pill: ABOUT US / WHO WE ARE (Exact Reference Style) */
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
}

/* Main Corporate Headline (Exact Reference Proportions) */
.about-ref-title {
  font-family: var(--font-heading);
  font-size: clamp(1.75rem, 2.35vw, 2.25rem);
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.22;
  letter-spacing: -0.02em;
}

/* Body Text (Crisp Corporate Typography) */
.about-ref-p {
  font-family: var(--font-body);
  font-size: 0.88rem;
  color: #475569;
  line-height: 1.58;
}

.about-ref-lead {
  font-size: 0.92rem;
  color: #334155;
}

.about-ref-p strong {
  color: var(--primary-navy);
  font-weight: 700;
}

/* CTA Button (Exact Reference Pill with Diagonal Arrow & Brand Colors) */
.about-ref-cta-wrap {
  margin-top: 0.5rem;
}

.btn-ref-cta {
  background-color: var(--primary-navy);
  color: #ffffff;
  padding: 0.72rem 1.85rem;
  border-radius: 50px;
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  box-shadow: 0 4px 16px rgba(6, 43, 85, 0.22);
  transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
  border: 1.5px solid transparent;
}

.btn-ref-cta i {
  font-size: 0.92rem;
  transition: transform 0.25s ease;
}

.btn-ref-cta:hover {
  background-color: var(--accent-orange);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(255, 121, 0, 0.38);
  border-color: var(--accent-orange);
}

.btn-ref-cta:hover i {
  transform: translate(2px, -2px);
}

/* Responsive adjustments */
@media (max-width: 991.98px) {
  .about-section {
    padding: 2.8rem 0;
  }

  .about-ref-content {
    padding-left: 0;
    margin-top: 1.25rem;
  }

  .about-ref-media-box {
    max-width: 480px;
  }

  .about-ref-exp-badge {
    bottom: 10px;
    right: 10px;
    padding: 0.75rem 1.15rem;
  }

  .exp-badge-number {
    font-size: 1.75rem;
  }
}

@media (max-width: 575.98px) {
  .about-ref-title {
    font-size: 1.55rem;
  }

  .about-ref-img-frame {
    aspect-ratio: 16 / 11;
  }

  .about-ref-exp-badge {
    padding: 0.65rem 1rem;
    bottom: 8px;
    right: 8px;
  }

  .exp-badge-number {
    font-size: 1.5rem;
  }

  .exp-badge-line {
    font-size: 0.70rem;
  }

  .btn-ref-cta {
    width: 100%;
    justify-content: center;
  }
}

'''

css = css[:c_idx1] + new_about_css + css[c_idx2:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/style.css with high-res & customizable badge styles!")
