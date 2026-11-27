import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'(<section class="commitment-mockup-section" id="commitment".*?</section>)', text, re.DOTALL)
if match:
    print(match.group(1))
