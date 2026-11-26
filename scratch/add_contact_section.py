import re

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

contact_section_html = """    <!-- ==========================================================================
         G. CONTACT / REQUEST A QUOTE (PRIMARY CONVERSION DUAL-TONE SECTION)
         ========================================================================== -->
    <section class="contact-quote-section" id="contact" aria-label="Contact and Request a Procurement Quote">
      <div class="container">

        <!-- Dual-Tone Split Master Card -->
        <div class="contact-quote-card fade-up-element">
          <div class="row g-0 align-items-stretch">

            <!-- Left Side: Dark Navy Contact Information (approx 42% width) -->
            <div class="col-lg-5 contact-dark-panel">
              <div class="contact-dark-inner">

                <!-- Eyebrow: Orange Dash + White Text -->
                <div class="contact-panel-eyebrow mb-3">
                  <span class="contact-panel-dash" aria-hidden="true"></span>
                  <span class="contact-panel-tag">CONTACT US</span>
                </div>

                <!-- Main Heading -->
                <h2 class="contact-panel-title mb-3">
                  Looking for a Reliable <span class="text-orange">Procurement Partner?</span>
                </h2>

                <!-- Lead Narrative -->
                <p class="contact-panel-desc mb-4">
                  Tell us what your business or project needs. Whether it's a single product requirement, bulk procurement or a large-scale institutional project, GSR Global Enterprises is ready to understand your requirements and explore the right sourcing solution.
                </p>

                <!-- Contact Info List -->
                <div class="contact-info-list">

                  <!-- Business Email -->
                  <div class="contact-info-item">
                    <div class="contact-icon-circle">
                      <i class="bi bi-envelope-fill"></i>
                    </div>
                    <div class="contact-info-details">
                      <span class="contact-info-label">Business Email</span>
                      <a href="mailto:gsrglobalenterprises@gmail.com" class="contact-info-link">
                        gsrglobalenterprises@gmail.com
                      </a>
                    </div>
                  </div>

                  <!-- Phone / WhatsApp -->
                  <div class="contact-info-item">
                    <div class="contact-icon-circle">
                      <i class="bi bi-telephone-fill"></i>
                    </div>
                    <div class="contact-info-details">
                      <span class="contact-info-label">Phone / WhatsApp</span>
                      <a href="tel:+917989635764" class="contact-info-link">
                        +91 7989635764
                      </a>
                    </div>
                  </div>

                  <!-- Office Address -->
                  <div class="contact-info-item">
                    <div class="contact-icon-circle">
                      <i class="bi bi-geo-alt-fill"></i>
                    </div>
                    <div class="contact-info-details">
                      <span class="contact-info-label">Office Address</span>
                      <span class="contact-info-text">
                        Visakhapatnam, Andhra Pradesh, India
                      </span>
                    </div>
                  </div>

                </div>

              </div>
            </div>

            <!-- Right Side: White Quote Request Form (approx 58% width) -->
            <div class="col-lg-7 contact-form-panel">
              <div class="contact-form-inner">

                <h3 class="quote-form-heading">Request a Procurement Quote</h3>
                <div class="quote-form-accent-line"></div>

                <form id="procurementQuoteForm" class="quote-form" novalidate>
                  <div class="row g-3">

                    <!-- Full Name -->
                    <div class="col-md-6">
                      <label for="quoteFullName" class="quote-form-label">Full Name</label>
                      <input type="text" class="form-control quote-form-control" id="quoteFullName" name="fullName"
                        placeholder="Enter your full name" required>
                    </div>

                    <!-- Company / Organization -->
                    <div class="col-md-6">
                      <label for="quoteCompany" class="quote-form-label">Company / Organization</label>
                      <input type="text" class="form-control quote-form-control" id="quoteCompany" name="company"
                        placeholder="Enter company name" required>
                    </div>

                    <!-- Email -->
                    <div class="col-md-6">
                      <label for="quoteEmail" class="quote-form-label">Email</label>
                      <input type="email" class="form-control quote-form-control" id="quoteEmail" name="email"
                        placeholder="name@company.com" required>
                    </div>

                    <!-- Contact Number -->
                    <div class="col-md-6">
                      <label for="quotePhone" class="quote-form-label">Contact Number</label>
                      <input type="tel" class="form-control quote-form-control" id="quotePhone" name="phone"
                        placeholder="Enter contact number" required>
                    </div>

                    <!-- Industry Dropdown -->
                    <div class="col-12">
                      <label for="quoteIndustry" class="quote-form-label">Industry</label>
                      <select class="form-select quote-form-select" id="quoteIndustry" name="industry" required>
                        <option value="" disabled selected>Select your industry</option>
                        <option value="medical">Medical &amp; Healthcare Supplies</option>
                        <option value="it">GCC &amp; IT Infrastructure</option>
                        <option value="education">Government &amp; Education Projects</option>
                        <option value="industrial">Industrial &amp; Manufacturing Supplies</option>
                        <option value="automotive">Automobile &amp; Transportation Supplies</option>
                        <option value="solar">Solar Energy Products</option>
                        <option value="other">General / Other Sourcing</option>
                      </select>
                    </div>

                    <!-- Submit Button -->
                    <div class="col-12 mt-4">
                      <button type="submit" class="btn-quote-submit" id="quoteSubmitBtn">
                        <span>Submit Your Enquiry</span>
                        <i class="bi bi-chevron-right ms-2"></i>
                      </button>
                    </div>

                  </div>

                  <!-- Form Feedback Alert (Hidden by default) -->
                  <div class="quote-form-alert d-none mt-3" id="quoteFormAlert">
                    <div class="alert alert-success d-flex align-items-center gap-2 mb-0" role="alert">
                      <i class="bi bi-check-circle-fill fs-5"></i>
                      <span>Thank you! Your procurement enquiry has been received. Our team will contact you shortly.</span>
                    </div>
                  </div>

                </form>

              </div>
            </div>

          </div>
        </div>

      </div>
    </section>"""

# Change footer id="contact" to id="footer" so id="contact" is uniquely for the new contact section
html = html.replace('<footer class="footer-corporate" id="contact"', '<footer class="footer-corporate" id="footer"')

# Insert the contact section right before </main>
if '</main>' in html:
    html = html.replace('</main>', contact_section_html + '\n\n  </main>')
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html updated with contact section.")
else:
    print("WARNING: Could not find </main> in index.html!")

# 2. Update css/style.css
contact_css = """
/* ==========================================================================
   G. Contact / Request a Quote (Primary Conversion Dual-Tone Section)
   ========================================================================== */
.contact-quote-section {
  padding: 5.5rem 0 6rem;
  background-color: #ffffff;
  position: relative;
}

.contact-quote-card {
  background: #ffffff;
  border-radius: 22px;
  box-shadow: 0 18px 48px rgba(6, 43, 85, 0.10);
  border: 1px solid rgba(6, 43, 85, 0.08);
  overflow: hidden;
}

/* Left Side: Dark Navy Panel */
.contact-dark-panel {
  background-color: var(--primary-navy);
  color: #ffffff;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.contact-dark-inner {
  padding: 3.5rem 2.85rem;
}

.contact-panel-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 12px;
}

.contact-panel-dash {
  width: 32px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  display: inline-block;
}

.contact-panel-tag {
  font-family: var(--font-heading);
  font-size: 0.80rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #e2e8f0;
}

.contact-panel-title {
  font-family: var(--font-heading);
  font-size: clamp(1.85rem, 2.5vw, 2.35rem);
  font-weight: 700;
  color: #ffffff;
  line-height: 1.22;
  letter-spacing: -0.02em;
}

.contact-panel-title .text-orange {
  color: var(--accent-orange);
  display: inline-block;
}

.contact-panel-desc {
  font-family: var(--font-body);
  font-size: 0.88rem;
  color: #cbd5e1;
  line-height: 1.62;
}

/* Contact Info Items */
.contact-info-list {
  display: flex;
  flex-direction: column;
  gap: 1.15rem;
}

.contact-info-item {
  display: flex;
  align-items: center;
  gap: 14px;
}

.contact-icon-circle {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background-color: var(--accent-orange);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(255, 121, 0, 0.35);
  transition: transform 0.25s ease;
}

.contact-info-item:hover .contact-icon-circle {
  transform: scale(1.08);
}

.contact-info-details {
  display: flex;
  flex-direction: column;
}

.contact-info-label {
  font-family: var(--font-heading);
  font-size: 0.72rem;
  font-weight: 600;
  color: #94a3b8;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.contact-info-link {
  font-family: var(--font-body);
  font-size: 0.90rem;
  font-weight: 500;
  color: #ffffff;
  text-decoration: none;
  transition: color 0.2s ease;
}

.contact-info-link:hover {
  color: var(--accent-orange);
}

.contact-info-text {
  font-family: var(--font-body);
  font-size: 0.90rem;
  font-weight: 500;
  color: #ffffff;
}

/* Right Side: Form Panel */
.contact-form-panel {
  background-color: #ffffff;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.contact-form-inner {
  padding: 3.5rem 3rem;
}

.quote-form-heading {
  font-family: var(--font-heading);
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--primary-navy);
  letter-spacing: -0.01em;
  margin-bottom: 0;
}

.quote-form-accent-line {
  width: 48px;
  height: 3px;
  background-color: var(--accent-orange);
  border-radius: 2px;
  margin-top: 8px;
  margin-bottom: 1.75rem;
}

.quote-form-label {
  font-family: var(--font-heading);
  font-size: 0.80rem;
  font-weight: 600;
  color: var(--primary-navy);
  margin-bottom: 0.35rem;
  display: block;
}

.quote-form-control,
.quote-form-select {
  background-color: #f1f5f9;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 0.72rem 1rem;
  font-family: var(--font-body);
  font-size: 0.88rem;
  color: #1e293b;
  transition: all 0.25s ease;
}

.quote-form-control:focus,
.quote-form-select:focus {
  background-color: #ffffff;
  border-color: var(--accent-orange);
  outline: none;
  box-shadow: 0 0 0 3px rgba(255, 121, 0, 0.15);
}

.quote-form-control::placeholder {
  color: #94a3b8;
  font-size: 0.86rem;
}

.btn-quote-submit {
  width: 100%;
  background-color: var(--accent-orange);
  color: #ffffff;
  border: none;
  border-radius: 50px;
  padding: 0.82rem 1.5rem;
  font-family: var(--font-heading);
  font-size: 0.90rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 18px rgba(255, 121, 0, 0.35);
  cursor: pointer;
}

.btn-quote-submit:hover {
  background-color: var(--brand-orange-hover);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(255, 121, 0, 0.45);
}

.btn-quote-submit i {
  font-size: 0.85rem;
  font-weight: 700;
  -webkit-text-stroke: 0.4px currentColor;
  transition: transform 0.2s ease;
}

.btn-quote-submit:hover i {
  transform: translateX(3px);
}

/* Responsive adjustments */
@media (max-width: 991.98px) {
  .contact-quote-section {
    padding: 3.5rem 0 4rem;
  }
  .contact-dark-inner {
    padding: 2.5rem 1.75rem;
  }
  .contact-form-inner {
    padding: 2.5rem 1.75rem;
  }
}

@media (max-width: 575.98px) {
  .contact-dark-inner {
    padding: 2rem 1.25rem;
  }
  .contact-form-inner {
    padding: 2rem 1.25rem;
  }
  .quote-form-heading {
    font-size: 1.35rem;
  }
}
"""

with open("css/style.css", "a", encoding="utf-8") as f:
    f.write(contact_css)

print("css/style.css appended with contact CSS.")

# 3. Update js/script.js to handle quote form
with open("js/script.js", "r", encoding="utf-8") as f:
    js = f.read()

quote_form_js = """
  // 8. Procurement Quote Form Interactive Submission
  const quoteForm = document.getElementById('procurementQuoteForm');
  const quoteAlert = document.getElementById('quoteFormAlert');
  if (quoteForm) {
    quoteForm.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!quoteForm.checkValidity()) {
        e.stopPropagation();
        quoteForm.classList.add('was-validated');
        return;
      }
      const submitBtn = document.getElementById('quoteSubmitBtn');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span>Submitting...</span>';
      }
      setTimeout(function () {
        if (quoteAlert) {
          quoteAlert.classList.remove('d-none');
        }
        quoteForm.reset();
        quoteForm.classList.remove('was-validated');
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = '<span>Submit Your Enquiry</span><i class="bi bi-chevron-right ms-2"></i>';
        }
      }, 700);
    });
  }
});
"""

if '});' in js:
    # replace last }); with handler and close
    idx = js.rfind('});')
    js_updated = js[:idx] + quote_form_js
    with open("js/script.js", "w", encoding="utf-8") as f:
        f.write(js_updated)
    print("js/script.js updated with form handler.")
