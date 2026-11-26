# scratch/apply_corporate_clean_about.py

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
         B. ABOUT US SECTION (PRESTIGIOUS CORPORATE ARCHITECTURE)
         ========================================================================== -->
    <section class="about-section" id="about">
      <div class="container">

        <div class="row g-4 g-xl-5 align-items-center">

          <!-- Left Column: Executive Corporate Statement & Trust Profile -->
          <div class="col-lg-5 fade-up-element">
            <div class="about-corp-left">

              <!-- Eyebrow -->
              <div class="about-corp-eyebrow mb-2">
                <span class="about-corp-eyebrow-dash"></span>
                <span class="about-corp-eyebrow-text">ABOUT GSR GLOBAL ENTERPRISES</span>
              </div>

              <!-- Main Title -->
              <h2 class="about-corp-title mb-3">
                Reliable Procurement &amp; Supply Services Across Core Industries
              </h2>

              <!-- Executive Statement Card (User's Exact Sentence) -->
              <div class="about-corp-statement-card mb-4">
                <p class="about-corp-statement-text mb-0">
                  From medical equipment and IT infrastructure to industrial materials, automotive components and renewable energy solutions, <strong>GSR Global Enterprises</strong> delivers reliable procurement and supply services tailored to diverse industry requirements.
                </p>
              </div>

              <!-- Trust & Compliance Badges -->
              <div class="about-corp-trust-list mb-4">
                <div class="trust-list-item">
                  <i class="bi bi-patch-check-fill text-orange"></i>
                  <span>Direct OEM &amp; Primary Mill Partnerships</span>
                </div>
                <div class="trust-list-item">
                  <i class="bi bi-patch-check-fill text-orange"></i>
                  <span>Rigorous Pre-Dispatch Quality Inspections</span>
                </div>
                <div class="trust-list-item">
                  <i class="bi bi-patch-check-fill text-orange"></i>
                  <span>100% Statutory, GST &amp; Tender Compliant</span>
                </div>
                <div class="trust-list-item">
                  <i class="bi bi-patch-check-fill text-orange"></i>
                  <span>Dual Regional Distribution Hubs in AP</span>
                </div>
              </div>

              <!-- Corporate Action CTA -->
              <div class="d-flex align-items-center gap-3 flex-wrap">
                <a href="#services" class="btn-corp-primary">
                  <span>Explore Our Services</span>
                  <i class="bi bi-arrow-right ms-1"></i>
                </a>
                <a href="#contact" class="btn-corp-outline">
                  <i class="bi bi-envelope-fill me-1"></i>
                  <span>Contact Sourcing Desk</span>
                </a>
              </div>

            </div>
          </div>

          <!-- Right Column: 5 Sector Procurement Matrix (Corporate Cards Grid) -->
          <div class="col-lg-7 fade-up-element">
            <div class="about-corp-sectors-panel">
              <div class="sectors-panel-header mb-3">
                <span class="sectors-panel-badge">CORE SOURCING SCOPE</span>
                <h3 class="sectors-panel-title">Procurement Solutions Tailored to Diverse Industry Requirements</h3>
              </div>

              <div class="row g-3">

                <!-- 1. Medical & Healthcare -->
                <div class="col-sm-6">
                  <div class="about-sector-card">
                    <div class="about-sector-icon-wrap">
                      <i class="bi bi-hospital"></i>
                    </div>
                    <div class="about-sector-info">
                      <h4 class="about-sector-name">Medical &amp; Healthcare</h4>
                      <p class="about-sector-sub">Diagnostic devices, hospital equipment &amp; clinical supplies</p>
                    </div>
                  </div>
                </div>

                <!-- 2. GCC & IT Infrastructure -->
                <div class="col-sm-6">
                  <div class="about-sector-card">
                    <div class="about-sector-icon-wrap">
                      <i class="bi bi-display"></i>
                    </div>
                    <div class="about-sector-info">
                      <h4 class="about-sector-name">GCC &amp; IT Infrastructure</h4>
                      <p class="about-sector-sub">Computer systems, networking &amp; school digital learning labs</p>
                    </div>
                  </div>
                </div>

                <!-- 3. Industrial & Manufacturing -->
                <div class="col-sm-6">
                  <div class="about-sector-card">
                    <div class="about-sector-icon-wrap">
                      <i class="bi bi-gear-wide-connected"></i>
                    </div>
                    <div class="about-sector-info">
                      <h4 class="about-sector-name">Industrial Materials</h4>
                      <p class="about-sector-sub">TMT steel rebar, structural sections &amp; industrial yarn</p>
                    </div>
                  </div>
                </div>

                <!-- 4. Automobile & Transportation -->
                <div class="col-sm-6">
                  <div class="about-sector-card">
                    <div class="about-sector-icon-wrap">
                      <i class="bi bi-bus-front"></i>
                    </div>
                    <div class="about-sector-info">
                      <h4 class="about-sector-name">Automotive &amp; Transit</h4>
                      <p class="about-sector-sub">Bus spare parts, fleet components &amp; vehicle maintenance</p>
                    </div>
                  </div>
                </div>

                <!-- 5. Renewable Energy Solutions -->
                <div class="col-12">
                  <div class="about-sector-card about-sector-card-highlight">
                    <div class="about-sector-icon-wrap">
                      <i class="bi bi-sun"></i>
                    </div>
                    <div class="about-sector-info">
                      <h4 class="about-sector-name">Renewable Energy Solutions</h4>
                      <p class="about-sector-sub">Commercial solar PV modules, clean energy hardware &amp; sustainable infrastructure supplies</p>
                    </div>
                    <div class="about-sector-tag d-none d-md-inline-block">
                      <span>Clean Energy</span>
                    </div>
                  </div>
                </div>

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

print("Updated index.html with new clean corporate About architecture!")

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
   B. About Us Section - Prestigious Corporate Architecture (Clean & Balanced)
   ========================================================================== */
.about-section {
  padding: 5rem 0 5.2rem;
  background-color: #ffffff;
  position: relative;
  border-bottom: 1px solid rgba(6, 43, 85, 0.06);
}

/* Left Column */
.about-corp-left {
  padding-right: 0.5rem;
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
  font-size: clamp(1.85rem, 2.5vw, 2.25rem);
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.25;
  letter-spacing: -0.02em;
}

/* Executive Statement Card (Accented Left Border) */
.about-corp-statement-card {
  background: #f8fafc;
  border-left: 4px solid var(--accent-orange);
  border-radius: 0 12px 12px 0;
  padding: 1.35rem 1.45rem;
  border-top: 1px solid rgba(6, 43, 85, 0.06);
  border-right: 1px solid rgba(6, 43, 85, 0.06);
  border-bottom: 1px solid rgba(6, 43, 85, 0.06);
  box-shadow: 0 4px 16px rgba(6, 43, 85, 0.03);
}

.about-corp-statement-text {
  font-family: var(--font-body);
  font-size: 0.98rem;
  color: #1e293b;
  line-height: 1.68;
  font-weight: 500;
}

/* Trust Checklist */
.about-corp-trust-list {
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.trust-list-item {
  display: flex;
  align-items: center;
  gap: 9px;
  font-family: var(--font-body);
  font-size: 0.88rem;
  font-weight: 600;
  color: #334155;
}

.trust-list-item i {
  color: var(--accent-orange);
  font-size: 1.05rem;
  flex-shrink: 0;
}

/* Corporate Buttons */
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

/* Right Column: Corporate Sectors Panel */
.about-corp-sectors-panel {
  background: #ffffff;
  border: 1px solid rgba(6, 43, 85, 0.08);
  border-radius: 20px;
  padding: 2.2rem 2.2rem 2rem;
  box-shadow: 0 14px 40px rgba(6, 43, 85, 0.07);
}

.sectors-panel-badge {
  display: inline-block;
  font-family: var(--font-heading);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--accent-orange);
  margin-bottom: 0.35rem;
}

.sectors-panel-title {
  font-family: var(--font-heading);
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.35;
}

/* Sector Card Item */
.about-sector-card {
  background: #f8fafc;
  border: 1px solid rgba(6, 43, 85, 0.06);
  border-radius: 12px;
  padding: 1.05rem 1.15rem;
  display: flex;
  align-items: center;
  gap: 14px;
  transition: all 0.25s ease;
  height: 100%;
}

.about-sector-card:hover {
  background: #ffffff;
  border-color: rgba(255, 121, 0, 0.4);
  box-shadow: 0 8px 24px rgba(6, 43, 85, 0.10);
  transform: translateY(-2px);
}

.about-sector-icon-wrap {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  background: rgba(6, 43, 85, 0.08);
  color: var(--primary-navy);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  flex-shrink: 0;
  transition: all 0.25s ease;
}

.about-sector-card:hover .about-sector-icon-wrap {
  background: var(--accent-orange);
  color: #ffffff;
}

.about-sector-name {
  font-family: var(--font-heading);
  font-size: 0.94rem;
  font-weight: 700;
  color: var(--primary-navy);
  margin-bottom: 0.2rem;
  line-height: 1.25;
}

.about-sector-sub {
  font-family: var(--font-body);
  font-size: 0.78rem;
  color: var(--text-grey);
  margin-bottom: 0;
  line-height: 1.4;
}

.about-sector-card-highlight {
  background: linear-gradient(135deg, rgba(6, 43, 85, 0.04) 0%, rgba(255, 121, 0, 0.05) 100%);
  border-color: rgba(6, 43, 85, 0.12);
}

.about-sector-tag {
  margin-left: auto;
  background: rgba(255, 121, 0, 0.12);
  color: var(--accent-orange);
  padding: 4px 10px;
  border-radius: 50px;
  font-family: var(--font-heading);
  font-size: 0.70rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  white-space: nowrap;
}

/* Responsiveness */
@media (max-width: 991.98px) {
  .about-section {
    padding: 3.8rem 0;
  }

  .about-corp-left {
    padding-right: 0;
  }

  .about-corp-sectors-panel {
    padding: 1.5rem;
  }
}

@media (max-width: 575.98px) {
  .about-sector-card {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
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

print("Updated css/style.css with prestigious corporate architecture CSS!")
