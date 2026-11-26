from PIL import Image

footer_preview = Image.open("scratch/preview_footer_logo.png")
print("Footer preview format:", footer_preview.format, footer_preview.size)

# Let's also check if there is another option:
# What if the user wants the exact original logo in the footer too,
# or wants the white version?
# In the white version:
# Top arc: Orange #FF7900
# GSR: White #FFFFFF
# Bottom arc: White #FFFFFF
# Vertical line: White #FFFFFF
# GSR GLOBAL: White #FFFFFF
# Globe: Blue/cyan globe with Orange orbit ring #FF7900
# ENTERPRISES: Silver #E2E8F0
print("White version has all brand elements clearly differentiated for dark backgrounds.")
