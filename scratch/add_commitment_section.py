# scratch/add_commitment_section.py

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

clients_end_marker = '      </div>\n    </section>\n\n\n  </main>'

if clients_end_marker not in html:
    # Try finding </section> before </main>
    import re
    m = re.search(r'(</section>\s*</main>)', html)
    if m:
        clients_end_marker = m.group(1)
        print("Found via regex:", clients_end_marker)
    else:
        print("Error: Could not find end of clients section before </main>")
        exit(1)

commitment_html = '''      </div>
    </section>

    <!-- ==========================================================================
         F. OUR COMMITMENT (UNIQUE & PROFESSIONAL EXECUTIVE PLEDGE)
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
          <h2 class="commitment-section-title mb-2">
            Building Enduring Partnerships on Trust, Quality &amp; Execution
          </h2>
          <p class="commitment-section-subtitle mx-auto">
            Procurement is more than supplying products — it is an active pledge to your organization's ongoing operational success.
          </p>
        </div>

        <div class="row g-4 g-xl-5 align-items-center">

          <!-- Left Column: Core Narrative & Value Pillars -->
          <div class="col-lg-7 fade-up-element">
            <div class="commitment-narrative-box">

              <!-- Primary Statement (User Provided Content) -->
              <p class="commitment-lead-p mb-3">
                At <strong>GSR Global Enterprises</strong>, we believe successful procurement goes beyond sourcing products. It is about understanding business needs, coordinating the right resources and building relationships based on trust.
              </p>

              <p class="commitment-body-p mb-4">
                Whether you require specialized medical devices, IT infrastructure for educational projects, industrial raw materials, automotive components or solar energy products, we are committed to supporting your procurement requirements with professionalism and dedication.
              </p>

              <!-- 3 Value Pillars -->
              <div class="commitment-pillars-grid">

                <!-- Pillar 1 -->
                <div class="commitment-pillar-card">
                  <div class="pillar-icon-box" aria-hidden="true">
                    <i class="bi bi-bullseye"></i>
                  </div>
                  <div class="pillar-content">
                    <h3 class="pillar-title">Understanding Business Needs</h3>
                    <p class="pillar-desc">
                      Deep-dive requirement mapping tailored to your technical specifications and timelines.
                    </p>
                  </div>
                </div>

                <!-- Pillar 2 -->
                <div class="commitment-pillar-card">
                  <div class="pillar-icon-box" aria-hidden="true">
                    <i class="bi bi-diagram-3"></i>
                  </div>
                  <div class="pillar-content">
                    <h3 class="pillar-title">Coordinating Right Resources</h3>
                    <p class="pillar-desc">
                      Direct supply-chain orchestration with verified OEM manufacturers and tier-one vendors.
                    </p>
                  </div>
                </div>

                <!-- Pillar 3 -->
                <div class="commitment-pillar-card">
                  <div class="pillar-icon-box" aria-hidden="true">
                    <i class="bi bi-shield-check"></i>
                  </div>
                  <div class="pillar-content">
                    <h3 class="pillar-title">Relationships Built on Trust</h3>
                    <p class="pillar-desc">
                      Transparent milestone communication, compliant documentation, and long-term business ethics.
                    </p>
                  </div>
                </div>

              </div>

            </div>
          </div>

          <!-- Right Column: The Executive Promise Plaque (Unique Standout Showcase) -->
          <div class="col-lg-5 fade-up-element">
            <div class="commitment-promise-plaque">

              <!-- Gold Top Accent Badge -->
              <div class="promise-plaque-eyebrow">
                <i class="bi bi-award-fill me-1"></i>
                <span>THE GSR ASSURANCE</span>
              </div>

              <h3 class="promise-plaque-title">Our Promise</h3>

              <!-- Slogan Chain Flow -->
              <div class="promise-chain">

                <!-- Step 1 -->
                <div class="promise-chain-item">
                  <div class="promise-chain-badge">01</div>
                  <div class="promise-chain-text">
                    <strong class="promise-chain-heading">Your Requirements.</strong>
                    <span class="promise-chain-sub">Identified with operational clarity</span>
                  </div>
                </div>

                <div class="promise-chain-arrow" aria-hidden="true">
                  <i class="bi bi-arrow-down"></i>
                </div>

                <!-- Step 2 -->
                <div class="promise-chain-item">
                  <div class="promise-chain-badge">02</div>
                  <div class="promise-chain-text">
                    <strong class="promise-chain-heading">Our Commitment.</strong>
                    <span class="promise-chain-sub">Dedicated, transparent coordination</span>
                  </div>
                </div>

                <div class="promise-chain-arrow" aria-hidden="true">
                  <i class="bi bi-arrow-down"></i>
                </div>

                <!-- Step 3 (Highlight) -->
                <div class="promise-chain-item promise-chain-featured">
                  <div class="promise-chain-badge"><i class="bi bi-check2"></i></div>
                  <div class="promise-chain-text">
                    <strong class="promise-chain-heading">Reliable Supply Solutions.</strong>
                    <span class="promise-chain-sub">Dependable, certified execution</span>
                  </div>
                </div>

              </div>

              <!-- Action Link -->
              <div class="promise-plaque-action mt-4 pt-2">
                <a href="#contact" class="btn-promise-action" aria-label="Discuss Your Procurement Requirements">
                  <span>Discuss Your Requirements</span>
                  <i class="bi bi-arrow-right ms-2"></i>
                </a>
              </div>

            </div>
          </div>

        </div>

      </div>
    </section>


  </main>'''

new_html = html.replace(clients_end_marker, commitment_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated index.html with Our Commitment section successfully!")

# Append CSS to css/style.css
commitment_css = '''
/* ==========================================================================
   F. Our Commitment Section (Unique & Professional Corporate Pledge)
   ========================================================================== */
.commitment-section {
  padding: 4.5rem 0 5rem;
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
  font-size: clamp(1.75rem, 2.35vw, 2.2rem);
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.25;
  letter-spacing: -0.02em;
}

.commitment-section-subtitle {
  font-family: var(--font-body);
  font-size: clamp(0.88rem, 0.98vw, 0.94rem);
  color: var(--text-grey);
  line-height: 1.55;
  max-width: 680px;
}

/* Narrative Left Box */
.commitment-narrative-box {
  padding-right: 0.5rem;
}

.commitment-lead-p {
  font-family: var(--font-body);
  font-size: 1.02rem;
  color: #1e293b;
  line-height: 1.65;
  font-weight: 400;
}

.commitment-lead-p strong {
  color: var(--primary-navy);
  font-weight: 700;
}

.commitment-body-p {
  font-family: var(--font-body);
  font-size: 0.90rem;
  color: #475569;
  line-height: 1.62;
}

/* 3 Value Pillars Grid */
.commitment-pillars-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.commitment-pillar-card {
  background: #ffffff;
  border: 1px solid rgba(6, 43, 85, 0.08);
  border-radius: 12px;
  padding: 1rem 1.25rem;
  display: flex;
  align-items: flex-start;
  gap: 14px;
  box-shadow: 0 4px 14px rgba(6, 43, 85, 0.04);
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.commitment-pillar-card:hover {
  transform: translateX(6px);
  border-color: rgba(255, 121, 0, 0.4);
  box-shadow: 0 8px 22px rgba(6, 43, 85, 0.09);
}

.pillar-icon-box {
  width: 42px;
  height: 42px;
  border-radius: 10px;
  background-color: rgba(6, 43, 85, 0.06);
  color: var(--primary-navy);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  flex-shrink: 0;
  transition: all 0.25s ease;
}

.commitment-pillar-card:hover .pillar-icon-box {
  background-color: var(--accent-orange);
  color: #ffffff;
  transform: scale(1.06);
}

.pillar-content {
  flex-grow: 1;
}

.pillar-title {
  font-family: var(--font-heading);
  font-size: 0.94rem;
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.3;
  margin-bottom: 0.25rem;
}

.pillar-desc {
  font-family: var(--font-body);
  font-size: 0.81rem;
  color: var(--text-grey);
  line-height: 1.48;
  margin-bottom: 0;
}

/* Right Column: Executive Promise Plaque */
.commitment-promise-plaque {
  background: linear-gradient(145deg, #062449 0%, #061c38 100%);
  border: 2px solid #c5a059;
  border-radius: 16px;
  padding: 2.4rem 2rem;
  color: #ffffff;
  box-shadow: 0 16px 44px rgba(6, 43, 85, 0.22);
  position: relative;
  overflow: hidden;
}

.commitment-promise-plaque::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -50%;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle, rgba(197, 160, 89, 0.12) 0%, transparent 70%);
  pointer-events: none;
}

.promise-plaque-eyebrow {
  display: inline-flex;
  align-items: center;
  background: rgba(197, 160, 89, 0.18);
  color: #d4af37;
  border: 1px solid rgba(197, 160, 89, 0.35);
  font-family: var(--font-heading);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 0.35rem 0.9rem;
  border-radius: 50px;
  margin-bottom: 1.15rem;
}

.promise-plaque-title {
  font-family: var(--font-heading);
  font-size: 1.75rem;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: -0.01em;
  margin-bottom: 1.5rem;
}

/* Slogan Chain Flow */
.promise-chain {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.promise-chain-item {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  padding: 0.9rem 1.15rem;
  display: flex;
  align-items: center;
  gap: 14px;
  transition: all 0.25s ease;
}

.promise-chain-item:hover {
  background: rgba(255, 255, 255, 0.10);
  border-color: rgba(197, 160, 89, 0.45);
}

.promise-chain-featured {
  background: rgba(197, 160, 89, 0.14);
  border-color: #c5a059;
}

.promise-chain-badge {
  width: 34px;
  height: 34px;
  border-radius: 8px;
  background-color: rgba(255, 255, 255, 0.15);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-heading);
  font-size: 0.85rem;
  font-weight: 700;
  flex-shrink: 0;
}

.promise-chain-featured .promise-chain-badge {
  background-color: #c5a059;
  color: #061c38;
}

.promise-chain-text {
  display: flex;
  flex-direction: column;
}

.promise-chain-heading {
  font-family: var(--font-heading);
  font-size: 0.92rem;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.25;
}

.promise-chain-featured .promise-chain-heading {
  color: #f7e6b5;
}

.promise-chain-sub {
  font-family: var(--font-body);
  font-size: 0.77rem;
  color: #cbd5e1;
  line-height: 1.35;
}

.promise-chain-arrow {
  text-align: center;
  color: #c5a059;
  font-size: 0.85rem;
  line-height: 1;
}

/* Plaque Action Button */
.btn-promise-action {
  background-color: var(--accent-orange);
  color: #ffffff;
  padding: 0.72rem 1.75rem;
  border-radius: 50px;
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  box-shadow: 0 4px 16px rgba(255, 121, 0, 0.35);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  width: 100%;
}

.btn-promise-action:hover {
  background-color: var(--brand-orange-hover);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(255, 121, 0, 0.45);
}

.btn-promise-action i {
  transition: transform 0.2s ease;
}

.btn-promise-action:hover i {
  transform: translateX(4px);
}

/* Responsive adjustments */
@media (max-width: 991.98px) {
  .commitment-section {
    padding: 3.5rem 0 4rem;
  }

  .commitment-narrative-box {
    padding-right: 0;
    margin-bottom: 1.5rem;
  }
}

@media (max-width: 575.98px) {
  .commitment-promise-plaque {
    padding: 1.75rem 1.25rem;
  }

  .promise-plaque-title {
    font-size: 1.5rem;
  }
}
'''

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(commitment_css)

print("Appended Our Commitment styles to css/style.css successfully!")
