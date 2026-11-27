from PIL import Image

cp = Image.open('assets/images/client-central-prison-emblem.png')
print("cp size:", cp.size, "mode:", cp.mode)
ap = Image.open('assets/images/client-apsrtc-logo.png')
print("ap size:", ap.size, "mode:", ap.mode)

# Let's clean up background to pure transparent if needed
def make_clean_transparent(img, bg_color_sample, tolerance=30):
    img = img.convert("RGBA")
    datas = img.getdata()
    new_data = []
    r_bg, g_bg, b_bg, _ = bg_color_sample
    for item in datas:
        # Check distance to bg_color
        dist = ((item[0]-r_bg)**2 + (item[1]-g_bg)**2 + (item[2]-b_bg)**2)**0.5
        if dist < tolerance:
            new_data.append((255, 255, 255, 0))
        elif dist < tolerance + 25:
            # smooth edge
            alpha = int(255 * ((dist - tolerance) / 25))
            new_data.append((item[0], item[1], item[2], min(item[3], alpha)))
        else:
            new_data.append(item)
    img.putdata(new_data)
    return img

cp_bg = cp.convert("RGBA").getpixel((2, 2))
cp_trans = make_clean_transparent(cp, cp_bg, tolerance=25)
cp_trans.save('assets/images/client-central-prison-emblem-clean.png')

ap_bg = ap.convert("RGBA").getpixel((2, 2))
ap_trans = make_clean_transparent(ap, ap_bg, tolerance=20)
ap_trans.save('assets/images/client-apsrtc-logo-clean.png')

print("Created clean transparent versions")
