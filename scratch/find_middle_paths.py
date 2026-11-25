import re

with open('scratch/letterhead.svg', 'r') as f:
    svg = f.read()

paths = re.findall(r'<path d="([^"]*)" fill="([^"]*)" stroke="([^"]*)"', svg)
print('Total paths:', len(paths))

middle_paths = []
for i, (d, fill, stroke) in enumerate(paths):
    coords = re.findall(r'[-+]?\d*\.\d+|\d+', d)
    ys = [float(coords[j]) for j in range(1, len(coords), 2)]
    xs = [float(coords[j]) for j in range(0, len(coords), 2)]
    if ys:
        min_y, max_y = min(ys), max(ys)
        min_x, max_x = min(xs), max(xs)
        if 150 < min_y < 700:
            middle_paths.append((i, min_x, max_x, min_y, max_y, fill, stroke, len(d)))

print('Middle paths count:', len(middle_paths))
for p in middle_paths[:20]:
    print(p)
