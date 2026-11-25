import zlib
import re
import os

pdf_path = r'C:/Users/sunseaz/.gemini/antigravity/brain/a4cbe818-6d35-404c-8a2c-b373e74e0891/.user_uploaded/media_1795599958895_36e3ed83.pdf'

with open(pdf_path, 'rb') as f:
    data = f.read()

stream_regex = re.compile(rb'stream[\r\n]+(.*?)[\r\n]+endstream', re.DOTALL)
streams = stream_regex.findall(data)
print('Found streams:', len(streams))

os.makedirs('scratch/extracted_pdf', exist_ok=True)

for i, s in enumerate(streams):
    print(f'Stream {i}: len={len(s)}')
    try:
        decomp = zlib.decompress(s)
        print(f'  Decompressed len={len(decomp)}')
        if decomp.startswith(b'\xff\xd8\xff'):
            print('  -> JPEG!')
            with open(f'scratch/extracted_pdf/stream_{i}.jpg', 'wb') as out:
                out.write(decomp)
        elif decomp.startswith(b'\x89PNG'):
            print('  -> PNG!')
            with open(f'scratch/extracted_pdf/stream_{i}.png', 'wb') as out:
                out.write(decomp)
        else:
            with open(f'scratch/extracted_pdf/stream_{i}.bin', 'wb') as out:
                out.write(decomp)
            # check printable text in decomp
            printable = re.findall(rb'[a-zA-Z0-9\s:,\.\-/\(\)]{4,}', decomp)
            print('  Sample text:', [p.decode('latin1', 'ignore') for p in printable[:10]])
    except Exception as e:
        print(f'  Decompress error: {e}')
        # Maybe raw JPEG without flate?
        if s.startswith(b'\xff\xd8\xff'):
            print('  -> RAW JPEG!')
            with open(f'scratch/extracted_pdf/stream_{i}_raw.jpg', 'wb') as out:
                out.write(s)
