import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

process_html = '''

    <!-- ==========================================================================
         8. OUR PROCUREMENT PROCESS (HOW WE WORK)
         ========================================================================== -->
    <section class="procurement-process-section" id="process" aria-label="Our Procurement Process">
      <div class="container">

        <!-- Section Header (Centered Brand Dash Style) -->
        <div class="text-center mb-5 fade-up-element">
          <div class="process-eyebrow mb-2">
            <span class="process-eyebrow-dash"></span>
            <span class="process-eyebrow-text">HOW WE WORK</span>
            <span class="process-eyebrow-dash"></span>
          </div>
          <h2 class="process-section-title mb-3">
            A Straightforward Approach to Reliable Procurement
          </h2>
          <div class="process-title-accent mx-auto mb-3"></div>
          <p class="process-section-subtitle mx-auto">
            We make the procurement process easier through structured coordination and a clear understanding of your requirements.
          </p>
        </div>

        <!-- Alternating Vertical Process Timeline -->
        <div class="process-timeline-container fade-up-element">
          <!-- Central Spine Line -->
          <div class="process-timeline-spine" aria-hidden="true"></div>

          <!-- Step 01: Understand Your Requirements (Left) -->
          <div class="process-timeline-row row align-items-center">
            <div class="col-lg-6 process-col-left">
              <div class="process-card">
                <h3 class="process-card-title">Understand Your Requirements</h3>
                <p class="process-card-desc mb-0">
                  We understand your product specifications, quantities, budget expectations and project needs.
                </p>
              </div>
            </div>
            <!-- Node 01 -->
            <div class="process-node-wrap" aria-hidden="true">
              <div class="process-circle-badge">
                <span class="process-node-num">01</span>
              </div>
            </div>
            <div class="col-lg-6 process-col-spacer d-none d-lg-block"></div>
          </div>

          <!-- Step 02: Source the Right Products (Right) -->
          <div class="process-timeline-row row align-items-center">
            <div class="col-lg-6 process-col-spacer d-none d-lg-block"></div>
            <!-- Node 02 -->
            <div class="process-node-wrap" aria-hidden="true">
              <div class="process-circle-badge">
                <span class="process-node-num">02</span>
              </div>
            </div>
            <div class="col-lg-6 process-col-right">
              <div class="process-card">
                <h3 class="process-card-title">Source the Right Products</h3>
                <p class="process-card-desc mb-0">
                  We coordinate sourcing based on your technical, commercial and quality requirements.
                </p>
              </div>
            </div>
          </div>

          <!-- Step 03: Coordinate Procurement (Left) -->
          <div class="process-timeline-row row align-items-center">
            <div class="col-lg-6 process-col-left">
              <div class="process-card">
                <h3 class="process-card-title">Coordinate Procurement</h3>
                <p class="process-card-desc mb-0">
                  We coordinate quotations, product details, availability and procurement arrangements.
                </p>
              </div>
            </div>
            <!-- Node 03 -->
            <div class="process-node-wrap" aria-hidden="true">
              <div class="process-circle-badge">
                <span class="process-node-num">03</span>
              </div>
            </div>
            <div class="col-lg-6 process-col-spacer d-none d-lg-block"></div>
          </div>

          <!-- Step 04: Support Supply & Delivery (Right) -->
          <div class="process-timeline-row row align-items-center">
            <div class="col-lg-6 process-col-spacer d-none d-lg-block"></div>
            <!-- Node 04 -->
            <div class="process-node-wrap" aria-hidden="true">
              <div class="process-circle-badge">
                <span class="process-node-num">04</span>
              </div>
            </div>
            <div class="col-lg-6 process-col-right">
              <div class="process-card">
                <h3 class="process-card-title">Support Supply &amp; Delivery</h3>
                <p class="process-card-desc mb-0">
                  We coordinate supply arrangements to support your purchasing and project timelines.
                </p>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>'''

client_match = re.search(r'(<section class="clients-section" id="clients".*?</section>)', html, re.DOTALL)
if client_match:
    insertion_idx = client_match.end()
    html_new = html[:insertion_idx] + process_html + html[insertion_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_new)
    print("Inserted process section into index.html successfully.")
else:
    print("Error: Could not find client section in index.html")
