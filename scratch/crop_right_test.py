from PIL import Image

full = Image.open('scratch/about_perfect_equal.png')
crop_right = full.crop((700, 50, 1300, 750))
crop_right.save('scratch/right_content_test.png')
print("Saved right_content_test.png, size:", crop_right.size)
