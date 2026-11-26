# scratch/apply_reference_footer.py

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '  <!-- ==========================================================================\n       H. FOOTER'
end_marker = '  <!-- ==========================================================================\n       MODAL: SERVICE SPECIFICATIONS QUICK VIEW'

idx1 = html.find(start_marker)
idx2 = html.find(end_marker)

if idx1 == -1 or idx2 == -1:
    print(f"Error finding markers: idx1={idx1}, idx2={idx2}")
    exit(1)

new_footer_html = '''  <!-- ==========================================================================
       H. FOOTER (EXACT USER REFERENCE DESIGN)
       ========================================================================== -->
  <footer class="footer-corporate" id="contact" aria-label="Corporate Footer">
    <!-- Top Gold Border Line -->
    <div class="footer-gold-line"></div>

    <!-- Main Navigation Bar Strip -->
    <div class="footer-nav-strip">
      <div class="container">
        <div class="d-flex flex-column flex-lg-row align-items-center justify-content-between gap-3 py-3">

          <!-- Brand Logo (Left) -->
          <a class="footer-brand" href="#hero" aria-label="GSR GLOBAL ENTERPRISES">
            <img src="assets/images/gsr-logo-official-white.webp"
              alt="GSR GLOBAL ENTERPRISES" class="footer-brand-logo">
          </a>

          <!-- Current Navbar Items (Center - Separated with Pipes) -->
          <nav aria-label="Footer Navigation">
            <ul class="footer-nav-links mb-0">
              <li><a href="#hero">Home</a></li>
              <li class="footer-nav-pipe" aria-hidden="true">|</li>
              <li><a href="#about">About Us</a></li>
              <li class="footer-nav-pipe" aria-hidden="true">|</li>
              <li><a href="#services">Services</a></li>
              <li class="footer-nav-pipe" aria-hidden="true">|</li>
              <li><a href="#Industries">Industries</a></li>
              <li class="footer-nav-pipe" aria-hidden="true">|</li>
              <li><a href="#why-us">Why Us</a></li>
              <li class="footer-nav-pipe" aria-hidden="true">|</li>
              <li><a href="#clients">Clients</a></li>
              <li class="footer-nav-pipe" aria-hidden="true">|</li>
              <li><a href="#contact">Contact Us</a></li>
            </ul>
          </nav>

          <!-- Social Media Round White Badges (Right) -->
          <div class="footer-social-group d-flex align-items-center gap-2">
            <a href="https://www.linkedin.com" target="_blank" rel="noopener noreferrer"
              class="footer-social-circle" aria-label="LinkedIn" title="LinkedIn">
              <i class="bi bi-linkedin"></i>
            </a>
            <a href="https://www.youtube.com" target="_blank" rel="noopener noreferrer"
              class="footer-social-circle" aria-label="YouTube" title="YouTube">
              <i class="bi bi-youtube"></i>
            </a>
            <a href="https://www.instagram.com" target="_blank" rel="noopener noreferrer"
              class="footer-social-circle" aria-label="Instagram" title="Instagram">
              <i class="bi bi-instagram"></i>
            </a>
          </div>

        </div>
      </div>
    </div>

    <!-- Middle Gold Divider Line -->
    <div class="footer-gold-line"></div>

    <!-- Bottom Copyright & Tagline Bar -->
    <div class="footer-bottom-strip">
      <div class="container">
        <div class="d-flex flex-column flex-md-row justify-content-between align-items-center gap-2 py-3">
          <div class="footer-copyright-text">
            &copy; 2026 GSR Global Enterprises. All Rights Reserved.
          </div>
          <div class="footer-tagline-text">
            Designed for a Better Tomorrow
          </div>
        </div>
      </div>
    </div>
  </footer>

'''

html = html[:idx1] + new_footer_html + html[idx2:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with reference footer!")

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

c_start = '/* ==========================================================================\n   Top Corporate Utility Bar'
# Find the footer CSS block
f_start = css.find('.footer-corporate {')
if f_start == -1:
    print("Error: Could not locate .footer-corporate in css/style.css")
    exit(1)

# Find where footer CSS ends (e.g. before back-to-top or modal)
f_end = css.find('.back-to-top {')
if f_end == -1:
    f_end = css.find('/* ==========================================================================\n   Modal')
if f_end == -1:
    print("Error: Could not find end of footer CSS")
    exit(1)

new_footer_css = '''.footer-corporate {
  background-color: #061c38;
  color: #ffffff;
  position: relative;
  overflow: hidden;
  padding: 0;
}

/* Gold Horizontal Dividing Line (Exact Reference Style) */
.footer-gold-line {
  height: 2px;
  background-color: #c5a059;
  width: 100%;
}

/* Main Navigation Bar Strip */
.footer-nav-strip {
  background-color: #061c38;
  padding: 0.25rem 0;
}

.footer-brand-logo {
  height: 38px;
  width: auto;
  display: block;
}

/* Horizontal Navbar Items Separated by Pipes */
.footer-nav-links {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 0.25rem 0;
}

.footer-nav-links a {
  color: #ffffff;
  font-family: var(--font-heading);
  font-size: 0.88rem;
  font-weight: 500;
  text-decoration: none;
  padding: 0.2rem 0.55rem;
  transition: color 0.2s ease;
}

.footer-nav-links a:hover {
  color: var(--accent-orange);
}

.footer-nav-pipe {
  color: rgba(255, 255, 255, 0.40);
  font-size: 0.82rem;
  font-weight: 300;
  user-select: none;
  padding: 0 0.1rem;
}

/* Round White Social Media Icons (Exact Reference Silhouette) */
.footer-social-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background-color: #ffffff;
  color: #062b55;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.85rem;
  text-decoration: none;
  transition: all 0.25s ease;
}

.footer-social-circle:hover {
  background-color: var(--accent-orange);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 121, 0, 0.35);
}

/* Bottom Strip: Copyright & Tagline */
.footer-bottom-strip {
  background-color: #04142a;
  padding: 0.25rem 0;
}

.footer-copyright-text {
  font-family: var(--font-body);
  font-size: 0.82rem;
  color: #cbd5e1;
}

.footer-tagline-text {
  font-family: var(--font-heading);
  font-size: 0.82rem;
  color: #cbd5e1;
  font-weight: 500;
  letter-spacing: 0.02em;
}

/* Responsive adjustments */
@media (max-width: 991.98px) {
  .footer-nav-links {
    gap: 0.4rem 0.2rem;
  }

  .footer-nav-links a {
    font-size: 0.82rem;
    padding: 0.15rem 0.4rem;
  }
}

@media (max-width: 575.98px) {
  .footer-copyright-text,
  .footer-tagline-text {
    text-align: center;
  }
}

'''

css = css[:f_start] + new_footer_css + css[f_end:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/style.css with reference footer styles!")
