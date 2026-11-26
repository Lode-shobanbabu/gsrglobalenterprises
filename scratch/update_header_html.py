# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Top Utility Bar & Main Navbar
topbar_marker = '<!-- ==========================================================================\n       TOP CORPORATE UTILITY BAR'
header_end_marker = '</header>'

idx_start = html.find(topbar_marker)
idx_end = html.find(header_end_marker)

if idx_start == -1 or idx_end == -1:
    print(f"Error finding markers: start={idx_start}, end={idx_end}")
    exit(1)

idx_end += len(header_end_marker)

new_header_html = '''<!-- ==========================================================================
       TOP CORPORATE UTILITY BAR (EXACT REFERENCE DESIGN)
       ========================================================================== -->
  <div class="top-utility-bar d-none d-lg-block">
    <div class="container">
      <div class="d-flex justify-content-between align-items-center">
        <!-- Direct Phone, Official Email & Location (Left Aligned) -->
        <div class="d-flex align-items-center gap-3">
          <a href="tel:+917989635764" class="topbar-contact-item">
            <i class="bi bi-telephone-fill"></i>
            <span>+91 7989635764</span>
          </a>
          <a href="mailto:gsrglobalenterprises@gmail.com" class="topbar-contact-item">
            <i class="bi bi-envelope-fill"></i>
            <span>gsrglobalenterprises@gmail.com</span>
          </a>
          <span class="topbar-v-pipe">|</span>
          <span class="topbar-location-item">
            <i class="bi bi-geo-alt-fill"></i>
            <span>Visakhapatnam, India</span>
          </span>
        </div>

        <!-- Social Media Badges (Right Aligned, White Circles with Navy Icons) -->
        <div class="d-flex align-items-center gap-2">
          <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" class="topbar-social-btn" aria-label="LinkedIn">
            <i class="bi bi-linkedin"></i>
          </a>
          <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" class="topbar-social-btn" aria-label="YouTube">
            <i class="bi bi-youtube"></i>
          </a>
          <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" class="topbar-social-btn" aria-label="Facebook">
            <i class="bi bi-facebook"></i>
          </a>
        </div>
      </div>
    </div>
  </div>


  <!-- ==========================================================================
       MAIN NAVIGATION BAR (EXACT REFERENCE ORDER & ORANGE CTA)
       ========================================================================== -->
  <header class="sticky-top">
    <nav class="navbar navbar-expand-lg navbar-corporate" id="mainNavbar" aria-label="Corporate Header">
      <div class="container">

        <!-- Official Corporate Logo (Client Color Logo on Transparent Background) -->
        <a class="brand-container" href="#hero" aria-label="GSR GLOBAL ENTERPRISES">
          <img src="assets/images/gsr-logo-official-transparent.webp"
            alt="GSR GLOBAL ENTERPRISES - Multi-Sector Procurement & Supply Experts" class="brand-logo-img">
        </a>

        <!-- Mobile Toggler -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent"
          aria-controls="navbarContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <!-- Nav Links (Exact Order From Second Screenshot) -->
        <div class="collapse navbar-collapse" id="navbarContent">
          <ul class="navbar-nav mx-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" href="#hero">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#about">About Us</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#services">Services</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#industries">Industries</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#clients">Clients</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#contact">Contact Us</a>
            </li>
          </ul>

          <!-- CTA Button: Request a Quote (Orange Pill with Arrow) -->
          <div class="d-flex align-items-center mt-3 mt-lg-0">
            <a href="#contact" class="header-cta-orange" aria-label="Request a Quote">
              <span>Request a Quote</span>
              <i class="bi bi-arrow-right ms-1"></i>
            </a>
          </div>
        </div>

      </div>
    </nav>
  </header>'''

html = html[:idx_start] + new_header_html + html[idx_end:]

# Add #industries scroll target to services-section if not present
if 'id="industries"' not in html:
    html = html.replace('<div class="services-carousel-wrapper fade-up-element">', '<div id="industries" style="scroll-margin-top: 100px;"></div>\n        <div class="services-carousel-wrapper fade-up-element">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")
