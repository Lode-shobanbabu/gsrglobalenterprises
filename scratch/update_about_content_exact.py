# scratch/update_about_content_exact.py

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sec_start = '<!-- ==========================================================================\n         B. ABOUT US SECTION'
sec_end = '<!-- ==========================================================================\n         C. OUR SERVICES'

idx1 = html.find(sec_start)
idx2 = html.find(sec_end)

if idx1 == -1 or idx2 == -1:
    print(f"Error finding markers: idx1={idx1}, idx2={idx2}")
    exit(1)

new_about_html = '''<!-- ==========================================================================
         B. ABOUT US SECTION (CORPORATE STYLE - EXACT USER CONTENT)
         ========================================================================== -->
    <section class="about-section" id="about">
      <div class="container">

        <div class="row align-items-center g-4 g-lg-5">

          <!-- Left Column: Corporate Imagery Showcase with Floating Trust Card -->
          <div class="col-lg-6 fade-up-element">
            <div class="about-corp-media-wrap">
              <!-- Main Corporate Photograph -->
              <div class="about-corp-main-img">
                <img src="assets/images/hero-corporate-meeting.webp"
                  alt="GSR Global Enterprises Senior Management and Procurement Operations" loading="lazy">
              </div>

              <!-- Floating Trust Badge: Experience & Credentials -->
              <div class="about-corp-badge">
                <div class="about-corp-badge-icon">
                  <i class="bi bi-shield-check"></i>
                </div>
                <div class="about-corp-badge-text">
                  <div class="about-corp-badge-num">10+ Years</div>
                  <div class="about-corp-badge-label">Procurement &amp; Supply Excellence</div>
                </div>
              </div>

              <!-- Floating Credential Card (Top Right) -->
              <div class="about-corp-cert-pill d-none d-sm-flex">
                <i class="bi bi-patch-check-fill"></i>
                <span>100% Tax &amp; GST Invoicing</span>
              </div>
            </div>
          </div>

          <!-- Right Column: Corporate Narrative & Procurement Solutions -->
          <div class="col-lg-6 fade-up-element">
            <div class="about-corp-content">

              <!-- Eyebrow -->
              <div class="about-corp-eyebrow mb-2">
                <span class="about-corp-eyebrow-dash"></span>
                <span class="about-corp-eyebrow-text">ABOUT GSR GLOBAL ENTERPRISES</span>
              </div>

              <!-- Main Title -->
              <h2 class="about-corp-title mb-3">
                Reliable Procurement &amp; Supply Services Tailored to Diverse Industry Requirements
              </h2>

              <!-- Core User Content Statement -->
              <p class="about-corp-lead mb-4">
                From medical equipment and IT infrastructure to industrial materials, automotive components and renewable energy solutions, <strong>GSR Global Enterprises</strong> delivers reliable procurement and supply services tailored to diverse industry requirements.
              </p>

              <!-- 4 Corporate Capability Cards -->
              <div class="row g-3 about-corp-feature-grid mb-4">
                <div class="col-sm-6">
                  <div class="about-corp-feature-card">
                    <div class="about-feature-icon">
                      <i class="bi bi-box-seam-fill"></i>
                    </div>
                    <div>
                      <h4 class="about-feature-title">Multi-Sector Sourcing</h4>
                      <p class="about-feature-desc">Comprehensive supply coverage across healthcare, IT, steel, auto &amp; solar.</p>
                    </div>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="about-corp-feature-card">
                    <div class="about-feature-icon">
                      <i class="bi bi-shield-check"></i>
                    </div>
                    <div>
                      <h4 class="about-feature-title">Direct OEM Channels</h4>
                      <p class="about-feature-desc">Direct mill-origin partnerships eliminating unnecessary layers and markups.</p>
                    </div>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="about-corp-feature-card">
                    <div class="about-feature-icon">
                      <i class="bi bi-patch-check-fill"></i>
                    </div>
                    <div>
                      <h4 class="about-feature-title">Verified Inspections</h4>
                      <p class="about-feature-desc">Rigorous pre-dispatch testing, standard MTR reports, and warranty support.</p>
                    </div>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="about-corp-feature-card">
                    <div class="about-feature-icon">
                      <i class="bi bi-geo-alt-fill"></i>
                    </div>
                    <div>
                      <h4 class="about-feature-title">Regional AP Logistics</h4>
                      <p class="about-feature-desc">Dual regional distribution hubs ensuring rapid, dependable on-site handover.</p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Corporate CTA Actions -->
              <div class="about-corp-actions d-flex align-items-center gap-3 flex-wrap">
                <a href="#services" class="btn-corp-primary">
                  <span>Explore Our Services</span>
                  <i class="bi bi-arrow-right ms-1"></i>
                </a>
                <a href="#contact" class="btn-corp-outline">
                  <i class="bi bi-telephone-fill me-1"></i>
                  <span>Contact Sourcing Desk</span>
                </a>
              </div>

            </div>
          </div>

        </div>

        <!-- Corporate Statistics Banner (Spanning Width with Crisp Dividers) -->
        <div class="about-corp-stats-bar mt-5 fade-up-element">
          <div class="row g-0 text-center align-items-center">

            <div class="col-6 col-lg-3 about-stat-border">
              <div class="about-stat-item">
                <div class="about-stat-number">100+</div>
                <div class="about-stat-text">Verified Consignments</div>
              </div>
            </div>

            <div class="col-6 col-lg-3 about-stat-border">
              <div class="about-stat-item">
                <div class="about-stat-number">5+</div>
                <div class="about-stat-text">Core Industry Sectors</div>
              </div>
            </div>

            <div class="col-6 col-lg-3 about-stat-border">
              <div class="about-stat-item">
                <div class="about-stat-number">2</div>
                <div class="about-stat-text">Regional AP Hubs</div>
              </div>
            </div>

            <div class="col-6 col-lg-3">
              <div class="about-stat-item">
                <div class="about-stat-number">100%</div>
                <div class="about-stat-text">GST &amp; Tax Compliant</div>
              </div>
            </div>

          </div>
        </div>

      </div>
    </section>

    '''

html = html[:idx1] + new_about_html + html[idx2:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html: exact user content applied and mission/vision removed!")

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

c_start = '/* ==========================================================================\n   B. About Us Section'
c_end = '/* ==========================================================================\n   C. Services Section'

c_idx1 = css.find(c_start)
c_idx2 = css.find(c_end)

if c_idx1 == -1 or c_idx2 == -1:
    print(f"Error finding CSS markers for About: c_idx1={c_idx1}, c_idx2={c_idx2}")
    exit(1)

new_about_css = '''/* ==========================================================================
   B. About Us Section - Clean, High-Trust Corporate Style
   ========================================================================== */
.about-section {
  padding: 5rem 0 5.5rem;
  background-color: #ffffff;
  position: relative;
  border-bottom: 1px solid rgba(6, 43, 85, 0.06);
}

/* Corporate Media Showcase (Left Column) */
.about-corp-media-wrap {
  position: relative;
  padding-bottom: 2rem;
  padding-right: 1.25rem;
}

.about-corp-main-img {
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 16px 44px rgba(6, 43, 85, 0.12);
  border: 1px solid rgba(6, 43, 85, 0.08);
  height: 460px;
  background-color: var(--primary-navy);
}

.about-corp-main-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.about-corp-media-wrap:hover .about-corp-main-img img {
  transform: scale(1.04);
}

/* Floating Trust Badge (Bottom-Left Overlap) */
.about-corp-badge {
  position: absolute;
  bottom: 0;
  left: 1.5rem;
  background: var(--primary-navy);
  color: #ffffff;
  padding: 1.05rem 1.35rem;
  border-radius: 14px;
  box-shadow: 0 14px 34px rgba(6, 43, 85, 0.28);
  display: flex;
  align-items: center;
  gap: 14px;
  border: 2px solid rgba(255, 121, 0, 0.65);
  backdrop-filter: blur(8px);
  z-index: 2;
  transition: transform 0.3s ease;
}

.about-corp-badge:hover {
  transform: translateY(-3px);
}

.about-corp-badge-icon {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--accent-orange);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  flex-shrink: 0;
  box-shadow: 0 3px 10px rgba(255, 121, 0, 0.35);
}

.about-corp-badge-num {
  font-family: var(--font-heading);
  font-size: 1.30rem;
  font-weight: 800;
  line-height: 1.15;
  color: #ffffff;
}

.about-corp-badge-label {
  font-family: var(--font-body);
  font-size: 0.76rem;
  color: rgba(255, 255, 255, 0.85);
  font-weight: 500;
  margin-top: 2px;
}

/* Floating Credential Pill (Top-Right Overlap) */
.about-corp-cert-pill {
  position: absolute;
  top: 1.5rem;
  right: 0;
  background: #ffffff;
  color: var(--primary-navy);
  padding: 0.55rem 1.15rem;
  border-radius: 50px;
  font-family: var(--font-heading);
  font-size: 0.80rem;
  font-weight: 700;
  box-shadow: 0 8px 24px rgba(6, 43, 85, 0.14);
  align-items: center;
  gap: 8px;
  border: 1px solid rgba(6, 43, 85, 0.10);
  z-index: 2;
}

.about-corp-cert-pill i {
  color: #16a34a;
  font-size: 1.05rem;
}

/* Right Column Content */
.about-corp-content {
  padding-left: 0.5rem;
}

.about-corp-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 10px;
}

.about-corp-eyebrow-dash {
  width: 24px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.about-corp-eyebrow-text {
  font-family: var(--font-heading);
  font-size: 0.80rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--primary-navy);
}

.about-corp-title {
  font-family: var(--font-heading);
  font-size: clamp(1.85rem, 2.6vw, 2.3rem);
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.25;
  letter-spacing: -0.02em;
}

.about-corp-lead {
  font-family: var(--font-body);
  font-size: 0.98rem;
  color: var(--text-grey);
  line-height: 1.68;
}

/* Corporate Capability Cards Grid */
.about-corp-feature-grid {
  margin-bottom: 1.5rem;
}

.about-corp-feature-card {
  background: #f8fafc;
  border: 1px solid rgba(6, 43, 85, 0.08);
  border-radius: 12px;
  padding: 1rem 1.15rem;
  display: flex;
  align-items: flex-start;
  gap: 12px;
  height: 100%;
  transition: all 0.25s ease;
}

.about-corp-feature-card:hover {
  background: #ffffff;
  border-color: rgba(255, 121, 0, 0.4);
  box-shadow: 0 6px 20px rgba(6, 43, 85, 0.08);
  transform: translateY(-2px);
}

.about-feature-icon {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  background: rgba(6, 43, 85, 0.08);
  color: var(--primary-navy);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.05rem;
  flex-shrink: 0;
  transition: all 0.25s ease;
}

.about-corp-feature-card:hover .about-feature-icon {
  background: var(--accent-orange);
  color: #ffffff;
}

.about-feature-title {
  font-family: var(--font-heading);
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.25;
  margin-bottom: 0.25rem;
}

.about-feature-desc {
  font-family: var(--font-body);
  font-size: 0.78rem;
  color: var(--text-grey);
  line-height: 1.45;
  margin-bottom: 0;
}

/* Corporate Action Buttons */
.btn-corp-primary {
  background: var(--accent-orange);
  color: #ffffff;
  padding: 0.65rem 1.55rem;
  border-radius: 50px;
  font-family: var(--font-heading);
  font-size: 0.86rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  box-shadow: 0 4px 14px rgba(255, 121, 0, 0.3);
  transition: all 0.25s ease;
  border: none;
}

.btn-corp-primary:hover {
  background: var(--brand-orange-hover);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(255, 121, 0, 0.42);
}

.btn-corp-outline {
  background: transparent;
  color: var(--primary-navy);
  border: 1.5px solid rgba(6, 43, 85, 0.3);
  padding: 0.62rem 1.45rem;
  border-radius: 50px;
  font-family: var(--font-heading);
  font-size: 0.86rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  transition: all 0.25s ease;
}

.btn-corp-outline:hover {
  background: var(--primary-navy);
  color: #ffffff;
  border-color: var(--primary-navy);
  transform: translateY(-2px);
}

/* Corporate Metrics Bar */
.about-corp-stats-bar {
  background: var(--primary-navy);
  border-radius: 16px;
  padding: 2rem 1.5rem;
  color: #ffffff;
  box-shadow: 0 16px 40px rgba(6, 43, 85, 0.16);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.about-stat-item {
  padding: 0.5rem 1rem;
}

.about-stat-border {
  border-right: 1px solid rgba(255, 255, 255, 0.12);
}

.about-stat-number {
  font-family: var(--font-heading);
  font-size: clamp(2rem, 2.7vw, 2.5rem);
  font-weight: 800;
  color: #ffffff;
  line-height: 1.1;
  margin-bottom: 0.35rem;
}

.about-stat-text {
  font-family: var(--font-body);
  font-size: 0.84rem;
  color: rgba(255, 255, 255, 0.82);
  font-weight: 500;
}

/* Responsiveness */
@media (max-width: 991.98px) {
  .about-section {
    padding: 3.8rem 0;
  }

  .about-corp-main-img {
    height: 380px;
  }

  .about-corp-content {
    padding-left: 0;
  }

  .about-stat-border {
    border-right: none;
  }

  .about-corp-stats-bar .col-6:nth-child(1),
  .about-corp-stats-bar .col-6:nth-child(2) {
    margin-bottom: 1.25rem;
  }
}

@media (max-width: 575.98px) {
  .about-corp-main-img {
    height: 300px;
  }

  .about-corp-badge {
    left: 0.75rem;
    padding: 0.85rem 1rem;
  }

  .about-corp-badge-icon {
    width: 38px;
    height: 38px;
    font-size: 1.1rem;
  }

  .about-corp-badge-num {
    font-size: 1.15rem;
  }

  .about-corp-actions {
    flex-direction: column;
    align-items: stretch;
  }

  .btn-corp-primary,
  .btn-corp-outline {
    width: 100%;
    justify-content: center;
  }
}

'''

css = css[:c_idx1] + new_about_css + css[c_idx2:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/style.css with streamlined corporate CSS!")
