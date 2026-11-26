import re

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Target navbar section
old_navbar_pattern = r'<!-- Mobile Toggler -->.*?<!-- CTA Button: Request a Quote \(Orange Pill with Arrow\) -->\s*<div class="d-flex align-items-center mt-3 mt-lg-0">\s*<a href="#contact" class="header-cta-orange"[^>]*>.*?</a>\s*</div>\s*</div>'

new_navbar_html = """<!-- Mobile Toggler (Triggers Side Offcanvas) -->
        <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#navbarOffcanvas"
          aria-controls="navbarOffcanvas" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <!-- Side Offcanvas Navigation Drawer (Slides from Left with 'X' Close) -->
        <div class="offcanvas offcanvas-start" tabindex="-1" id="navbarOffcanvas" aria-labelledby="navbarOffcanvasLabel">
          <div class="offcanvas-header border-bottom">
            <a class="brand-container me-0" href="#hero" aria-label="GSR GLOBAL ENTERPRISES">
              <img src="assets/images/gsr-logo-official-transparent.webp"
                alt="GSR GLOBAL ENTERPRISES - Multi-Sector Procurement & Supply Experts"
                class="brand-logo-img offcanvas-logo-img">
            </a>
            <button type="button" class="btn-close offcanvas-close-btn" data-bs-dismiss="offcanvas" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
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
                <a class="nav-link" href="#Industries">Industries</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#why-us">Why Us</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#clients">Clients</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#commitment">Commitment</a>
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
        </div>"""

match = re.search(old_navbar_pattern, html, flags=re.DOTALL)
if match:
    html = html[:match.start()] + new_navbar_html + html[match.end():]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html updated with offcanvas navigation.")
else:
    print("WARNING: Could not find old navbar toggler/collapse pattern in index.html!")

# 2. Update css/style.css
with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Remove old .navbar-collapse styling in max-width: 991.98px media query if present
old_nav_collapse_css = """.navbar-collapse {
    background: var(--navy-950);
    border-radius: 10px;
    padding: 1.25rem;
    margin-top: 0.75rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
  }"""

if old_nav_collapse_css in css:
    css = css.replace(old_nav_collapse_css, "/* navbar-collapse replaced by offcanvas */")
    print("Removed old .navbar-collapse CSS rule.")

offcanvas_css = """
/* ==========================================================================
   Mobile Side Offcanvas Navigation Drawer (Exact Reference Design)
   ========================================================================== */
@media (max-width: 991.98px) {
  #navbarOffcanvas.offcanvas-start {
    width: 320px;
    max-width: 82vw;
    background-color: #ffffff;
    border: none;
    box-shadow: 6px 0 28px rgba(6, 43, 85, 0.16);
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .offcanvas-header {
    padding: 1.25rem 1.5rem;
    background-color: #ffffff;
    border-bottom: 1px solid rgba(6, 43, 85, 0.08);
  }

  .offcanvas-logo-img {
    height: 38px;
    width: auto;
    object-fit: contain;
  }

  .offcanvas-close-btn {
    font-size: 0.95rem;
    opacity: 0.65;
    transition: opacity 0.2s ease, transform 0.2s ease;
    padding: 0.5rem;
    cursor: pointer;
  }

  .offcanvas-close-btn:hover {
    opacity: 1;
    transform: rotate(90deg);
  }

  .offcanvas-body {
    padding: 1.5rem 1.5rem 2rem;
    display: flex;
    flex-direction: column;
  }

  .offcanvas-body .navbar-nav {
    display: flex;
    flex-direction: column;
    gap: 0;
    margin-bottom: 1.5rem;
  }

  .offcanvas-body .nav-item {
    border-bottom: 1px solid rgba(6, 43, 85, 0.06);
  }

  .offcanvas-body .nav-link {
    color: var(--primary-navy) !important;
    font-family: var(--font-heading);
    font-size: 0.95rem;
    font-weight: 500;
    padding: 0.85rem 0 !important;
    display: flex;
    align-items: center;
    justify-content: space-between;
    transition: all 0.2s ease;
  }

  .offcanvas-body .nav-link:hover,
  .offcanvas-body .nav-link.active {
    color: var(--accent-orange) !important;
    padding-left: 6px !important;
  }

  .offcanvas-body .header-cta-orange {
    width: 100%;
    justify-content: center;
    margin-top: 1rem;
    padding: 0.75rem 1.5rem;
  }
}

/* Ensure on Desktop (min-width: 992px) the offcanvas sits horizontally as a standard navbar */
@media (min-width: 992px) {
  #navbarOffcanvas.offcanvas-start {
    position: static;
    z-index: auto;
    flex-grow: 1;
    width: auto !important;
    height: auto !important;
    visibility: visible !important;
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    transform: none !important;
    transition: none !important;
    overflow: visible;
  }

  #navbarOffcanvas .offcanvas-header {
    display: none !important;
  }

  #navbarOffcanvas .offcanvas-body {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 0 !important;
    overflow: visible !important;
  }

  #navbarOffcanvas .navbar-nav {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    margin-bottom: 0 !important;
  }
}
"""

with open("css/style.css", "a", encoding="utf-8") as f:
    f.write(offcanvas_css)

print("css/style.css updated with offcanvas rules.")

# 3. Update js/script.js for auto-closing offcanvas on link click
with open("js/script.js", "r", encoding="utf-8") as f:
    js = f.read()

old_js_collapse_pattern = r'// 2\. Mobile Nav auto-collapse on link click.*?navbarCollapse\.classList\.remove\(\'show\'\);\s*\}\s*\}\s*\}\);\s*\}\);'

new_js_offcanvas = """// 2. Mobile Nav auto-close on link click (Side Offcanvas Drawer)
  const navLinks = document.querySelectorAll('#navbarOffcanvas .nav-link, #navbarOffcanvas .header-cta-orange');
  const offcanvasEl = document.getElementById('navbarOffcanvas');
  navLinks.forEach((link) => {
    link.addEventListener('click', () => {
      if (offcanvasEl?.classList.contains('show')) {
        const bsOffcanvas = bootstrap.Offcanvas.getInstance(offcanvasEl) || new bootstrap.Offcanvas(offcanvasEl);
        bsOffcanvas.hide();
      }
    });
  });"""

js_match = re.search(old_js_collapse_pattern, js, flags=re.DOTALL)
if js_match:
    js = js[:js_match.start()] + new_js_offcanvas + js[js_match.end():]
    with open("js/script.js", "w", encoding="utf-8") as f:
        f.write(js)
    print("js/script.js updated with offcanvas auto-close logic.")
else:
    print("WARNING: Could not find old js mobile collapse logic in js/script.js!")
