import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

commitment_css_replacement = '''/* ==========================================================================
   F. Our Commitment Section (Executive Procurement Showcase Banner)
   ========================================================================== */
.commitment-mockup-section {
  padding: 5.5rem 0 6rem;
  background-color: #f8fafc;
  position: relative;
  border-bottom: 1px solid rgba(6, 43, 85, 0.06);
}

.commitment-banner-card {
  position: relative;
  border-radius: 24px;
  overflow: hidden;
  background: var(--primary-navy);
  box-shadow: 0 20px 50px rgba(6, 43, 85, 0.16);
  border: 1px solid rgba(6, 43, 85, 0.08);
}

.commitment-banner-row {
  min-height: 480px;
}

/* Left Content Area */
.commitment-content-col {
  position: relative;
  z-index: 3;
  padding: 4.5rem 3.5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* Left Background Image & Brand Navy Gradient Overlay */
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
  opacity: 0.28;
  filter: saturate(1.1);
}

.commitment-left-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(105deg, rgba(6, 43, 85, 0.98) 0%, rgba(6, 43, 85, 0.94) 52%, rgba(6, 43, 85, 0.72) 80%, rgba(6, 43, 85, 0.35) 100%);
}

.commitment-radial-glow {
  position: absolute;
  top: 20%;
  left: 10%;
  width: 500px;
  height: 500px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(19, 88, 157, 0.40) 0%, transparent 70%);
  pointer-events: none;
}

/* Eyebrow: Brand Orange Dash & Text */
.commitment-mockup-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 12px;
}

.mockup-eyebrow-dash {
  width: 28px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.mockup-eyebrow-text {
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--accent-orange);
}

/* Main Heading */
.commitment-mockup-title {
  font-family: var(--font-heading);
  font-size: clamp(2rem, 3.2vw, 3rem);
  font-weight: 700;
  color: #ffffff;
  line-height: 1.18;
  letter-spacing: -0.02em;
}

.commitment-mockup-title .text-orange {
  color: var(--accent-orange) !important;
}

/* Narrative Body Copy (0.98rem / 400 Weight Site-Wide Standard) */
.commitment-mockup-lead {
  font-family: var(--font-body);
  font-size: 0.98rem;
  color: rgba(255, 255, 255, 0.95);
  line-height: 1.65;
  font-weight: 400;
  max-width: 640px;
}

.commitment-mockup-lead strong {
  color: #ffffff;
  font-weight: 700;
}

.commitment-mockup-body {
  font-family: var(--font-body);
  font-size: 0.98rem;
  font-weight: 400;
  color: rgba(226, 232, 240, 0.90);
  line-height: 1.62;
  max-width: 640px;
}

/* Right Side Image Area (Website-Related Visual, Not Mobile!) */
.commitment-visual-col {
  position: relative;
  overflow: hidden;
  min-height: 420px;
  z-index: 2;
}

.commitment-visual-img {
  width: 100%;
  height: 100%;
  min-height: 100%;
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
  background: linear-gradient(to right, rgba(6, 43, 85, 0.95) 0%, rgba(6, 43, 85, 0.45) 20%, transparent 55%),
              linear-gradient(to top, rgba(6, 43, 85, 0.40) 0%, transparent 35%);
  pointer-events: none;
}

/* Trust Badge Pill */
.commitment-badge-pill {
  position: absolute;
  bottom: 1.85rem;
  right: 1.85rem;
  background: rgba(6, 43, 85, 0.88);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.22);
  border-radius: 50px;
  padding: 0.65rem 1.35rem;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  color: #ffffff;
  font-family: var(--font-heading);
  font-size: 0.84rem;
  font-weight: 600;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.30);
  z-index: 4;
}

.commitment-badge-pill .text-orange {
  color: var(--accent-orange) !important;
  font-size: 1.1rem;
}

@media (max-width: 991.98px) {
  .commitment-mockup-section {
    padding: 3.8rem 0;
  }

  .commitment-content-col {
    padding: 3rem 2rem 2.5rem;
  }

  .commitment-visual-col {
    min-height: 320px;
  }

  .commitment-visual-blend-overlay {
    background: linear-gradient(to bottom, rgba(6, 43, 85, 0.90) 0%, transparent 40%);
  }

  .commitment-badge-pill {
    bottom: 1.25rem;
    right: 1.25rem;
    padding: 0.5rem 1rem;
    font-size: 0.78rem;
  }
}

@media (max-width: 575.98px) {
  .commitment-banner-card {
    border-radius: 18px;
  }

  .commitment-content-col {
    padding: 2.25rem 1.35rem 2rem;
  }

  .commitment-visual-col {
    min-height: 260px;
  }

  .commitment-mockup-title {
    font-size: 1.85rem;
  }
}'''

# Replace section F in css/style.css
css_new, n_css = re.subn(
    r'/\* =+\s*F\. Our Commitment Section.*?(?=/\* =+\s*G\. Contact)',
    commitment_css_replacement.strip() + '\n\n\n',
    css,
    flags=re.DOTALL
)

print(f"Replaced in css/style.css: {n_css} occurrence(s)")
if n_css == 1:
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css_new)
    print("Saved css/style.css successfully.")
else:
    print("Error: Could not match Section F in css/style.css")
