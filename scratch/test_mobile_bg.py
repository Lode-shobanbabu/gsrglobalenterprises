import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

test_css = """
@media (max-width: 991.98px) {
  .top-utility-bar {
    display: none !important;
  }

  .hero-section {
    min-height: auto !important;
    background-image: url('assets/images/hero-mobile.webp') !important;
    background-position: center center !important;
    background-size: cover !important;
    background-repeat: no-repeat !important;
    background-color: #0b1e36 !important;
    padding: 3.5rem 0 4rem !important;
  }

  .hero-section::before {
    background: linear-gradient(180deg,
        rgba(4, 21, 43, 0.76) 0%,
        rgba(4, 21, 43, 0.65) 60%,
        rgba(4, 21, 43, 0.45) 100%) !important;
  }

  .hero-main-title {
    color: #ffffff !important;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.35);
  }

  .hero-lead-desc {
    color: rgba(255, 255, 255, 0.94) !important;
    text-shadow: 0 1px 4px rgba(0, 0, 0, 0.3);
  }

  .hero-sub-desc {
    color: rgba(255, 255, 255, 0.88) !important;
    text-shadow: 0 1px 4px rgba(0, 0, 0, 0.3);
  }
}

@media (max-width: 575.98px) {
  .hero-section {
    padding: 2.8rem 0 3.2rem !important;
  }

  .hero-main-title {
    font-size: clamp(1.4rem, 5.8vw, 1.7rem) !important;
    line-height: 1.25 !important;
    margin-bottom: 0.85rem !important;
  }

  .hero-lead-desc {
    font-size: 0.92rem !important;
    line-height: 1.55 !important;
    margin-bottom: 0.65rem !important;
  }

  .hero-sub-desc {
    font-size: 0.88rem !important;
    line-height: 1.5 !important;
    margin-bottom: 1.25rem !important;
  }

  .hero-action-row {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    gap: 0.65rem;
  }

  .btn-hero-primary,
  .btn-hero-secondary {
    width: 100%;
    justify-content: center;
    text-align: center;
    padding: 0.72rem 1.25rem;
  }
}
"""

print("Test CSS snippet ready")
