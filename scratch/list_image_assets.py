import os

for f in sorted(os.listdir('assets/images')):
    if f.endswith(('.jpg', '.webp', '.png')):
        print(f)
