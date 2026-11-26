# apply_services_3_cards_grid.py

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the services section
sec_start = '<!-- ==========================================================================\n         C. OUR SERVICES'
sec_end = '<!-- ==========================================================================\n         E. OUR CLIENTS'

idx1 = html.find(sec_start)
idx2 = html.find(sec_end)

if idx1 == -1 or idx2 == -1:
    print(f"Error finding services section markers: idx1={idx1}, idx2={idx2}")
    exit(1)

new_services_html = '''<!-- ==========================================================================
         C. OUR SERVICES (3 CARDS PER ROW - PROFESSIONAL GRID LAYOUT)
         ========================================================================== -->
    <section class="services-section" id="services">
      <div class="container">

        <!-- Section Header (Centered Corporate Style) -->
        <div class="text-center mb-5 fade-up-element">
          <div class="services-eyebrow mb-2">
            <span class="services-eyebrow-dash"></span>
            <span class="services-eyebrow-text">WHAT WE DO</span>
            <span class="services-eyebrow-dash"></span>
          </div>
          <h2 class="services-section-title mb-3">
            Comprehensive Procurement Solutions Across Multiple Industries
          </h2>
          <p class="services-section-subtitle mx-auto">
            From specialized equipment to essential industrial materials, we help customers source the right products for their business and project requirements.
          </p>
        </div>

        <div id="industries" style="scroll-margin-top: 100px;"></div>

        <!-- 3 Cards Per Row Grid Layout -->
        <div class="row g-4 justify-content-center">

          <!-- Card 1: Medical & Healthcare Supplies -->
          <div class="col-lg-4 col-md-6 fade-up-element">
            <div class="service-pro-card h-100">
              <div class="service-pro-media">
                <img src="assets/images/service-medical.webp" alt="Medical & Healthcare Supplies" loading="lazy">
                <span class="service-pro-num-badge">01</span>
                <span class="service-pro-cat-pill">HEALTHCARE</span>
                <div class="service-pro-icon-circle">
                  <i class="bi bi-hospital"></i>
                </div>
              </div>
              <div class="service-pro-body">
                <h3 class="service-pro-title">Medical &amp; Healthcare Supplies</h3>
                <p class="service-pro-desc">
                  Supporting healthcare institutions, hospitals and medical organizations with procurement of essential medical equipment and devices.
                </p>
                <div class="service-pro-divider"></div>
                <ul class="service-pro-checklist">
                  <li><i class="bi bi-check-circle-fill"></i><span>Medical equipment and devices</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Hospital and clinical supplies</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Diagnostic and monitoring equipment</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Healthcare infrastructure requirements</span></li>
                </ul>
                <div class="service-pro-footer">
                  <button type="button" class="btn-pro-readmore" data-service-key="medical">
                    <span>Read More</span>
                    <i class="bi bi-info-circle ms-1"></i>
                  </button>
                  <a href="#contact" class="btn-pro-enquire" data-select-service="01">
                    <span>Enquire Now</span>
                    <i class="bi bi-arrow-right ms-1"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 2: GCC & IT Infrastructure -->
          <div class="col-lg-4 col-md-6 fade-up-element">
            <div class="service-pro-card h-100">
              <div class="service-pro-media">
                <img src="assets/images/service-it.webp" alt="GCC & IT Infrastructure" loading="lazy">
                <span class="service-pro-num-badge">02</span>
                <span class="service-pro-cat-pill">IT &amp; INFRASTRUCTURE</span>
                <div class="service-pro-icon-circle">
                  <i class="bi bi-display"></i>
                </div>
              </div>
              <div class="service-pro-body">
                <h3 class="service-pro-title">GCC &amp; IT Infrastructure</h3>
                <p class="service-pro-desc">
                  Providing computer systems, technology products and IT infrastructure for organizations and large-scale school transformation projects and programs.
                </p>
                <div class="service-pro-divider"></div>
                <ul class="service-pro-checklist">
                  <li><i class="bi bi-check-circle-fill"></i><span>Desktop computers and laptops</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Computer laboratory equipment</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Networking and IT infrastructure</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Hardware and technology accessories</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Digital learning infrastructure</span></li>
                </ul>
                <div class="service-pro-footer">
                  <button type="button" class="btn-pro-readmore" data-service-key="it">
                    <span>Read More</span>
                    <i class="bi bi-info-circle ms-1"></i>
                  </button>
                  <a href="#contact" class="btn-pro-enquire" data-select-service="02">
                    <span>Enquire Now</span>
                    <i class="bi bi-arrow-right ms-1"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 3: Government & Education Projects -->
          <div class="col-lg-4 col-md-6 fade-up-element">
            <div class="service-pro-card h-100">
              <div class="service-pro-media">
                <img src="assets/images/about-it-classroom.webp" alt="Government & Education Projects" loading="lazy">
                <span class="service-pro-num-badge">03</span>
                <span class="service-pro-cat-pill">PUBLIC SECTOR &amp; EDUCATION</span>
                <div class="service-pro-icon-circle">
                  <i class="bi bi-bank2"></i>
                </div>
              </div>
              <div class="service-pro-body">
                <h3 class="service-pro-title">Government &amp; Education Projects</h3>
                <p class="service-pro-desc">
                  Supporting government departments, educational institutions and project implementation agencies through coordinated procurement and supply solutions.
                </p>
                <div class="service-pro-divider"></div>
                <ul class="service-pro-checklist">
                  <li><i class="bi bi-check-circle-fill"></i><span>School transformation projects</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Educational technology and equipment</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Institutional infrastructure supplies</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Bulk procurement for public-sector projects</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Project-specific sourcing requirements</span></li>
                </ul>
                <div class="service-pro-footer">
                  <button type="button" class="btn-pro-readmore" data-service-key="govt-education">
                    <span>Read More</span>
                    <i class="bi bi-info-circle ms-1"></i>
                  </button>
                  <a href="#contact" class="btn-pro-enquire" data-select-service="03">
                    <span>Enquire Now</span>
                    <i class="bi bi-arrow-right ms-1"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 4: Industrial & Manufacturing Supplies -->
          <div class="col-lg-4 col-md-6 fade-up-element">
            <div class="service-pro-card h-100">
              <div class="service-pro-media">
                <img src="assets/images/service-steel.webp" alt="Industrial & Manufacturing Supplies" loading="lazy">
                <span class="service-pro-num-badge">04</span>
                <span class="service-pro-cat-pill">INDUSTRIAL &amp; MANUFACTURING</span>
                <div class="service-pro-icon-circle">
                  <i class="bi bi-gear-wide-connected"></i>
                </div>
              </div>
              <div class="service-pro-body">
                <h3 class="service-pro-title">Industrial &amp; Manufacturing Supplies</h3>
                <p class="service-pro-desc">
                  Helping manufacturers and industrial businesses source essential raw materials and production-related supplies.
                </p>
                <div class="service-pro-divider"></div>
                <ul class="service-pro-checklist">
                  <li><i class="bi bi-check-circle-fill"></i><span>Iron and steel materials</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Industrial raw materials</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Textile yarn and related supplies</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Manufacturing and production requirements</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Bulk material procurement</span></li>
                </ul>
                <div class="service-pro-footer">
                  <button type="button" class="btn-pro-readmore" data-service-key="industrial">
                    <span>Read More</span>
                    <i class="bi bi-info-circle ms-1"></i>
                  </button>
                  <a href="#contact" class="btn-pro-enquire" data-select-service="04">
                    <span>Enquire Now</span>
                    <i class="bi bi-arrow-right ms-1"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 5: Automobile & Transportation Supplies -->
          <div class="col-lg-4 col-md-6 fade-up-element">
            <div class="service-pro-card h-100">
              <div class="service-pro-media">
                <img src="assets/images/service-transit.webp" alt="Automobile & Transportation Supplies" loading="lazy">
                <span class="service-pro-num-badge">05</span>
                <span class="service-pro-cat-pill">AUTOMOTIVE &amp; TRANSIT</span>
                <div class="service-pro-icon-circle">
                  <i class="bi bi-bus-front"></i>
                </div>
              </div>
              <div class="service-pro-body">
                <h3 class="service-pro-title">Automobile &amp; Transportation Supplies</h3>
                <p class="service-pro-desc">
                  Supporting automotive businesses, fleet operators and transportation projects with procurement of bus parts and automotive components.
                </p>
                <div class="service-pro-divider"></div>
                <ul class="service-pro-checklist">
                  <li><i class="bi bi-check-circle-fill"></i><span>Bus spare parts and components</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Automotive mechanical components</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Vehicle maintenance supplies</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Transportation industry requirements</span></li>
                  <li><i class="bi bi-check-circle-fill"></i><span>Project-based automotive procurement</span></li>
                </ul>
                <div class="service-pro-footer">
                  <button type="button" class="btn-pro-readmore" data-service-key="auto">
                    <span>Read More</span>
                    <i class="bi bi-info-circle ms-1"></i>
                  </button>
                  <a href="#contact" class="btn-pro-enquire" data-select-service="05">
                    <span>Enquire Now</span>
                    <i class="bi bi-arrow-right ms-1"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>

    '''

html = html[:idx1] + new_services_html + html[idx2:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with new 3-cards per row Services Section!")

# 2. Update css/style.css to style the new professional services cards
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

c_start = '/* ==========================================================================\n   C. Services Section'
c_end = '/* ==========================================================================\n   D. Industries We Serve'

c_idx1 = css.find(c_start)
c_idx2 = css.find(c_end)

if c_idx1 == -1 or c_idx2 == -1:
    print(f"Error finding CSS markers for Services: c_idx1={c_idx1}, c_idx2={c_idx2}")
    exit(1)

new_services_css = '''/* ==========================================================================
   C. Services Section - 3 Cards Per Row Professional Corporate Grid
   ========================================================================== */
.services-section {
  padding: 5rem 0 5.5rem 0;
  background-color: var(--light-bg);
  border-top: 1px solid rgba(6, 43, 85, 0.06);
  border-bottom: 1px solid rgba(6, 43, 85, 0.06);
  position: relative;
}

/* Section Header */
.services-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 10px;
}

.services-eyebrow-dash {
  width: 26px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.services-eyebrow-text {
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--primary-navy);
}

.services-section-title {
  font-family: var(--font-heading);
  font-size: clamp(1.9rem, 2.7vw, 2.45rem);
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.25;
  letter-spacing: -0.02em;
  max-width: 820px;
  margin-left: auto;
  margin-right: auto;
}

.services-section-subtitle {
  font-family: var(--font-body);
  font-size: clamp(0.92rem, 1.05vw, 0.98rem);
  color: var(--text-grey);
  line-height: 1.62;
}

/* Professional Service Card */
.service-pro-card {
  background: #ffffff;
  border: 1px solid rgba(6, 43, 85, 0.08);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(6, 43, 85, 0.06);
  display: flex;
  flex-direction: column;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.service-pro-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 18px 44px rgba(6, 43, 85, 0.12);
  border-color: rgba(255, 121, 0, 0.35);
}

/* Card Media */
.service-pro-media {
  position: relative;
  height: 210px;
  overflow: hidden;
  background-color: var(--primary-navy);
}

.service-pro-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.65s cubic-bezier(0.16, 1, 0.3, 1);
}

.service-pro-card:hover .service-pro-media img {
  transform: scale(1.07);
}

.service-pro-num-badge {
  position: absolute;
  top: 14px;
  left: 14px;
  background: rgba(6, 43, 85, 0.9);
  color: #ffffff;
  font-family: var(--font-heading);
  font-size: 0.76rem;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 6px;
  backdrop-filter: blur(4px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.service-pro-cat-pill {
  position: absolute;
  top: 14px;
  right: 14px;
  background: rgba(255, 255, 255, 0.95);
  color: var(--primary-navy);
  font-family: var(--font-heading);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 4px 11px;
  border-radius: 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
}

.service-pro-icon-circle {
  position: absolute;
  bottom: 12px;
  right: 14px;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: #ffffff;
  color: var(--primary-navy);
  border: 2px solid var(--accent-orange);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.15rem;
  box-shadow: 0 4px 12px rgba(6, 43, 85, 0.16);
  transition: all 0.3s ease;
}

.service-pro-card:hover .service-pro-icon-circle {
  background: var(--accent-orange);
  color: #ffffff;
  transform: scale(1.08);
}

/* Card Body */
.service-pro-body {
  padding: 1.5rem 1.45rem 1.35rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.service-pro-title {
  font-family: var(--font-heading);
  font-size: 1.18rem;
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.32;
  margin-bottom: 0.65rem;
}

.service-pro-desc {
  font-family: var(--font-body);
  font-size: 0.88rem;
  color: var(--text-grey);
  line-height: 1.58;
  margin-bottom: 1rem;
}

.service-pro-divider {
  height: 1px;
  background: rgba(6, 43, 85, 0.08);
  margin-bottom: 1rem;
}

/* Checklist */
.service-pro-checklist {
  list-style: none;
  padding: 0;
  margin: 0 0 1.35rem 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.service-pro-checklist li {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  font-family: var(--font-body);
  font-size: 0.84rem;
  color: #2c3e50;
  line-height: 1.45;
  font-weight: 500;
}

.service-pro-checklist li i {
  color: var(--accent-orange);
  font-size: 0.95rem;
  flex-shrink: 0;
  margin-top: 1px;
}

/* Card Footer */
.service-pro-footer {
  margin-top: auto;
  padding-top: 1rem;
  border-top: 1px solid rgba(6, 43, 85, 0.06);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.btn-pro-readmore {
  background: transparent;
  color: var(--primary-navy);
  border: 1.5px solid rgba(6, 43, 85, 0.3);
  border-radius: 50px;
  padding: 0.45rem 0.95rem;
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 6px;
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
  padding: 0.48rem 1.05rem;
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  text-decoration: none;
  box-shadow: 0 3px 10px rgba(255, 121, 0, 0.28);
  transition: all 0.25s ease;
}

.btn-pro-enquire:hover {
  background: var(--brand-orange-hover);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 5px 14px rgba(255, 121, 0, 0.4);
}

@media (max-width: 991.98px) {
  .services-section {
    padding: 3.8rem 0;
  }
}

'''

css = css[:c_idx1] + new_services_css + css[c_idx2:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/style.css with professional 3-cards per row styling!")
