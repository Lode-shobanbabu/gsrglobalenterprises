import shutil

src = r"scratch\dock_cards_rendered.png"
dst = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\dock_cards_glass_preview.png"
shutil.copyfile(src, dst)
print("Copied preview to brain artifact dir.")
