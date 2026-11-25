from PIL import Image

bg_color = (2, 6, 18, 255) # Dark navbar background

# Load darkmode version
dark_logo = Image.open('assets/images/gsr-logo-white.webp')
orig_logo = Image.open('assets/images/gsr-logo.png')

w, h = dark_logo.size
preview = Image.new('RGBA', (w + 60, (h + 40) * 2), bg_color)

# Paste darkmode version at top
preview.paste(dark_logo, (30, 20), dark_logo)

# Paste original version below
preview.paste(orig_logo, (30, h + 60), orig_logo)

preview.save('scratch/compare_dark_vs_orig.png')
print("Saved scratch/compare_dark_vs_orig.png")
