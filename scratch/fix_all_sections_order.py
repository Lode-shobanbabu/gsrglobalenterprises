import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# First, remove ALL occurrences of <section class="industries-section" ... </section>
content = re.sub(r'\s*<!-- ==========================================================================\s*D\. INDUSTRIES WE SERVE.*?<\/section>', '', content, flags=re.DOTALL)
content = re.sub(r'\s*<section class="industries-section"[^>]*>.*?<\/section>', '', content, flags=re.DOTALL)

# The exact clean Industries We Support section
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
    </section>'''

# Place it EXACTLY below Services: after </section> of id="services"
services_end_marker = '</section>'
# Find the services section and its end
services_match = re.search(r'<section class="services-section" id="services".*?<\/section>', content, flags=re.DOTALL)
if services_match:
    end_pos = services_match.end()
    content = content[:end_pos] + industries_section_html + content[end_pos:]
    print("Placed Industries section directly below Services section!")
else:
    print("ERROR: services section not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html written successfully!")
