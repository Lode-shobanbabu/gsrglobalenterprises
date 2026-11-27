with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'(<section class="clients-section" id="clients".*?</section>)', text, re.DOTALL)
if match:
    print("Match length:", len(match.group(1)))
    print("Exact snippet:")
    print(match.group(1)[:250])
    print("...")
    print(match.group(1)[-250:])
else:
    print("Not found")
