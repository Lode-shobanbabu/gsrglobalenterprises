# apply_user_target_hero.py
import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate hero section
hero_start = '<!-- ==========================================================================\n         A. HOME / HERO SECTION'
hero_end = '<!-- ==========================================================================\n         B. ABOUT US SECTION'

idx1 = html.find(hero_start)
idx2 = html.find(hero_end)

if idx1 == -1 or idx2 == -1:
    print(f"Error finding hero markers: idx1={idx1}, idx2={idx2}")
    exit(1)

new_hero_html = '''<!-- ==========================================================================
         A. HOME / HERO SECTION - EXACT USER DESIGN REFERENCE
         ========================================================================== -->
    <section class="hero-section" id="hero">
      <div class="container hero-container">
        <div class="row align-items-center">
          <div class="col-lg-8 col-xl-7 hero-content-col">

            <!-- Eyebrow Tagline (Matching User Image Reference) -->
            <div class="hero-eyebrow fade-up-element">
              <span class="hero-eyebrow-dash"></span>
              <span class="hero-eyebrow-text">YOUR TRUSTED PROCUREMENT &amp; SUPPLY PARTNER</span>
            </div>

            <!-- Main Headline (Exact 3-Line Composition Matching Image 1) -->
            <h1 class="hero-main-title fade-up-element">
              <span class="hero-title-line">Connecting Industries with</span><br>
              <span class="hero-title-line">the Right Products,</span><br>
              <span class="hero-title-line">Resources &amp; Solutions</span>
            </h1>

            <!-- Body Descriptions -->
            <p class="hero-lead-desc fade-up-element">
              From medical equipment and IT infrastructure to industrial materials, automotive components and renewable energy solutions, GSR Global Enterprises delivers reliable procurement and supply services tailored to diverse industry requirements.
            </p>
            <p class="hero-sub-desc fade-up-element">
              We simplify sourcing, streamline procurement and help organizations access the products and resources they need to move forward.
            </p>

            <!-- CTA Action Buttons -->
            <div class="hero-action-row fade-up-element">
              <a href="#services" class="btn-hero-primary" aria-label="Explore Our Services">
                <span>Explore Our Services</span>
                <i class="bi bi-arrow-right ms-1"></i>
              </a>
              <a href="#contact" class="btn-hero-secondary" aria-label="Discuss Your Requirements">
                <span class="btn-icon-circle"><i class="bi bi-chat-left-text-fill"></i></span>
                <span>Discuss Your Requirements</span>
              </a>
            </div>

          </div>
        </div>
      </div>
    </section>

    '''

html = html[:idx1] + new_hero_html + html[idx2:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html: Hero section matches Image 1 exactly (3 balanced lines, no bottom cards)!")

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
   A. Hero Section - Exact User Design Reference (Image 1 & Image 2)
   ========================================================================== */
.hero-section {
  position: relative;
  min-height: clamp(500px, 46vw, 640px);
  background: url('../assets/images/hero-logistics-global.webp') right center/cover no-repeat;
  background-color: #e5f1fd;
  padding: clamp(3.8rem, 6vh, 5.2rem) 0;
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
  margin-bottom: 0.95rem;
}

.hero-eyebrow-dash {
  width: 28px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.hero-eyebrow-text {
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--primary-navy);
}

/* Exact 3-Line Headline (Proportions Matching Reference Image 1) */
.hero-main-title {
  font-family: var(--font-heading);
  font-size: clamp(1.85rem, 2.7vw, 2.45rem);
  font-weight: 700;
  line-height: 1.22;
  letter-spacing: -0.02em;
  color: var(--primary-navy);
  margin-bottom: 1.15rem;
  max-width: 620px;
  white-space: normal;
}

.hero-title-line {
  display: inline-block;
  white-space: nowrap;
}

.hero-lead-desc {
  font-family: var(--font-body);
  font-size: clamp(0.92rem, 1.02vw, 0.98rem);
  font-weight: 400;
  color: var(--text-grey);
  line-height: 1.62;
  max-width: 530px;
  margin-bottom: 0.65rem;
}

.hero-sub-desc {
  font-family: var(--font-body);
  font-size: clamp(0.90rem, 1vw, 0.95rem);
  font-weight: 400;
  color: var(--text-grey);
  line-height: 1.6;
  max-width: 530px;
  margin-bottom: 1.85rem;
}

.hero-action-row {
  display: flex;
  align-items: center;
  gap: 1.35rem;
  flex-wrap: wrap;
}

/* Primary CTA Button: Explore Our Services -> */
.btn-hero-primary {
  background-color: var(--accent-orange);
  color: #ffffff;
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 0.92rem;
  padding: 0.72rem 1.7rem;
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
  gap: 12px;
  color: var(--primary-navy);
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 0.92rem;
  text-decoration: none;
  transition: color 0.2s ease;
}

.btn-hero-secondary .btn-icon-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1.5px solid rgba(6, 43, 85, 0.35);
  background-color: #d2e4f7;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--primary-navy);
  font-size: 0.95rem;
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
  padding-top: 4.85rem !important;
}

.text-orange {
  color: var(--brand-orange) !important;
}

.bg-orange {
  background-color: var(--brand-orange) !important;
}

@media (max-width: 991.98px) {
  .hero-section {
    padding: 3.5rem 0;
    min-height: auto;
    background-position: right 20% center;
  }

  .about-section {
    padding-top: 3.8rem !important;
  }
}

@media (max-width: 767.98px) {
  .hero-title-line {
    white-space: normal;
  }
}

@media (max-width: 575.98px) {
  .hero-main-title {
    font-size: 1.7rem;
  }

  .hero-action-row {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }
}

'''

css = css[:c_idx1] + new_hero_css + css[c_idx2:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/style.css: Exact user reference hero styling applied!")
