with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '    <!-- ==========================================================================\n         A. HOME / HERO SECTION'
end_marker = '    </section>\n\n    <!-- ==========================================================================\n         B. ABOUT US SECTION'

s_idx = html.find(start_marker)
e_idx = html.find(end_marker)

if s_idx == -1 or e_idx == -1:
    print(f"Error: markers not found (start={s_idx}, end={e_idx})")
    exit(1)

new_hero = """    <!-- ==========================================================================
         A. HOME / HERO SECTION - CINEMATIC BOARDROOM PHOTOGRAPHY (CONNEXHIRE STYLE)
         ========================================================================== -->
    <section class="hero-section" id="hero">
      <div class="container hero-container">
        <div class="row align-items-center">
          <div class="col-lg-11 col-xl-10 hero-content-col">

            <!-- Verified Status Pill -->
            <div class="hero-status-pill fade-up-element">
              <i class="bi bi-shield-check text-orange me-2"></i>
              <span class="hero-status-text">Government &amp; Multi-Sector Sourcing Experts</span>
            </div>

            <!-- Main Headline (Inspired by Reference Design) -->
            <h1 class="hero-main-title fade-up-element">
              Empowering Global Supply Chains <br>
              <span class="hero-title-highlight">&amp; Delivering Procurement</span> Excellence.
            </h1>

            <!-- Lead Paragraph -->
            <p class="hero-lead-desc fade-up-element">
              Reliable turnkey sourcing, quality-driven procurement, and dependable supply solutions for healthcare institutions, government agencies, transit workshops, and clean energy projects.
            </p>

            <!-- Action Buttons Row -->
            <div class="hero-action-row fade-up-element">
              <a href="#services" class="btn-hero-action">
                <span>Explore Procurement Services</span>
                <span class="btn-hero-circle"><i class="bi bi-arrow-right"></i></span>
              </a>
              <a href="#contact" class="btn-hero-outline">
                <i class="bi bi-telephone-fill me-2 text-orange"></i>
                <span>Contact Procurement Team</span>
              </a>
            </div>

            <!-- Sourcing Verticals Strip -->
            <div class="hero-sectors-strip fade-up-element">
              <div class="hero-sector-tag"><i class="bi bi-hospital text-orange"></i> Healthcare &amp; Medical</div>
              <div class="hero-sector-tag"><i class="bi bi-bus-front text-orange"></i> APSRTC Fleet Spares</div>
              <div class="hero-sector-tag"><i class="bi bi-sun text-orange"></i> Solar Renewable Energy</div>
              <div class="hero-sector-tag"><i class="bi bi-buildings text-orange"></i> Structural Steel &amp; Metals</div>
            </div>

          </div>
        </div>
      </div>"""

html = html[:s_idx] + new_hero + html[e_idx:]

# Update footer logo
html = html.replace('src="assets/images/gsr-logo-white.webp"', 'src="assets/images/gsr-logo-official-white.webp"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html hero section and footer logo successfully!")
