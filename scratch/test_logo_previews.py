from PIL import Image

transparent_logo = Image.open("assets/images/gsr-logo-official-transparent.png")
white_logo = Image.open("assets/images/gsr-logo-official-white.png")

# Preview on white background
w, h = transparent_logo.size
preview_light = Image.new("RGBA", (w + 40, h + 40), (255, 255, 255, 255))
preview_light.paste(transparent_logo, (20, 20), transparent_logo)
preview_light.save("scratch/preview_navbar_logo.png")

# Preview on navy background (#062B55)
preview_dark = Image.new("RGBA", (w + 40, h + 40), (6, 43, 85, 255))
preview_dark.paste(white_logo, (20, 20), white_logo)
preview_dark.save("scratch/preview_footer_logo.png")

print("Created previews in scratch/preview_navbar_logo.png and scratch/preview_footer_logo.png")
