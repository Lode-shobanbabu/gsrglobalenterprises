import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Option 1: Mobile Background Image with clean overlay
# Option 2: Responsive Picture / Hero visual card on mobile

# Let's create two test HTML files and capture them at 1400px (Desktop) and 390px (Mobile)
test_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<style>
/* Option A: Pure CSS background switcher */
.hero-opt-a {
  position: relative;
  min-height: 480px;
  background-image: url('assets/images/hero-desktop.webp');
  background-repeat: no-repeat;
  background-position: right center;
  background-size: cover;
  background-color: #0d274c;
  display: flex;
  align-items: center;
  padding: 3.2rem 0;
  isolation: isolate;
  overflow: hidden;
}

.hero-opt-a::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
  background: linear-gradient(90deg,
    rgba(255, 255, 255, 0.95) 0%,
    rgba(255, 255, 255, 0.90) 38%,
    rgba(255, 255, 255, 0.50) 58%,
    rgba(255, 255, 255, 0) 75%) !important;
}

@media (max-width: 991.98px) {
  .hero-opt-a {
    min-height: auto;
    background-image: url('assets/images/hero-mobile.webp') !important;
    background-position: center bottom !important;
    background-size: cover !important;
    padding: 2.5rem 0 340px !important;
  }
  .hero-opt-a::before {
    background: linear-gradient(180deg,
      rgba(255, 255, 255, 0.96) 0%,
      rgba(255, 255, 255, 0.92) 48%,
      rgba(255, 255, 255, 0.40) 65%,
      rgba(255, 255, 255, 0) 78%) !important;
  }
}
</style>
</head>
<body>
  <!-- Header placeholder -->
  <div style="background: white; padding: 15px; border-bottom: 1px solid #eee; font-weight: 600; text-align: center;">GSR GLOBAL ENTERPRISES</div>
  
  <section class="hero-opt-a" id="hero">
    <div class="container hero-container">
      <div class="row align-items-center">
        <div class="col-lg-8 col-xl-7 hero-content-col">
          <div class="hero-eyebrow">
            <span class="hero-eyebrow-dash"></span>
            <span class="hero-eyebrow-text">YOUR TRUSTED PROCUREMENT &amp; SUPPLY PARTNER</span>
          </div>
          <h1 class="hero-main-title">
            Connecting Industries With The Right Products, Resources &amp; Solutions
          </h1>
          <p class="hero-lead-desc">
            From medical equipment and IT infrastructure to industrial materials, automotive components and renewable
            energy solutions, GSR Global Enterprises delivers reliable procurement and supply services tailored to
            diverse industry requirements.
          </p>
          <p class="hero-sub-desc">
            We simplify sourcing, streamline procurement and help organizations access the products and resources they
            need to move forward.
          </p>
          <div class="hero-action-row">
            <a href="#services" class="btn-hero-primary">
              <span>Explore Our Services</span>
              <i class="bi bi-arrow-right ms-1"></i>
            </a>
            <a href="#contact" class="btn-hero-secondary">
              <span>Discuss Your Requirements</span>
              <i class="bi bi-arrow-right ms-1"></i>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</body>
</html>
"""

with open('scratch/test_opt_a.html', 'w', encoding='utf-8') as f:
    f.write(test_html_content)

# Render Desktop (1400px)
cmd_d = [
    chrome_path, "--headless=new", "--disable-gpu", "--no-sandbox",
    "--window-size=1400,900", f"--screenshot={os.path.abspath('scratch/hero_opt_a_desktop.png')}",
    f"file:///{os.path.abspath('scratch/test_opt_a.html').replace(chr(92), '/')}"
]
subprocess.run(cmd_d, capture_output=True)

# Render Mobile (390px x 1000px)
cmd_m = [
    chrome_path, "--headless=new", "--disable-gpu", "--no-sandbox",
    "--window-size=390,1100", f"--screenshot={os.path.abspath('scratch/hero_opt_a_mobile.png')}",
    f"file:///{os.path.abspath('scratch/test_opt_a.html').replace(chr(92), '/')}"
]
subprocess.run(cmd_m, capture_output=True)

print("Rendered Option A desktop and mobile")
