with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# Check brand-logo-img rule
m = re.search(r'\.brand-logo-img\s*\{([^}]+)\}', css)
if m:
    print("Current .brand-logo-img:")
    print(m.group(0))

m_scrolled = re.search(r'\.navbar-corporate\.scrolled \.brand-logo-img\s*\{([^}]+)\}', css)
if m_scrolled:
    print("\nCurrent .navbar-corporate.scrolled .brand-logo-img:")
    print(m_scrolled.group(0))

m_footer = re.search(r'\.footer-logo-img\s*\{([^}]+)\}', css)
if m_footer:
    print("\nCurrent .footer-logo-img:")
    print(m_footer.group(0))
