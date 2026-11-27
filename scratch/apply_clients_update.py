import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

clients_html_replacement = '''    <section class="clients-section" id="clients" aria-label="Our Trusted Institutional Clients">
      <div class="container">

        <!-- Section Header (Centered Brand Dash Style) -->
        <div class="text-center mb-5 fade-up-element">
          <div class="clients-eyebrow mb-2">
            <span class="clients-eyebrow-dash"></span>
            <span class="clients-eyebrow-text">TRUSTED INSTITUTIONAL CLIENTS</span>
            <span class="clients-eyebrow-dash"></span>
          </div>
          <h2 class="clients-section-title mb-3">
            Supporting Government &amp; Public-Sector Organizations
          </h2>
          <div class="clients-title-accent mx-auto mb-3"></div>
          <p class="clients-section-subtitle mx-auto">
            We value the opportunity to serve institutional and public-sector organizations through our procurement and supply capabilities. Our client relationships reflect our commitment to understanding organizational requirements and providing dependable business support.
          </p>
        </div>

        <!-- Client Logos Carousel (Auto-scroll with 2 Repeating Institutional Clients) -->
        <div class="clients-carousel-container position-relative fade-up-element">
          <div class="clients-carousel-viewport" id="clientCarouselViewport">
            <div class="clients-carousel-track" id="clientCarouselTrack">

              <!-- Set 1 (Item 1: Central Prison) -->
              <div class="client-logo-card" data-client-index="0">
                <div class="client-card-symbol-wrap">
                  <picture>
                    <source srcset="assets/images/client-central-prison-emblem@2x.webp" type="image/webp">
                    <img src="assets/images/client-central-prison-emblem@2x.png" alt="National Emblem of India - Central Prison Visakhapatnam" class="client-card-logo-img emblem-ashoka">
                  </picture>
                </div>
                <div class="client-card-details">
                  <span class="client-card-badge">Government Institution</span>
                  <h3 class="client-card-name">Central Prison</h3>
                  <p class="client-card-location">Visakhapatnam, Andhra Pradesh</p>
                </div>
              </div>

              <!-- Set 1 (Item 2: APSRTC) -->
              <div class="client-logo-card" data-client-index="1">
                <div class="client-card-symbol-wrap">
                  <picture>
                    <source srcset="assets/images/client-apsrtc-logo@2x.webp" type="image/webp">
                    <img src="assets/images/client-apsrtc-logo@2x.png" alt="APSRTC Official Logo" class="client-card-logo-img emblem-apsrtc">
                  </picture>
                </div>
                <div class="client-card-details">
                  <span class="client-card-badge">State Public Transport</span>
                  <h3 class="client-card-name">APSRTC</h3>
                  <p class="client-card-location">Zonal Workshop, Vizianagaram</p>
                </div>
              </div>

              <!-- Set 2 (Item 1: Central Prison - Repeat) -->
              <div class="client-logo-card" data-client-index="0">
                <div class="client-card-symbol-wrap">
                  <picture>
                    <source srcset="assets/images/client-central-prison-emblem@2x.webp" type="image/webp">
                    <img src="assets/images/client-central-prison-emblem@2x.png" alt="National Emblem of India - Central Prison Visakhapatnam" class="client-card-logo-img emblem-ashoka">
                  </picture>
                </div>
                <div class="client-card-details">
                  <span class="client-card-badge">Government Institution</span>
                  <h3 class="client-card-name">Central Prison</h3>
                  <p class="client-card-location">Visakhapatnam, Andhra Pradesh</p>
                </div>
              </div>

              <!-- Set 2 (Item 2: APSRTC - Repeat) -->
              <div class="client-logo-card" data-client-index="1">
                <div class="client-card-symbol-wrap">
                  <picture>
                    <source srcset="assets/images/client-apsrtc-logo@2x.webp" type="image/webp">
                    <img src="assets/images/client-apsrtc-logo@2x.png" alt="APSRTC Official Logo" class="client-card-logo-img emblem-apsrtc">
                  </picture>
                </div>
                <div class="client-card-details">
                  <span class="client-card-badge">State Public Transport</span>
                  <h3 class="client-card-name">APSRTC</h3>
                  <p class="client-card-location">Zonal Workshop, Vizianagaram</p>
                </div>
              </div>

              <!-- Set 3 (Item 1: Central Prison - Repeat) -->
              <div class="client-logo-card" data-client-index="0">
                <div class="client-card-symbol-wrap">
                  <picture>
                    <source srcset="assets/images/client-central-prison-emblem@2x.webp" type="image/webp">
                    <img src="assets/images/client-central-prison-emblem@2x.png" alt="National Emblem of India - Central Prison Visakhapatnam" class="client-card-logo-img emblem-ashoka">
                  </picture>
                </div>
                <div class="client-card-details">
                  <span class="client-card-badge">Government Institution</span>
                  <h3 class="client-card-name">Central Prison</h3>
                  <p class="client-card-location">Visakhapatnam, Andhra Pradesh</p>
                </div>
              </div>

              <!-- Set 3 (Item 2: APSRTC - Repeat) -->
              <div class="client-logo-card" data-client-index="1">
                <div class="client-card-symbol-wrap">
                  <picture>
                    <source srcset="assets/images/client-apsrtc-logo@2x.webp" type="image/webp">
                    <img src="assets/images/client-apsrtc-logo@2x.png" alt="APSRTC Official Logo" class="client-card-logo-img emblem-apsrtc">
                  </picture>
                </div>
                <div class="client-card-details">
                  <span class="client-card-badge">State Public Transport</span>
                  <h3 class="client-card-name">APSRTC</h3>
                  <p class="client-card-location">Zonal Workshop, Vizianagaram</p>
                </div>
              </div>

              <!-- Set 4 (Item 1: Central Prison - Repeat) -->
              <div class="client-logo-card" data-client-index="0">
                <div class="client-card-symbol-wrap">
                  <picture>
                    <source srcset="assets/images/client-central-prison-emblem@2x.webp" type="image/webp">
                    <img src="assets/images/client-central-prison-emblem@2x.png" alt="National Emblem of India - Central Prison Visakhapatnam" class="client-card-logo-img emblem-ashoka">
                  </picture>
                </div>
                <div class="client-card-details">
                  <span class="client-card-badge">Government Institution</span>
                  <h3 class="client-card-name">Central Prison</h3>
                  <p class="client-card-location">Visakhapatnam, Andhra Pradesh</p>
                </div>
              </div>

              <!-- Set 4 (Item 2: APSRTC - Repeat) -->
              <div class="client-logo-card" data-client-index="1">
                <div class="client-card-symbol-wrap">
                  <picture>
                    <source srcset="assets/images/client-apsrtc-logo@2x.webp" type="image/webp">
                    <img src="assets/images/client-apsrtc-logo@2x.png" alt="APSRTC Official Logo" class="client-card-logo-img emblem-apsrtc">
                  </picture>
                </div>
                <div class="client-card-details">
                  <span class="client-card-badge">State Public Transport</span>
                  <h3 class="client-card-name">APSRTC</h3>
                  <p class="client-card-location">Zonal Workshop, Vizianagaram</p>
                </div>
              </div>

            </div>
          </div>

          <!-- Centered Carousel Dots (Repeat Two Only) -->
          <div class="clients-carousel-dots d-flex justify-content-center align-items-center gap-2" id="clientCarouselDots" role="tablist" aria-label="Client Slide Indicators">
            <button type="button" class="client-carousel-dot active" data-index="0" aria-label="Slide 1: Central Prison Visakhapatnam" aria-current="true"></button>
            <button type="button" class="client-carousel-dot" data-index="1" aria-label="Slide 2: APSRTC" aria-current="false"></button>
          </div>
        </div>

      </div>
    </section>'''

html_new, n_html = re.subn(
    r'<section class="clients-section" id="clients".*?</section>',
    clients_html_replacement.strip(),
    html,
    flags=re.DOTALL
)

print(f"Replaced in index.html: {n_html} occurrence(s)")
if n_html == 1:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_new)
    print("Saved index.html successfully.")
else:
    print("Error: Could not match clients section in index.html")
