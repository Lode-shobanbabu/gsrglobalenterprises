from PIL import Image

im = Image.open('scratch/text_name.png')

# Let's crop before 360 and after 360
part1 = im.crop((0, 0, 360, 64))
part1.save('scratch/part1.png')

part2 = im.crop((360, 0, 930, 64))
part2.save('scratch/part2.png')

print("Part 1 bbox:", part1.getbbox())
print("Part 2 bbox:", part2.getbbox())
