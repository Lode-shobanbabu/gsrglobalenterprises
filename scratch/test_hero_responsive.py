import subprocess
import os
from PIL import Image

# Let's test a clean CSS implementation for the hero section
test_css = """
/* Desktop Hero (992px and up) */
.test-hero {
  position: relative;
  min-height: 480px;
  background-image: url('assets/images/hero-desktop.webp');
  background-repeat: no-repeat;
  background-position: right center;
  background-size: cover;
  background-color: #0d274c;
  display: flex;
  align-items: center;
  padding: 3rem 0;
  isolation: isolate;
  overflow: hidden;
}

.test-hero::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
  background: linear-gradient(90deg,
    rgba(255, 255, 255, 0.95) 0%,
    rgba(255, 255, 255, 0.90) 38%,
    rgba(255, 255, 255, 0.50) 58%,
    rgba(255, 255, 255, 0.05) 75%) !important;
}

/* Tablet (768px to 991px) */
@media (min-width: 768px) and (max-width: 991.98px) {
  .test-hero {
    min-height: auto;
    background-image: url('assets/images/hero-desktop.webp');
    background-position: center right;
    background-size: cover;
    padding: 3rem 0 3.5rem;
  }
  .test-hero::before {
    background: linear-gradient(90deg,
      rgba(255, 255, 255, 0.96) 0%,
      rgba(255, 255, 255, 0.92) 55%,
      rgba(255, 255, 255, 0.60) 75%,
      rgba(255, 255, 255, 0.20) 100%) !important;
  }
}

/* Mobile (under 768px) */
@media (max-width: 767.98px) {
  .test-hero {
    min-height: auto;
    background-image: url('assets/images/hero-mobile.webp') !important;
    background-position: center bottom !important;
    background-size: 100% auto !important;
    background-repeat: no-repeat !important;
    background-color: #f4f8fc !important;
    padding: 2.2rem 0 320px !important; /* leaves 320px for the beautiful mobile image */
  }
  
  .test-hero::before {
    background: linear-gradient(180deg,
      #f4f8fc 0%,
      #f4f8fc calc(100% - 340px),
      rgba(244, 248, 252, 0.85) calc(100% - 300px),
      rgba(244, 248, 252, 0) calc(100% - 240px)) !important;
  }
}
"""

print("Test script ready")
