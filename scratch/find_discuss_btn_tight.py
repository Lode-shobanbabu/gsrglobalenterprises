from PIL import Image

full = Image.open(r"scratch\discuss_btn_preview.png")
w, h = full.size

# Search for orange pixels of the discuss button in the lower half of #services (y: 1100 to 1800)
orange_pts = []
for x in range(300, 1100, 2):
    for y in range(1000, 1800, 2):
        r, g, b, *a = full.getpixel((x, y))
        if r > 240 and 110 <= g <= 135 and b < 20:
            orange_pts.append((x, y))

print("Total orange button pixels found:", len(orange_pts))
if orange_pts:
    min_x = min(p[0] for p in orange_pts)
    max_x = max(p[0] for p in orange_pts)
    min_y = min(p[1] for p in orange_pts)
    max_y = max(p[1] for p in orange_pts)
    print(f"Discuss Button bounds: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}], width={max_x - min_x}px, height={max_y - min_y}px")
    
    tight = full.crop((max(0, min_x - 30), max(0, min_y - 20), min(w, max_x + 30), min(h, max_y + 20)))
    tight.save(r"scratch\discuss_btn_tight.png")
    
    import shutil
    shutil.copyfile(r"scratch\discuss_btn_tight.png", r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\services_discuss_btn_preview.png")
    print("Saved preview to brain directory.")
