from PIL import Image

src = Image.open(r"C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795677832868_afa5e5b5.jpg")
w, h = src.size

# Let's see: in media_1795677832868_afa5e5b5.jpg
# Where does the original text end horizontally?
# The words "Your Trusted Partner for Global Solutions"
# "Global Solutions": where does "Solutions" end?
# Let's inspect columns from x=350 to x=550 to find where the dark text ends!
pixels = src.load()

# Look at y around 80-160 (where headline was)
text_columns = []
for x in range(350, 550):
    # Dark text pixels (navy blue: r < 50, g < 80, b < 120)
    dark_text_count = sum(1 for y in range(80, 200) if pixels[x, y][0] < 50 and pixels[x, y][1] < 80)
    if dark_text_count > 0:
        text_columns.append((x, dark_text_count))

print("Columns with dark text between x=350 and 550:")
for x, c in text_columns[::5]:
    print(f"x={x}: {c} dark pixels")
if text_columns:
    print("Last column with dark text:", text_columns[-1][0])
else:
    print("No dark text found with this threshold")
