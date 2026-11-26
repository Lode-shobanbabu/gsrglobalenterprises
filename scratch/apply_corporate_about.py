# scratch/apply_corporate_about.py

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
         B. ABOUT US SECTION (MODERN CLEAN CORPORATE STYLE)
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

          <!-- Right Column: Corporate Narrative, Interactive Tabs & Capabilities -->
          <div class="col-lg-6 fade-up-element">
            <div class="about-corp-content">

              <!-- Eyebrow -->
              <div class="about-corp-eyebrow mb-2">
                <span class="about-corp-eyebrow-dash"></span>
                <span class="about-corp-eyebrow-text">ABOUT GSR GLOBAL ENTERPRISES</span>
              </div>

              <!-- Main Title -->
              <h2 class="about-corp-title mb-3">
                Your Strategic Procurement Partner Delivering Verified Institutional Excellence
              </h2>

              <!-- Lead Description -->
              <p class="about-corp-lead mb-3">
                Headquartered in Andhra Pradesh, <strong>GSR GLOBAL ENTERPRISES</strong> is an established multi-sector procurement, industrial supply, and infrastructure solutions enterprise. We bridge institutional demand with dependable manufacturing channels across critical healthcare, education, transport, and industrial sectors.
              </p>

              <!-- Corporate Nav Tabs: Our Profile / Our Mission / Our Vision -->
              <div class="about-corp-tabs-wrap mb-3">
                <ul class="nav nav-pills" id="aboutTab" role="tablist">
                  <li class="nav-item" role="presentation">
                    <button class="nav-link active" id="pill-history-tab" data-bs-toggle="pill"
                      data-bs-target="#pill-history" type="button" role="tab" aria-controls="pill-history"
                      aria-selected="true">Our Profile</button>
                  </li>
                  <li class="nav-item" role="presentation">
                    <button class="nav-link" id="pill-mission-tab" data-bs-toggle="pill"
                      data-bs-target="#pill-mission" type="button" role="tab" aria-controls="pill-mission"
                      aria-selected="false">Our Mission</button>
                  </li>
                  <li class="nav-item" role="presentation">
                    <button class="nav-link" id="pill-vision-tab" data-bs-toggle="pill"
                      data-bs-target="#pill-vision" type="button" role="tab" aria-controls="pill-vision"
                      aria-selected="false">Our Vision</button>
                  </li>
                </ul>
              </div>

              <!-- Tab Contents -->
              <div class="tab-content about-corp-tab-content mb-4" id="aboutTabContent">

                <!-- Tab 1: Our Profile (Active) -->
                <div class="tab-pane fade show active" id="pill-history" role="tabpanel"
                  aria-labelledby="pill-history-tab">
                  <p class="about-corp-tab-desc">
                    Operating through direct mill-origin tie-ups and tier-1 OEM relationships, we manage complex bulk sourcing programs with end-to-end statutory compliance, strict pre-dispatch quality verification, and disciplined handover.
                  </p>
                  <div class="row g-2 about-corp-check-grid">
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Direct OEM &amp; Primary Stockists</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Strict Pre-Dispatch Inspections</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>100% Tax &amp; GST Invoicing</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Dual Regional Distribution Hubs</span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Tab 2: Our Mission -->
                <div class="tab-pane fade" id="pill-mission" role="tabpanel" aria-labelledby="pill-mission-tab">
                  <p class="about-corp-tab-desc">
                    Our mission is to empower government institutions, transit workshops, educational development programs, and industrial businesses with seamless, transparent, and on-time procurement solutions that eliminate supply bottlenecks.
                  </p>
                  <div class="row g-2 about-corp-check-grid">
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Eliminating Sourcing Bottlenecks</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Standardized Technical Compliance</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Transparent Commercial Invoicing</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Disciplined On-Site Handover</span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Tab 3: Our Vision -->
                <div class="tab-pane fade" id="pill-vision" role="tabpanel" aria-labelledby="pill-vision-tab">
                  <p class="about-corp-tab-desc">
                    Our vision is to be recognized as Andhra Pradesh's most dependable and comprehensive institutional supply partner, respected for uncompromising integrity, multi-sector agility, and long-term public and commercial trust.
                  </p>
                  <div class="row g-2 about-corp-check-grid">
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Multi-Industry Sourcing Reach</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Zero-Defect Delivery Discipline</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Sustainable Supply Pipelines</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Enduring Institutional Trust</span>
                      </div>
                    </div>
                  </div>
                </div>

              </div>

              <!-- Corporate CTA Actions -->
              <div class="about-corp-actions d-flex align-items-center gap-3 flex-wrap">
                <a href="#services" class="btn-corp-primary">
                  <span>Explore Our Capabilities</span>
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

print("Updated index.html with new Corporate About section!")

# 2. Update css/style.css with Corporate About Section CSS
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

c_start = '/* ==========================================================================\n   B. About Us Section'
c_end = '/* ==========================================================================\n   C. Services Section'

c_idx1 = css.find(c_start)
c_idx2 = css.find(c_end)

if c_idx1 == -1 or c_idx2 == -1:
    print(f"Error finding CSS markers for About section: c_idx1={c_idx1}, c_idx2={c_idx2}")
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
  font-size: 0.94rem;
  color: var(--text-grey);
  line-height: 1.65;
}

/* Corporate Pill Tabs */
.about-corp-tabs-wrap {
  display: inline-flex;
  background: #f1f5f9;
  padding: 4px;
  border-radius: 8px;
  border: 1px solid rgba(6, 43, 85, 0.08);
}

.about-corp-tabs-wrap .nav-link {
  border-radius: 6px;
  padding: 0.45rem 1.2rem;
  font-family: var(--font-heading);
  font-size: 0.84rem;
  font-weight: 600;
  color: var(--text-grey);
  border: none;
  background: transparent;
  transition: all 0.25s ease;
}

.about-corp-tabs-wrap .nav-link:hover {
  color: var(--primary-navy);
}

.about-corp-tabs-wrap .nav-link.active {
  background: var(--primary-navy);
  color: #ffffff;
  box-shadow: 0 3px 10px rgba(6, 43, 85, 0.2);
}

.about-corp-tab-desc {
  font-family: var(--font-body);
  font-size: 0.88rem;
  color: var(--text-grey);
  line-height: 1.6;
  margin-bottom: 1rem;
}

/* Corporate Checklist */
.about-corp-check-grid {
  margin-bottom: 0.5rem;
}

.about-corp-check-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-body);
  font-size: 0.85rem;
  font-weight: 600;
  color: #1e293b;
  padding: 2px 0;
}

.about-corp-check-item i {
  color: var(--accent-orange);
  font-size: 0.95rem;
  flex-shrink: 0;
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

print("Updated css/style.css with Corporate About Section CSS!")
