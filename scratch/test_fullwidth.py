# Let's test the CSS for full-width edge-to-edge section
test_css = """
/* Full-Width Edge-to-Edge Commitment Banner */
.commitment-mockup-section {
  padding: 0;
  margin: 0;
  width: 100%;
  position: relative;
  overflow: hidden;
  background: #15589e;
}

.commitment-banner-wrapper {
  position: relative;
  width: 100%;
  overflow: hidden;
}

.commitment-banner-row {
  min-height: 340px;
}

/* Left Content Area */
.commitment-content-col {
  position: relative;
  z-index: 3;
  padding: 3.5rem 3rem 3.5rem max(2rem, calc((100vw - 1280px) / 2 + 1rem));
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* Lighter, Luminous Blue Gradient Overlay */
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
  opacity: 0.52;
  filter: saturate(1.15) contrast(1.05);
}

.commitment-left-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(100deg, rgba(20, 88, 168, 0.85) 0%, rgba(28, 110, 198, 0.78) 46%, rgba(24, 98, 182, 0.54) 75%, rgba(18, 80, 155, 0.10) 100%);
}

.commitment-radial-glow {
  position: absolute;
  top: 25%;
  left: 15%;
  width: 550px;
  height: 550px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(96, 175, 255, 0.38) 0%, transparent 65%);
  pointer-events: none;
}
"""
print("Full-width CSS ready")
