# scratch/create_why_us_section.py

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

services_end_marker = '    </section>\n\n    <!-- ==========================================================================\n         E. OUR CLIENTS'
if services_end_marker not in html:
    print("Error: Could not locate end of services section!")
    exit(1)

why_us_html = '''    </section>

    <!-- ==========================================================================
         D. WHY CHOOSE US (EXACT REFERENCE DESIGN - 3x2 DARK CORPORATE GRID)
         ========================================================================== -->
    <section class="why-us-section" id="why-us" aria-label="Why Partner With GSR Global Enterprises">
      <div class="container">

        <!-- Section Header (Centered Brand Dash Style) -->
        <div class="text-center mb-5 fade-up-element">
          <div class="why-eyebrow mb-2">
            <span class="why-eyebrow-dash"></span>
            <span class="why-eyebrow-text">WHY CHOOSE US</span>
            <span class="why-eyebrow-dash"></span>
          </div>
          <h2 class="why-section-title mb-2">
            Why Partner With GSR GLOBAL ENTERPRISES
          </h2>
          <p class="why-section-subtitle mx-auto">
            We simplify complex procurement challenges by providing a single, dependable corporate interface across diverse industry sectors.
          </p>
        </div>

        <!-- 3x2 Grid (Exact Reference Card Design: Dark Card, Outline Icon Box, Bold Title, Clean Desc) -->
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">

          <!-- Card 1: Multi-Sector Capabilities -->
          <div class="col fade-up-element">
            <div class="why-ref-card h-100">
              <div class="why-ref-icon-box" aria-hidden="true">
                <i class="bi bi-layers"></i>
              </div>
              <h3 class="why-ref-title">MULTI-SECTOR CAPABILITIES</h3>
              <p class="why-ref-desc">
                Broad sourcing reach spanning healthcare, digital IT infrastructure, industrial materials, transit spares, and renewable power.
              </p>
            </div>
          </div>

          <!-- Card 2: Diverse Product Sourcing -->
          <div class="col fade-up-element">
            <div class="why-ref-card h-100">
              <div class="why-ref-icon-box" aria-hidden="true">
                <i class="bi bi-box-seam"></i>
              </div>
              <h3 class="why-ref-title">DIVERSE PRODUCT SOURCING</h3>
              <p class="why-ref-desc">
                Direct connections with certified OEM factories, foundries, and technology vendors capable of handling specialized procurement batches.
              </p>
            </div>
          </div>

          <!-- Card 3: Reliable Supply Solutions -->
          <div class="col fade-up-element">
            <div class="why-ref-card h-100">
              <div class="why-ref-icon-box" aria-hidden="true">
                <i class="bi bi-truck"></i>
              </div>
              <h3 class="why-ref-title">RELIABLE SUPPLY SOLUTIONS</h3>
              <p class="why-ref-desc">
                Established regional transport and distribution logistics that ensure timely arrivals and dependable inventory delivery.
              </p>
            </div>
          </div>

          <!-- Card 4: Customer-Oriented Service -->
          <div class="col fade-up-element">
            <div class="why-ref-card h-100">
              <div class="why-ref-icon-box" aria-hidden="true">
                <i class="bi bi-people"></i>
              </div>
              <h3 class="why-ref-title">CUSTOMER-ORIENTED SERVICE</h3>
              <p class="why-ref-desc">
                Tailored procurement strategies matched to the exact operational objectives and administrative schedules of each client organization.
              </p>
            </div>
          </div>

          <!-- Card 5: Quality-Focused Approach -->
          <div class="col fade-up-element">
            <div class="why-ref-card h-100">
              <div class="why-ref-icon-box" aria-hidden="true">
                <i class="bi bi-shield-check"></i>
              </div>
              <h3 class="why-ref-title">QUALITY-FOCUSED APPROACH</h3>
              <p class="why-ref-desc">
                Uncompromising standard of material verification, compliance certification checks, and rigorous batch quality assurance.
              </p>
            </div>
          </div>

          <!-- Card 6: Professional Coordination -->
          <div class="col fade-up-element">
            <div class="why-ref-card h-100">
              <div class="why-ref-icon-box" aria-hidden="true">
                <i class="bi bi-briefcase"></i>
              </div>
              <h3 class="why-ref-title">PROFESSIONAL COORDINATION</h3>
              <p class="why-ref-desc">
                Clear communication, proactive milestone tracking, and seamless administrative support throughout the purchase order lifecycle.
              </p>
            </div>
          </div>

        </div>

      </div>
    </section>'''

# Replace the boundary with why_us_html followed by the clients section marker
new_html = html.replace(services_end_marker, why_us_html + '\n\n    <!-- ==========================================================================\n         E. CLIENTS')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated index.html with Why Choose Us section!")

# Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

why_us_css = '''
/* ==========================================================================
   D. Why Choose Us Section - Exact Reference Design (Dark 3x2 Corporate Grid)
   ========================================================================== */
.why-us-section {
  padding: 4.5rem 0 5rem;
  background-color: #071529; /* Deep Dark Corporate Navy */
  position: relative;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

/* Eyebrow in Dark Mode */
.why-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 10px;
}

.why-eyebrow-dash {
  width: 24px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.why-eyebrow-text {
  font-family: var(--font-heading);
  font-size: 0.80rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--accent-orange);
}

.why-section-title {
  font-family: var(--font-heading);
  font-size: clamp(1.75rem, 2.4vw, 2.15rem);
  font-weight: 700;
  color: #ffffff;
  line-height: 1.25;
  letter-spacing: -0.02em;
}

.why-section-subtitle {
  font-family: var(--font-body);
  font-size: clamp(0.88rem, 0.98vw, 0.94rem);
  color: #94a3b8;
  line-height: 1.55;
  max-width: 700px;
}

/* Reference Card Style (Dark Background, Thin Outline, Centered Icon Box) */
.why-ref-card {
  background-color: #0d213d; /* Dark Card Surface */
  border: 1px solid rgba(255, 255, 255, 0.10);
  border-radius: 10px;
  padding: 2.2rem 1.6rem 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  transition: all 0.32s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.22);
}

.why-ref-card:hover {
  transform: translateY(-6px);
  border-color: var(--accent-orange);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.40);
  background-color: #102849;
}

/* Square Icon Box with Coral/Orange Outline (Exact Reference Style) */
.why-ref-icon-box {
  width: 44px;
  height: 44px;
  border: 1.5px solid var(--accent-orange);
  border-radius: 8px;
  background-color: rgba(255, 121, 0, 0.08);
  color: var(--accent-orange);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  margin-bottom: 1.15rem;
  transition: all 0.28s ease;
}

.why-ref-card:hover .why-ref-icon-box {
  background-color: var(--accent-orange);
  color: #ffffff;
  transform: scale(1.08);
  box-shadow: 0 4px 14px rgba(255, 121, 0, 0.35);
}

/* Card Title (Bold Uppercase White) */
.why-ref-title {
  font-family: var(--font-heading);
  font-size: 0.94rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #ffffff;
  line-height: 1.35;
  margin-bottom: 0.65rem;
  transition: color 0.25s ease;
}

.why-ref-card:hover .why-ref-title {
  color: var(--accent-orange);
}

/* Card Description (Light Grey Open Sans) */
.why-ref-desc {
  font-family: var(--font-body);
  font-size: 0.82rem;
  color: #94a3b8;
  line-height: 1.55;
  margin-bottom: 0;
  flex-grow: 1;
}

/* Responsive adjustments */
@media (max-width: 991.98px) {
  .why-us-section {
    padding: 3.5rem 0 4rem;
  }
}

@media (max-width: 575.98px) {
  .why-ref-card {
    padding: 1.75rem 1.25rem;
  }
  
  .why-section-title {
    font-size: 1.55rem;
  }
}
'''

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(why_us_css)

print("Appended Why Choose Us styles to css/style.css successfully!")
