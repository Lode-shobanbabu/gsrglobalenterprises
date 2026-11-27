import subprocess
import os
from PIL import Image

out_full = os.path.abspath(r"scratch\process_full.png")

if os.path.exists(out_full):
    im = Image.open(out_full)
    # Full process section from top of section
    # Let's crop from Y=5420 to Y=6350
    crop_im = im.crop((80, 5420, 1320, 6300))
    artifact_path = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\process_section_updated.png"
    crop_im.save(artifact_path)
    print("Cropped from 5420 to 6300 successfully.")
