from PIL import Image

# Let's inspect white logo pixels
white_img = Image.open("assets/images/gsr-logo-official-white.png").convert('RGBA')
w, h = white_img.size

# Let's see some stats
colors = white_img.getcolors(maxcolors=100000)
print(f"Total unique RGBA colors in white logo: {len(colors)}")

# Check against a dark navy background (Team lead's #062B55)
bg = Image.new("RGBA", (w, h), (6, 43, 85, 255))
composite = Image.alpha_composite(bg, white_img)
composite.save("scratch/composite_dark_navy.png")

# Check against a secondary blue background (Team lead's #0D3D70)
bg2 = Image.new("RGBA", (w, h), (13, 61, 112, 255))
composite2 = Image.alpha_composite(bg2, white_img)
composite2.save("scratch/composite_secondary_blue.png")

print("Composites saved to scratch/ for inspection.")
