import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

fullwidth_commitment_css = '''/* ==========================================================================
   F. Our Commitment Section (Full-Width Edge-to-Edge Procurement Banner)
   ========================================================================== */
.commitment-mockup-section {
  padding: 0;
  margin: 0;
  width: 100%;
  position: relative;
  overflow: hidden;
  background-color: #125197;
  border-bottom: 1px solid rgba(6, 43, 85, 0.08);
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

/* Left Content Area - Full-Width Responsive Alignment */
.commitment-content-col {
  position: relative;
  z-index: 3;
  padding: 3.5rem 3.5rem 3.5rem max(2rem, calc((100vw - 1280px) / 2 + 1rem));
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* Left Background Image & Lighter Luminous Gradient Overlay */
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

/* Right Side Full-Bleed Image Area (Website-Related Visual, Not Mobile!) */
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

/* Trust Badge Pill */
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

@media (max-width: 991.98px) {
  .commitment-content-col {
    padding: 2.75rem 2rem 2.25rem;
  }

  .commitment-visual-col {
    min-height: 270px;
  }

  .commitment-visual-blend-overlay {
    background: linear-gradient(to bottom, rgba(22, 94, 180, 0.85) 0%, transparent 40%);
  }

  .commitment-badge-pill {
    bottom: 1rem;
    right: 1rem;
    padding: 0.45rem 1rem;
    font-size: 0.75rem;
  }
}

@media (max-width: 575.98px) {
  .commitment-content-col {
    padding: 2rem 1.25rem 1.75rem;
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
    fullwidth_commitment_css.strip() + '\n\n\n',
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
