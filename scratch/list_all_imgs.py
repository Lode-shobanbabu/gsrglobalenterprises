import os

for f in sorted(os.listdir('assets/images')):
    if f.endswith(('.webp', '.jpg', '.png')):
        size = os.path.getsize(os.path.join('assets/images', f))
        print(f"{f}: {size // 1024} KB")
