import re

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

refined_commitment_css = '''/* ==========================================================================
   F. Our Commitment Section (Sleek Horizontal Procurement Banner)
   ========================================================================== */
.commitment-mockup-section {
  padding: 3.25rem 0 3.5rem;
  background-color: #f8fafc;
  position: relative;
  border-bottom: 1px solid rgba(6, 43, 85, 0.06);
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

/* Eyebrow: Brand Orange Dash & Crisp White Text */
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

/* Main Heading */
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

/* Narrative Body Copy (0.98rem / 400 Weight Site-Wide Standard) */
.commitment-mockup-lead {
  font-family: var(--font-body);
  font-size: 0.98rem;
  color: rgba(255, 255, 255, 0.95);
  line-height: 1.6;
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

/* Trust Badge Pill */
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
  .commitment-mockup-section {
    padding: 2.75rem 0;
  }

  .commitment-content-col {
    padding: 2.25rem 1.75rem 2rem;
  }

  .commitment-visual-col {
    min-height: 260px;
  }

  .commitment-visual-blend-overlay {
    background: linear-gradient(to bottom, rgba(16, 75, 148, 0.85) 0%, transparent 40%);
  }

  .commitment-badge-pill {
    bottom: 1rem;
    right: 1rem;
    padding: 0.45rem 0.95rem;
    font-size: 0.75rem;
  }
}

@media (max-width: 575.98px) {
  .commitment-banner-card {
    border-radius: 16px;
  }

  .commitment-content-col {
    padding: 1.85rem 1.25rem 1.65rem;
  }

  .commitment-visual-col {
    min-height: 220px;
  }

  .commitment-mockup-title {
    font-size: 1.75rem;
  }
}'''

# Replace Section F in css/style.css
css_new, n_css = re.subn(
    r'/\* =+\s*F\. Our Commitment Section.*?(?=/\* =+\s*G\. Contact)',
    refined_commitment_css.strip() + '\n\n\n',
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
