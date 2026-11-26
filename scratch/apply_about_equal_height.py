# scratch/apply_about_equal_height.py

# 1. Update index.html with the user's exact content and equal-height layout
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sec_start = '<!-- ==========================================================================\n         B. ABOUT US SECTION'
sec_end = '<!-- ==========================================================================\n         C. OUR SERVICES'

idx1 = html.find(sec_start)
idx2 = html.find(sec_end)

if idx1 == -1 or idx2 == -1:
    print(f"Error finding markers: idx1={idx1}, idx2={idx2}")
    exit(1)

new_about_html = '''<!-- ==========================================================================
         B. ABOUT US SECTION (EQUAL HEIGHT IMAGE & CONTENT)
         ========================================================================== -->
    <section class="about-section" id="about">
      <div class="container">

        <div class="row g-4 g-lg-5 align-items-stretch">

          <!-- Left Column: Equal Height Corporate Procurement Logistics Image -->
          <div class="col-lg-6 d-flex flex-column fade-up-element">
            <div class="about-equal-media h-100">
              <img src="assets/images/about-warehouse-logistics.webp"
                alt="GSR Global Enterprises Multi-Sector Procurement & Logistics Operations"
                class="about-equal-img" loading="lazy">
              <!-- Trust Pill -->
              <div class="about-img-trust-tag">
                <i class="bi bi-shield-check"></i>
                <span>Verified Sourcing &amp; Procurement Solutions</span>
              </div>
            </div>
          </div>

          <!-- Right Column: Equal Height Content -->
          <div class="col-lg-6 d-flex flex-column justify-content-center fade-up-element">
            <div class="about-equal-content h-100 d-flex flex-column justify-content-center">

              <!-- Small Heading: WHO WE ARE -->
              <div class="about-eyebrow mb-2">
                <span class="about-eyebrow-dash"></span>
                <span class="about-eyebrow-text">WHO WE ARE</span>
              </div>

              <!-- Main Heading -->
              <h2 class="about-equal-title mb-3">
                Your Partner in Smarter Sourcing and Reliable Procurement
              </h2>

              <!-- Paragraph 1 -->
              <p class="about-equal-p mb-3">
                <strong>GSR Global Enterprises</strong> is a multi-sector procurement and supply company committed to supporting businesses, institutions, government initiatives and industrial organizations with dependable sourcing solutions.
              </p>

              <!-- Paragraph 2 -->
              <p class="about-equal-p mb-3">
                We specialize in procuring and supplying a diverse range of products across medical and healthcare, information technology, education infrastructure, industrial manufacturing, automotive and renewable energy sectors.
              </p>

              <!-- Paragraph 3 -->
              <p class="about-equal-p mb-3">
                Understanding that every industry has unique operational requirements, we focus on identifying suitable products, coordinating procurement and delivering solutions aligned with our customers' specifications, timelines and objectives.
              </p>

              <!-- Paragraph 4 -->
              <p class="about-equal-p mb-4">
                Our approach is built around professional coordination, transparent communication and long-term business relationships.
              </p>

              <!-- CTA: Know More About Our Capabilities -->
              <div class="about-equal-cta">
                <a href="#services" class="btn-about-capabilities">
                  <span>Know More About Our Capabilities</span>
                  <i class="bi bi-arrow-right ms-2"></i>
                </a>
              </div>

            </div>
          </div>

        </div>

      </div>
    </section>

    '''

html = html[:idx1] + new_about_html + html[idx2:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with equal-height About section!")

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

c_start = '/* ==========================================================================\n   B. About Us Section'
c_end = '/* ==========================================================================\n   C. Services Section'

c_idx1 = css.find(c_start)
c_idx2 = css.find(c_end)

if c_idx1 == -1 or c_idx2 == -1:
    print(f"Error finding CSS markers for About: c_idx1={c_idx1}, c_idx2={c_idx2}")
    exit(1)

new_about_css = '''/* ==========================================================================
   B. About Us Section - Equal Height Left Image & Right Content
   ========================================================================== */
.about-section {
  padding: 5rem 0;
  background-color: #ffffff;
  position: relative;
  border-bottom: 1px solid rgba(6, 43, 85, 0.06);
}

/* Equal Height Left Image Container */
.about-equal-media {
  position: relative;
  width: 100%;
  height: 100%;
  min-height: 480px;
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 16px 44px rgba(6, 43, 85, 0.10);
  border: 1px solid rgba(6, 43, 85, 0.08);
  background-color: var(--primary-navy);
}

.about-equal-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.65s cubic-bezier(0.16, 1, 0.3, 1);
}

.about-equal-media:hover .about-equal-img {
  transform: scale(1.04);
}

/* Trust Pill on Image */
.about-img-trust-tag {
  position: absolute;
  bottom: 1.5rem;
  left: 1.5rem;
  background: rgba(6, 43, 85, 0.92);
  color: #ffffff;
  padding: 0.6rem 1.15rem;
  border-radius: 50px;
  font-family: var(--font-heading);
  font-size: 0.80rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 121, 0, 0.45);
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.25);
}

.about-img-trust-tag i {
  color: var(--accent-orange);
  font-size: 1rem;
}

/* Right Content */
.about-equal-content {
  padding-left: 0.75rem;
}

.about-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 10px;
}

.about-eyebrow-dash {
  width: 24px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.about-eyebrow-text {
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--primary-navy);
}

.about-equal-title {
  font-family: var(--font-heading);
  font-size: clamp(1.85rem, 2.6vw, 2.35rem);
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.24;
  letter-spacing: -0.02em;
}

.about-equal-p {
  font-family: var(--font-body);
  font-size: 0.95rem;
  color: #475569;
  line-height: 1.68;
}

.about-equal-p strong {
  color: var(--primary-navy);
  font-weight: 700;
}

/* CTA: Know More About Our Capabilities */
.btn-about-capabilities {
  background: var(--accent-orange);
  color: #ffffff;
  padding: 0.72rem 1.75rem;
  border-radius: 50px;
  font-family: var(--font-heading);
  font-size: 0.88rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  box-shadow: 0 4px 14px rgba(255, 121, 0, 0.32);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  border: none;
}

.btn-about-capabilities:hover {
  background: var(--brand-orange-hover);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 121, 0, 0.45);
}

.btn-about-capabilities i {
  transition: transform 0.2s ease;
}

.btn-about-capabilities:hover i {
  transform: translateX(3px);
}

/* Responsiveness */
@media (max-width: 991.98px) {
  .about-section {
    padding: 3.8rem 0;
  }

  .about-equal-media {
    min-height: 380px;
    height: 380px;
  }

  .about-equal-content {
    padding-left: 0;
    margin-top: 1rem;
  }
}

@media (max-width: 575.98px) {
  .about-equal-media {
    min-height: 290px;
    height: 290px;
  }

  .about-img-trust-tag {
    bottom: 1rem;
    left: 1rem;
    font-size: 0.74rem;
    padding: 0.45rem 0.9rem;
  }

  .btn-about-capabilities {
    width: 100%;
    justify-content: center;
  }
}

'''

css = css[:c_idx1] + new_about_css + css[c_idx2:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/style.css with equal height styling!")
