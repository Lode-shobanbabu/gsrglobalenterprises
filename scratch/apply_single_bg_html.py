import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_commitment_html = '''    <!-- ==========================================================================
         F. OUR COMMITMENT (FULL-WIDTH SINGLE BACKGROUND BANNER)
         ========================================================================== -->
    <section class="commitment-mockup-section" id="commitment" aria-label="Our Commitment">
      <!-- Single Full-Width Background Image -->
      <div class="commitment-single-bg" aria-hidden="true">
        <picture>
          <source srcset="assets/images/hero-logistics-global.webp" type="image/webp">
          <img src="assets/images/hero-logistics-global.jpg" alt="Global Procurement Logistics" loading="lazy">
        </picture>
      </div>

      <!-- Gradient Overlay on Left Side (Dissolves to Transparent on Right) -->
      <div class="commitment-gradient-overlay" aria-hidden="true"></div>

      <!-- Content Container -->
      <div class="commitment-content-wrap fade-up-element position-relative z-3">
        <!-- Eyebrow: Brand Orange Dash + Bold White Text -->
        <div class="commitment-eyebrow mb-2">
          <span class="commitment-eyebrow-dash" aria-hidden="true"></span>
          <span class="commitment-eyebrow-text">OUR COMMITMENT</span>
        </div>

        <!-- Section Title -->
        <h2 class="commitment-title mb-3">Our Commitment</h2>

        <!-- Narrative Paragraph 1 -->
        <p class="commitment-text mb-2">
          At <strong>GSR Global Enterprises</strong>, we believe successful procurement goes beyond sourcing products. It is about understanding business needs, coordinating the right resources and building relationships based on trust.
        </p>

        <!-- Narrative Paragraph 2 -->
        <p class="commitment-text mb-3">
          Whether you require specialized medical devices, IT infrastructure for educational projects, industrial raw materials, automotive components or solar energy products, we are committed to supporting your procurement requirements with professionalism and dedication.
        </p>

        <!-- Our Promise Callout Pill -->
        <div class="commitment-promise-pill">
          <i class="bi bi-shield-fill-check text-orange" aria-hidden="true"></i>
          <strong class="text-white">Our Promise:</strong>
          <span class="promise-highlight ms-1">Your Requirements. Our Commitment. Reliable Supply Solutions.</span>
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
