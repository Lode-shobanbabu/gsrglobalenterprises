with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
selectors = re.findall(r'([.#][\w\-]+)\s*\{', css)
print("Unique classes and IDs in CSS:")
btns = [s for s in set(selectors) if 'btn' in s or 'button' in s or 'cta' in s]
cards = [s for s in set(selectors) if 'card' in s or 'box' in s]
abouts = [s for s in set(selectors) if 'about' in s]
contacts = [s for s in set(selectors) if 'contact' in s]

print("Buttons/CTA:", sorted(btns))
print("Cards/Boxes:", sorted(cards))
print("About:", sorted(abouts))
print("Contact:", sorted(contacts))
