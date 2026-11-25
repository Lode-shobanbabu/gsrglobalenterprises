import re

with open('scratch/letterhead.svg', 'r', encoding='utf-8') as f:
    svg = f.read()

paths = re.findall(r'<path d="(.*?)" fill="(.*?)" stroke="(.*?)"(?: stroke-width="(.*?)")? />', svg)
print(f"Total paths in SVG: {len(paths)}")

# Let's find paths in the top region (y < 200)
top_paths = []
for d, fill, stroke, sw in paths:
    coords = re.findall(r'[-+]?\d*\.\d+|\d+', d)
    # y coordinates are at odd indices in M/L/C
    ys = [float(coords[i]) for i in range(1, len(coords), 2)]
    xs = [float(coords[i]) for i in range(0, len(coords), 2)]
    if ys:
        min_y = min(ys)
        max_y = max(ys)
        min_x = min(xs)
        max_x = max(xs)
        if min_y < 160:
            top_paths.append((min_x, max_x, min_y, max_y, fill, stroke, d))

print(f"Top paths (y < 160): {len(top_paths)}")
for i, (min_x, max_x, min_y, max_y, fill, stroke, d) in enumerate(top_paths[:35]):
    print(f"Path {i}: X=[{min_x:.1f}..{max_x:.1f}] Y=[{min_y:.1f}..{max_y:.1f}] fill={fill} stroke={stroke} len_d={len(d)}")
