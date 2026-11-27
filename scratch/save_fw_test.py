html_fullwidth = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Full-Width Edge-to-Edge Test</title>
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
      margin: 0;
      padding: 0;
      background: #f8fafc;
      font-family: var(--font-body);
    }
    .dummy-section {
      padding: 4rem 1rem;
      background: #ffffff;
      text-align: center;
    }
    /* Full-Width Edge-to-Edge Commitment Banner */
    .commitment-mockup-section {
      padding: 0;
      margin: 0;
      width: 100%;
      position: relative;
      overflow: hidden;
      background-color: #125197;
    }
    .commitment-fullwidth-banner {
      position: relative;
      width: 100%;
      overflow: hidden;
      background: #125197;
    }
    .commitment-banner-row {
      min-height: 340px;
    }
    .commitment-content-col {
      position: relative;
      z-index: 3;
      padding: 3.5rem 3.5rem 3.5rem max(2rem, calc((100vw - 1280px) / 2 + 1rem));
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
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
      opacity: 0.55;
      filter: saturate(1.2) contrast(1.05);
    }
    .commitment-left-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(100deg, rgba(22, 94, 180, 0.84) 0%, rgba(30, 116, 210, 0.78) 46%, rgba(24, 102, 192, 0.52) 75%, rgba(18, 80, 155, 0.10) 100%);
    }
    .commitment-radial-glow {
      position: absolute;
      top: 25%;
      left: 15%;
      width: 550px;
      height: 550px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(110, 185, 255, 0.38) 0%, transparent 65%);
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
      color: rgba(255, 255, 255, 0.96);
      line-height: 1.62;
      font-weight: 400;
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
      color: rgba(241, 245, 249, 0.92);
      line-height: 1.6;
      max-width: 620px;
    }
    .commitment-visual-col {
      position: relative;
      overflow: hidden;
      min-height: 340px;
      z-index: 2;
    }
    .commitment-visual-img {
      width: 100%;
      height: 100%;
      min-height: 340px;
      object-fit: cover;
      object-position: center;
      display: block;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .commitment-fullwidth-banner:hover .commitment-visual-img {
      transform: scale(1.03);
    }
    .commitment-visual-blend-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(to right, rgba(22, 94, 180, 0.88) 0%, rgba(22, 94, 180, 0.38) 22%, transparent 58%),
                  linear-gradient(to top, rgba(18, 80, 155, 0.25) 0%, transparent 35%);
      pointer-events: none;
    }
    .commitment-badge-pill {
      position: absolute;
      bottom: 1.5rem;
      right: max(1.5rem, calc((100vw - 1280px) / 2 + 1rem));
      background: rgba(18, 80, 155, 0.85);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.25);
      border-radius: 50px;
      padding: 0.55rem 1.25rem;
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
  </style>
</head>
<body>
  <div class="dummy-section">
    <h2>Clients Section Above (Inside Container)</h2>
  </div>

  <section class="commitment-mockup-section" id="commitment" aria-label="Our Commitment to Reliable Sourcing">
    <div class="commitment-fullwidth-banner position-relative">
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
  </section>

  <div class="dummy-section">
    <h2>Contact Section Below (Inside Container)</h2>
  </div>
</body>
</html>
'''

with open('scratch/test_fullwidth_render.html', 'w', encoding='utf-8') as f:
    f.write(html_fullwidth)
print("Saved scratch/test_fullwidth_render.html")
