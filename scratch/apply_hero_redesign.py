# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

hero_start = '<!-- ==========================================================================\n         A. HOME / HERO SECTION'
hero_end = '<!-- ==========================================================================\n         B. ABOUT US SECTION'

idx1 = html.find(hero_start)
idx2 = html.find(hero_end)

if idx1 == -1 or idx2 == -1:
    print(f"Error finding hero markers in index.html: idx1={idx1}, idx2={idx2}")
    exit(1)

new_hero_html = '''<!-- ==========================================================================
         A. HOME / HERO SECTION - GLOBAL LOGISTICS & SOURCING (EXACT REFERENCE DESIGN)
         ========================================================================== -->
    <section class="hero-section" id="hero">
      <div class="container hero-container">
        <div class="row align-items-center">
          <div class="col-lg-8 col-xl-7 hero-content-col">

            <!-- Eyebrow Tagline (Matching Screenshot 1 & 2) -->
            <div class="hero-eyebrow fade-up-element">
              <span class="hero-eyebrow-dash"></span>
              <span class="hero-eyebrow-text">YOUR TRUSTED PROCUREMENT &amp; SUPPLY PARTNER</span>
            </div>

            <!-- Main Headline (Matching Screenshot 2) -->
            <h1 class="hero-main-title fade-up-element">
              Connecting Industries with the Right Products, <br class="d-none d-md-inline">
              <span class="hero-headline-accent">Resources &amp; Solutions</span>
            </h1>

            <!-- Body Paragraphs (Matching Screenshot 2) -->
            <p class="hero-lead-desc fade-up-element">
              From medical equipment and IT infrastructure to industrial materials, automotive components and renewable energy solutions, GSR Global Enterprises delivers reliable procurement and supply services tailored to diverse industry requirements.
            </p>
            <p class="hero-sub-desc fade-up-element">
              We simplify sourcing, streamline procurement and help organizations access the products and resources they need to move forward.
            </p>

            <!-- CTA Buttons Row (Matching Screenshot 1 & 2) -->
            <div class="hero-action-row fade-up-element">
              <a href="#services" class="btn-hero-primary" aria-label="Explore Our Services">
                <span>Explore Our Services</span>
                <i class="bi bi-arrow-right ms-1"></i>
              </a>
              <a href="#contact" class="btn-hero-secondary" aria-label="Discuss Your Requirements">
                <span class="btn-icon-circle"><i class="bi bi-chat-text-fill"></i></span>
                <span>Discuss Your Requirements</span>
              </a>
            </div>

          </div>
        </div>
      </div>

      <!-- Floating Services Bar (Exact Reference Design Matching Screenshot 3) -->
      <div class="hero-services-bar-wrapper fade-up-element">
        <div class="container">
          <div class="hero-services-bar">

            <!-- 1. Medical & Healthcare Supplies -->
            <a href="#services" class="hero-service-card" title="Medical & Healthcare Supplies">
              <div class="hero-service-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="m10.5 20.5 10-10a4.95 4.95 0 1 0-7-7l-10 10a4.95 4.95 0 1 0 7 7Z"/>
                  <path d="m8.5 8.5 7 7"/>
                </svg>
              </div>
              <span class="hero-service-label">Medical &amp;<br>Healthcare Supplies</span>
            </a>

            <div class="hero-service-divider"></div>

            <!-- 2. Computers & Infrastructure -->
            <a href="#services" class="hero-service-card" title="Computers & Infrastructure">
              <div class="hero-service-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect width="20" height="14" x="2" y="3" rx="2"/>
                  <line x1="8" x2="16" y1="21" y2="21"/>
                  <line x1="12" x2="12" y1="17" y2="21"/>
                </svg>
              </div>
              <span class="hero-service-label">Computers &amp;<br>Infrastructure</span>
            </a>

            <div class="hero-service-divider"></div>

            <!-- 3. Iron & Steel and Yarn -->
            <a href="#services" class="hero-service-card" title="Iron & Steel and Yarn">
              <div class="hero-service-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <ellipse cx="12" cy="5" rx="8" ry="3"/>
                  <path d="M4 5v14c0 1.66 3.58 3 8 3s8-1.34 8-3V5"/>
                  <path d="M4 12c0 1.66 3.58 3 8 3s8-1.34 8-3"/>
                </svg>
              </div>
              <span class="hero-service-label">Iron &amp; Steel<br>and Yarn</span>
            </a>

            <div class="hero-service-divider"></div>

            <!-- 4. Automobile Industry Parts -->
            <a href="#services" class="hero-service-card" title="Automobile Industry Parts">
              <div class="hero-service-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9C2.1 11.2 2 11.6 2 12v4c0 .6.4 1 1 1h2"/>
                  <circle cx="7" cy="17" r="2"/>
                  <path d="M9 17h6"/>
                  <circle cx="17" cy="17" r="2"/>
                </svg>
              </div>
              <span class="hero-service-label">Automobile Industry<br>Parts</span>
            </a>

            <div class="hero-service-divider"></div>

            <!-- 5. Solar Panels Procurement -->
            <a href="#services" class="hero-service-card" title="Solar Panels Procurement">
              <div class="hero-service-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="3.5" r="1.5"/>
                  <path d="m5 5 1.2 1.2"/>
                  <path d="m17.8 6.2 1.2-1.2"/>
                  <rect width="18" height="12" x="3" y="9" rx="1.5"/>
                  <line x1="3" x2="21" y1="15" y2="15"/>
                  <line x1="9" x2="9" y1="9" y2="21"/>
                  <line x1="15" x2="15" y1="9" y2="21"/>
                </svg>
              </div>
              <span class="hero-service-label">Solar Panels<br>Procurement</span>
            </a>

          </div>
        </div>
      </div>
    </section>

    '''

html = html[:idx1] + new_hero_html + html[idx2:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html hero section successfully!")

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_start_marker = '/* ==========================================================================\n   A. Hero Section - Cinematic Boardroom Photography'
css_end_marker = '/* ==========================================================================\n   B. About Us Section'

c_idx1 = css.find(css_start_marker)
c_idx2 = css.find(css_end_marker)

if c_idx1 == -1 or c_idx2 == -1:
    print(f"Error finding CSS markers: c_idx1={c_idx1}, c_idx2={c_idx2}")
    exit(1)

new_hero_css = '''/* ==========================================================================
   A. Hero Section - Global Logistics & Supply Chain (Matching Screenshot 1 & 3)
   ========================================================================== */
.hero-section {
  position: relative;
  min-height: clamp(620px, 86vh, 760px);
  background: url('../assets/images/hero-logistics-global.webp') right center/cover no-repeat;
  background-color: #f4f8fc;
  padding: 5.5rem 0 7rem 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: visible;
}

/* Atmospheric light gradient on left to ensure high text contrast */
.hero-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(90deg, rgba(244, 248, 252, 0.98) 0%, rgba(244, 248, 252, 0.94) 44%, rgba(244, 248, 252, 0.55) 62%, transparent 100%);
  pointer-events: none;
  z-index: 1;
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
  gap: 12px;
  margin-bottom: 1.15rem;
}

.hero-eyebrow-dash {
  width: 32px;
  height: 3.5px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.hero-eyebrow-text {
  font-family: var(--font-heading);
  font-size: 0.88rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--primary-navy);
}

.hero-main-title {
  font-family: var(--font-heading);
  font-size: clamp(2.3rem, 4.3vw, 3.85rem);
  font-weight: 700;
  line-height: 1.16;
  letter-spacing: -0.025em;
  color: var(--primary-navy);
  margin-bottom: 1.4rem;
}

.hero-headline-accent {
  color: var(--primary-navy);
}

.hero-lead-desc {
  font-family: var(--font-body);
  font-size: clamp(1rem, 1.15vw, 1.08rem);
  font-weight: 400;
  color: var(--text-grey);
  line-height: 1.68;
  max-width: 630px;
  margin-bottom: 0.85rem;
}

.hero-sub-desc {
  font-family: var(--font-body);
  font-size: clamp(0.96rem, 1.1vw, 1.02rem);
  font-weight: 400;
  color: var(--text-grey);
  line-height: 1.65;
  max-width: 630px;
  margin-bottom: 2.25rem;
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
  font-size: 0.96rem;
  padding: 0.75rem 1.85rem;
  border-radius: 50px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 16px rgba(255, 121, 0, 0.35);
  border: none;
}

.btn-hero-primary:hover {
  background-color: var(--brand-orange-hover);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 6px 22px rgba(255, 121, 0, 0.45);
}

.btn-hero-primary i {
  transition: transform 0.2s ease;
}

.btn-hero-primary:hover i {
  transform: translateX(3px);
}

/* Secondary CTA Button: Discuss Your Requirements with circular icon */
.btn-hero-secondary {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  color: var(--primary-navy);
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 0.96rem;
  text-decoration: none;
  transition: color 0.2s ease;
}

.btn-hero-secondary .btn-icon-circle {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  border: 2px solid var(--primary-navy);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--primary-navy);
  font-size: 1rem;
  transition: all 0.25s ease;
  background-color: rgba(255, 255, 255, 0.85);
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

/* ==========================================================================
   Floating Services Bar (Matching Screenshot 3)
   ========================================================================== */
.hero-services-bar-wrapper {
  position: relative;
  z-index: 5;
  margin-top: 3.8rem;
  margin-bottom: -4.2rem;
}

.hero-services-bar {
  background: #ffffff;
  border-radius: 14px;
  border: 1px solid rgba(6, 43, 85, 0.1);
  box-shadow: 0 10px 36px rgba(6, 43, 85, 0.10), 0 2px 8px rgba(6, 43, 85, 0.04);
  display: flex;
  align-items: stretch;
  justify-content: space-between;
  padding: 1.35rem 1rem;
}

.hero-service-card {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 12px;
  padding: 0.5rem 0.85rem;
  text-decoration: none;
  transition: transform 0.25s ease;
  color: var(--primary-navy);
}

.hero-service-icon {
  width: 46px;
  height: 46px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--primary-navy);
  transition: color 0.25s ease, transform 0.25s ease;
}

.hero-service-label {
  font-family: var(--font-heading);
  font-size: 0.90rem;
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.32;
  transition: color 0.25s ease;
}

.hero-service-card:hover {
  transform: translateY(-4px);
}

.hero-service-card:hover .hero-service-icon {
  color: var(--accent-orange);
  transform: scale(1.1);
}

.hero-service-card:hover .hero-service-label {
  color: var(--accent-orange);
}

.hero-service-divider {
  width: 1px;
  background-color: rgba(6, 43, 85, 0.12);
  align-self: stretch;
  margin: 0.4rem 0;
}

/* Adjust About Section Top Padding to accommodate Floating Services Bar */
.about-section {
  padding-top: 6.8rem !important;
}

.text-orange {
  color: var(--brand-orange) !important;
}

.bg-orange {
  background-color: var(--brand-orange) !important;
}

@media (max-width: 991.98px) {
  .hero-section {
    padding: 3.8rem 0 4rem 0;
    min-height: auto;
  }

  .hero-section::before {
    background: linear-gradient(180deg, rgba(244, 248, 252, 0.96) 0%, rgba(244, 248, 252, 0.92) 100%);
  }

  .hero-services-bar-wrapper {
    margin-top: 2.5rem;
    margin-bottom: 0;
  }

  .hero-services-bar {
    flex-wrap: wrap;
    gap: 1.25rem 0;
    padding: 1.25rem 0.5rem;
  }

  .hero-service-card {
    flex: 0 0 50%;
  }

  .hero-service-divider {
    display: none;
  }

  .about-section {
    padding-top: 4rem !important;
  }
}

@media (max-width: 575.98px) {
  .hero-service-card {
    flex: 0 0 100%;
    padding: 0.75rem 0.5rem;
    border-bottom: 1px solid rgba(6, 43, 85, 0.06);
  }

  .hero-service-card:last-child {
    border-bottom: none;
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

print("Updated css/style.css hero section successfully!")
