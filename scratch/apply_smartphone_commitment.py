import re

# 1. New HTML for #commitment section matching smartphone reference image exactly
new_commitment_html = """    <!-- ==========================================================================
         F. OUR COMMITMENT (EXACT REFERENCE DESIGN - 3D PHONE MOCKUP & JOURNEY)
         ========================================================================== -->
    <section class="commitment-mockup-section" id="commitment" aria-label="Our Commitment to Reliable Sourcing">
      <!-- Decorative Orbital Rings Background -->
      <div class="mockup-orbital-glow" aria-hidden="true"></div>
      <div class="mockup-orbital-ring-1" aria-hidden="true"></div>
      <div class="mockup-orbital-ring-2" aria-hidden="true"></div>

      <div class="container position-relative z-1">
        <div class="row align-items-center g-5">

          <!-- Left Column: Executive Narrative & Dual Action Buttons -->
          <div class="col-lg-6 col-xl-7 fade-up-element">
            <div class="commitment-mockup-content">

              <!-- Eyebrow: Orange Dash + Bold White Text -->
              <div class="commitment-mockup-eyebrow mb-3">
                <span class="mockup-eyebrow-dash" aria-hidden="true"></span>
                <span class="mockup-eyebrow-text">OUR COMMITMENT</span>
              </div>

              <!-- Main Heading with Highlighted "Count On" -->
              <h2 class="commitment-mockup-title mb-4">
                A Commitment<br>You Can <span class="text-orange">Count On</span>
              </h2>

              <!-- Narrative Body Paragraphs (User Provided Content) -->
              <p class="commitment-mockup-lead mb-3">
                At <strong>GSR Global Enterprises</strong>, we believe successful procurement goes beyond sourcing products. It is about understanding business needs, coordinating the right resources and building relationships based on trust.
              </p>

              <p class="commitment-mockup-body mb-4">
                Whether you require specialized medical devices, IT infrastructure for educational projects, industrial raw materials, automotive components or solar energy products, we are committed to supporting your procurement requirements with professionalism and dedication.
              </p>

              <!-- Dual CTA Action Buttons (Matching Image Exactly) -->
              <div class="commitment-mockup-btn-row">
                <a href="#contact" class="btn-mockup-primary" aria-label="Request a Quote">
                  <span>Request a Quote</span>
                </a>
                <a href="#services" class="btn-mockup-secondary" aria-label="Explore Our Services">
                  <span class="btn-mockup-arrow"><i class="bi bi-arrow-right"></i></span>
                  <span>Explore Our Services</span>
                </a>
              </div>

            </div>
          </div>

          <!-- Right Column: 3D Smartphone Mockup with Floating Badges -->
          <div class="col-lg-6 col-xl-5 fade-up-element">
            <div class="mockup-device-wrapper">

              <!-- Floating Pill 1: Quality First (Top Left) -->
              <div class="floating-mockup-pill pill-top-left">
                <span class="pill-status-dot orange"></span>
                <span class="pill-label-text">Quality First</span>
              </div>

              <!-- Floating Pill 2: Lasting Partnership (Bottom Right) -->
              <div class="floating-mockup-pill pill-bottom-right">
                <span class="pill-status-dot orange"></span>
                <span class="pill-label-text">Lasting Partnership</span>
              </div>

              <!-- Smartphone Chassis -->
              <div class="mockup-smartphone">
                
                <!-- Dynamic Island / Top Camera -->
                <div class="smartphone-island"></div>

                <!-- Phone Screen Content -->
                <div class="smartphone-screen">

                  <!-- Header inside Phone -->
                  <div class="screen-header text-center mb-3">
                    <h3 class="screen-app-title mb-1">GSR Promise</h3>
                    <span class="screen-app-subtitle">Your enquiry journey</span>
                  </div>

                  <!-- 4 Journey Step Cards -->
                  <div class="screen-cards-stack">

                    <!-- Step 1 Card -->
                    <div class="journey-item-card">
                      <div class="journey-card-icon navy">
                        <i class="bi bi-check2"></i>
                      </div>
                      <div class="journey-card-info">
                        <strong class="journey-info-title">Requirement understood</strong>
                        <span class="journey-info-desc">Specifications confirmed</span>
                      </div>
                    </div>

                    <!-- Step 2 Card -->
                    <div class="journey-item-card">
                      <div class="journey-card-icon navy">
                        <i class="bi bi-check2"></i>
                      </div>
                      <div class="journey-card-info">
                        <strong class="journey-info-title">Sourced with care</strong>
                        <span class="journey-info-desc">Matched to your industry</span>
                      </div>
                    </div>

                    <!-- Step 3 Card -->
                    <div class="journey-item-card">
                      <div class="journey-card-icon navy">
                        <i class="bi bi-check2"></i>
                      </div>
                      <div class="journey-card-info">
                        <strong class="journey-info-title">Updates shared</strong>
                        <span class="journey-info-desc">Clear communication</span>
                      </div>
                    </div>

                    <!-- Step 4 Card (Featured Orange Delivery Highlight) -->
                    <div class="journey-item-card card-featured-orange">
                      <div class="journey-card-icon white">
                        <i class="bi bi-truck"></i>
                      </div>
                      <div class="journey-card-info">
                        <strong class="journey-info-title">On the way to you</strong>
                        <span class="journey-info-desc">Delivery planned</span>
                      </div>
                    </div>

                  </div>

                  <!-- Bottom Enquiry Action Button inside Phone -->
                  <div class="screen-bottom-action mt-3">
                    <a href="#contact" class="btn-screen-action">
                      <span>Start Your Enquiry</span>
                    </a>
                  </div>

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
    html = html[:match.start()] + new_commitment_html + html[match.end():]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html updated with smartphone mockup commitment section.")
else:
    print("WARNING: Could not find commitment section pattern in index.html!")

# 2. Update css/style.css
new_commitment_css = """/* ==========================================================================
   F. Our Commitment Section (Exact Reference Design - 3D Smartphone Mockup)
   ========================================================================== */
.commitment-mockup-section {
  padding: 6rem 0 6.5rem;
  background: radial-gradient(circle at 78% 45%, #13589d 0%, #0a3a6e 40%, #062852 75%, #041d3b 100%);
  position: relative;
  overflow: hidden;
  color: #ffffff;
}

/* Ambient Radial Glow & Orbital Rings */
.mockup-orbital-glow {
  position: absolute;
  top: 50%;
  right: 15%;
  transform: translate(50%, -50%);
  width: 650px;
  height: 650px;
  background: radial-gradient(circle, rgba(19, 88, 157, 0.45) 0%, rgba(6, 40, 82, 0) 70%);
  pointer-events: none;
}

.mockup-orbital-ring-1 {
  position: absolute;
  top: 50%;
  right: 20%;
  transform: translate(50%, -50%);
  width: 580px;
  height: 580px;
  border-radius: 50%;
  border: 1.5px dashed rgba(255, 255, 255, 0.12);
  pointer-events: none;
}

.mockup-orbital-ring-2 {
  position: absolute;
  top: 50%;
  right: 20%;
  transform: translate(50%, -50%);
  width: 760px;
  height: 760px;
  border-radius: 50%;
  border: 1px dotted rgba(255, 255, 255, 0.08);
  pointer-events: none;
}

/* Eyebrow */
.commitment-mockup-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 12px;
}

.mockup-eyebrow-dash {
  width: 32px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.mockup-eyebrow-text {
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #e2e8f0;
}

/* Main Heading */
.commitment-mockup-title {
  font-family: var(--font-heading);
  font-size: clamp(2.2rem, 3.2vw, 3.2rem);
  font-weight: 700;
  color: #ffffff;
  line-height: 1.16;
  letter-spacing: -0.02em;
}

.commitment-mockup-title .text-orange {
  color: var(--accent-orange) !important;
}

/* Narrative Body */
.commitment-mockup-lead {
  font-family: var(--font-body);
  font-size: 1.02rem;
  color: #e2e8f0;
  line-height: 1.65;
  font-weight: 400;
}

.commitment-mockup-lead strong {
  color: #ffffff;
  font-weight: 700;
}

.commitment-mockup-body {
  font-family: var(--font-body);
  font-size: 0.90rem;
  color: #cbd5e1;
  line-height: 1.62;
}

/* Dual Buttons Row */
.commitment-mockup-btn-row {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.btn-mockup-primary {
  background-color: var(--accent-orange);
  color: #ffffff;
  border-radius: 10px;
  padding: 0.82rem 1.85rem;
  font-family: var(--font-heading);
  font-size: 0.88rem;
  font-weight: 600;
  text-decoration: none;
  box-shadow: 0 6px 20px rgba(255, 121, 0, 0.40);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  display: inline-flex;
  align-items: center;
}

.btn-mockup-primary:hover {
  background-color: var(--brand-orange-hover);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 10px 28px rgba(255, 121, 0, 0.50);
}

.btn-mockup-secondary {
  background-color: rgba(4, 25, 53, 0.75);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 10px;
  padding: 0.65rem 1.5rem 0.65rem 0.75rem;
  font-family: var(--font-heading);
  font-size: 0.88rem;
  font-weight: 600;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 12px;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
}

.btn-mockup-secondary:hover {
  background-color: rgba(6, 40, 82, 0.95);
  border-color: rgba(255, 255, 255, 0.30);
  color: #ffffff;
  transform: translateY(-2px);
}

.btn-mockup-arrow {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background-color: #ffffff;
  color: var(--primary-navy);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.90rem;
  transition: transform 0.2s ease;
}

.btn-mockup-secondary:hover .btn-mockup-arrow {
  transform: translateX(3px);
  background-color: var(--accent-orange);
  color: #ffffff;
}

/* Right Column: 3D Smartphone Wrapper */
.mockup-device-wrapper {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1.5rem 0;
}

/* Floating Badges */
.floating-mockup-pill {
  position: absolute;
  z-index: 5;
  background: #ffffff;
  color: var(--primary-navy);
  border-radius: 50px;
  padding: 0.55rem 1.15rem;
  font-family: var(--font-heading);
  font-size: 0.80rem;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.22);
  white-space: nowrap;
  animation: floatPill 4s ease-in-out infinite alternate;
}

.pill-status-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  display: inline-block;
}

.pill-status-dot.orange {
  background-color: var(--accent-orange);
  box-shadow: 0 0 8px rgba(255, 121, 0, 0.7);
}

.floating-mockup-pill.pill-top-left {
  top: 12%;
  left: 0;
  transform: translateY(0);
}

.floating-mockup-pill.pill-bottom-right {
  bottom: 8%;
  right: -10px;
  animation-delay: -2s;
}

@keyframes floatPill {
  0% { transform: translateY(0); }
  100% { transform: translateY(-8px); }
}

/* The Smartphone Chassis */
.mockup-smartphone {
  width: 325px;
  max-width: 100%;
  background: #f4f7fc;
  border: 10px solid #0f172a;
  border-radius: 46px;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.45), 0 0 0 2px rgba(255, 255, 255, 0.15);
  position: relative;
  overflow: hidden;
  padding: 1.1rem 1.15rem 1.4rem;
  transform: rotate(-1deg);
  transition: transform 0.4s ease;
}

.mockup-smartphone:hover {
  transform: rotate(0deg) scale(1.02);
}

/* Dynamic Island */
.smartphone-island {
  width: 85px;
  height: 22px;
  background-color: #000000;
  border-radius: 20px;
  margin: 0 auto 1rem;
}

/* Screen Header */
.screen-app-title {
  font-family: var(--font-heading);
  font-size: 1.12rem;
  font-weight: 700;
  color: var(--primary-navy);
  margin-bottom: 0.15rem;
}

.screen-app-subtitle {
  font-family: var(--font-body);
  font-size: 0.75rem;
  color: #64748b;
}

/* 4 Journey Cards */
.screen-cards-stack {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}

.journey-item-card {
  background: #ffffff;
  border-radius: 14px;
  padding: 0.75rem 0.95rem;
  display: flex;
  align-items: center;
  gap: 12px;
  box-shadow: 0 4px 14px rgba(6, 43, 85, 0.05);
  border: 1px solid rgba(6, 43, 85, 0.04);
}

.journey-card-icon {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.95rem;
  flex-shrink: 0;
}

.journey-card-icon.navy {
  background-color: var(--primary-navy);
  color: #ffffff;
}

.journey-card-icon.white {
  background-color: #ffffff;
  color: var(--accent-orange);
}

.journey-card-info {
  display: flex;
  flex-direction: column;
}

.journey-info-title {
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.25;
}

.journey-info-desc {
  font-family: var(--font-body);
  font-size: 0.72rem;
  color: #64748b;
  line-height: 1.3;
}

/* Featured Orange Card */
.journey-item-card.card-featured-orange {
  background-color: var(--accent-orange);
  border-color: var(--accent-orange);
  box-shadow: 0 6px 18px rgba(255, 121, 0, 0.35);
}

.journey-item-card.card-featured-orange .journey-info-title {
  color: #ffffff;
}

.journey-item-card.card-featured-orange .journey-info-desc {
  color: #ffeedb;
}

/* Bottom App Button inside Phone */
.btn-screen-action {
  display: block;
  width: 100%;
  background-color: #062449;
  color: #ffffff;
  border-radius: 10px;
  padding: 0.72rem 1rem;
  text-align: center;
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(6, 36, 73, 0.35);
}

.btn-screen-action:hover {
  background-color: #041935;
  color: #ffffff;
}

/* Responsive adjustments */
@media (max-width: 991.98px) {
  .commitment-mockup-section {
    padding: 4.5rem 0 5rem;
  }
  .mockup-device-wrapper {
    margin-top: 1.5rem;
  }
  .floating-mockup-pill.pill-top-left {
    left: 10px;
  }
  .floating-mockup-pill.pill-bottom-right {
    right: 10px;
  }
}

@media (max-width: 575.98px) {
  .mockup-smartphone {
    width: 295px;
    padding: 1rem 0.9rem 1.25rem;
  }
  .floating-mockup-pill {
    padding: 0.45rem 0.9rem;
    font-size: 0.74rem;
  }
  .commitment-mockup-btn-row {
    flex-direction: column;
    align-items: stretch;
  }
  .btn-mockup-primary,
  .btn-mockup-secondary {
    justify-content: center;
  }
}
"""

with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace the previous commitment-ref CSS
old_commit_pattern = r'/\* =+[\r\n\s]+F\. Our Commitment Section.*?(?=/\* =+[\r\n\s]+G\. Contact)'
match_css = re.search(old_commit_pattern, css, flags=re.DOTALL)
if match_css:
    css = css[:match_css.start()] + new_commitment_css + "\n\n" + css[match_css.end():]
    with open("css/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("css/style.css updated with smartphone mockup commitment rules.")
else:
    print("WARNING: Could not find commitment CSS pattern in css/style.css!")
