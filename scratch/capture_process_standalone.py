import os
import subprocess
from PIL import Image

html_file = os.path.abspath('scratch/test_process_standalone.html').replace('\\', '/')
out_img = os.path.abspath('scratch/process_standalone_shot.png').replace('\\', '/')

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1440,1100",
    "--virtual-time-budget=2500",
    f"--screenshot={out_img}",
    f"file:///{html_file}"
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

if os.path.exists(out_img):
    im = Image.open(out_img)
    print("Screenshot captured:", im.size)
    
    # Save a copy to artifact directory
    artifact_path = r"C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\process_section_preview.png"
    im.save(artifact_path)
    print(f"Saved preview to: {artifact_path}")
    
    # Let's inspect the bounding box of non-white pixels
    # Find image bounds on left side (x between 100 and 600)
    left_pixels = []
    right_pixels = []
    
    for y in range(0, im.height):
        # sample left image column (around x=300)
        p_left = im.getpixel((300, y))[:3]
        if p_left != (255, 255, 255):
            left_pixels.append(y)
            
        # sample right column (around x=800, checking for text/badges)
        # badge or text non-white
        for x in range(600, 1300, 10):
            p_right = im.getpixel((x, y))[:3]
            if p_right != (255, 255, 255):
                right_pixels.append(y)
                break

    if left_pixels and right_pixels:
        left_top, left_bottom = min(left_pixels), max(left_pixels)
        right_top, right_bottom = min(right_pixels), max(right_pixels)
        print(f"Left image card vertical span: top={left_top}px, bottom={left_bottom}px, height={left_bottom - left_top}px")
        print(f"Right content vertical span: top={right_top}px, bottom={right_bottom}px, height={right_bottom - right_top}px")
        print(f"Height Difference: {abs((left_bottom - left_top) - (right_bottom - right_top))}px")
else:
    print("Failed to capture screenshot.")
