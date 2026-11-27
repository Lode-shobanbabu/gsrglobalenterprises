import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_commitment_html = '''    <!-- ==========================================================================
         F. OUR COMMITMENT (EXECUTIVE PROCUREMENT SHOWCASE BANNER)
         ========================================================================== -->
    <section class="commitment-mockup-section" id="commitment" aria-label="Our Commitment to Reliable Sourcing">
      <div class="container">

        <div class="commitment-banner-card fade-up-element">

          <!-- Left Side Background Image & Brand Navy Gradient Overlay -->
          <div class="commitment-left-bg" aria-hidden="true">
            <picture>
              <source srcset="assets/images/hero-logistics-global.webp" type="image/webp">
              <img src="assets/images/hero-logistics-global.jpg" alt="" class="commitment-left-bg-img" loading="lazy">
            </picture>
            <div class="commitment-left-overlay"></div>
            <div class="commitment-radial-glow"></div>
          </div>

          <div class="row g-0 commitment-banner-row align-items-stretch">

            <!-- Left Column: Content with Brand Colors & Typography (No Buttons) -->
            <div class="col-lg-7 col-xl-7 commitment-content-col">
              <div class="commitment-text-wrap position-relative z-3">

                <!-- Eyebrow: Orange Dash + Bold Orange Text -->
                <div class="commitment-mockup-eyebrow mb-3">
                  <span class="mockup-eyebrow-dash" aria-hidden="true"></span>
                  <span class="mockup-eyebrow-text">OUR COMMITMENT</span>
                </div>

                <!-- Main Heading with Highlighted "Count On" in Brand Orange -->
                <h2 class="commitment-mockup-title mb-4">
                  A Commitment<br>You Can <span class="text-orange">Count On</span>
                </h2>

                <!-- Narrative Body Paragraphs (0.98rem / 400 Weight Site-Wide Standard) -->
                <p class="commitment-mockup-lead mb-3">
                  At <strong>GSR Global Enterprises</strong>, we believe successful procurement goes beyond sourcing
                  products. It is about understanding business needs, coordinating the right resources and building
                  relationships based on trust.
                </p>

                <p class="commitment-mockup-body mb-0">
                  Whether you require specialized medical devices, IT infrastructure for educational projects, industrial
                  raw materials, automotive components or solar energy products, we are committed to supporting your
                  procurement requirements with professionalism and dedication.
                </p>

              </div>
            </div>

            <!-- Right Column: Website-Related Visual Showcase (Not Mobile!) -->
            <div class="col-lg-5 col-xl-5 commitment-visual-col">
              <picture>
                <source srcset="assets/images/about-procurement-facility.webp" type="image/webp">
                <img src="assets/images/about-procurement-facility.webp" alt="GSR Global Procurement &amp; Distribution Operations" class="commitment-visual-img" loading="lazy">
              </picture>
              <div class="commitment-visual-blend-overlay" aria-hidden="true"></div>

              <!-- Trust Badge Pill -->
              <div class="commitment-badge-pill">
                <i class="bi bi-shield-fill-check text-orange" aria-hidden="true"></i>
                <span>Multi-Industry Supply Network</span>
              </div>
            </div>

          </div>

        </div>

      </div>
    </section>'''

html_new, n_html = re.subn(
    r'<section class="commitment-mockup-section" id="commitment".*?</section>',
    new_commitment_html.strip(),
    html,
    flags=re.DOTALL
)

print(f"Replaced in index.html: {n_html} occurrence(s)")
if n_html == 1:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_new)
    print("Saved index.html successfully.")
else:
    print("Error: Could not match commitment section in index.html")
