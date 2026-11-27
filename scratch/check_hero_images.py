import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

hero_match = re.search(r'(<section[^>]*id=["\']hero["\'].*?</section>)', text, re.DOTALL)
if hero_match:
    for m in re.findall(r'assets/images/[^\s"\'\)]+', hero_match.group(1)):
        print('Hero image:', m)
