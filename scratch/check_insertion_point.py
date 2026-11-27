with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
client_match = re.search(r'(<section class="clients-section" id="clients".*?</section>)', text, re.DOTALL)
if client_match:
    print("Found client section, ends at index:", client_match.end())
    snippet = text[client_match.end():client_match.end()+200]
    print("Immediately after client section:")
    print(snippet)
else:
    print("Client section not found")
