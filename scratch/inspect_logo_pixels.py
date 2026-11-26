import os
from PIL import Image
import numpy as np

src_path = r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795675948188_7896240d.webp"
img = Image.open(src_path).convert('RGBA')
arr = np.array(img)

# Filter out transparent pixels
visible = arr[arr[:, :, 3] > 30]

print("Total visible pixels:", len(visible))

# Let's inspect unique prominent colors
# Separate into Orange-ish, Blue-ish/Dark, and Grey-ish
r = visible[:, 0].astype(int)
g = visible[:, 1].astype(int)
b = visible[:, 2].astype(int)

# Orange: R significantly higher than B and G
orange_mask = (r > 150) & (r > b + 60)
# Dark navy / blue: B higher than R, or R,G,B all low
dark_mask = (r < 60) & (g < 80) & (b < 120)

print(f"Orange pixels: {np.sum(orange_mask)}")
print(f"Dark/Navy pixels: {np.sum(dark_mask)}")

# Let's see some sample RGB values of visible non-orange pixels
non_orange = visible[~orange_mask]
print("Sample non-orange RGBs (first 10):", non_orange[:10, :3].tolist())
