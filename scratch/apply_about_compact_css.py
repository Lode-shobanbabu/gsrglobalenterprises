# scratch/apply_about_compact_css.py

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

c_start = '/* ==========================================================================\n   B. About Us Section'
c_end = '/* ==========================================================================\n   C. Services Section'

c_idx1 = css.find(c_start)
c_idx2 = css.find(c_end)

if c_idx1 == -1 or c_idx2 == -1:
    print(f"Error finding CSS markers: c_idx1={c_idx1}, c_idx2={c_idx2}")
    exit(1)

compact_about_css = '''/* ==========================================================================
   B. About Us Section - Compact Height Equal Left Image & Right Content
   ========================================================================== */
.about-section {
  padding: 3.2rem 0 3.5rem;
  background-color: #ffffff;
  position: relative;
  border-bottom: 1px solid rgba(6, 43, 85, 0.06);
}

/* Equal Height Left Image Container (Compact) */
.about-equal-media {
  position: relative;
  width: 100%;
  height: 100%;
  min-height: 380px;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 12px 36px rgba(6, 43, 85, 0.09);
  border: 1px solid rgba(6, 43, 85, 0.08);
  background-color: var(--primary-navy);
}

.about-equal-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.65s cubic-bezier(0.16, 1, 0.3, 1);
}

.about-equal-media:hover .about-equal-img {
  transform: scale(1.04);
}

/* Trust Pill on Image */
.about-img-trust-tag {
  position: absolute;
  bottom: 1.15rem;
  left: 1.15rem;
  background: rgba(6, 43, 85, 0.92);
  color: #ffffff;
  padding: 0.5rem 1rem;
  border-radius: 50px;
  font-family: var(--font-heading);
  font-size: 0.76rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 121, 0, 0.45);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.22);
}

.about-img-trust-tag i {
  color: var(--accent-orange);
  font-size: 0.9rem;
}

/* Right Content (Compact & Streamlined) */
.about-equal-content {
  padding-left: 0.5rem;
}

.about-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.about-eyebrow-dash {
  width: 22px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.about-eyebrow-text {
  font-family: var(--font-heading);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: var(--primary-navy);
}

.about-equal-title {
  font-family: var(--font-heading);
  font-size: clamp(1.55rem, 2.1vw, 1.95rem);
  font-weight: 700;
  color: var(--primary-navy);
  line-height: 1.22;
  letter-spacing: -0.02em;
}

.about-equal-p {
  font-family: var(--font-body);
  font-size: 0.88rem;
  color: #475569;
  line-height: 1.54;
  margin-bottom: 0.65rem;
}

.about-equal-p strong {
  color: var(--primary-navy);
  font-weight: 700;
}

/* CTA: Know More About Our Capabilities */
.btn-about-capabilities {
  background: var(--accent-orange);
  color: #ffffff;
  padding: 0.58rem 1.45rem;
  border-radius: 50px;
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  text-decoration: none;
  box-shadow: 0 3px 12px rgba(255, 121, 0, 0.28);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  border: none;
}

.btn-about-capabilities:hover {
  background: var(--brand-orange-hover);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 5px 16px rgba(255, 121, 0, 0.40);
}

.btn-about-capabilities i {
  transition: transform 0.2s ease;
}

.btn-about-capabilities:hover i {
  transform: translateX(3px);
}

/* Responsiveness */
@media (max-width: 991.98px) {
  .about-section {
    padding: 2.8rem 0;
  }

  .about-equal-media {
    min-height: 320px;
    height: 320px;
  }

  .about-equal-content {
    padding-left: 0;
    margin-top: 0.85rem;
  }
}

@media (max-width: 575.98px) {
  .about-equal-media {
    min-height: 260px;
    height: 260px;
  }

  .about-img-trust-tag {
    bottom: 0.85rem;
    left: 0.85rem;
    font-size: 0.70rem;
    padding: 0.4rem 0.8rem;
  }

  .btn-about-capabilities {
    width: 100%;
    justify-content: center;
  }
}

'''

css = css[:c_idx1] + compact_about_css + css[c_idx2:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/style.css with compact About section styles!")
