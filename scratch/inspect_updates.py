from PIL import Image

nav = Image.open('scratch/navbar_capitalized.png')
print("Nav crop size:", nav.size)

about = Image.open('scratch/about_btn_orange.png')
print("About crop size:", about.size)

# Find the orange button in about crop
# Search for pixels matching var(--accent-orange) which is rgb(255, 121, 0)
orange_pixels = []
w, h = about.size
for x in range(w):
    for y in range(h):
        r, g, b, *a = about.getpixel((x, y))
        if r > 240 and 100 <= g <= 140 and b < 25:
            orange_pixels.append((x, y))

print(f"Found {len(orange_pixels)} orange button pixels in About Us section!")
if orange_pixels:
    min_x = min(p[0] for p in orange_pixels)
    max_x = max(p[0] for p in orange_pixels)
    min_y = min(p[1] for p in orange_pixels)
    max_y = max(p[1] for p in orange_pixels)
    print(f"About Button bounds in crop: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]")
    
    # Save a tight crop of the button
    tight_btn = about.crop((max(0, min_x - 20), max(0, min_y - 15), min(w, max_x + 20), min(h, max_y + 15)))
    tight_btn.save('scratch/about_button_tight.png')
    print("Saved tight crop of the updated About button to scratch/about_button_tight.png")
