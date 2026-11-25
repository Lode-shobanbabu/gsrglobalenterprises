with open('scratch/extracted_pdf/stream_0.bin', 'r', encoding='latin1', errors='ignore') as f:
    text = f.read()

print("Length of stream_0:", len(text))

# Let's search for words like GSR, GLOBAL, ENTERPRISES, or text strings
import re
# Look for text strings in parentheses (standard PDF)
matches = re.findall(r'\((.*?)\)', text)
print("Text in parens:", len(matches))
for m in matches[:20]:
    if any(c.isalnum() for c in m):
        print("  Found paren text:", m)

# Also look for Tj or TJ commands
tj_matches = re.findall(r'(\[.*?\]|\(.*?\))\s*(Tj|TJ|\')', text)
print("TJ matches:", len(tj_matches))
for tj in tj_matches[:10]:
    print("  TJ:", tj)

# If the letterhead has converted fonts to paths (outlines):
# Let's check the bounding boxes of filled paths in stream_0!
paths = []
# Each path ends with f, F, f*, b, B, s, S
lines = text.split('\n')
print(f"Total lines in stream_0: {len(lines)}")
