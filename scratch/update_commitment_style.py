import re

# 1. New HTML for #commitment section
new_commitment_html = """    <!-- ==========================================================================
         F. OUR COMMITMENT (SYMMETRICAL EXECUTIVE CORPORATE DESIGN)
         ========================================================================== -->
    <section class="commitment-section" id="commitment" aria-label="Our Commitment to Reliable Sourcing">
      <div class="container">

        <!-- Section Header (Centered Brand Dash Style) -->
        <div class="text-center mb-5 fade-up-element">
          <div class="commitment-eyebrow mb-2">
            <span class="commitment-eyebrow-dash"></span>
            <span class="commitment-eyebrow-text">OUR COMMITMENT</span>
            <span class="commitment-eyebrow-dash"></span>
          </div>
          <h2 class="commitment-section-title mb-3">
            Delivering Excellence Beyond Sourcing
          </h2>
          <p class="commitment-lead-intro mx-auto">
            At <strong>GSR Global Enterprises</strong>, we believe successful procurement goes beyond sourcing products. It is about understanding business needs, coordinating the right resources and building relationships based on trust.
          </p>
        </div>

        <!-- 3 Core Pillars (Symmetrical 3-Column Grid) -->
        <div class="row g-4 mb-5 justify-content-center">

          <!-- Pillar 1 -->
          <div class="col-lg-4 col-md-6 fade-up-element">
            <div class="commitment-pillar-card h-100">
              <div class="pillar-card-top">
                <div class="pillar-icon-wrapper">
                  <i class="bi bi-bullseye"></i>
                </div>
                <span class="pillar-index">01</span>
              </div>
              <h3 class="pillar-card-title">Understanding Business Needs</h3>
              <p class="pillar-card-text">
                Every procurement begins with listening. We analyze your technical specifications, project requirements, and operational timelines to ensure flawless execution from day one.
              </p>
              <div class="pillar-card-accent"></div>
            </div>
          </div>

          <!-- Pillar 2 -->
          <div class="col-lg-4 col-md-6 fade-up-element">
            <div class="commitment-pillar-card h-100">
              <div class="pillar-card-top">
                <div class="pillar-icon-wrapper">
                  <i class="bi bi-diagram-3"></i>
                </div>
                <span class="pillar-index">02</span>
              </div>
              <h3 class="pillar-card-title">Coordinating Right Resources</h3>
              <p class="pillar-card-text">
                We align direct OEM relationships, verified tier-one manufacturers, and specialized logistics channels to guarantee supply continuity and certified product quality.
              </p>
              <div class="pillar-card-accent"></div>
            </div>
          </div>

          <!-- Pillar 3 -->
          <div class="col-lg-4 col-md-6 fade-up-element">
            <div class="commitment-pillar-card h-100">
              <div class="pillar-card-top">
                <div class="pillar-icon-wrapper">
                  <i class="bi bi-shield-check"></i>
                </div>
                <span class="pillar-index">03</span>
              </div>
              <h3 class="pillar-card-title">Relationships Built on Trust</h3>
              <p class="pillar-card-text">
                Trust is our currency. Through transparent communication, compliant institutional documentation, and dependable service, we forge partnerships that endure.
              </p>
              <div class="pillar-card-accent"></div>
            </div>
          </div>

        </div>

        <!-- Executive Promise Banner (Full Width High-Impact Showcase) -->
        <div class="commitment-promise-banner fade-up-element">
          <div class="promise-banner-inner text-center">
            
            <div class="promise-badge-pill mb-3">
              <i class="bi bi-award-fill me-1"></i>
              <span>OUR PROMISE</span>
            </div>

            <!-- The Central Slogan Triad -->
            <h3 class="promise-motto mb-3">
              <span class="motto-item">Your Requirements.</span>
              <span class="motto-sep" aria-hidden="true">•</span>
              <span class="motto-item">Our Commitment.</span>
              <span class="motto-sep" aria-hidden="true">•</span>
              <span class="motto-item motto-highlight">Reliable Supply Solutions.</span>
            </h3>

            <!-- Comprehensive Scope Narrative -->
            <p class="promise-scope-desc mx-auto mb-4">
              Whether you require specialized medical devices, IT infrastructure for educational projects, industrial raw materials, automotive components or solar energy products, we are committed to supporting your procurement requirements with professionalism and dedication.
            </p>

            <a href="#contact" class="btn-promise-cta">
              <span>Partner With GSR Global Enterprises</span>
              <i class="bi bi-arrow-right ms-2"></i>
            </a>

          </div>
        </div>

      </div>
    </section>"""

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the commitment section
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
   F. Our Commitment Section (Symmetrical Executive Corporate Design)
   ========================================================================== */
.commitment-section {
  padding: 5rem 0 5.25rem;
  background-color: #f8fafc;
  border-top: 1px solid rgba(6, 43, 85, 0.08);
  border-bottom: 1px solid rgba(6, 43, 85, 0.08);
  position: relative;
}

/* Eyebrow */
.commitment-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 10px;
}

.commitment-eyebrow-dash {
  width: 24px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.commitment-eyebrow-text {
  font-family: var(--font-heading);
  font-size: 0.80rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--primary-navy);
}

.commitment-section-title {
  font-family: var(--font-heading);
  font-size: clamp(1.75rem, 2.35vw, 2.25rem);
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.25;
  letter-spacing: -0.02em;
}

.commitment-lead-intro {
  font-family: var(--font-body);
  font-size: clamp(0.95rem, 1.05vw, 1.05rem);
  color: #334155;
  line-height: 1.65;
  max-width: 820px;
}

.commitment-lead-intro strong {
  color: var(--primary-navy);
  font-weight: 700;
}

/* 3 Core Pillars (Symmetrical 3-Column Grid) */
.commitment-pillar-card {
  background: #ffffff;
  border: 1px solid rgba(6, 43, 85, 0.09);
  border-radius: 14px;
  padding: 2rem 1.75rem 1.75rem;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(6, 43, 85, 0.04);
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.commitment-pillar-card:hover {
  transform: translateY(-6px);
  border-color: rgba(255, 121, 0, 0.40);
  box-shadow: 0 12px 30px rgba(6, 43, 85, 0.10);
}

.pillar-card-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.25rem;
}

.pillar-icon-wrapper {
  width: 50px;
  height: 50px;
  border-radius: 12px;
  background: rgba(6, 43, 85, 0.06);
  color: var(--primary-navy);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.35rem;
  transition: all 0.28s ease;
}

.commitment-pillar-card:hover .pillar-icon-wrapper {
  background-color: var(--accent-orange);
  color: #ffffff;
  transform: scale(1.06);
}

.pillar-index {
  font-family: var(--font-heading);
  font-size: 1.35rem;
  font-weight: 800;
  color: rgba(6, 43, 85, 0.14);
  letter-spacing: -0.02em;
}

.pillar-card-title {
  font-family: var(--font-heading);
  font-size: 1.12rem;
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.32;
  margin-bottom: 0.75rem;
}

.pillar-card-text {
  font-family: var(--font-body);
  font-size: 0.88rem;
  color: #475569;
  line-height: 1.58;
  margin-bottom: 0;
}

.pillar-card-accent {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: transparent;
  transition: background 0.3s ease;
}

.commitment-pillar-card:hover .pillar-card-accent {
  background: linear-gradient(90deg, var(--primary-navy), var(--accent-orange));
}

/* Executive Promise Banner */
.commitment-promise-banner {
  background: linear-gradient(135deg, #062B55 0%, #082142 60%, #031428 100%);
  border-radius: 18px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: 3rem 2.25rem;
  position: relative;
  overflow: hidden;
  box-shadow: 0 16px 44px rgba(6, 43, 85, 0.20);
}

.commitment-promise-banner::before {
  content: '';
  position: absolute;
  top: -40%;
  right: -20%;
  width: 450px;
  height: 450px;
  background: radial-gradient(circle, rgba(255, 121, 0, 0.18) 0%, transparent 70%);
  pointer-events: none;
}

.promise-badge-pill {
  display: inline-flex;
  align-items: center;
  background: rgba(255, 121, 0, 0.16);
  color: var(--accent-orange);
  border: 1px solid rgba(255, 121, 0, 0.35);
  font-family: var(--font-heading);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 0.35rem 1rem;
  border-radius: 50px;
}

.promise-motto {
  font-family: var(--font-heading);
  font-size: clamp(1.25rem, 2.2vw, 1.85rem);
  font-weight: 700;
  color: #ffffff;
  line-height: 1.35;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 0.5rem 0.85rem;
}

.motto-item {
  display: inline-block;
}

.motto-sep {
  color: var(--accent-orange);
  font-size: 1.2rem;
}

.motto-highlight {
  color: #ff9a3c;
  text-shadow: 0 0 20px rgba(255, 154, 60, 0.35);
}

.promise-scope-desc {
  font-family: var(--font-body);
  font-size: 0.94rem;
  color: #cbd5e1;
  line-height: 1.65;
  max-width: 780px;
}

.btn-promise-cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: var(--accent-orange);
  color: #ffffff;
  border-radius: 50px;
  padding: 0.75rem 2rem;
  font-family: var(--font-heading);
  font-size: 0.86rem;
  font-weight: 700;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  text-decoration: none;
  box-shadow: 0 4px 18px rgba(255, 121, 0, 0.35);
  transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
}

.btn-promise-cta:hover {
  background: var(--brand-orange-hover);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(255, 121, 0, 0.45);
}

.btn-promise-cta i {
  transition: transform 0.2s ease;
}

.btn-promise-cta:hover i {
  transform: translateX(4px);
}

/* Responsive adjustments */
@media (max-width: 991.98px) {
  .commitment-section {
    padding: 3.75rem 0 4rem;
  }
  .commitment-promise-banner {
    padding: 2.25rem 1.5rem;
  }
}

@media (max-width: 575.98px) {
  .promise-motto {
    font-size: 1.15rem;
    flex-direction: column;
    gap: 0.25rem;
  }
  .motto-sep {
    display: none;
  }
}"""

with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace commitment CSS starting from `/* ====... F. Our Commitment Section` to the end of file
css_pattern = r'/\* =+[\r\n\s]+F\. Our Commitment Section.*$'
css_match = re.search(css_pattern, css, flags=re.DOTALL)
if css_match:
    css_new = css[:css_match.start()] + new_commitment_css + "\n"
    with open("css/style.css", "w", encoding="utf-8") as f:
        f.write(css_new)
    print("css/style.css updated successfully.")
else:
    print("WARNING: Could not match commitment section in css/style.css!")
