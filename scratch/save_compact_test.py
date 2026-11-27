html_test = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Compact Commitment Banner Test</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <style>
    :root {
      --primary-navy: #062b55;
      --accent-orange: #ff7900;
      --font-heading: 'Poppins', sans-serif;
      --font-body: 'Roboto', sans-serif;
    }
    body {
      background: #f1f5f9;
      margin: 0;
      padding: 3rem 1rem;
      font-family: var(--font-body);
    }
    .commitment-mockup-section {
      padding: 3rem 0;
    }
    .commitment-banner-card {
      position: relative;
      border-radius: 20px;
      overflow: hidden;
      background: #114a8f;
      box-shadow: 0 16px 44px rgba(6, 43, 85, 0.14);
      border: 1px solid rgba(255, 255, 255, 0.12);
    }
    .commitment-banner-row {
      min-height: 330px;
    }
    /* Left Content Area */
    .commitment-content-col {
      position: relative;
      z-index: 3;
      padding: 2.75rem 2.85rem;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    /* Left Background Image & Luminous Blue Gradient Overlay */
    .commitment-left-bg {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 1;
      pointer-events: none;
    }
    .commitment-left-bg-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      opacity: 0.50;
      filter: saturate(1.15) contrast(1.05);
    }
    .commitment-left-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(100deg, rgba(16, 75, 148, 0.90) 0%, rgba(22, 92, 175, 0.84) 48%, rgba(18, 80, 155, 0.60) 75%, rgba(14, 68, 134, 0.15) 100%);
    }
    .commitment-radial-glow {
      position: absolute;
      top: 25%;
      left: 15%;
      width: 420px;
      height: 420px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(56, 138, 228, 0.35) 0%, transparent 65%);
      pointer-events: none;
    }
    .commitment-mockup-eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 10px;
    }
    .mockup-eyebrow-dash {
      width: 24px;
      height: 3px;
      background-color: var(--accent-orange);
      border-radius: 2px;
      display: inline-block;
    }
    .mockup-eyebrow-text {
      font-family: var(--font-heading);
      font-size: 0.80rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #ffffff;
    }
    .commitment-mockup-title {
      font-family: var(--font-heading);
      font-size: clamp(1.85rem, 2.7vw, 2.5rem);
      font-weight: 700;
      color: #ffffff;
      line-height: 1.2;
      letter-spacing: -0.02em;
    }
    .commitment-mockup-title .text-orange {
      color: var(--accent-orange) !important;
    }
    .commitment-mockup-lead {
      font-family: var(--font-body);
      font-size: 0.98rem;
      font-weight: 400;
      color: rgba(255, 255, 255, 0.95);
      line-height: 1.6;
      max-width: 620px;
    }
    .commitment-mockup-lead strong {
      color: #ffffff;
      font-weight: 700;
    }
    .commitment-mockup-body {
      font-family: var(--font-body);
      font-size: 0.98rem;
      font-weight: 400;
      color: rgba(241, 245, 249, 0.90);
      line-height: 1.58;
      max-width: 620px;
    }
    /* Right Side Image Area (Website-Related Visual, Not Mobile!) */
    .commitment-visual-col {
      position: relative;
      overflow: hidden;
      min-height: 330px;
      z-index: 2;
    }
    .commitment-visual-img {
      width: 100%;
      height: 100%;
      min-height: 330px;
      object-fit: cover;
      object-position: center;
      display: block;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .commitment-banner-card:hover .commitment-visual-img {
      transform: scale(1.03);
    }
    .commitment-visual-blend-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(to right, rgba(16, 75, 148, 0.90) 0%, rgba(16, 75, 148, 0.40) 22%, transparent 58%),
                  linear-gradient(to top, rgba(16, 75, 148, 0.30) 0%, transparent 35%);
      pointer-events: none;
    }
    .commitment-badge-pill {
      position: absolute;
      bottom: 1.35rem;
      right: 1.35rem;
      background: rgba(16, 75, 148, 0.85);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.25);
      border-radius: 50px;
      padding: 0.5rem 1.15rem;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      color: #ffffff;
      font-family: var(--font-heading);
      font-size: 0.80rem;
      font-weight: 600;
      box-shadow: 0 6px 18px rgba(0, 0, 0, 0.25);
      z-index: 4;
    }
    .commitment-badge-pill .text-orange {
      color: var(--accent-orange) !important;
      font-size: 1rem;
    }
    @media (max-width: 991.98px) {
      .commitment-content-col {
        padding: 2.25rem 1.75rem 2rem;
      }
      .commitment-visual-col {
        min-height: 260px;
      }
      .commitment-visual-blend-overlay {
        background: linear-gradient(to bottom, rgba(16, 75, 148, 0.85) 0%, transparent 40%);
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="commitment-banner-card">
      <div class="commitment-left-bg" aria-hidden="true">
        <img src="assets/images/hero-logistics-global.webp" alt="" class="commitment-left-bg-img">
        <div class="commitment-left-overlay"></div>
        <div class="commitment-radial-glow"></div>
      </div>
      <div class="row g-0 commitment-banner-row align-items-stretch">
        <div class="col-lg-7 col-xl-7 commitment-content-col">
          <div class="commitment-text-wrap position-relative z-3">
            <div class="commitment-mockup-eyebrow mb-2">
              <span class="mockup-eyebrow-dash" aria-hidden="true"></span>
              <span class="mockup-eyebrow-text">OUR COMMITMENT</span>
            </div>
            <h2 class="commitment-mockup-title mb-3">
              A Commitment You Can <span class="text-orange">Count On</span>
            </h2>
            <p class="commitment-mockup-lead mb-2">
              At <strong>GSR Global Enterprises</strong>, we believe successful procurement goes beyond sourcing
              products. It is about understanding business needs, coordinating the right resources and building
              relationships based on trust.
            </p>
            <p class="commitment-mockup-body mb-0">
              Whether you require specialized medical devices, IT infrastructure for educational projects, industrial
              raw materials, automotive components or solar energy products, we are committed to supporting your
              procurement requirements with professionalism and dedication.
            </p>
          </div>
        </div>
        <div class="col-lg-5 col-xl-5 commitment-visual-col">
          <img src="assets/images/hero-procurement.webp" alt="GSR Global Procurement Operations" class="commitment-visual-img">
          <div class="commitment-visual-blend-overlay"></div>
          <div class="commitment-badge-pill">
            <i class="bi bi-shield-fill-check text-orange"></i>
            <span>Multi-Industry Supply Network</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
'''

with open('scratch/test_compact_commitment.html', 'w', encoding='utf-8') as f:
    f.write(html_test)
print("Saved scratch/test_compact_commitment.html")
