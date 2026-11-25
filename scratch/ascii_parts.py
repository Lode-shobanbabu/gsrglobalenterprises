from PIL import Image

p1 = Image.open('scratch/part1.png').resize((40, 10))
p2 = Image.open('scratch/part2.png').resize((50, 10))
chars = " .:-=+*#%@"

print("PART 1:")
for y in range(10):
    print("".join(chars[min(len(chars)-1, int(p1.getpixel((x, y))[3]/25.6))] for x in range(40)))

print("\nPART 2:")
for y in range(10):
    print("".join(chars[min(len(chars)-1, int(p2.getpixel((x, y))[3]/25.6))] for x in range(50)))
