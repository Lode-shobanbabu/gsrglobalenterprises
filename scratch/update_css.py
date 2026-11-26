with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update Header / Navbar Styles
old_header_start = '/* ==========================================================================\n   Main Navigation Bar - Transparent Dark Glass (Cyberguard Reference)\n   ========================================================================== */'
old_header_end = '/* ==========================================================================\n   Floating Glass Cards matching Cyberguard 99.9% Threat detection style'

# Let's find navbar section
nav_idx_start = css.find('/* ==========================================================================\n   Main Navigation Bar')
nav_idx_end = css.find('/* ==========================================================================\n   A. Hero Section')

if nav_idx_start == -1 or nav_idx_end == -1:
    print(f"Error: Navbar markers not found (start={nav_idx_start}, end={nav_idx_end})")
    exit(1)

new_navbar = '''/* ==========================================================================
   Main Navigation Bar - Clean Corporate Header (ConnexHire Reference Style)
   ========================================================================== */
header.sticky-top {
  position: sticky;
  top: 0;
  z-index: 1030;
  background: #ffffff;
}

.navbar-corporate {
  background-color: #ffffff;
  border-bottom: 1px solid rgba(1, 30, 74, 0.08);
  box-shadow: 0 2px 14px rgba(1, 30, 74, 0.05);
  padding: 0.85rem 0;
  transition: all 0.3s ease;
}

.navbar-corporate.scrolled {
  background-color: rgba(255, 255, 255, 0.98);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  box-shadow: 0 6px 24px rgba(1, 30, 74, 0.09);
  border-bottom-color: rgba(1, 30, 74, 0.12);
  padding: 0.6rem 0;
}

.brand-container {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  text-decoration: none;
  transition: transform 0.25s ease;
}

.brand-container:hover {
  transform: translateY(-1px);
}

.brand-logo-img {
  height: 52px;
  width: auto;
  max-width: 250px;
  object-fit: contain;
  display: block;
  transition: transform 0.25s ease, height 0.25s ease;
}

.navbar-corporate.scrolled .brand-logo-img {
  height: 46px;
}

.navbar-corporate .navbar-nav {
  gap: 1.5rem;
  align-items: center;
}

.navbar-corporate .nav-link {
  font-size: 1rem;
  font-weight: 600;
  color: var(--navy-900);
  padding: 0.5rem 0.75rem;
  position: relative;
  transition: all 0.2s ease;
  letter-spacing: 0.01em;
}

.navbar-corporate .nav-link:hover {
  color: var(--brand-orange);
}

.navbar-corporate .nav-link.active {
  color: var(--brand-orange);
  font-weight: 700;
}

.navbar-corporate .nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 2.5px;
  background: var(--brand-orange);
  transition: width 0.25s ease;
  border-radius: 2px;
}

.navbar-corporate .nav-link:hover::after,
.navbar-corporate .nav-link.active::after {
  width: 65%;
}

/* Rounded Dark Pill CTA Button (ConnexHire Reference Style) */
.header-cta-pill {
  background: var(--navy-900);
  color: #ffffff;
  font-family: var(--font-body);
  font-weight: 700;
  font-size: 0.92rem;
  padding: 0.65rem 1.65rem;
  border-radius: 50px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 14px rgba(1, 30, 74, 0.25);
  border: 1.5px solid transparent;
}

.header-cta-pill:hover {
  background: var(--brand-orange);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 118, 0, 0.4);
}

'''

css = css[:nav_idx_start] + new_navbar + css[nav_idx_end:]

# 2. Update Hero Section Styles
hero_idx_start = css.find('/* ==========================================================================\n   A. Hero Section')
hero_idx_end = css.find('/* ==========================================================================\n   B. About Us Section')

if hero_idx_start == -1 or hero_idx_end == -1:
    print(f"Error: Hero markers not found (start={hero_idx_start}, end={hero_idx_end})")
    exit(1)

new_hero_css = '''/* ==========================================================================
   A. Hero Section - Cinematic Boardroom Photography (ConnexHire Reference Style)
   ========================================================================== */
.hero-section {
  position: relative;
  min-height: clamp(560px, 80vh, 720px);
  background: linear-gradient(135deg, rgba(1, 30, 74, 0.90) 0%, rgba(1, 30, 74, 0.72) 55%, rgba(7, 39, 92, 0.88) 100%),
              url('../assets/images/hero-boardroom.webp') center/cover no-repeat;
  color: var(--white);
  display: flex;
  align-items: center;
  overflow: hidden;
  padding: 4.8rem 0;
}

.hero-content-col {
  position: relative;
  z-index: 3;
}

.hero-status-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 18px;
  border-radius: 50px;
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.22);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  margin-bottom: 1.25rem;
  font-size: 0.85rem;
  font-weight: 600;
  color: #f8fafc;
  letter-spacing: 0.03em;
}

.hero-main-title {
  font-family: var(--font-heading);
  font-size: clamp(2.2rem, 4vw, 3.85rem);
  font-weight: 800;
  line-height: 1.14;
  letter-spacing: -0.025em;
  color: #ffffff;
  margin-bottom: 1.35rem;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.45);
}

.hero-title-highlight {
  color: var(--brand-orange);
  display: inline;
}

.hero-lead-desc {
  font-size: clamp(1rem, 1.2vw, 1.15rem);
  color: #e2e8f0;
  line-height: 1.65;
  max-width: 680px;
  margin-bottom: 2.2rem;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.35);
}

.hero-action-row {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  flex-wrap: wrap;
  margin-bottom: 2.5rem;
}

.btn-hero-action {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  background: var(--brand-orange);
  color: #ffffff;
  font-weight: 700;
  font-size: 0.98rem;
  padding: 0.75rem 1.65rem;
  border-radius: 50px;
  text-decoration: none;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 20px rgba(255, 118, 0, 0.45);
}

.btn-hero-action:hover {
  background: var(--brand-orange-hover);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 8px 28px rgba(255, 118, 0, 0.6);
}

.btn-hero-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #ffffff;
  color: var(--brand-orange);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.95rem;
  font-weight: 800;
  transition: transform 0.25s ease;
}

.btn-hero-action:hover .btn-hero-circle {
  transform: translateX(3px);
}

.btn-hero-outline {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff;
  font-weight: 700;
  font-size: 0.98rem;
  padding: 0.75rem 1.65rem;
  border-radius: 50px;
  border: 1.5px solid rgba(255, 255, 255, 0.35);
  backdrop-filter: blur(10px);
  text-decoration: none;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.btn-hero-outline:hover {
  background: rgba(255, 255, 255, 0.25);
  color: #ffffff;
  border-color: #ffffff;
  transform: translateY(-2px);
}

/* Sourcing Verticals Strip */
.hero-sectors-strip {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
  padding-top: 1.25rem;
  border-top: 1px solid rgba(255, 255, 255, 0.18);
}

.hero-sector-tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 0.88rem;
  font-weight: 600;
  color: #f1f5f9;
  background: rgba(1, 30, 74, 0.55);
  border: 1px solid rgba(255, 255, 255, 0.18);
  padding: 6px 16px;
  border-radius: 30px;
  backdrop-filter: blur(8px);
  transition: background 0.2s ease, border-color 0.2s ease;
}

.hero-sector-tag:hover {
  background: rgba(1, 30, 74, 0.8);
  border-color: var(--brand-orange);
}

.text-orange {
  color: var(--brand-orange) !important;
}

.bg-orange {
  background-color: var(--brand-orange) !important;
}

@media (max-width: 991.98px) {
  .hero-section {
    padding: 3.8rem 0;
    min-height: auto;
  }
  .navbar-collapse {
    background: #ffffff;
    border-radius: 10px;
    padding: 1.25rem;
    margin-top: 0.75rem;
    border: 1px solid rgba(1, 30, 74, 0.1);
    box-shadow: 0 10px 30px rgba(1, 30, 74, 0.12);
  }
}

@media (max-width: 575.98px) {
  .hero-main-title {
    font-size: 2.1rem;
  }
  .hero-action-row {
    flex-direction: column;
    align-items: stretch;
  }
  .btn-hero-action,
  .btn-hero-outline {
    justify-content: center;
    width: 100%;
  }
}

'''

css = css[:hero_idx_start] + new_hero_css + css[hero_idx_end:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/style.css navbar and hero styles successfully!")
