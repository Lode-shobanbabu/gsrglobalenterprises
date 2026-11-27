with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'(<section class="commitment-mockup-section" id="commitment".*?</section>)', text, re.DOTALL)
if match:
    print("Found commitment block in index.html, length:", len(match.group(1)))
    print("Starts with:", match.group(1)[:120])
    print("Ends with:", match.group(1)[-120:])
else:
    print("Not found")
