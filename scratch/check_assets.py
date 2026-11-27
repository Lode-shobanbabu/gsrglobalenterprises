import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Scripts in index.html:')
for s in re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', text):
    print(' ', s)
print('Stylesheets in index.html:')
for c in re.findall(r'<link[^>]*href=["\']([^"\']+)["\']', text):
    print(' ', c)
