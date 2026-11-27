import os
import re
import subprocess
from PIL import Image

# 1. Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build the complete updated services section
services_start = '<!-- ==========================================================================\n         C. OUR SERVICES'
services_end = '<!-- ==========================================================================\n         D. INDUSTRIES WE SERVE'

idx1 = html.find(services_start)
idx2 = html.find(services_end)
assert idx1 != -1 and idx2 != -1, f"Services section markers not found: idx1={idx1}, idx2={idx2}"

new_services_html = '''<!-- ==========================================================================
         C. OUR SERVICES (6 CARDS - 3 PER ROW PROFESSIONAL GRID WITH BOTTOM CTA)
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
          <h2 class="services-section-title mb-2">
            Comprehensive Procurement Solutions Across Multiple Industries
          </h2>
          <p class="services-section-subtitle mx-auto">
            From specialized equipment to essential industrial materials, we help customers source the right products
            for their business and project requirements.
          </p>
        </div>

        <!-- 3 Cards Per Row Grid Layout (6 Cards Total) -->
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
                <div class="service-pro-footer">
                  <a href="#contact" class="service-pro-link" aria-label="Request Quote for Medical &amp; Healthcare Supplies">
                    <span>Request Quote</span>
                    <i class="bi bi-arrow-right"></i>
                  </a>
                </div>
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
                <div class="service-pro-footer">
                  <a href="#contact" class="service-pro-link" aria-label="Request Quote for GCC &amp; IT Infrastructure">
                    <span>Request Quote</span>
                    <i class="bi bi-arrow-right"></i>
                  </a>
                </div>
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
                  Supporting government departments, educational programs and institutional development projects with
                  dependable procurement and supply services.
                </p>
                <div class="service-pro-divider"></div>
                <ul class="service-pro-checklist">
                  <li><i class="bi bi-chevron-right"></i><span>School transformation projects</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Educational technology and equipment</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Institutional infrastructure supplies</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Bulk procurement for public-sector projects</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Project-specific sourcing requirements</span></li>
                </ul>
                <div class="service-pro-footer">
                  <a href="#contact" class="service-pro-link" aria-label="Request Quote for Government &amp; Education Projects">
                    <span>Request Quote</span>
                    <i class="bi bi-arrow-right"></i>
                  </a>
                </div>
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
                <div class="service-pro-footer">
                  <a href="#contact" class="service-pro-link" aria-label="Request Quote for Industrial &amp; Manufacturing Supplies">
                    <span>Request Quote</span>
                    <i class="bi bi-arrow-right"></i>
                  </a>
                </div>
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
                <div class="service-pro-footer">
                  <a href="#contact" class="service-pro-link" aria-label="Request Quote for Automobile &amp; Transportation Supplies">
                    <span>Request Quote</span>
                    <i class="bi bi-arrow-right"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 6: Solar & Renewable Energy Supplies -->
          <div class="col-lg-4 col-md-6 fade-up-element">
            <div class="service-pro-card h-100">
              <div class="service-pro-media">
                <img src="assets/images/service-pro-solar.webp" alt="Solar & Renewable Energy Supplies"
                  loading="lazy">
              </div>
              <div class="service-pro-body">
                <h3 class="service-pro-title">Solar &amp; Renewable Energy Supplies</h3>
                <p class="service-pro-desc">
                  Supporting renewable energy initiatives through procurement of solar panels and related solar energy products.
                </p>
                <div class="service-pro-divider"></div>
                <ul class="service-pro-checklist">
                  <li><i class="bi bi-chevron-right"></i><span>Solar photovoltaic panels</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Solar energy equipment</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Renewable energy project supplies</span></li>
                  <li><i class="bi bi-chevron-right"></i><span>Solar installation-related materials</span></li>
                </ul>
                <div class="service-pro-footer">
                  <a href="#contact" class="service-pro-link" aria-label="Request Quote for Solar &amp; Renewable Energy Supplies">
                    <span>Request Quote</span>
                    <i class="bi bi-arrow-right"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>

        </div>

        <!-- Centered Bottom CTA Section (Below All 6 Cards) -->
        <div class="services-bottom-cta text-center mt-5 fade-up-element">
          <p class="services-cta-heading mb-3">Have a Specific Requirement? Let's Discuss.</p>
          <a href="#contact" class="btn header-cta-orange services-center-cta" aria-label="Request a Procurement Quote">
            <span>Request a Quote</span>
            <i class="bi bi-arrow-right"></i>
          </a>
        </div>

      </div>
    </section>

    '''

html = html[:idx1] + new_services_html + html[idx2:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html updated with 6 service cards and centered CTA!")

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update .service-pro-checklist li and li i
target_checklist_css = """.service-pro-checklist li {
  display: flex;
  align-items: flex-start;
  gap: 9px;
  font-family: var(--font-body);
  font-size: 0.83rem;
  color: #2c3e50;
  line-height: 1.42;
  font-weight: 400;
}

.service-pro-checklist li i {
  color: #FF7900;
  font-size: 0.85rem;
  font-weight: 700;
  flex-shrink: 0;
  margin-top: 2px;
  transition: transform 0.22s ease, color 0.22s ease;
}

.service-pro-card:hover .service-pro-checklist li i {
  transform: translateX(3px);
  color: #FF7900;
}"""

replacement_checklist_css = """.service-pro-checklist li {
  display: flex;
  align-items: flex-start;
  gap: 9px;
  font-family: var(--font-body);
  font-size: 0.98rem;
  color: #2c3e50;
  line-height: 1.52;
  font-weight: 400;
}

.service-pro-checklist li span {
  font-size: 0.98rem;
  font-weight: 400;
}

.service-pro-checklist li i {
  color: #FF7900;
  font-size: 0.82rem;
  font-weight: 300;
  -webkit-text-stroke: 0;
  flex-shrink: 0;
  margin-top: 4px;
  transition: transform 0.22s ease, color 0.22s ease;
}

.service-pro-card:hover .service-pro-checklist li i {
  transform: translateX(3px);
  color: #FF7900;
}"""

assert target_checklist_css in css, "target_checklist_css not found in css/style.css"
css = css.replace(target_checklist_css, replacement_checklist_css, 1)

# Add styling for .service-pro-link and .services-bottom-cta
target_footer_css = """/* Card Footer (Single Full-Width Sleek Button) */
.service-pro-footer {
  margin-top: auto;
  padding-top: 0.95rem;
  border-top: 1px solid rgba(6, 43, 85, 0.08);
}

.btn-pro-readmore {
  width: 100%;
  background: var(--primary-navy);
  color: #ffffff;
  border: 1.5px solid var(--primary-navy);
  border-radius: 50px;
  padding: 0.65rem 1.25rem;
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: 0.03em;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.28s ease;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(6, 43, 85, 0.12);
}

.btn-pro-readmore i {
  font-size: 0.85rem;
  font-weight: 700;
  -webkit-text-stroke: 0.4px currentColor;
  transition: transform 0.25s ease;
}

.btn-pro-readmore:hover {
  background: var(--accent-orange);
  border-color: var(--accent-orange);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(255, 121, 0, 0.32);
}

.btn-pro-readmore:hover i {
  transform: translateX(4px);
}"""

replacement_footer_css = """/* Card Footer: Clean "Request Quote ->" Link Matching User Reference Style */
.service-pro-footer {
  margin-top: auto;
  padding-top: 1.1rem;
  border-top: 1px solid rgba(6, 43, 85, 0.08);
}

.service-pro-link {
  font-family: var(--font-heading);
  font-size: 0.90rem;
  font-weight: 600;
  color: var(--primary-navy);
  display: inline-flex;
  align-items: center;
  gap: 6px;
  text-decoration: none;
  transition: all 0.25s ease;
}

.service-pro-link i {
  font-size: 0.95rem;
  transition: transform 0.22s ease;
}

.service-pro-link:hover {
  color: var(--accent-orange);
}

.service-pro-link:hover i {
  transform: translateX(4px);
}

/* Centered Bottom CTA Section Below All Cards */
.services-bottom-cta {
  padding-top: 1.5rem;
}

.services-cta-heading {
  font-family: var(--font-heading);
  font-size: clamp(1.2rem, 1.8vw, 1.5rem);
  font-weight: 600;
  color: var(--primary-navy);
  margin-bottom: 1rem;
}

.services-center-cta {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 0.72rem 2rem;
  font-size: 0.95rem;
}"""

assert target_footer_css in css, "target_footer_css not found in css/style.css"
css = css.replace(target_footer_css, replacement_footer_css, 1)

# Also ensure .service-pro-checklist li span is included in site-wide body standard
if '.service-pro-desc,' in css:
    css = css.replace('.service-pro-desc,', '.service-pro-desc,\n.service-pro-checklist li,\n.service-pro-checklist li span,')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: css/style.css updated with card links, checklist font size, and centered bottom CTA!")

# 3. Verification
open_b = css.count('{')
close_b = css.count('}')
print(f"CSS Braces: {open_b} open, {close_b} close (diff = {open_b - close_b})")
assert open_b == close_b

div_o = len(re.findall(r'<div\b', html))
div_c = html.count('</div>')
sec_o = len(re.findall(r'<section\b', html))
sec_c = html.count('</section>')
print(f"HTML <div>: {div_o} vs {div_c}")
print(f"HTML <section>: {sec_o} vs {sec_c}")
assert div_o == div_c
assert sec_o == sec_c

sections = re.findall(r'<section[^>]+id=[\"\']([^\"\']+)[\"\']', html)
expected = ['hero', 'sectors', 'about', 'services', 'Industries', 'why-us', 'clients', 'process', 'commitment', 'contact']
print(f"HTML Sections: {sections}")
assert sections == expected

# Check card count in services
cards = len(re.findall(r'class="service-pro-card\b', html))
print(f"Total service cards in HTML: {cards}")
assert cards == 6

# 4. Take Screenshot with Chrome Headless
html_path = r"file:///D:/shoban/GSR%20GLOBAL%20ENTERPRISES/index.html#services"
abs_out = os.path.abspath(r"scratch\services_6cards_preview.png").replace('\\', '/')

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1400,1800",
    "--virtual-time-budget=2000",
    f"--screenshot={abs_out}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(abs_out):
    print("Screenshot captured at", abs_out)
    img_shot = Image.open(abs_out)
    # Crop the bottom rows of cards and centered CTA
    w, h = img_shot.size
    crop_bottom = img_shot.crop((50, 400, 1350, min(h, 1600)))
    crop_bottom.save(r"scratch\services_cards_bottom_crop.png")
    print("Crop saved to scratch/services_cards_bottom_crop.png")
