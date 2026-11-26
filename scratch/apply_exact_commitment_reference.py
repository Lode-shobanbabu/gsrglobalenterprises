import re

# 1. New HTML for #commitment section matching reference image exactly
new_commitment_html = """    <!-- ==========================================================================
         F. OUR COMMITMENT (EXACT REFERENCE DESIGN - SPLIT WITH 2x2 CARDS)
         ========================================================================== -->
    <section class="commitment-ref-section" id="commitment" aria-label="Our Commitment to Reliable Sourcing">
      <div class="container">
        <div class="row align-items-center g-4 g-xl-5">

          <!-- Left Column: Content & Action Button -->
          <div class="col-lg-5 fade-up-element">
            <div class="commitment-ref-content">

              <!-- Eyebrow: Orange Dash + Dark Navy Text -->
              <div class="commitment-ref-eyebrow mb-3">
                <span class="commitment-ref-dash" aria-hidden="true"></span>
                <span class="commitment-ref-tag">OUR COMMITMENT</span>
              </div>

              <!-- Main Heading -->
              <h2 class="commitment-ref-title mb-3">
                Reliable Supply, Built on Trust
              </h2>

              <!-- Lead Description -->
              <p class="commitment-ref-desc mb-4">
                We are committed to understanding each requirement, sourcing with care and keeping our clients informed at every step.
              </p>

              <!-- CTA Button -->
              <div class="commitment-ref-btn-wrap">
                <a href="#contact" class="btn-commitment-ref">
                  <span>Discuss Your Requirements</span>
                  <i class="bi bi-chevron-right ms-2"></i>
                </a>
              </div>

            </div>
          </div>

          <!-- Right Column: 2x2 Grid of 4 White Cards -->
          <div class="col-lg-7 fade-up-element">
            <div class="row g-4">

              <!-- Card 01: Quality-Focused Sourcing (Navy Badge) -->
              <div class="col-sm-6">
                <div class="commitment-ref-card h-100">
                  <div class="commitment-ref-badge badge-navy">01</div>
                  <h3 class="commitment-ref-card-title">Quality-Focused Sourcing</h3>
                  <p class="commitment-ref-card-desc">
                    Products selected to match your specifications and industry needs.
                  </p>
                </div>
              </div>

              <!-- Card 02: Clear Communication (Orange Badge) -->
              <div class="col-sm-6">
                <div class="commitment-ref-card h-100">
                  <div class="commitment-ref-badge badge-orange">02</div>
                  <h3 class="commitment-ref-card-title">Clear Communication</h3>
                  <p class="commitment-ref-card-desc">
                    Straightforward updates from the first enquiry to final delivery.
                  </p>
                </div>
              </div>

              <!-- Card 03: Timely Delivery (Orange Badge) -->
              <div class="col-sm-6">
                <div class="commitment-ref-card h-100">
                  <div class="commitment-ref-badge badge-orange">03</div>
                  <h3 class="commitment-ref-card-title">Timely Delivery</h3>
                  <p class="commitment-ref-card-desc">
                    Procurement planned carefully around your timelines.
                  </p>
                </div>
              </div>

              <!-- Card 04: Long-Term Partnership (Navy Badge) -->
              <div class="col-sm-6">
                <div class="commitment-ref-card h-100">
                  <div class="commitment-ref-badge badge-navy">04</div>
                  <h3 class="commitment-ref-card-title">Long-Term Partnership</h3>
                  <p class="commitment-ref-card-desc">
                    Support that continues as your requirements grow and change.
                  </p>
                </div>
              </div>

            </div>
          </div>

        </div>
      </div>
    </section>"""

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

pattern = r'<!-- =+[\r\n\s]+F\. OUR COMMITMENT.*?<\/section>'
match = re.search(pattern, html, flags=re.DOTALL)
if match:
    html_new = html[:match.start()] + new_commitment_html + html[match.end():]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_new)
    print("index.html updated successfully.")
else:
    print("WARNING: Could not match commitment section in index.html!")

# 2. New CSS for commitment section
new_commitment_css = """/* ==========================================================================
   F. Our Commitment Section (Exact Reference Design - Split Layout + 2x2 Grid)
   ========================================================================== */
.commitment-ref-section {
  padding: 5.5rem 0 5.75rem;
  background-color: #f4f8fc;
  border-top: 1px solid rgba(6, 43, 85, 0.06);
  border-bottom: 1px solid rgba(6, 43, 85, 0.06);
  position: relative;
}

/* Eyebrow with Left Orange Dash */
.commitment-ref-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 12px;
}

.commitment-ref-dash {
  width: 34px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.commitment-ref-tag {
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--primary-navy);
}

/* Headline */
.commitment-ref-title {
  font-family: var(--font-heading);
  font-size: clamp(2rem, 2.7vw, 2.65rem);
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.2;
  letter-spacing: -0.02em;
}

/* Subtext */
.commitment-ref-desc {
  font-family: var(--font-body);
  font-size: 0.98rem;
  color: #4b5868;
  line-height: 1.62;
  max-width: 440px;
}

/* Orange Pill Button */
.btn-commitment-ref {
  display: inline-flex;
  align-items: center;
  background-color: var(--accent-orange);
  color: #ffffff;
  border-radius: 50px;
  padding: 0.78rem 1.85rem;
  font-family: var(--font-heading);
  font-size: 0.88rem;
  font-weight: 600;
  letter-spacing: 0.01em;
  text-decoration: none;
  box-shadow: 0 4px 18px rgba(255, 121, 0, 0.32);
  transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
}

.btn-commitment-ref:hover {
  background-color: var(--brand-orange-hover);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(255, 121, 0, 0.45);
}

.btn-commitment-ref i {
  font-size: 0.82rem;
  font-weight: 700;
  -webkit-text-stroke: 0.4px currentColor;
  transition: transform 0.2s ease;
}

.btn-commitment-ref:hover i {
  transform: translateX(3px);
}

/* 2x2 Grid Cards */
.commitment-ref-card {
  background: #ffffff;
  border-radius: 20px;
  padding: 2.1rem 1.85rem 2rem;
  box-shadow: 0 10px 30px rgba(6, 43, 85, 0.05);
  border: 1px solid rgba(6, 43, 85, 0.04);
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
}

.commitment-ref-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 18px 40px rgba(6, 43, 85, 0.10);
  border-color: rgba(255, 121, 0, 0.3);
}

/* Circular Number Badges */
.commitment-ref-badge {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-heading);
  font-size: 0.95rem;
  font-weight: 700;
  margin-bottom: 1.35rem;
  flex-shrink: 0;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
}

.commitment-ref-badge.badge-navy {
  background-color: var(--primary-navy);
  color: #ffffff;
}

.commitment-ref-badge.badge-orange {
  background-color: var(--accent-orange);
  color: #ffffff;
}

/* Card Title */
.commitment-ref-card-title {
  font-family: var(--font-heading);
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.32;
  margin-bottom: 0.65rem;
}

/* Card Description */
.commitment-ref-card-desc {
  font-family: var(--font-body);
  font-size: 0.88rem;
  color: #556980;
  line-height: 1.55;
  margin-bottom: 0;
}

/* Responsive adjustments */
@media (max-width: 991.98px) {
  .commitment-ref-section {
    padding: 3.75rem 0 4.25rem;
  }
  .commitment-ref-desc {
    max-width: 100%;
  }
}

@media (max-width: 575.98px) {
  .commitment-ref-card {
    padding: 1.75rem 1.4rem;
  }
}"""

with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css_pattern = r'/\* =+[\r\n\s]+F\. Our Commitment Section.*$'
css_match = re.search(css_pattern, css, flags=re.DOTALL)
if css_match:
    css_new = css[:css_match.start()] + new_commitment_css + "\n"
    with open("css/style.css", "w", encoding="utf-8") as f:
        f.write(css_new)
    print("css/style.css updated successfully.")
else:
    print("WARNING: Could not match commitment section in css/style.css!")
