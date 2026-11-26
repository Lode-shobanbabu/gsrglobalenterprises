# scratch/remove_stats_bar.py

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_html = '''        <!-- Corporate Statistics Banner (Spanning Width with Crisp Dividers) -->
        <div class="about-corp-stats-bar mt-5 fade-up-element">
          <div class="row g-0 text-center align-items-center">

            <div class="col-6 col-lg-3 about-stat-border">
              <div class="about-stat-item">
                <div class="about-stat-number">100+</div>
                <div class="about-stat-text">Verified Consignments</div>
              </div>
            </div>

            <div class="col-6 col-lg-3 about-stat-border">
              <div class="about-stat-item">
                <div class="about-stat-number">5+</div>
                <div class="about-stat-text">Core Industry Sectors</div>
              </div>
            </div>

            <div class="col-6 col-lg-3 about-stat-border">
              <div class="about-stat-item">
                <div class="about-stat-number">2</div>
                <div class="about-stat-text">Regional AP Hubs</div>
              </div>
            </div>

            <div class="col-6 col-lg-3">
              <div class="about-stat-item">
                <div class="about-stat-number">100%</div>
                <div class="about-stat-text">GST &amp; Tax Compliant</div>
              </div>
            </div>

          </div>
        </div>
'''

if target_html in html:
    html = html.replace(target_html, '')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Removed stats bar from index.html")
else:
    print("Exact target_html not found in index.html, doing substring search...")
    bar_start = '        <!-- Corporate Statistics Banner'
    bar_end = '      </div>\n    </section>'
    b1 = html.find(bar_start)
    b2 = html.find(bar_end)
    if b1 != -1 and b2 != -1:
        html = html[:b1] + html[b2:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Removed stats bar via markers from index.html")
    else:
        print("Could not find markers!")

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

target_css = '''/* Corporate Metrics Bar */
.about-corp-stats-bar {
  background: var(--primary-navy);
  border-radius: 16px;
  padding: 2rem 1.5rem;
  color: #ffffff;
  box-shadow: 0 16px 40px rgba(6, 43, 85, 0.16);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.about-stat-item {
  padding: 0.5rem 1rem;
}

.about-stat-border {
  border-right: 1px solid rgba(255, 255, 255, 0.12);
}

.about-stat-number {
  font-family: var(--font-heading);
  font-size: clamp(2rem, 2.7vw, 2.5rem);
  font-weight: 800;
  color: #ffffff;
  line-height: 1.1;
  margin-bottom: 0.35rem;
}

.about-stat-text {
  font-family: var(--font-body);
  font-size: 0.84rem;
  color: rgba(255, 255, 255, 0.82);
  font-weight: 500;
}
'''

if target_css in css:
    css = css.replace(target_css, '')
    print("Removed main stats bar CSS from css/style.css")

# Also remove from media query
mq_css = '''  .about-stat-border {
    border-right: none;
  }

  .about-corp-stats-bar .col-6:nth-child(1),
  .about-corp-stats-bar .col-6:nth-child(2) {
    margin-bottom: 1.25rem;
  }
'''

if mq_css in css:
    css = css.replace(mq_css, '')
    print("Removed stats bar media query CSS from css/style.css")

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/style.css successfully!")
