# add_professional_sector_cards.py
import re

# 1. Update index.html to add the Docked Core Sectors Cards Bar right after #hero
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

hero_closing_tag = '</section>\n\n    <!-- ==========================================================================\n         B. ABOUT US SECTION'

if hero_closing_tag not in html:
    print("Exact hero_closing_tag not found, searching with regex...")
    match = re.search(r'</section>\s*<!-- =+\s*B\.\s*ABOUT US SECTION', html)
    if not match:
        print("Could not find boundary between Hero and About Us!")
        exit(1)
    hero_end_pos = match.start() + len('</section>')
else:
    hero_end_pos = html.find(hero_closing_tag) + len('</section>')

sector_cards_bar_html = '''

    <!-- ==========================================================================
         A2. CORE SECTORS CARDS BAR (5 PROFESSIONAL SECTORS)
         ========================================================================== -->
    <section class="sectors-cards-bar-section" id="sectors" aria-label="Core Business Sectors">
      <div class="container">
        <div class="sectors-cards-bar fade-up-element">

          <!-- 1. Medical & Healthcare Supplies -->
          <a href="#services" class="sector-card" title="Medical & Healthcare Supplies">
            <div class="sector-card-icon-box">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="m10.5 20.5 10-10a4.95 4.95 0 1 0-7-7l-10 10a4.95 4.95 0 1 0 7 7Z"/>
                <path d="m8.5 8.5 7 7"/>
              </svg>
            </div>
            <div class="sector-card-text">
              <span class="sector-card-title">Medical &amp;<br>Healthcare Supplies</span>
            </div>
          </a>

          <div class="sector-card-divider"></div>

          <!-- 2. GCC & IT Infrastructure -->
          <a href="#services" class="sector-card" title="GCC & IT Infrastructure">
            <div class="sector-card-icon-box">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect width="20" height="14" x="2" y="3" rx="2"/>
                <line x1="8" x2="16" y1="21" y2="21"/>
                <line x1="12" x2="12" y1="17" y2="21"/>
              </svg>
            </div>
            <div class="sector-card-text">
              <span class="sector-card-title">GCC &amp; IT<br>Infrastructure</span>
            </div>
          </a>

          <div class="sector-card-divider"></div>

          <!-- 3. Government & Education Projects -->
          <a href="#services" class="sector-card" title="Government & Education Projects">
            <div class="sector-card-icon-box">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 22h16"/>
                <path d="M2 11h20"/>
                <path d="M12 2 2 7h20L12 2z"/>
                <path d="M6 11v7"/>
                <path d="M10 11v7"/>
                <path d="M14 11v7"/>
                <path d="M18 11v7"/>
              </svg>
            </div>
            <div class="sector-card-text">
              <span class="sector-card-title">Government &amp;<br>Education Projects</span>
            </div>
          </a>

          <div class="sector-card-divider"></div>

          <!-- 4. Industrial & Manufacturing Supplies -->
          <a href="#services" class="sector-card" title="Industrial & Manufacturing Supplies">
            <div class="sector-card-icon-box">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <ellipse cx="12" cy="5" rx="8" ry="3"/>
                <path d="M4 5v14c0 1.66 3.58 3 8 3s8-1.34 8-3V5"/>
                <path d="M4 12c0 1.66 3.58 3 8 3s8-1.34 8-3"/>
              </svg>
            </div>
            <div class="sector-card-text">
              <span class="sector-card-title">Industrial &amp;<br>Manufacturing Supplies</span>
            </div>
          </a>

          <div class="sector-card-divider"></div>

          <!-- 5. Automobile & Transportation Supplies -->
          <a href="#services" class="sector-card" title="Automobile & Transportation Supplies">
            <div class="sector-card-icon-box">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9C2.1 11.2 2 11.6 2 12v4c0 .6.4 1 1 1h2"/>
                <circle cx="7" cy="17" r="2"/>
                <path d="M9 17h6"/>
                <circle cx="17" cy="17" r="2"/>
              </svg>
            </div>
            <div class="sector-card-text">
              <span class="sector-card-title">Automobile &amp;<br>Transportation Supplies</span>
            </div>
          </a>

        </div>
      </div>
    </section>'''

html = html[:hero_end_pos] + sector_cards_bar_html + html[hero_end_pos:]

# 2. Update the 5 Cards in the Services Section (#services)
services_carousel_track_pattern = r'<div class="services-carousel-track" id="servicesCarouselTrack">([\s\S]*?)</div>\s*</div>\s*</div>\s*</section>'

new_services_cards = '''<div class="services-carousel-track" id="servicesCarouselTrack">

            <!-- Card 01: Medical & Healthcare Supplies -->
            <div class="service-carousel-card">
              <div class="service-card-media">
                <img src="assets/images/service-medical.webp" alt="Medical and Healthcare Supplies Procurement"
                  loading="lazy">
                <div class="service-card-icon-badge" title="Medical Devices">
                  <i class="bi bi-hospital"></i>
                </div>
              </div>
              <div class="service-card-content">
                <div class="service-cat-pill">01 • HEALTHCARE</div>
                <h3 class="service-card-heading">Medical &amp; Healthcare Supplies</h3>
                <p class="service-card-summary">
                  Procurement and supply of hospital-grade medical equipment, clinical diagnostic devices, surgical tools, sterilization units, and certified healthcare consumables.
                </p>
                <div class="service-card-bottom-row">
                  <button type="button" class="btn btn-outline-navy btn-sm" data-service-key="medical">
                    <i class="bi bi-info-circle me-1"></i>
                    <span>Read More</span>
                  </button>
                  <a href="#contact" class="btn btn-gold btn-sm btn-enroll-now" data-select-service="01">
                    <span>Enquire Now</span>
                    <i class="bi bi-arrow-right ms-1"></i>
                  </a>
                </div>
              </div>
            </div>

            <!-- Card 02: GCC & IT Infrastructure -->
            <div class="service-carousel-card">
              <div class="service-card-media">
                <img src="assets/images/service-it.webp" alt="GCC and IT Infrastructure Procurement"
                  loading="lazy">
                <div class="service-card-icon-badge" title="IT Infrastructure">
                  <i class="bi bi-display"></i>
                </div>
              </div>
              <div class="service-card-content">
                <div class="service-cat-pill">02 • IT &amp; INFRASTRUCTURE</div>
                <h3 class="service-card-heading">GCC &amp; IT Infrastructure</h3>
                <p class="service-card-summary">
                  Supply of enterprise servers, computing workstations, interactive displays, high-speed networking, and digital infrastructure for Global Capability Centers.
                </p>
                <div class="service-card-bottom-row">
                  <button type="button" class="btn btn-outline-navy btn-sm" data-service-key="it">
                    <i class="bi bi-info-circle me-1"></i>
                    <span>Read More</span>
                  </button>
                  <a href="#contact" class="btn btn-gold btn-sm btn-enroll-now" data-select-service="02">
                    <span>Enquire Now</span>
                    <i class="bi bi-arrow-right ms-1"></i>
                  </a>
                </div>
              </div>
            </div>

            <!-- Card 03: Government & Education Projects -->
            <div class="service-carousel-card">
              <div class="service-card-media">
                <img src="assets/images/about-it-classroom.webp" alt="Government and Education Projects Procurement" loading="lazy">
                <div class="service-card-icon-badge" title="Public Sector & Education">
                  <i class="bi bi-mortarboard"></i>
                </div>
              </div>
              <div class="service-card-content">
                <div class="service-cat-pill">03 • PUBLIC SECTOR &amp; EDUCATION</div>
                <h3 class="service-card-heading">Government &amp; Education Projects</h3>
                <p class="service-card-summary">
                  Comprehensive school transformation, digital classroom labs, institutional supplies, and turnkey public sector equipment deployments under government initiatives.
                </p>
                <div class="service-card-bottom-row">
                  <button type="button" class="btn btn-outline-navy btn-sm" data-service-key="govt-education">
                    <i class="bi bi-info-circle me-1"></i>
                    <span>Read More</span>
                  </button>
                  <a href="#contact" class="btn btn-gold btn-sm btn-enroll-now" data-select-service="03">
                    <span>Enquire Now</span>
                    <i class="bi bi-arrow-right ms-1"></i>
                  </a>
                </div>
              </div>
            </div>

            <!-- Card 04: Industrial & Manufacturing Supplies -->
            <div class="service-carousel-card">
              <div class="service-card-media">
                <img src="assets/images/service-steel.webp" alt="Industrial and Manufacturing Supplies Procurement"
                  loading="lazy">
                <div class="service-card-icon-badge" title="Industrial & Manufacturing">
                  <i class="bi bi-gear-wide-connected"></i>
                </div>
              </div>
              <div class="service-card-content">
                <div class="service-cat-pill">04 • INDUSTRIAL &amp; MANUFACTURING</div>
                <h3 class="service-card-heading">Industrial &amp; Manufacturing Supplies</h3>
                <p class="service-card-summary">
                  Procurement and supply of certified structural TMT steel, heavy plates, industrial fabrication sections, commercial yarn, and manufacturing raw materials.
                </p>
                <div class="service-card-bottom-row">
                  <button type="button" class="btn btn-outline-navy btn-sm" data-service-key="industrial">
                    <i class="bi bi-info-circle me-1"></i>
                    <span>Read More</span>
                  </button>
                  <a href="#contact" class="btn btn-gold btn-sm btn-enroll-now" data-select-service="04">
                    <span>Enquire Now</span>
                    <i class="bi bi-arrow-right ms-1"></i>
                  </a>
                </div>
              </div>
            </div>

            <!-- Card 05: Automobile & Transportation Supplies -->
            <div class="service-carousel-card">
              <div class="service-card-media">
                <img src="assets/images/service-transit.webp" alt="Automobile and Transportation Supplies Procurement"
                  loading="lazy">
                <div class="service-card-icon-badge" title="Automotive & Transit">
                  <i class="bi bi-bus-front"></i>
                </div>
              </div>
              <div class="service-card-content">
                <div class="service-cat-pill">05 • AUTOMOTIVE &amp; TRANSIT</div>
                <h3 class="service-card-heading">Automobile &amp; Transportation Supplies</h3>
                <p class="service-card-summary">
                  Sourcing of commercial fleet transit spares, heavy bus assemblies, braking components, suspension units, and certified maintenance hardware for transport workshops.
                </p>
                <div class="service-card-bottom-row">
                  <button type="button" class="btn btn-outline-navy btn-sm" data-service-key="auto">
                    <i class="bi bi-info-circle me-1"></i>
                    <span>Read More</span>
                  </button>
                  <a href="#contact" class="btn btn-gold btn-sm btn-enroll-now" data-select-service="05">
                    <span>Enquire Now</span>
                    <i class="bi bi-arrow-right ms-1"></i>
                  </a>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>'''

html = re.sub(services_carousel_track_pattern, new_services_cards, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html: Added docked core sectors bar and aligned 5 service carousel cards!")

# 3. Update css/style.css with styling for .sectors-cards-bar-section
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

sectors_bar_css = '''
/* ==========================================================================
   A2. Core Business Sectors Cards Bar (Elevated Docked Corporate Style)
   ========================================================================== */
.sectors-cards-bar-section {
  position: relative;
  z-index: 10;
  margin-top: -2.8rem;
  margin-bottom: 0.5rem;
  padding: 0;
}

.sectors-cards-bar {
  background: #ffffff;
  border-radius: 14px;
  border: 1px solid rgba(6, 43, 85, 0.08);
  box-shadow: 0 12px 36px rgba(6, 43, 85, 0.10), 0 2px 8px rgba(6, 43, 85, 0.04);
  display: flex;
  align-items: stretch;
  justify-content: space-between;
  padding: 1.25rem 0.85rem;
  transition: all 0.3s ease;
}

.sectors-cards-bar:hover {
  box-shadow: 0 16px 44px rgba(6, 43, 85, 0.13), 0 3px 10px rgba(6, 43, 85, 0.05);
}

.sector-card {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 12px;
  padding: 0.5rem 0.75rem;
  text-decoration: none;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  color: var(--primary-navy);
  border-radius: 10px;
}

.sector-card-icon-box {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background-color: var(--light-bg);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--primary-navy);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  border: 1px solid rgba(6, 43, 85, 0.06);
}

.sector-card-text {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.sector-card-title {
  font-family: var(--font-heading);
  font-size: 0.86rem;
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.34;
  transition: color 0.25s ease;
  text-align: center;
}

.sector-card:hover {
  transform: translateY(-4px);
}

.sector-card:hover .sector-card-icon-box {
  background-color: var(--accent-orange);
  color: #ffffff;
  border-color: var(--accent-orange);
  transform: scale(1.08);
  box-shadow: 0 4px 14px rgba(255, 121, 0, 0.35);
}

.sector-card:hover .sector-card-title {
  color: var(--accent-orange);
}

.sector-card-divider {
  width: 1px;
  background-color: rgba(6, 43, 85, 0.10);
  align-self: stretch;
  margin: 0.4rem 0;
}

/* Responsive adjustments */
@media (max-width: 991.98px) {
  .sectors-cards-bar-section {
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
  }

  .sectors-cards-bar {
    flex-wrap: wrap;
    gap: 1.25rem 0;
    padding: 1.25rem 0.5rem;
  }

  .sector-card {
    flex: 0 0 50%;
  }

  .sector-card:last-child {
    flex: 0 0 100%;
  }

  .sector-card-divider {
    display: none;
  }
}

@media (max-width: 575.98px) {
  .sector-card {
    flex: 0 0 100%;
    padding: 0.75rem 0.5rem;
    border-bottom: 1px solid rgba(6, 43, 85, 0.06);
  }

  .sector-card:last-child {
    border-bottom: none;
  }
}
'''

# Adjust .about-section top padding
old_about_padding = '.about-section {\n  padding-top: 4.5rem !important;\n}'
new_about_padding = '.about-section {\n  padding-top: 5.5rem !important;\n}'

if old_about_padding in css:
    css = css.replace(old_about_padding, new_about_padding)
    print("Updated .about-section padding-top to 5.5rem!")

# Append sectors bar css before B. About Us Section
about_marker = '/* ==========================================================================\n   B. About Us Section'
if about_marker in css:
    css = css.replace(about_marker, sectors_bar_css + '\n' + about_marker)
    print("Appended sectors bar CSS into style.css!")
else:
    css += '\n' + sectors_bar_css
    print("Appended sectors bar CSS to end of style.css!")

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 4. Update js/script.js serviceDetailsData to include the new keys
with open('js/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update serviceDetailsData in js/script.js
old_js_start = 'const serviceDetailsData = {'
new_js_data = '''const serviceDetailsData = {
    'medical': {
      title: 'Medical & Healthcare Supplies',
      category: 'Procurement Sector 01',
      description: 'Procurement and supply of hospital-grade medical equipment, clinical diagnostic devices, surgical instruments, sterilization systems, and certified clinical consumables. Compliant with ISO and CE standards.',
      items: [
        'Diagnostic & Patient Monitoring Systems',
        'Hospital Surgical Instruments & Equipment',
        'Clinical Laboratory Diagnostic Analyzers',
        'Healthcare Disposables & Sterilization Gear',
        'Emergency Care & ICU Support Hardware',
        'Direct OEM Healthcare Sourcing'
      ],
      compliance: 'Strict adherence to medical-grade standards, manufacturer calibration records, and rapid institutional delivery.'
    },
    'medical-equipment': {
      title: 'Medical & Healthcare Supplies',
      category: 'Procurement Sector 01',
      description: 'Procurement and supply of medical equipment, healthcare devices, and related clinical requirements.',
      items: ['Diagnostic Systems', 'Surgical Instruments', 'Clinical Disposables'],
      compliance: 'ISO/CE certified'
    },
    'it': {
      title: 'GCC & IT Infrastructure',
      category: 'Procurement Sector 02',
      description: 'Comprehensive computing, server hardware, cloud workstations, high-speed networking, and enterprise infrastructure tailored for Global Capability Centers and corporate enterprises.',
      items: [
        'Enterprise Servers & Data Center Racks',
        'High-Performance Workstations & Smart Laptops',
        'Managed Switches, Routers & Structured Cabling',
        'Modular UPS Power & Secure Server Cabinets',
        'GCC Command Center Systems & Displays',
        'Multi-facility Enterprise IT Hardware Deployment'
      ],
      compliance: 'OEM-backed warranty support, bulk configuration, and turn-key deployment.'
    },
    'it-infrastructure': {
      title: 'GCC & IT Infrastructure',
      category: 'Procurement Sector 02',
      description: 'Supply of enterprise servers and IT infrastructure.',
      items: ['Enterprise Servers', 'Networking Hardware', 'Cloud Workstations'],
      compliance: 'OEM-backed warranty'
    },
    'govt-education': {
      title: 'Government & Education Projects',
      category: 'Procurement Sector 03',
      description: 'Institutional procurement, school transformation programs, interactive digital classroom setups, and turnkey equipment deployments for state government initiatives.',
      items: [
        'Interactive Smart Boards & Digital Classroom Panels',
        'Computer Labs & Educational Hardware Systems',
        'Institutional Furniture & STEM Lab Equipment',
        'Public Infrastructure Project Hardware',
        'School Transformation & Turnkey Sourcing',
        'State-Wide Bulk Logistics Coordination'
      ],
      compliance: 'Government tender specifications compliance, rigorous pre-dispatch testing, and on-site commissioning.'
    },
    'industrial': {
      title: 'Industrial & Manufacturing Supplies',
      category: 'Procurement Sector 04',
      description: 'Certified structural TMT steel, heavy plates, industrial fabrication sections, raw materials, and commercial-grade textile yarn for production and manufacturing plants.',
      items: [
        'TMT Steel Bars (Fe 500 / 550 Grade Standards)',
        'Structural Steel Sections (Beams, Channels, Angles, Pipes)',
        'Industrial Grade Plates & Cold-Rolled Sheets',
        'Commercial & Industrial Cotton/Synthetic Yarn',
        'Specialty Textile Fibers & Heavy Filament Yarns',
        'Custom Bulk Mill-Direct Freight Coordination'
      ],
      compliance: 'Certified mill test reports (MTR), standard metallurgical tolerances, and transparent weight verification.'
    },
    'steel-yarn': {
      title: 'Industrial & Manufacturing Supplies',
      category: 'Procurement Sector 04',
      description: 'Structural steel and industrial supplies.',
      items: ['TMT Steel', 'Industrial Sections', 'Commercial Yarn'],
      compliance: 'MTR certified'
    },
    'auto': {
      title: 'Automobile & Transportation Supplies',
      category: 'Procurement Sector 05',
      description: 'Sourcing and procurement of commercial transport vehicle spares, heavy bus assemblies, braking components, suspension units, and certified maintenance hardware for public transport workshops.',
      items: [
        'Commercial Bus Chassis & Suspension Components',
        'Heavy-Duty Braking Drums, Liners & Air Brake Valves',
        'Engine Overhaul Components, Gaskets & Bearings',
        'Transmission Gears, Clutch Assemblies & Propeller Shafts',
        'Electrical Starters, Alternators & Fleet Lighting Systems',
        'OEM & Grade-A Aftermarket Maintenance Spares'
      ],
      compliance: 'High endurance benchmarks, precision dimensional matching for commercial fleet durability.'
    },
    'automobile-parts': {
      title: 'Automobile & Transportation Supplies',
      category: 'Procurement Sector 05',
      description: 'Fleet vehicle spares and transit components.',
      items: ['Chassis Components', 'Braking Systems', 'Engine Parts'],
      compliance: 'Fleet endurance certified'
    }'''

if old_js_start in js:
    # find closing brace of serviceDetailsData
    end_pos = js.find('};\n', js.find(old_js_start))
    if end_pos != -1:
        js = js[:js.find(old_js_start)] + new_js_data + '\n  ' + js[end_pos:]
        print("Updated js/script.js serviceDetailsData with 5 new professional sectors!")
    else:
        print("Could not find end of serviceDetailsData in js/script.js")

with open('js/script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("All updates applied cleanly!")
