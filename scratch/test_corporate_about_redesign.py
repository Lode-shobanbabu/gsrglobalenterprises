# scratch/test_corporate_about_redesign.py

about_html = '''<!-- ==========================================================================
         B. ABOUT US SECTION (CLEAN CORPORATE ARCHITECTURE)
         ========================================================================== -->
    <section class="about-section" id="about">
      <div class="container">

        <div class="row g-4 g-xl-5 align-items-center">

          <!-- Left Column: Executive Corporate Statement & Trust Profile -->
          <div class="col-lg-5 fade-up-element">
            <div class="about-corp-left">

              <!-- Eyebrow -->
              <div class="about-corp-eyebrow mb-2">
                <span class="about-corp-eyebrow-dash"></span>
                <span class="about-corp-eyebrow-text">ABOUT GSR GLOBAL ENTERPRISES</span>
              </div>

              <!-- Main Title -->
              <h2 class="about-corp-title mb-3">
                Delivering Reliable Procurement &amp; Supply Services Across Core Industries
              </h2>

              <!-- Executive Statement Card (User's Exact Sentence Highlighted) -->
              <div class="about-corp-statement-card mb-4">
                <div class="statement-accent-bar"></div>
                <p class="about-corp-statement-text mb-0">
                  From medical equipment and IT infrastructure to industrial materials, automotive components and renewable energy solutions, <strong>GSR Global Enterprises</strong> delivers reliable procurement and supply services tailored to diverse industry requirements.
                </p>
              </div>

              <!-- Trust & Compliance Badges -->
              <div class="about-corp-trust-list mb-4">
                <div class="trust-list-item">
                  <i class="bi bi-patch-check-fill text-orange"></i>
                  <span>Direct OEM &amp; Primary Mill Partnerships</span>
                </div>
                <div class="trust-list-item">
                  <i class="bi bi-patch-check-fill text-orange"></i>
                  <span>Rigorous Pre-Dispatch Quality Inspections</span>
                </div>
                <div class="trust-list-item">
                  <i class="bi bi-patch-check-fill text-orange"></i>
                  <span>100% Statutory, GST &amp; Tender Compliant</span>
                </div>
                <div class="trust-list-item">
                  <i class="bi bi-patch-check-fill text-orange"></i>
                  <span>Dual Regional Distribution Hubs in AP</span>
                </div>
              </div>

              <!-- Corporate Action CTA -->
              <div class="d-flex align-items-center gap-3 flex-wrap">
                <a href="#services" class="btn-corp-primary">
                  <span>Explore Our Services</span>
                  <i class="bi bi-arrow-right ms-1"></i>
                </a>
                <a href="#contact" class="btn-corp-outline">
                  <i class="bi bi-envelope-fill me-1"></i>
                  <span>Contact Sourcing Desk</span>
                </a>
              </div>

            </div>
          </div>

          <!-- Right Column: 5 Sector Procurement Matrix (Corporate Cards Grid) -->
          <div class="col-lg-7 fade-up-element">
            <div class="about-corp-sectors-panel">
              <div class="sectors-panel-header mb-3">
                <span class="sectors-panel-badge">PROCUREMENT VERTICALS</span>
                <h3 class="sectors-panel-title">Tailored Solutions for Government &amp; Enterprise Requirements</h3>
              </div>

              <div class="row g-3">

                <!-- 1. Medical & Healthcare -->
                <div class="col-sm-6">
                  <div class="about-sector-card">
                    <div class="about-sector-icon-wrap">
                      <i class="bi bi-hospital"></i>
                    </div>
                    <div class="about-sector-info">
                      <h4 class="about-sector-name">Medical &amp; Healthcare</h4>
                      <p class="about-sector-sub">Diagnostic devices, ICU monitors &amp; clinical supplies</p>
                    </div>
                  </div>
                </div>

                <!-- 2. GCC & IT Infrastructure -->
                <div class="col-sm-6">
                  <div class="about-sector-card">
                    <div class="about-sector-icon-wrap">
                      <i class="bi bi-display"></i>
                    </div>
                    <div class="about-sector-info">
                      <h4 class="about-sector-name">GCC &amp; IT Infrastructure</h4>
                      <p class="about-sector-sub">Computer systems, networking &amp; school digital labs</p>
                    </div>
                  </div>
                </div>

                <!-- 3. Industrial & Manufacturing -->
                <div class="col-sm-6">
                  <div class="about-sector-card">
                    <div class="about-sector-icon-wrap">
                      <i class="bi bi-gear-wide-connected"></i>
                    </div>
                    <div class="about-sector-info">
                      <h4 class="about-sector-name">Industrial Materials</h4>
                      <p class="about-sector-sub">TMT steel rebar, structural sections &amp; industrial yarn</p>
                    </div>
                  </div>
                </div>

                <!-- 4. Automobile & Transportation -->
                <div class="col-sm-6">
                  <div class="about-sector-card">
                    <div class="about-sector-icon-wrap">
                      <i class="bi bi-bus-front"></i>
                    </div>
                    <div class="about-sector-info">
                      <h4 class="about-sector-name">Automotive &amp; Transit</h4>
                      <p class="about-sector-sub">Bus spare parts, fleet components &amp; mechanical spares</p>
                    </div>
                  </div>
                </div>

                <!-- 5. Renewable Energy Solutions -->
                <div class="col-12">
                  <div class="about-sector-card about-sector-card-highlight">
                    <div class="about-sector-icon-wrap">
                      <i class="bi bi-sun"></i>
                    </div>
                    <div class="about-sector-info">
                      <h4 class="about-sector-name">Renewable Energy Solutions</h4>
                      <p class="about-sector-sub">Solar photovoltaic modules, sustainable infrastructure hardware &amp; clean energy systems</p>
                    </div>
                    <div class="about-sector-tag d-none d-md-inline-block">
                      <span>Clean Energy</span>
                    </div>
                  </div>
                </div>

              </div>

            </div>
          </div>

        </div>

      </div>
    </section>
'''

print("Created about_html successfully!")
