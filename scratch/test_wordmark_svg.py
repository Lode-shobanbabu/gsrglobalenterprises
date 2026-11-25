with open('scratch/wordmark_white.svg', 'r') as f:
    svg = f.read()

print("wordmark_white.svg length:", len(svg))
print("First 200 chars:")
print(svg[:200])
