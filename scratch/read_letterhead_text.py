import re

with open('scratch/extracted_pdf/stream_0.bin', 'r', encoding='latin1', errors='ignore') as f:
    text = f.read()

# Let's inspect all paths and see where the text characters are located
# On the letterhead, what is written on the right side in white text (Y ~ 48-56)?
# We know paths 24 to 44 are at X=[427..572], Y=[48..56]
# Let's see what is written in the bottom paths (Y > 750)
