# scratch/build_corporate_about.py

# 1. New HTML for About Section
new_about_html = '''<!-- ==========================================================================
         B. ABOUT US SECTION (MODERN CLEAN CORPORATE STYLE)
         ========================================================================== -->
    <section class="about-section" id="about">
      <div class="container">

        <div class="row align-items-center g-4 g-lg-5">

          <!-- Left Column: Corporate Imagery Showcase with Floating Trust Card -->
          <div class="col-lg-6 fade-up-element">
            <div class="about-corp-media-wrap">
              <!-- Main Corporate Photograph -->
              <div class="about-corp-main-img">
                <img src="assets/images/hero-corporate-meeting.webp"
                  alt="GSR Global Enterprises Senior Management and Procurement Operations" loading="lazy">
              </div>

              <!-- Floating Trust Badge: Experience & Credentials -->
              <div class="about-corp-badge">
                <div class="about-corp-badge-icon">
                  <i class="bi bi-shield-check"></i>
                </div>
                <div class="about-corp-badge-text">
                  <div class="about-corp-badge-num">10+ Years</div>
                  <div class="about-corp-badge-label">Procurement &amp; Supply Excellence</div>
                </div>
              </div>

              <!-- Floating Credential Card (Top Right) -->
              <div class="about-corp-cert-pill d-none d-sm-flex">
                <i class="bi bi-patch-check-fill"></i>
                <span>100% Tax &amp; GST Invoicing</span>
              </div>
            </div>
          </div>

          <!-- Right Column: Corporate Narrative, Interactive Tabs & Capabilities -->
          <div class="col-lg-6 fade-up-element">
            <div class="about-corp-content">

              <!-- Eyebrow -->
              <div class="about-corp-eyebrow mb-2">
                <span class="about-corp-eyebrow-dash"></span>
                <span class="about-corp-eyebrow-text">ABOUT GSR GLOBAL ENTERPRISES</span>
              </div>

              <!-- Main Title -->
              <h2 class="about-corp-title mb-3">
                Your Strategic Procurement Partner Delivering Verified Institutional Excellence
              </h2>

              <!-- Lead Description -->
              <p class="about-corp-lead mb-3">
                Headquartered in Andhra Pradesh, <strong>GSR GLOBAL ENTERPRISES</strong> is an established multi-sector procurement, industrial supply, and infrastructure solutions enterprise. We bridge institutional demand with dependable manufacturing channels across critical healthcare, education, transport, and industrial sectors.
              </p>

              <!-- Corporate Nav Tabs: Our History / Our Mission / Our Vision -->
              <div class="about-corp-tabs-wrap mb-3">
                <ul class="nav nav-pills" id="aboutTab" role="tablist">
                  <li class="nav-item" role="presentation">
                    <button class="nav-link active" id="pill-history-tab" data-bs-toggle="pill"
                      data-bs-target="#pill-history" type="button" role="tab" aria-controls="pill-history"
                      aria-selected="true">Our Profile</button>
                  </li>
                  <li class="nav-item" role="presentation">
                    <button class="nav-link" id="pill-mission-tab" data-bs-toggle="pill"
                      data-bs-target="#pill-mission" type="button" role="tab" aria-controls="pill-mission"
                      aria-selected="false">Our Mission</button>
                  </li>
                  <li class="nav-item" role="presentation">
                    <button class="nav-link" id="pill-vision-tab" data-bs-toggle="pill"
                      data-bs-target="#pill-vision" type="button" role="tab" aria-controls="pill-vision"
                      aria-selected="false">Our Vision</button>
                  </li>
                </ul>
              </div>

              <!-- Tab Contents -->
              <div class="tab-content about-corp-tab-content mb-4" id="aboutTabContent">

                <!-- Tab 1: Our Profile (Active) -->
                <div class="tab-pane fade show active" id="pill-history" role="tabpanel"
                  aria-labelledby="pill-history-tab">
                  <p class="about-corp-tab-desc">
                    Operating through direct mill-origin tie-ups and tier-1 OEM relationships, we manage complex bulk sourcing programs with end-to-end statutory compliance, strict pre-dispatch quality verification, and disciplined handover.
                  </p>
                  <div class="row g-2 about-corp-check-grid">
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Direct OEM &amp; Primary Stockists</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Strict Pre-Dispatch Inspections</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>100% Tax &amp; GST Invoicing</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Dual Regional Distribution Hubs</span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Tab 2: Our Mission -->
                <div class="tab-pane fade" id="pill-mission" role="tabpanel" aria-labelledby="pill-mission-tab">
                  <p class="about-corp-tab-desc">
                    Our mission is to empower government institutions, transit workshops, educational development programs, and industrial businesses with seamless, transparent, and on-time procurement solutions that eliminate supply bottlenecks.
                  </p>
                  <div class="row g-2 about-corp-check-grid">
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Eliminating Sourcing Bottlenecks</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Standardized Technical Compliance</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Transparent Commercial Invoicing</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Disciplined On-Site Handover</span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Tab 3: Our Vision -->
                <div class="tab-pane fade" id="pill-vision" role="tabpanel" aria-labelledby="pill-vision-tab">
                  <p class="about-corp-tab-desc">
                    Our vision is to be recognized as Andhra Pradesh's most dependable and comprehensive institutional supply partner, respected for uncompromising integrity, multi-sector agility, and long-term public and commercial trust.
                  </p>
                  <div class="row g-2 about-corp-check-grid">
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Multi-Industry Sourcing Reach</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Zero-Defect Delivery Discipline</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Sustainable Supply Pipelines</span>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="about-corp-check-item">
                        <i class="bi bi-check-circle-fill"></i>
                        <span>Enduring Institutional Trust</span>
                      </div>
                    </div>
                  </div>
                </div>

              </div>

              <!-- Corporate CTA Actions -->
              <div class="about-corp-actions d-flex align-items-center gap-3 flex-wrap">
                <a href="#services" class="btn-corp-primary">
                  <span>Explore Our Capabilities</span>
                  <i class="bi bi-arrow-right ms-1"></i>
                </a>
                <a href="#contact" class="btn-corp-outline">
                  <i class="bi bi-telephone-fill me-1"></i>
                  <span>Request Procurement Consultation</span>
                </a>
              </div>

            </div>
          </div>

        </div>

        <!-- Corporate Statistics Banner (Spanning Width with Crisp Dividers) -->
        <div class="about-corp-stats-bar mt-5 fade-up-element">
          <div class="row g-0 text-center align-items-center">

            <div class="col-6 col-lg-3 about-stat-border">
              <div class="about-stat-item">
                <div class="about-stat-number">100+</div>
                <div class="about-stat-text">Verified Consignments</div>
              </div>
            </div>

            <div class="col-6 col-lg-3 about-stat-border">
              <div class="about-stat-item">
                <div class="about-stat-number">5+</div>
                <div class="about-stat-text">Core Industry Sectors</div>
              </div>
            </div>

            <div class="col-6 col-lg-3 about-stat-border">
              <div class="about-stat-item">
                <div class="about-stat-number">2</div>
                <div class="about-stat-text">Regional AP Hubs</div>
              </div>
            </div>

            <div class="col-6 col-lg-3">
              <div class="about-stat-item">
                <div class="about-stat-number">100%</div>
                <div class="about-stat-text">GST &amp; Tax Compliant</div>
              </div>
            </div>

          </div>
        </div>

      </div>
    </section>
'''

print("Corporate About HTML template defined successfully!")
