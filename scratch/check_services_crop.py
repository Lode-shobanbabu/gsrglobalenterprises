from PIL import Image

img = Image.open(r"scratch\services_cards_bottom_crop.png")
print("Services cards crop size:", img.size)

# Copy the crop to the brain artifact directory
import shutil
shutil.copyfile(r"scratch\services_cards_bottom_crop.png", r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\services_6cards_and_cta_preview.png")
print("Saved preview to brain directory.")
