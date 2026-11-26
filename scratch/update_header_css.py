with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

start_marker = '/* ==========================================================================\n   Top Corporate Utility Bar'
end_marker = '/* ==========================================================================\n   A. Hero Section'

idx_start = css.find(start_marker)
idx_end = css.find(end_marker)

if idx_start == -1 or idx_end == -1:
    print(f"Error finding markers: start={idx_start}, end={idx_end}")
    exit(1)

new_header_css = '''/* ==========================================================================
   Top Corporate Utility Bar (Exact Reference Design Matching Screenshot 1)
   ========================================================================== */
.top-utility-bar {
  background-color: var(--primary-navy);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.82rem;
  color: #e2e8f0;
  padding: 0.45rem 0;
  position: relative;
  z-index: 1031;
}

.topbar-contact-item {
  color: #e2e8f0;
  text-decoration: none;
  font-weight: 500;
  font-size: 0.82rem;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: color 0.2s ease;
}

.topbar-contact-item i {
  color: #ffffff;
  font-size: 0.82rem;
}

.topbar-contact-item:hover {
  color: #ffffff;
}

.topbar-v-pipe {
  color: rgba(255, 255, 255, 0.35);
  user-select: none;
  margin: 0 4px;
}

.topbar-location-item {
  color: #e2e8f0;
  font-weight: 500;
  font-size: 0.82rem;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.topbar-location-item i {
  color: #ffffff;
  font-size: 0.82rem;
}

/* White Circle Social Buttons on Top Right (Matching Screenshot 1) */
.topbar-social-btn {
  width: 25px;
  height: 25px;
  border-radius: 50%;
  background-color: #ffffff;
  color: var(--primary-navy);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.72rem;
  text-decoration: none;
  transition: transform 0.2s ease, background-color 0.2s ease, color 0.2s ease;
}

.topbar-social-btn:hover {
  background-color: var(--accent-orange);
  color: #ffffff;
  transform: scale(1.12);
}

/* ==========================================================================
   Main Navigation Bar (Exact Reference Design Matching Screenshot 1 & 2)
   ========================================================================== */
header.sticky-top {
  position: sticky;
  top: 0;
  z-index: 1030;
  background: #ffffff;
}

.navbar-corporate {
  background-color: #ffffff;
  border-bottom: 1px solid rgba(6, 43, 85, 0.08);
  box-shadow: 0 2px 14px rgba(6, 43, 85, 0.04);
  padding: 0.85rem 0;
  transition: all 0.3s ease;
}

.navbar-corporate.scrolled {
  background-color: rgba(255, 255, 255, 0.98);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  box-shadow: 0 6px 24px rgba(6, 43, 85, 0.08);
  border-bottom-color: rgba(6, 43, 85, 0.12);
  padding: 0.55rem 0;
}

.brand-container {
  display: flex;
  align-items: center;
  text-decoration: none;
  transition: transform 0.25s ease;
}

.brand-container:hover {
  transform: translateY(-1px);
}

.brand-logo-img {
  height: 52px;
  width: auto;
  max-width: 255px;
  object-fit: contain;
  display: block;
  transition: transform 0.25s ease, height 0.25s ease;
}

.navbar-corporate.scrolled .brand-logo-img {
  height: 46px;
}

@media (max-width: 575.98px) {
  .brand-logo-img {
    height: 40px;
    max-width: 195px;
  }
}

.navbar-corporate .navbar-nav {
  gap: 1.85rem;
  align-items: center;
}

.navbar-corporate .nav-link {
  font-family: var(--font-heading);
  font-size: 0.94rem;
  font-weight: 600;
  color: var(--primary-navy);
  padding: 0.4rem 0.2rem;
  position: relative;
  transition: color 0.2s ease;
  letter-spacing: 0.01em;
}

.navbar-corporate .nav-link:hover,
.navbar-corporate .nav-link.active {
  color: var(--primary-navy);
}

/* Active Orange Underline Bar (Exact Reference Indicator Under Home) */
.navbar-corporate .nav-link::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 3px;
  background-color: var(--accent-orange);
  transition: width 0.25s ease;
  border-radius: 2px;
}

.navbar-corporate .nav-link:hover::after,
.navbar-corporate .nav-link.active::after {
  width: 32px;
}

/* Orange Pill CTA Button: Request a Quote -> (Exact Reference Style) */
.header-cta-orange {
  background-color: var(--accent-orange);
  color: #ffffff;
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 0.92rem;
  padding: 0.62rem 1.65rem;
  border-radius: 50px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 14px rgba(255, 121, 0, 0.35);
  border: none;
  white-space: nowrap;
}

.header-cta-orange:hover {
  background-color: var(--brand-orange-hover);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 121, 0, 0.45);
}

.header-cta-orange i {
  font-size: 0.95rem;
  transition: transform 0.2s ease;
}

.header-cta-orange:hover i {
  transform: translateX(3px);
}

'''

css = css[:idx_start] + new_header_css + css[idx_end:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/style.css successfully!")
