import re

with open('scratch/extracted_pdf/stream_0.bin', 'r', encoding='latin1', errors='ignore') as f:
    content = f.read()

# PDF coordinate system: bottom-left is (0,0), height is 842.04
page_w = 595.39
page_h = 842.04

tokens = content.split()
i = 0
n = len(tokens)

svg_parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {page_w} {page_h}" width="{page_w}" height="{page_h}">'
]

current_path_d = []
fill_color = "none"
stroke_color = "none"
stroke_w = "1"

def cmyk_to_rgb_hex(c, m, y, k):
    r = int(255 * (1 - c) * (1 - k))
    g = int(255 * (1 - m) * (1 - k))
    b = int(255 * (1 - y) * (1 - k))
    return f"#{r:02x}{g:02x}{b:02x}"

def rgb_to_hex(r, g, b):
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"

while i < n:
    tok = tokens[i]
    if tok == 'scn' or tok == 'g' or tok == 'rg' or tok == 'k':
        # Check backwards how many numbers
        nums = []
        j = i - 1
        while j >= 0:
            try:
                nums.append(float(tokens[j]))
                j -= 1
            except ValueError:
                break
        nums.reverse()
        if len(nums) == 1:
            val = int(nums[0] * 255)
            fill_color = f"#{val:02x}{val:02x}{val:02x}"
        elif len(nums) == 3:
            fill_color = rgb_to_hex(nums[0], nums[1], nums[2])
        elif len(nums) >= 4:
            fill_color = cmyk_to_rgb_hex(nums[-4], nums[-3], nums[-2], nums[-1])
    elif tok == 'SCN' or tok == 'G' or tok == 'RG' or tok == 'K':
        nums = []
        j = i - 1
        while j >= 0:
            try:
                nums.append(float(tokens[j]))
                j -= 1
            except ValueError:
                break
        nums.reverse()
        if len(nums) == 1:
            val = int(nums[0] * 255)
            stroke_color = f"#{val:02x}{val:02x}{val:02x}"
        elif len(nums) == 3:
            stroke_color = rgb_to_hex(nums[0], nums[1], nums[2])
        elif len(nums) >= 4:
            stroke_color = cmyk_to_rgb_hex(nums[-4], nums[-3], nums[-2], nums[-1])
    elif tok == 'w':
        try:
            stroke_w = tokens[i-1]
        except Exception:
            pass
    elif tok == 'm': # moveto
        try:
            x = float(tokens[i-2])
            y = page_h - float(tokens[i-1]) # flip Y for SVG
            current_path_d.append(f"M {x:.2f} {y:.2f}")
        except Exception:
            pass
    elif tok == 'l': # lineto
        try:
            x = float(tokens[i-2])
            y = page_h - float(tokens[i-1])
            current_path_d.append(f"L {x:.2f} {y:.2f}")
        except Exception:
            pass
    elif tok == 'c': # curveto
        try:
            x1 = float(tokens[i-6])
            y1 = page_h - float(tokens[i-5])
            x2 = float(tokens[i-4])
            y2 = page_h - float(tokens[i-3])
            x3 = float(tokens[i-2])
            y3 = page_h - float(tokens[i-1])
            current_path_d.append(f"C {x1:.2f} {y1:.2f} {x2:.2f} {y2:.2f} {x3:.2f} {y3:.2f}")
        except Exception:
            pass
    elif tok == 'h': # closepath
        current_path_d.append("Z")
    elif tok in ('f', 'F', 'f*'):
        if current_path_d:
            d_str = " ".join(current_path_d)
            svg_parts.append(f'<path d="{d_str}" fill="{fill_color}" stroke="none" />')
            current_path_d = []
    elif tok in ('s', 'S'):
        if current_path_d:
            d_str = " ".join(current_path_d)
            svg_parts.append(f'<path d="{d_str}" fill="none" stroke="{stroke_color}" stroke-width="{stroke_w}" />')
            current_path_d = []
    elif tok in ('b', 'B', 'b*', 'B*'):
        if current_path_d:
            d_str = " ".join(current_path_d)
            svg_parts.append(f'<path d="{d_str}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="{stroke_w}" />')
            current_path_d = []
    i += 1

svg_parts.append('</svg>')

svg_content = "\n".join(svg_parts)
with open('scratch/letterhead.svg', 'w', encoding='utf-8') as out:
    out.write(svg_content)

print(f"Generated scratch/letterhead.svg with {len(svg_parts)} elements!")
