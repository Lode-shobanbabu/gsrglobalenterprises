# scratch/create_5_docked_cards.py

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sec_start = '<!-- ==========================================================================\n         A2. CORE SECTORS CARDS BAR'
sec_end = '<!-- ==========================================================================\n         B. ABOUT US SECTION'

idx1 = html.find(sec_start)
idx2 = html.find(sec_end)

if idx1 == -1 or idx2 == -1:
    print(f"Error finding markers: idx1={idx1}, idx2={idx2}")
    exit(1)

new_cards_html = '''<!-- ==========================================================================
         A2. 5 CORE SECTOR CARDS (EXACT REFERENCE STYLE - STANDALONE CARDS)
         ========================================================================== -->
    <section class="hero-docked-cards-section" id="sectors" aria-label="Core Business Sectors">
      <div class="container">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-5 g-3 g-xl-4 justify-content-center">

          <!-- Card 1: Medical & Healthcare Supplies -->
          <div class="col fade-up-element">
            <div class="hero-dock-card h-100">
              <div class="dock-card-badge">
                <i class="bi bi-hospital"></i>
              </div>
              <div class="dock-card-body">
                <h4 class="dock-card-title">Medical &amp; Healthcare</h4>
                <p class="dock-card-desc">Diagnostic equipment, ICU devices &amp; clinical hospital supplies.</p>
                <a href="#services" class="dock-card-more" data-select-service="01">
                  <span>MORE</span>
                  <i class="bi bi-arrow-right"></i>
                </a>
              </div>
            </div>
          </div>

          <!-- Card 2: GCC & IT Infrastructure -->
          <div class="col fade-up-element">
            <div class="hero-dock-card h-100">
              <div class="dock-card-badge">
                <i class="bi bi-display"></i>
              </div>
              <div class="dock-card-body">
                <h4 class="dock-card-title">GCC &amp; IT Infrastructure</h4>
                <p class="dock-card-desc">Enterprise computers, networking hardware &amp; digital learning labs.</p>
                <a href="#services" class="dock-card-more" data-select-service="02">
                  <span>MORE</span>
                  <i class="bi bi-arrow-right"></i>
                </a>
              </div>
            </div>
          </div>

          <!-- Card 3: Government & Education Projects -->
          <div class="col fade-up-element">
            <div class="hero-dock-card h-100">
              <div class="dock-card-badge">
                <i class="bi bi-bank2"></i>
              </div>
              <div class="dock-card-body">
                <h4 class="dock-card-title">Government &amp; Education</h4>
                <p class="dock-card-desc">School transformation programs &amp; public sector bulk procurement.</p>
                <a href="#services" class="dock-card-more" data-select-service="03">
                  <span>MORE</span>
                  <i class="bi bi-arrow-right"></i>
                </a>
              </div>
            </div>
          </div>

          <!-- Card 4: Industrial & Manufacturing Supplies -->
          <div class="col fade-up-element">
            <div class="hero-dock-card h-100">
              <div class="dock-card-badge">
                <i class="bi bi-gear-wide-connected"></i>
              </div>
              <div class="dock-card-body">
                <h4 class="dock-card-title">Industrial Materials</h4>
                <p class="dock-card-desc">TMT steel rebar, structural sections &amp; manufacturing raw materials.</p>
                <a href="#services" class="dock-card-more" data-select-service="04">
                  <span>MORE</span>
                  <i class="bi bi-arrow-right"></i>
                </a>
              </div>
            </div>
          </div>

          <!-- Card 5: Automobile & Transportation Supplies -->
          <div class="col fade-up-element">
            <div class="hero-dock-card h-100">
              <div class="dock-card-badge">
                <i class="bi bi-bus-front"></i>
              </div>
              <div class="dock-card-body">
                <h4 class="dock-card-title">Automotive &amp; Transit</h4>
                <p class="dock-card-desc">Commercial bus components, fleet spares &amp; vehicle maintenance.</p>
                <a href="#services" class="dock-card-more" data-select-service="05">
                  <span>MORE</span>
                  <i class="bi bi-arrow-right"></i>
                </a>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    '''

html = html[:idx1] + new_cards_html + html[idx2:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with 5 standalone reference-style cards!")

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

c_start = '/* ==========================================================================\n   A2. Core Sectors Bar'
c_end = '/* ==========================================================================\n   B. About Us Section'

c_idx1 = css.find(c_start)
c_idx2 = css.find(c_end)

if c_idx1 == -1 or c_idx2 == -1:
    print(f"Error finding CSS markers for A2: c_idx1={c_idx1}, c_idx2={c_idx2}")
    exit(1)

new_cards_css = '''/* ==========================================================================
   A2. 5 Core Sector Cards (Exact Reference Design Style - Standalone Cards)
   ========================================================================== */
.hero-docked-cards-section {
  position: relative;
  z-index: 10;
  margin-top: -1.8rem;
  margin-bottom: 2.2rem;
  padding: 0;
}

/* Individual Reference Style Card */
.hero-dock-card {
  background: #ffffff;
  border-radius: 14px;
  border: 1px solid rgba(6, 43, 85, 0.08);
  box-shadow: 0 10px 30px rgba(6, 43, 85, 0.08), 0 2px 8px rgba(6, 43, 85, 0.04);
  padding: 1.65rem 1.15rem 1.35rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  position: relative;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.hero-dock-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 18px 44px rgba(6, 43, 85, 0.14), 0 4px 12px rgba(6, 43, 85, 0.06);
  border-color: rgba(255, 121, 0, 0.35);
}

/* Dark Square Icon Badge (Exact Reference Silhouette) */
.dock-card-badge {
  width: 48px;
  height: 48px;
  border-radius: 10px;
  background-color: var(--primary-navy);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  margin-bottom: 1.15rem;
  box-shadow: 0 4px 14px rgba(6, 43, 85, 0.22);
  transition: all 0.3s ease;
}

.hero-dock-card:hover .dock-card-badge {
  background-color: var(--accent-orange);
  color: #ffffff;
  transform: scale(1.08);
  box-shadow: 0 6px 18px rgba(255, 121, 0, 0.38);
}

/* Card Body */
.dock-card-body {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-grow: 1;
  width: 100%;
}

.dock-card-title {
  font-family: var(--font-heading);
  font-size: 0.94rem;
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.32;
  margin-bottom: 0.55rem;
  transition: color 0.25s ease;
}

.hero-dock-card:hover .dock-card-title {
  color: var(--accent-orange);
}

.dock-card-desc {
  font-family: var(--font-body);
  font-size: 0.79rem;
  color: var(--text-grey);
  line-height: 1.48;
  margin-bottom: 1.15rem;
  flex-grow: 1;
}

/* Bottom Action: MORE -> (Exact Reference Style) */
.dock-card-more {
  font-family: var(--font-heading);
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--primary-navy);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: auto;
  transition: all 0.25s ease;
}

.dock-card-more i {
  font-size: 0.82rem;
  transition: transform 0.25s ease;
}

.hero-dock-card:hover .dock-card-more {
  color: var(--accent-orange);
}

.hero-dock-card:hover .dock-card-more i {
  transform: translateX(4px);
}

/* Responsiveness */
@media (max-width: 991.98px) {
  .hero-docked-cards-section {
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
  }
}

@media (max-width: 575.98px) {
  .hero-dock-card {
    padding: 1.35rem 1rem 1.15rem;
  }
}

'''

css = css[:c_idx1] + new_cards_css + css[c_idx2:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/style.css with 5 standalone reference-style cards CSS!")
