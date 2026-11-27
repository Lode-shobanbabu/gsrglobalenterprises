# Let's inspect the exact styling for seamless right-side image blend
css_test = """
.commitment-mockup-section {
  padding: 5rem 0 5.5rem;
  background-color: #f8fafc;
  position: relative;
}

.commitment-banner-card {
  position: relative;
  border-radius: 24px;
  overflow: hidden;
  background: var(--primary-navy);
  box-shadow: 0 20px 50px rgba(6, 43, 85, 0.16);
  border: 1px solid rgba(6, 43, 85, 0.08);
}

.commitment-banner-row {
  min-height: 460px;
}

/* Left Content Area */
.commitment-content-col {
  position: relative;
  z-index: 3;
  padding: 4.5rem 3.5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* Background image & overlay on left */
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
  opacity: 0.28;
  filter: saturate(1.1);
}

.commitment-left-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(105deg, rgba(6, 43, 85, 0.98) 0%, rgba(6, 43, 85, 0.94) 50%, rgba(6, 43, 85, 0.72) 80%, rgba(6, 43, 85, 0.35) 100%);
}

.commitment-radial-glow {
  position: absolute;
  top: 20%;
  left: 10%;
  width: 480px;
  height: 480px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(19, 88, 157, 0.40) 0%, transparent 70%);
  pointer-events: none;
}

/* Right Side Image Area (Website-Related Visual, Not Mobile!) */
.commitment-visual-col {
  position: relative;
  overflow: hidden;
  min-height: 420px;
  z-index: 2;
}

.commitment-visual-img {
  width: 100%;
  height: 100%;
  min-height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.commitment-banner-card:hover .commitment-visual-img {
  transform: scale(1.03);
}

.commitment-visual-blend-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to right, rgba(6, 43, 85, 0.95) 0%, rgba(6, 43, 85, 0.50) 18%, transparent 50%),
              linear-gradient(to top, rgba(6, 43, 85, 0.40) 0%, transparent 35%);
  pointer-events: none;
}

.commitment-badge-pill {
  position: absolute;
  bottom: 1.85rem;
  right: 1.85rem;
  background: rgba(6, 43, 85, 0.88);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.22);
  border-radius: 50px;
  padding: 0.65rem 1.35rem;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  color: #ffffff;
  font-family: var(--font-heading);
  font-size: 0.84rem;
  font-weight: 600;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.30);
  z-index: 4;
}
"""
print("CSS test block ready")
