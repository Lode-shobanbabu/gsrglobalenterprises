from PIL import Image

im = Image.open(r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\process_section_preview.png")

# Top slice: header subtitle down into step 1 and image top
top_slice = im.crop((0, 150, im.width, 420))
top_slice.save(r"scratch/slice_top.png")

# Bottom slice: step 4 and image bottom
bot_slice = im.crop((0, 750, im.width, im.height))
bot_slice.save(r"scratch/slice_bot.png")

print("Saved top and bottom slices.")
