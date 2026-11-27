html_preview = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Commitment Banner Test</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <style>
    :root {
      --primary-navy: #062b55;
      --navy-900: #0a3366;
      --navy-950: #031b38;
      --accent-orange: #ff7900;
      --white: #ffffff;
      --text-grey: #555b63;
      --font-heading: 'Poppins', sans-serif;
      --font-body: 'Roboto', sans-serif;
    }
    body {
      background: #f1f5f9;
      font-family: var(--font-body);
      margin: 0;
      padding: 3rem 1rem;
    }
    .commitment-banner-section {
      padding: 2rem 0;
    }
    .commitment-banner-card {
      position: relative;
      border-radius: 24px;
      overflow: hidden;
      background: var(--primary-navy);
      box-shadow: 0 20px 50px rgba(6, 43, 85, 0.18);
      min-height: 480px;
      display: flex;
      align-items: center;
    }
    .commitment-banner-bg {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 1;
    }
    .commitment-bg-image {
      width: 100%;
      height: 100%;
      object-fit: cover;
      opacity: 0.32;
      filter: saturate(1.15) contrast(1.05);
    }
    .commitment-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(100deg, rgba(6, 43, 85, 0.98) 0%, rgba(6, 43, 85, 0.94) 46%, rgba(6, 43, 85, 0.72) 75%, rgba(6, 43, 85, 0.28) 100%);
    }
    .commitment-radial-glow {
      position: absolute;
      top: 25%;
      left: 15%;
      width: 500px;
      height: 500px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(19, 88, 157, 0.45) 0%, transparent 70%);
      pointer-events: none;
    }
    .commitment-content-container {
      position: relative;
      z-index: 2;
      padding: 4rem 3.5rem;
      width: 100%;
    }
    .commitment-eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 12px;
    }
    .commitment-eyebrow-dash {
      width: 28px;
      height: 3px;
      background-color: var(--accent-orange);
      border-radius: 2px;
      display: inline-block;
    }
    .commitment-eyebrow-text {
      font-family: var(--font-heading);
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--accent-orange);
    }
    .commitment-main-title {
      font-family: var(--font-heading);
      font-size: clamp(2rem, 3.2vw, 2.9rem);
      font-weight: 700;
      color: #ffffff;
      line-height: 1.2;
      letter-spacing: -0.02em;
    }
    .commitment-main-title .text-orange {
      color: var(--accent-orange) !important;
    }
    .commitment-lead-text {
      font-family: var(--font-body);
      font-size: 0.98rem;
      font-weight: 400;
      color: rgba(255, 255, 255, 0.95);
      line-height: 1.65;
    }
    .commitment-lead-text strong {
      color: #ffffff;
      font-weight: 700;
    }
    .commitment-body-text {
      font-family: var(--font-body);
      font-size: 0.98rem;
      font-weight: 400;
      color: rgba(226, 232, 240, 0.90);
      line-height: 1.65;
    }
    .commitment-visual-wrapper {
      position: relative;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .commitment-showcase-card {
      position: relative;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.40), 0 0 0 1px rgba(255, 255, 255, 0.18);
      max-width: 460px;
      width: 100%;
      background: #0f172a;
      transition: transform 0.4s ease, box-shadow 0.4s ease;
    }
    .commitment-showcase-card:hover {
      transform: translateY(-5px) scale(1.01);
      box-shadow: 0 30px 70px rgba(0, 0, 0, 0.50), 0 0 0 1px rgba(255, 121, 0, 0.35);
    }
    .commitment-showcase-img {
      width: 100%;
      height: 340px;
      object-fit: cover;
      display: block;
      transition: transform 0.5s ease;
    }
    .commitment-showcase-card:hover .commitment-showcase-img {
      transform: scale(1.04);
    }
    .commitment-showcase-badge {
      position: absolute;
      bottom: 1.25rem;
      left: 1.25rem;
      right: 1.25rem;
      background: rgba(6, 43, 85, 0.88);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.20);
      border-radius: 12px;
      padding: 0.75rem 1.15rem;
      display: flex;
      align-items: center;
      gap: 10px;
      color: #ffffff;
      font-family: var(--font-heading);
      font-size: 0.84rem;
      font-weight: 600;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="commitment-banner-card">
      <div class="commitment-banner-bg">
        <img src="assets/images/hero-procurement.webp" alt="" class="commitment-bg-image">
        <div class="commitment-overlay"></div>
        <div class="commitment-radial-glow"></div>
      </div>
      <div class="commitment-content-container">
        <div class="row align-items-center g-5">
          <div class="col-lg-7 col-xl-7">
            <div class="commitment-eyebrow mb-3">
              <span class="commitment-eyebrow-dash"></span>
              <span class="commitment-eyebrow-text">OUR COMMITMENT</span>
            </div>
            <h2 class="commitment-main-title mb-4">
              A Commitment You Can <span class="text-orange">Count On</span>
            </h2>
            <p class="commitment-lead-text mb-3">
              At <strong>GSR Global Enterprises</strong>, we believe successful procurement goes beyond sourcing
              products. It is about understanding business needs, coordinating the right resources and building
              relationships based on trust.
            </p>
            <p class="commitment-body-text mb-0">
              Whether you require specialized medical devices, IT infrastructure for educational projects, industrial
              raw materials, automotive components or solar energy products, we are committed to supporting your
              procurement requirements with professionalism and dedication.
            </p>
          </div>
          <div class="col-lg-5 col-xl-5">
            <div class="commitment-visual-wrapper">
              <div class="commitment-showcase-card">
                <img src="assets/images/about-procurement-facility.webp" alt="GSR Global Procurement Operations" class="commitment-showcase-img">
                <div class="commitment-showcase-badge">
                  <i class="bi bi-shield-fill-check text-warning fs-5"></i>
                  <span>Comprehensive Multi-Industry Sourcing</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
'''

with open('scratch/test_commitment_render.html', 'w', encoding='utf-8') as f:
    f.write(html_preview)
print("Preview HTML written")
