import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

single_bg_commitment_css = '''/* ==========================================================================
   F. Our Commitment Section (Full-Width Single Background Banner)
   ========================================================================== */
.commitment-mockup-section {
  padding: 0;
  margin: 0;
  width: 100%;
  position: relative;
  overflow: hidden;
  background-color: #125197;
  border-bottom: 1px solid rgba(6, 43, 85, 0.08);
  min-height: 340px;
  display: flex;
  align-items: center;
}

/* Single Full-Width Background Image Across Entire Section */
.commitment-single-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  pointer-events: none;
}

.commitment-single-bg img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center right;
  display: block;
  filter: saturate(1.15) contrast(1.05);
}

/* Lighter Blue Gradient Overlay on Left Side (Dissolves to Transparent on Right) */
.commitment-gradient-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(100deg, rgba(20, 88, 168, 0.92) 0%, rgba(28, 110, 198, 0.86) 45%, rgba(24, 98, 182, 0.58) 68%, rgba(18, 80, 155, 0.15) 85%, transparent 100%);
  z-index: 2;
  pointer-events: none;
}

/* Content Area - Aligned to Site Grid */
.commitment-content-wrap {
  position: relative;
  z-index: 3;
  padding: 3.5rem 3.5rem 3.5rem max(2rem, calc((100vw - 1280px) / 2 + 1rem));
  max-width: 820px;
}

/* Eyebrow: Brand Orange Dash & Crisp White Text */
.commitment-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 10px;
}

.commitment-eyebrow-dash {
  width: 24px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.commitment-eyebrow-text {
  font-family: var(--font-heading);
  font-size: 0.80rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #ffffff;
}

/* Main Heading */
.commitment-title {
  font-family: var(--font-heading);
  font-size: clamp(1.85rem, 2.7vw, 2.5rem);
  font-weight: 700;
  color: #ffffff;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

/* Narrative Body Copy (0.98rem / 400 Weight Site-Wide Standard) */
.commitment-text {
  font-family: var(--font-body);
  font-size: 0.98rem;
  font-weight: 400;
  color: rgba(255, 255, 255, 0.96);
  line-height: 1.62;
}

.commitment-text strong {
  color: #ffffff;
  font-weight: 700;
}

/* Our Promise Callout Badge */
.commitment-promise-pill {
  display: inline-flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  background: rgba(6, 43, 85, 0.75);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-radius: 50px;
  padding: 0.55rem 1.25rem;
  color: #ffffff;
  font-size: 0.92rem;
  margin-top: 0.5rem;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.20);
}

.commitment-promise-pill strong {
  color: #ffffff;
  font-weight: 700;
}

.commitment-promise-pill .promise-highlight {
  color: #f1f5f9;
  font-weight: 500;
}

.commitment-promise-pill .text-orange {
  color: var(--accent-orange) !important;
  font-size: 1.05rem;
}

@media (max-width: 991.98px) {
  .commitment-content-wrap {
    padding: 3rem 2rem 3rem max(1.5rem, calc((100vw - 1280px) / 2 + 1rem));
    max-width: 100%;
  }

  .commitment-gradient-overlay {
    background: linear-gradient(100deg, rgba(20, 88, 168, 0.94) 0%, rgba(28, 110, 198, 0.90) 60%, rgba(24, 98, 182, 0.75) 85%, rgba(18, 80, 155, 0.50) 100%);
  }

  .commitment-promise-pill {
    font-size: 0.85rem;
    padding: 0.5rem 1rem;
    border-radius: 12px;
  }
}

@media (max-width: 575.98px) {
  .commitment-content-wrap {
    padding: 2.5rem 1.25rem;
  }

  .commitment-title {
    font-size: 1.75rem;
  }

  .commitment-promise-pill {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 4px;
    border-radius: 12px;
  }
}'''

# Replace Section F in css/style.css
css_new, n_css = re.subn(
    r'/\* =+\s*F\. Our Commitment Section.*?(?=/\* =+\s*G\. Contact)',
    single_bg_commitment_css.strip() + '\n\n\n',
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
