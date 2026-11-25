from PIL import Image

# Load clean white emblem
emb = Image.open('assets/images/gsr-emblem-white.png') # 779 x 382
w_emb, h_emb = emb.size

# Load text_orig and clean it
im_text_orig = Image.open('scratch/text_orig.png')
w_t, h_t = im_text_orig.size
clean_name = Image.new('RGBA', (w_t, h_t), (0, 0, 0, 0))
for y in range(h_t):
    for x in range(w_t):
        r, g, b = im_text_orig.getpixel((x, y))
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        if lum < 220:
            alpha = int(255 * (1.0 - (lum / 220.0)))
            clean_name.putpixel((x, y), (255, 255, 255, min(255, int(alpha * 1.35))))

# Crop tightly
clean_name = clean_name.crop(clean_name.getbbox())

im_tag_orig = Image.open('scratch/tagline_orig.png')
w_tg, h_tg = im_tag_orig.size
clean_tag = Image.new('RGBA', (w_tg, h_tg), (0, 0, 0, 0))
for y in range(h_tg):
    for x in range(w_tg):
        r, g, b = im_tag_orig.getpixel((x, y))
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        if lum < 220:
            alpha = int(255 * (1.0 - (lum / 220.0)))
            clean_tag.putpixel((x, y), (241, 150, 48, min(255, int(alpha * 1.4))))

clean_tag = clean_tag.crop(clean_tag.getbbox())

p_global = clean_name.crop((0, 0, 346, clean_name.size[1]))
p_global = p_global.crop(p_global.getbbox())

p_enterprises = clean_name.crop((360, 0, clean_name.size[0], clean_name.size[1]))
p_enterprises = p_enterprises.crop(p_enterprises.getbbox())

p_tagline = clean_tag.crop(clean_tag.getbbox())

print(f"p_global: {p_global.size}, p_enterprises: {p_enterprises.size}, p_tagline: {p_tagline.size}")

# Target height = 120px (renders at 60px height in browser, 2x retina)
# Emblem height = 104px. Width = 104 * (779/382) = 212px.
emb_h = 104
emb_w = int(w_emb * (emb_h / h_emb))
emb_resized = emb.resize((emb_w, emb_h), Image.Resampling.LANCZOS)

# Text: "GLOBAL" height = 40px
g_h = 40
g_w = int(p_global.size[0] * (g_h / p_global.size[1]))
g_resized = p_global.resize((g_w, g_h), Image.Resampling.LANCZOS)

# "ENTERPRISES" height = 24px in amber gold
e_h = 24
e_w = int(p_enterprises.size[0] * (e_h / p_enterprises.size[1]))
e_resized = p_enterprises.resize((e_w, e_h), Image.Resampling.LANCZOS)
e_gold = Image.new('RGBA', e_resized.size, (0, 0, 0, 0))
for y in range(e_resized.size[1]):
    for x in range(e_resized.size[0]):
        a = e_resized.getpixel((x, y))[3]
        if a > 0:
            e_gold.putpixel((x, y), (241, 140, 32, a))

# "YOUR TRUST, OUR PRIORITY" height = 16px in silver (#94a3b8)
t_h = 16
t_w = int(p_tagline.size[0] * (t_h / p_tagline.size[1]))
t_resized = p_tagline.resize((t_w, t_h), Image.Resampling.LANCZOS)
t_silver = Image.new('RGBA', t_resized.size, (0, 0, 0, 0))
for y in range(t_resized.size[1]):
    for x in range(t_resized.size[0]):
        a = t_resized.getpixel((x, y))[3]
        if a > 0:
            t_silver.putpixel((x, y), (148, 163, 184, a))

gap = 24
margin = 8
total_w = margin * 2 + emb_w + gap + max(g_w, e_w, t_w)
total_h = 120

out_im = Image.new('RGBA', (total_w, total_h), (0, 0, 0, 0))
out_im.paste(emb_resized, (margin, (total_h - emb_h)//2), emb_resized)

tx = margin + emb_w + gap
ty = (total_h - (g_h + 4 + e_h + 4 + t_h)) // 2
out_im.paste(g_resized, (tx, ty), g_resized)
out_im.paste(e_gold, (tx, ty + g_h + 4), e_gold)
out_im.paste(t_silver, (tx, ty + g_h + 4 + e_h + 4), t_silver)

out_im.save('assets/images/gsr-logo-stacked-horizontal.png')
out_im.save('assets/images/gsr-logo-stacked-horizontal.webp', quality=95)
print(f"Generated stacked horizontal logo: {total_w} x {total_h}")

# Also replace gsr-logo-white.webp with a crisp, updated version of this!
# Back up old gsr-logo-white.webp first
if not os.path.exists('assets/images/gsr-logo-white-old-vertical.webp'):
    import shutil
    shutil.copyfile('assets/images/gsr-logo-white.webp', 'assets/images/gsr-logo-white-old-vertical.webp')

out_im.save('assets/images/gsr-logo-white.webp', quality=95)
out_im.save('assets/images/gsr-logo-white.png')
print("Updated assets/images/gsr-logo-white.webp and .png with horizontal layout!")
