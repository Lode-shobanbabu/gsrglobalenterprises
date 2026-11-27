import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Hero Docked Cards: Ensure 4 cards with no descriptions
old_dock_pattern = re.compile(
    r'<section class="hero-docked-cards-section"[^>]*>.*?</section>',
    re.DOTALL
)

new_dock_section = '''<section class="hero-docked-cards-section" id="sectors" aria-label="Core Business Sectors">
      <div class="container">
        <div class="row row-cols-2 row-cols-lg-4 g-3 g-xl-4 justify-content-center">

          <!-- Card 1: Multi-Industry Procurement -->
          <div class="col fade-up-element">
            <div class="hero-dock-card h-100">
              <div class="dock-card-badge" aria-hidden="true">
                <i class="bi bi-boxes"></i>
              </div>
              <div class="dock-card-body">
                <h3 class="dock-card-title">Multi-Industry Procurement</h3>
              </div>
            </div>
          </div>

          <!-- Card 2: Reliable Sourcing Network -->
          <div class="col fade-up-element">
            <div class="hero-dock-card h-100">
              <div class="dock-card-badge" aria-hidden="true">
                <i class="bi bi-globe2"></i>
              </div>
              <div class="dock-card-body">
                <h3 class="dock-card-title">Reliable Sourcing Network</h3>
              </div>
            </div>
          </div>

          <!-- Card 3: Customer-Focused Solutions -->
          <div class="col fade-up-element">
            <div class="hero-dock-card h-100">
              <div class="dock-card-badge" aria-hidden="true">
                <i class="bi bi-person-check"></i>
              </div>
              <div class="dock-card-body">
                <h3 class="dock-card-title">Customer-Focused Solutions</h3>
              </div>
            </div>
          </div>

          <!-- Card 4: Quality-Driven Supply -->
          <div class="col fade-up-element">
            <div class="hero-dock-card h-100">
              <div class="dock-card-badge" aria-hidden="true">
                <i class="bi bi-patch-check"></i>
              </div>
              <div class="dock-card-body">
                <h3 class="dock-card-title">Quality-Driven Supply</h3>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>'''

html = old_dock_pattern.sub(new_dock_section, html, count=1)

# 2. Hero Headline: clean single-line title with no <br> tags
old_headline_pattern = re.compile(
    r'<h1 class="hero-main-title[^"]*">.*?</h1>',
    re.DOTALL
)
new_headline = '''<h1 class="hero-main-title fade-up-element">
              Connecting Industries With The Right Products, Resources &amp; Solutions
            </h1>'''
html = old_headline_pattern.sub(new_headline, html, count=1)

# 3. About Us: remove experience badge and frame-wrap
old_about_media_pattern = re.compile(
    r'<div class="about-ref-media-box">.*?</div>\s*</div>\s*</div>\s*<!-- Right Column',
    re.DOTALL
)
new_about_media = '''<div class="about-ref-media-box">
              <div class="about-ref-img-frame">
                <picture class="about-ref-picture">
                  <source srcset="assets/images/about-corporate-team-meeting.webp" type="image/webp">
                  <img src="assets/images/about-corporate-team-meeting.jpg"
                    alt="GSR Global Enterprises Corporate Team Consultation and Procurement Strategy"
                    class="about-ref-img" width="1200" height="896" loading="lazy">
                </picture>
              </div>
            </div>
          </div>

          <!-- Right Column'''
html = old_about_media_pattern.sub(new_about_media, html, count=1)

# 4. Services: Update 5 service cards without buttons and with complete bullet points
old_services_pattern = re.compile(
    r'<section class="services-section"[^>]*>.*?</section>',
    re.DOTALL
)

new_services_section = '''<section class="services-section" id="services">
      <div class="container">

        <!-- Section Header (Centered Corporate Style) -->
        <div class="text-center mb-4 fade-up-element">
          <div class="services-eyebrow mb-2">
            <span class="services-eyebrow-dash"></span>
            <span class="services-eyebrow-text">WHAT WE DO</span>
            <span class="services-eyebrow-dash"></span>
          </div>
          <h2 class="services-section-title mb-2">
            Comprehensive Procurement Solutions Across Multiple Industries
          </h2>
          <p class="services-section-subtitle mx-auto">
            From specialized equipment to essential industrial materials, we help customers source the right products
            for their business and project requirements.
          </p>
        </div>

        <!-- 3 Cards Per Row Grid Layout (Compact 3 Points Each) -->
        <div class="row g-4 justify-content-center">

          <!-- Card 1: Medical & Healthcare Supplies -->
          <div class="col-lg-4 col-md-6 fade-up-element">
            <div class="service-pro-card h-100">
              <div class="service-pro-media">
                <img src="assets/images/service-pro-medical.webp" alt="Medical & Healthcare Supplies" loading="lazy">
              </div>
              <div class="service-pro-body">
                <h3 class="service-pro-title">Medical &amp; Healthcare Supplies</h3>
                <p class="service-pro-desc">
                  Supporting healthcare institutions, hospitals and medical organizations with procurement of essential
                  medical equipment and devices.
                </p>
                <div class="service-pro-divider"></div>
                <ul class="service-pro-checklist">
                  <li><i class="bi bi-chevron-right"></i><span>Medical equipment and devices</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Hospital and clinical supplies</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Diagnostic and monitoring equipment</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Healthcare infrastructure requirements</span></li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Card 2: GCC & IT Infrastructure -->
          <div class="col-lg-4 col-md-6 fade-up-element">
            <div class="service-pro-card h-100">
              <div class="service-pro-media">
                <img src="assets/images/service-pro-it.webp" alt="GCC & IT Infrastructure" loading="lazy">
              </div>
              <div class="service-pro-body">
                <h3 class="service-pro-title">GCC &amp; IT Infrastructure</h3>
                <p class="service-pro-desc">
                  Providing computer systems, technology products and IT infrastructure for organizations and
                  large-scale school transformation projects and programs.
                </p>
                <div class="service-pro-divider"></div>
                <ul class="service-pro-checklist">
                  <li><i class="bi bi-chevron-right"></i><span>Desktop computers and laptops</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Computer laboratory equipment</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Networking and IT infrastructure</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Hardware and technology accessories</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Digital learning infrastructure</span></li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Card 3: Government & Education Projects -->
          <div class="col-lg-4 col-md-6 fade-up-element">
            <div class="service-pro-card h-100">
              <div class="service-pro-media">
                <img src="assets/images/service-pro-education.webp" alt="Government & Education Projects"
                  loading="lazy">
              </div>
              <div class="service-pro-body">
                <h3 class="service-pro-title">Government &amp; Education Projects</h3>
                <p class="service-pro-desc">
                  Supporting government departments, educational institutions and project implementation agencies
                  through coordinated procurement and supply solutions.
                </p>
                <div class="service-pro-divider"></div>
                <ul class="service-pro-checklist">
                  <li><i class="bi bi-chevron-right"></i><span>School transformation projects</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Educational technology and equipment</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Institutional infrastructure supplies</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Bulk procurement for public-sector projects</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Project-specific sourcing requirements</span></li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Card 4: Industrial & Manufacturing Supplies -->
          <div class="col-lg-4 col-md-6 fade-up-element">
            <div class="service-pro-card h-100">
              <div class="service-pro-media">
                <img src="assets/images/service-pro-industrial.webp" alt="Industrial & Manufacturing Supplies"
                  loading="lazy">
              </div>
              <div class="service-pro-body">
                <h3 class="service-pro-title">Industrial &amp; Manufacturing Supplies</h3>
                <p class="service-pro-desc">
                  Helping manufacturers and industrial businesses source essential raw materials and production-related
                  supplies.
                </p>
                <div class="service-pro-divider"></div>
                <ul class="service-pro-checklist">
                  <li><i class="bi bi-chevron-right"></i><span>Iron and steel materials</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Industrial raw materials</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Textile yarn and related supplies</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Manufacturing and production requirements</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Bulk material procurement</span></li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Card 5: Automobile & Transportation Supplies -->
          <div class="col-lg-4 col-md-6 fade-up-element">
            <div class="service-pro-card h-100">
              <div class="service-pro-media">
                <img src="assets/images/service-pro-automotive.webp" alt="Automobile & Transportation Supplies"
                  loading="lazy">
              </div>
              <div class="service-pro-body">
                <h3 class="service-pro-title">Automobile &amp; Transportation Supplies</h3>
                <p class="service-pro-desc">
                  Supporting automotive businesses, fleet operators and transportation projects with procurement of bus
                  parts and automotive components.
                </p>
                <div class="service-pro-divider"></div>
                <ul class="service-pro-checklist">
                  <li><i class="bi bi-chevron-right"></i><span>Bus spare parts and components</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Automotive mechanical components</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Vehicle maintenance supplies</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Transportation industry requirements</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Project-based automotive procurement</span></li>
                </ul>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>'''

html = old_services_pattern.sub(new_services_section, html, count=1)

# 5. Insert Industries We Serve right after Services and before Why Choose Us
industries_section_html = '''

    <!-- ==========================================================================
         D. INDUSTRIES WE SERVE (EXACT REFERENCE DESIGN - MINIMAL ARCHITECTURAL GRID)
         ========================================================================== -->
    <section class="industries-section" id="Industries" aria-label="Industries We Support">
      <div class="container">

        <!-- Section Header (Centered Brand Dash Style) -->
        <div class="text-center mb-5 fade-up-element">
          <div class="industries-eyebrow mb-2">
            <span class="industries-eyebrow-dash"></span>
            <span class="industries-eyebrow-text">INDUSTRIES WE SUPPORT</span>
            <span class="industries-eyebrow-dash"></span>
          </div>
          <h2 class="industries-section-title mb-3">
            Procurement Solutions Designed Around Your Industry
          </h2>
          <div class="industries-title-accent mx-auto mb-3"></div>
          <p class="industries-section-subtitle mx-auto">
            Different industries require different products, standards and supply capabilities. GSR Global Enterprises works across diverse sectors to support their sourcing and procurement needs.
          </p>
        </div>

        <!-- 3x2 Grid (3 Columns on Desktop, 2 on Tablet, 1 on Mobile) -->
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 g-lg-5">

          <!-- Item 1: Healthcare & Medical Institutions -->
          <div class="col fade-up-element">
            <div class="industry-grid-item">
              <div class="industry-item-icon" aria-hidden="true">
                <i class="bi bi-hospital"></i>
              </div>
              <h3 class="industry-item-title">Healthcare &amp; Medical Institutions</h3>
              <p class="industry-item-desc">
                Hospitals, clinics, healthcare providers and medical institutions.
              </p>
            </div>
          </div>

          <!-- Item 2: Education & Government -->
          <div class="col fade-up-element">
            <div class="industry-grid-item">
              <div class="industry-item-icon" aria-hidden="true">
                <i class="bi bi-bank"></i>
              </div>
              <h3 class="industry-item-title">Education &amp; Government</h3>
              <p class="industry-item-desc">
                Schools, government departments and institutional projects.
              </p>
            </div>
          </div>

          <!-- Item 3: Industrial & Manufacturing -->
          <div class="col fade-up-element">
            <div class="industry-grid-item">
              <div class="industry-item-icon" aria-hidden="true">
                <i class="bi bi-buildings"></i>
              </div>
              <h3 class="industry-item-title">Industrial &amp; Manufacturing</h3>
              <p class="industry-item-desc">
                Manufacturers, factories and industrial businesses.
              </p>
            </div>
          </div>

          <!-- Item 4: Automotive & Transportation -->
          <div class="col fade-up-element">
            <div class="industry-grid-item">
              <div class="industry-item-icon" aria-hidden="true">
                <i class="bi bi-bus-front"></i>
              </div>
              <h3 class="industry-item-title">Automotive &amp; Transportation</h3>
              <p class="industry-item-desc">
                Bus operators, automotive businesses and fleet management companies.
              </p>
            </div>
          </div>

          <!-- Item 5: Renewable Energy -->
          <div class="col fade-up-element">
            <div class="industry-grid-item">
              <div class="industry-item-icon" aria-hidden="true">
                <i class="bi bi-brightness-high"></i>
              </div>
              <h3 class="industry-item-title">Renewable Energy</h3>
              <p class="industry-item-desc">
                Solar energy businesses and renewable energy projects.
              </p>
            </div>
          </div>

          <!-- Item 6: IT & Technology -->
          <div class="col fade-up-element">
            <div class="industry-grid-item">
              <div class="industry-item-icon" aria-hidden="true">
                <i class="bi bi-display"></i>
              </div>
              <h3 class="industry-item-title">IT &amp; Technology</h3>
              <p class="industry-item-desc">
                Technology companies, institutions and digital infrastructure projects.
              </p>
            </div>
          </div>

        </div>

      </div>
    </section>
'''

# Find insertion point right before Why Choose Us
why_marker = '    <!-- ==========================================================================\n         D. WHY CHOOSE US'
if why_marker in html:
    html = html.replace(why_marker, industries_section_html + why_marker)
else:
    # Alternative marker
    why_section_marker = '<section class="why-us-section"'
    html = html.replace(why_section_marker, industries_section_html + '    ' + why_section_marker)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully!")
