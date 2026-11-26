# scratch/apply_about_exact_reference.py

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- ==========================================================================\n         B. ABOUT US SECTION'
if html.find(start_marker) == -1:
    start_marker = '<!-- ==========================================================================\n         B. ABOUT US SECTION (EXACT REFERENCE'
end_marker = '<!-- ==========================================================================\n         C. OUR SERVICES'

idx1 = html.find(start_marker)
idx2 = html.find(end_marker)

if idx1 == -1 or idx2 == -1:
    print(f"Error finding markers: idx1={idx1}, idx2={idx2}")
    exit(1)

new_about_html = '''<!-- ==========================================================================
         B. ABOUT US SECTION (EXACT REFERENCE DESIGN STYLE - CORPORATE CONSULTING)
         ========================================================================== -->
    <section class="about-section" id="about" aria-label="About GSR Global Enterprises">
      <div class="container">

        <div class="row g-4 g-lg-5 align-items-center">

          <!-- Left Column: Exact Reference Geometric Cutout Image with Experience Badge -->
          <div class="col-lg-6 fade-up-element">
            <div class="about-ref-media-box">
              <picture>
                <source srcset="assets/images/about-reference-exact.webp" type="image/webp">
                <img src="assets/images/about-reference-exact.png"
                  alt="GSR Global Enterprises Corporate Team Consultation and Procurement Strategy"
                  class="about-ref-img" width="732" height="568" loading="lazy">
              </picture>
            </div>
          </div>

          <!-- Right Column: Exact Reference Content Layout -->
          <div class="col-lg-6 fade-up-element">
            <div class="about-ref-content">

              <!-- Top Outlined Pill: ABOUT US (Exact Reference Style) -->
              <div class="about-ref-pill mb-3">
                <span>ABOUT US</span>
              </div>

              <!-- Main Corporate Heading -->
              <h2 class="about-ref-title mb-3">
                Your Partner in Smarter Sourcing and Reliable Procurement
              </h2>

              <!-- Corporate Content Paragraphs (Clean & Balanced Typography) -->
              <p class="about-ref-p about-ref-lead mb-3">
                <strong>GSR Global Enterprises</strong> is a multi-sector procurement and supply company committed to supporting businesses, institutions, government initiatives and industrial organizations with dependable sourcing solutions.
              </p>

              <p class="about-ref-p mb-3">
                We specialize in procuring and supplying a diverse range of products across medical and healthcare, information technology, education infrastructure, industrial manufacturing, automotive and renewable energy sectors.
              </p>

              <p class="about-ref-p mb-3">
                Understanding that every industry has unique operational requirements, we focus on identifying suitable products, coordinating procurement and delivering solutions aligned with our customers' specifications, timelines and objectives.
              </p>

              <p class="about-ref-p mb-4">
                Our approach is built around professional coordination, transparent communication and long-term business relationships.
              </p>

              <!-- CTA Button: Exact Reference Shape & Arrow with Brand Colors -->
              <div class="about-ref-cta-wrap">
                <a href="#services" class="btn-ref-cta" aria-label="Know More About Our Capabilities">
                  <span>Know More About Our Capabilities</span>
                  <i class="bi bi-arrow-up-right"></i>
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

print("Updated index.html with exact reference About Us section!")

# Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

c_start = '/* ==========================================================================\n   B. About Us Section'
c_end = '/* ==========================================================================\n   C. Services Section - Compact 3 Cards Per Row'

c_idx1 = css.find(c_start)
c_idx2 = css.find(c_end)

if c_idx1 == -1 or c_idx2 == -1:
    print(f"Error finding CSS markers: c_idx1={c_idx1}, c_idx2={c_idx2}")
    exit(1)

new_about_css = '''/* ==========================================================================
   B. About Us Section - Exact Reference Design Style (Corporate Consulting)
   ========================================================================== */
.about-section {
  padding: 3.5rem 0 3.8rem;
  background-color: #ffffff;
  position: relative;
  border-bottom: 1px solid rgba(6, 43, 85, 0.06);
}

/* Left Column: Geometric Cutout Image with Built-in Badge */
.about-ref-media-box {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.about-ref-img {
  width: 100%;
  max-width: 530px;
  height: auto;
  display: block;
  filter: drop-shadow(0 14px 32px rgba(6, 43, 85, 0.11));
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s ease;
}

.about-ref-media-box:hover .about-ref-img {
  transform: translateY(-5px);
  filter: drop-shadow(0 20px 42px rgba(6, 43, 85, 0.16));
}

/* Right Column Content */
.about-ref-content {
  padding-left: 0.85rem;
}

/* Top Outlined Pill: ABOUT US (Exact Reference Style) */
.about-ref-pill {
  display: inline-block;
  border: 1.5px solid rgba(6, 43, 85, 0.18);
  background-color: #ffffff;
  border-radius: 50px;
  padding: 0.35rem 1.25rem;
  box-shadow: 0 2px 6px rgba(6, 43, 85, 0.04);
}

.about-ref-pill span {
  font-family: var(--font-heading);
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--primary-navy);
}

/* Main Corporate Headline (Exact Reference Proportions) */
.about-ref-title {
  font-family: var(--font-heading);
  font-size: clamp(1.75rem, 2.35vw, 2.25rem);
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.22;
  letter-spacing: -0.02em;
}

/* Body Text (Crisp Corporate Typography) */
.about-ref-p {
  font-family: var(--font-body);
  font-size: 0.88rem;
  color: #475569;
  line-height: 1.58;
}

.about-ref-lead {
  font-size: 0.92rem;
  color: #334155;
}

.about-ref-p strong {
  color: var(--primary-navy);
  font-weight: 700;
}

/* CTA Button (Exact Reference Pill with Diagonal Arrow & Brand Colors) */
.about-ref-cta-wrap {
  margin-top: 0.5rem;
}

.btn-ref-cta {
  background-color: var(--primary-navy);
  color: #ffffff;
  padding: 0.72rem 1.85rem;
  border-radius: 50px;
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  box-shadow: 0 4px 16px rgba(6, 43, 85, 0.22);
  transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
  border: 1.5px solid transparent;
}

.btn-ref-cta i {
  font-size: 0.92rem;
  transition: transform 0.25s ease;
}

.btn-ref-cta:hover {
  background-color: var(--accent-orange);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(255, 121, 0, 0.38);
  border-color: var(--accent-orange);
}

.btn-ref-cta:hover i {
  transform: translate(2px, -2px);
}

/* Responsive adjustments */
@media (max-width: 991.98px) {
  .about-section {
    padding: 2.8rem 0;
  }

  .about-ref-content {
    padding-left: 0;
    margin-top: 1.25rem;
  }

  .about-ref-img {
    max-width: 440px;
  }
}

@media (max-width: 575.98px) {
  .about-ref-title {
    font-size: 1.55rem;
  }

  .btn-ref-cta {
    width: 100%;
    justify-content: center;
  }
}

'''

css = css[:c_idx1] + new_about_css + css[c_idx2:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/style.css with exact reference About Us styles!")
