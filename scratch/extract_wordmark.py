import re

with open('scratch/letterhead.svg', 'r') as f:
    svg = f.read()

paths = re.findall(r'<path d="([^"]*)" fill="([^"]*)" stroke="([^"]*)"', svg)

# Extract paths 4 to 23 (index 6 to 25 or based on coordinates)
wordmark_paths = []
for d, fill, stroke in paths:
    coords = re.findall(r'[-+]?\d*\.\d+|\d+', d)
    ys = [float(coords[j]) for j in range(1, len(coords), 2)]
    xs = [float(coords[j]) for j in range(0, len(coords), 2)]
    if ys and 50 < min(ys) < 70 and 38 < min(xs) < 370 and max(xs) < 370:
        wordmark_paths.append((d, min(xs), max(xs), min(ys), max(ys)))

print(f"Found {len(wordmark_paths)} letter paths for wordmark!")
min_x = min(p[1] for p in wordmark_paths)
max_x = max(p[2] for p in wordmark_paths)
min_y = min(p[3] for p in wordmark_paths)
max_y = max(p[4] for p in wordmark_paths)

print(f"Wordmark bounds: X=[{min_x:.2f}..{max_x:.2f}], Y=[{min_y:.2f}..{max_y:.2f}], W={max_x-min_x:.2f}, H={max_y-min_y:.2f}")

# Create clean standalone SVG for GSR GLOBAL ENTERPRISES in white (and gold accent)
w = max_x - min_x
h = max_y - min_y
padding = 4
svg_w = w + padding * 2
svg_h = h + padding * 2

svg_out = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w:.2f} {svg_h:.2f}" width="{svg_w:.2f}" height="{svg_h:.2f}">'
]

# Shift coordinates so it starts at (padding, padding)
for d, px_min, px_max, py_min, py_max in wordmark_paths:
    # We can shift path by wrapping in <g transform="translate(...)">
    pass

svg_out.append(f'  <g transform="translate({padding - min_x:.2f}, {padding - min_y:.2f})">')
for d, px_min, px_max, py_min, py_max in wordmark_paths:
    svg_out.append(f'    <path d="{d}" fill="#ffffff" />')
svg_out.append('  </g>')
svg_out.append('</svg>')

with open('scratch/wordmark_white.svg', 'w') as f:
    f.write("\n".join(svg_out))

print("Saved scratch/wordmark_white.svg")
