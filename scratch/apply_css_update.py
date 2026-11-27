import re

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_replacement = '''/* ==========================================================================
   E. Our Clients - Institutional Showcase Carousel
   ========================================================================== */
.clients-section {
  padding: 4.8rem 0 5.2rem;
  background-color: #ffffff;
  position: relative;
  border-bottom: 1px solid rgba(6, 43, 85, 0.06);
}

/* Eyebrow - Unified Brand Dash Style */
.clients-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 10px;
}

.clients-eyebrow-dash {
  width: 24px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.clients-eyebrow-text {
  font-family: var(--font-heading);
  font-size: 0.80rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--accent-orange);
}

.clients-section-title {
  font-family: var(--font-heading);
  font-size: clamp(1.85rem, 2.6vw, 2.35rem);
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.25;
  letter-spacing: -0.02em;
  max-width: 840px;
  margin-left: auto;
  margin-right: auto;
}

.clients-title-accent {
  width: 40px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
}

.clients-section-subtitle {
  font-family: var(--font-body);
  font-size: 0.98rem;
  font-weight: 400;
  color: var(--text-grey);
  line-height: 1.6;
  max-width: 780px;
}

/* Client Logos Carousel Viewport & Track */
.clients-carousel-container {
  max-width: 1140px;
  margin: 0 auto;
}

.clients-carousel-viewport {
  overflow: hidden;
  width: 100%;
  padding: 1rem 0;
  position: relative;
  mask-image: linear-gradient(to right, transparent, black 6%, black 94%, transparent);
  -webkit-mask-image: linear-gradient(to right, transparent, black 6%, black 94%, transparent);
}

.clients-carousel-track {
  display: flex;
  align-items: center;
  gap: 1.85rem;
  width: max-content;
  will-change: transform;
}

/* Client Logo Card (Matching Image 2 Rounded Reference Card) */
.client-logo-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 18px;
  box-shadow: 0 4px 18px rgba(6, 43, 85, 0.04), 0 1px 3px rgba(6, 43, 85, 0.02);
  padding: 1.5rem 2rem;
  width: clamp(320px, 34vw, 420px);
  flex-shrink: 0;
  display: flex;
  align-items: center;
  gap: 1.35rem;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  cursor: pointer;
  user-select: none;
}

.client-logo-card:hover {
  transform: translateY(-6px);
  border-color: rgba(255, 121, 0, 0.45);
  box-shadow: 0 14px 34px rgba(6, 43, 85, 0.10), 0 3px 8px rgba(6, 43, 85, 0.04);
}

.client-card-symbol-wrap {
  width: 72px;
  height: 72px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f8fafc;
  border: 1px solid #edf2f7;
  border-radius: 14px;
  padding: 0.45rem;
  transition: all 0.3s ease;
}

.client-logo-card:hover .client-card-symbol-wrap {
  background: #ffffff;
  border-color: rgba(255, 121, 0, 0.25);
  box-shadow: 0 4px 12px rgba(6, 43, 85, 0.06);
}

.client-card-logo-img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  transition: transform 0.3s ease;
}

.client-logo-card:hover .client-card-logo-img {
  transform: scale(1.08);
}

.client-card-details {
  display: flex;
  flex-direction: column;
}

.client-card-badge {
  display: inline-block;
  font-family: var(--font-heading);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--accent-orange);
  margin-bottom: 0.25rem;
}

.client-card-name {
  font-family: var(--font-heading);
  font-size: 1.35rem;
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.22;
  margin-bottom: 0.2rem;
  transition: color 0.25s ease;
}

.client-logo-card:hover .client-card-name {
  color: var(--accent-orange);
}

.client-card-location {
  font-family: var(--font-body);
  font-size: 0.90rem;
  font-weight: 400;
  color: var(--text-grey);
  line-height: 1.4;
  margin-bottom: 0;
}

/* Centered Carousel Indicator Dots */
.clients-carousel-dots {
  margin-top: 1.85rem;
}

.client-carousel-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: #cbd5e1;
  border: none;
  padding: 0;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  cursor: pointer;
}

.client-carousel-dot:hover {
  background-color: #94a3b8;
}

.client-carousel-dot.active {
  width: 32px;
  border-radius: 6px;
  background-color: var(--accent-orange);
  box-shadow: 0 2px 8px rgba(255, 121, 0, 0.35);
}

@media (max-width: 991.98px) {
  .clients-carousel-viewport {
    mask-image: none;
    -webkit-mask-image: none;
  }

  .client-logo-card {
    width: clamp(290px, 45vw, 360px);
    padding: 1.25rem 1.5rem;
    gap: 1.15rem;
  }

  .client-card-symbol-wrap {
    width: 62px;
    height: 62px;
  }

  .client-card-name {
    font-size: 1.2rem;
  }
}

@media (max-width: 575.98px) {
  .client-logo-card {
    width: 285px;
    padding: 1.15rem 1.25rem;
    gap: 1rem;
    border-radius: 16px;
  }

  .client-card-symbol-wrap {
    width: 54px;
    height: 54px;
  }

  .client-card-name {
    font-size: 1.12rem;
  }

  .client-card-location {
    font-size: 0.85rem;
  }
}'''

css_new, n_css = re.subn(
    r'/\* =+\s*E\. Our Clients - Institutional Showcase.*?\*/\s*\.clients-section\s*\{.*?\.client-cred-scope i\s*\{[^\}]+\}',
    css_replacement.strip(),
    css,
    flags=re.DOTALL
)

print(f"Replaced in css/style.css: {n_css} occurrence(s)")
if n_css == 1:
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css_new)
    print("Saved css/style.css successfully.")
else:
    print("Error: Could not match CSS block")
