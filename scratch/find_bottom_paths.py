import re

with open('scratch/letterhead.svg', 'r') as f:
    svg = f.read()

paths = re.findall(r'<path d="([^"]*)" fill="([^"]*)" stroke="([^"]*)"', svg)

bottom_paths = []
for i, (d, fill, stroke) in enumerate(paths):
    coords = re.findall(r'[-+]?\d*\.\d+|\d+', d)
    ys = [float(coords[j]) for j in range(1, len(coords), 2)]
    xs = [float(coords[j]) for j in range(0, len(coords), 2)]
    if ys and min(ys) > 750:
        bottom_paths.append((i, min(xs), max(xs), min(ys), max(ys), fill, stroke, len(d)))

print('Bottom paths count:', len(bottom_paths))
for p in bottom_paths[:20]:
    print(p)
