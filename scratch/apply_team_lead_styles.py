with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Replace :root and Base / Typography (up to top-utility-bar)
root_start = '/* ==========================================================================\n   GSR GLOBAL ENTERPRISES'
topbar_start = '/* ==========================================================================\n   Top Corporate Utility Bar'

idx_root = css.find(root_start)
idx_topbar = css.find(topbar_start)

if idx_root == -1 or idx_topbar == -1:
    print(f"Error finding root/topbar markers: idx_root={idx_root}, idx_topbar={idx_topbar}")
    exit(1)

new_root_and_base = '''/* ==========================================================================
   GSR GLOBAL ENTERPRISES - Corporate Design System
   Configured to Team Lead & Official Brand Guidelines
   ========================================================================== */

:root {
  /* 1. Primary Navy Blue (#062B55): Headers, footer, buttons */
  --primary-navy: #062b55;
  --navy-950: #021226;
  --navy-900: #062b55;
  --navy-850: #093466;
  --navy-800: #0d3d70;
  --navy-700: #124c8a;
  --navy-600: #1a5ea8;

  /* 2. Secondary Blue (#0D3D70): Gradients, section backgrounds */
  --secondary-blue: #0d3d70;
  --secondary-blue-dark: #08294d;
  --secondary-blue-light: #164f8f;

  /* 3. Accent Orange (#FF7900): CTA buttons, highlights */
  --accent-orange: #ff7900;
  --brand-orange: #ff7900;
  --brand-orange-hover: #ff8e26;
  --brand-orange-dark: #e66d00;
  --orange-500: #ff7900;
  --orange-400: #ff8e26;
  --orange-300: #ffa552;
  --orange-200: #ffc999;
  --orange-100: #ffe8d1;
  --orange-gradient: linear-gradient(135deg, #ff7900 0%, #ff9633 100%);
  --orange-gradient-hover: linear-gradient(135deg, #e66d00 0%, #ff7900 100%);
  --orange-glow: rgba(255, 121, 0, 0.35);

  /* Mapped Brand Accent Variables for Site-Wide Theme Harmony */
  --gold-600: #d96700;
  --gold-500: #ff7900;
  --gold-400: #ff8e26;
  --gold-300: #ffa552;
  --gold-200: #ffc999;
  --gold-100: #ffe8d1;
  --gold-gradient: linear-gradient(135deg, #ff7900 0%, #ff9633 100%);
  --gold-gradient-hover: linear-gradient(135deg, #e66d00 0%, #ff7900 100%);
  --gold-glow: rgba(255, 121, 0, 0.35);

  /* 4. Light Background (#F4F8FC): Alternate sections */
  --bg-light: #f4f8fc;
  --section-alt-bg: #f4f8fc;

  /* 5. White (#FFFFFF): Main background, cards */
  --white: #ffffff;
  --card-bg: #ffffff;
  --bg-main: #ffffff;

  /* 6. Text Grey (#555B63): Body text, descriptions */
  --text-grey: #555b63;
  --slate-700: #3b3f45;
  --slate-600: #555b63;
  --slate-500: #555b63;
  --slate-400: #7b838f;
  --slate-300: #cbd5e1;
  --slate-200: #e2e8f0;
  --slate-100: #f4f8fc;
  --slate-50: #f8fafc;

  --border-light: rgba(226, 232, 240, 0.85);
  --border-dark: rgba(255, 255, 255, 0.1);

  /* 7. Typography (Team Lead Specification) */
  /* Headings: Poppins 600 / 700 */
  --font-heading: 'Poppins', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  /* Body: Open Sans 400 / 500 / 600 */
  --font-body: 'Open Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;

  /* Refined Corporate Shadows */
  --shadow-sm: 0 2px 4px rgba(6, 43, 85, 0.04);
  --shadow-md: 0 4px 16px rgba(6, 43, 85, 0.06);
  --shadow-lg: 0 12px 32px rgba(6, 43, 85, 0.08);
  --shadow-xl: 0 20px 48px rgba(6, 43, 85, 0.12);

  /* Transitions */
  --transition-fast: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-base: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

/* ==========================================================================
   Base & Reset
   ========================================================================== */
*,
*::before,
*::after {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
  scroll-padding-top: 86px;
  background-color: var(--white);
}

body {
  font-family: var(--font-body);
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.68;
  color: var(--text-grey);
  background-color: var(--white);
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

h1,
h2,
h3,
h4,
h5,
h6,
.font-heading {
  font-family: var(--font-heading);
  color: var(--primary-navy);
  font-weight: 700;
  line-height: 1.25;
  letter-spacing: -0.015em;
}

p,
.lead {
  color: var(--text-grey);
}

a {
  color: var(--accent-orange);
  text-decoration: none;
  transition: var(--transition-fast);
}

a:hover {
  color: var(--brand-orange-hover);
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: var(--bg-light);
}

::-webkit-scrollbar-thumb {
  background: var(--secondary-blue);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: var(--accent-orange);
}

'''

css = css[:idx_root] + new_root_and_base + css[idx_topbar:]

# 2. Update Top Utility Bar Background to Primary Navy #062B55
css = css.replace('.top-utility-bar {\n  background-color: #020612;', '.top-utility-bar {\n  background-color: var(--primary-navy);')

# 3. Update Hero Section background gradient to use #062B55 and #0D3D70
old_hero_bg = "background: linear-gradient(135deg, rgba(1, 30, 74, 0.90) 0%, rgba(1, 30, 74, 0.72) 55%, rgba(7, 39, 92, 0.88) 100%),\n              url('../assets/images/hero-boardroom.webp') center/cover no-repeat;"
new_hero_bg = "background: linear-gradient(135deg, rgba(6, 43, 85, 0.92) 0%, rgba(13, 61, 112, 0.78) 55%, rgba(6, 43, 85, 0.90) 100%),\n              url('../assets/images/hero-boardroom.webp') center/cover no-repeat;"
css = css.replace(old_hero_bg, new_hero_bg)

# 4. Update Services section background to #F4F8FC
css = css.replace('.services-section {\n  padding: 4.85rem 0;\n  background-color: var(--slate-50);', '.services-section {\n  padding: 4.85rem 0;\n  background-color: var(--bg-light);')

# 5. Update FAQ section background to #F4F8FC
old_faq_bg = ".faq-section {\n  padding: 4.85rem 0;\n  background: linear-gradient(180deg, #f8fafc 0%, #ffffff 50%, #f8fafc 100%);"
new_faq_bg = ".faq-section {\n  padding: 4.85rem 0;\n  background-color: var(--bg-light);"
css = css.replace(old_faq_bg, new_faq_bg)

# 6. Update Footer background to Primary Navy #062B55 and Secondary Blue #0D3D70
old_footer_bg = ".footer-corporate {\n  background: radial-gradient(ellipse 90% 60% at 50% 0%, #0c2044 0%, #050d1a 100%);"
new_footer_bg = ".footer-corporate {\n  background: radial-gradient(ellipse 90% 60% at 50% 0%, #0d3d70 0%, #062b55 100%);"
css = css.replace(old_footer_bg, new_footer_bg)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied Team Lead design guidelines successfully!")
