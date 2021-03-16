import os

colourenc = ['I4', 'I8', 'IA4', 'IA8', 'RGB565', 'RGB5A3', 'RGBA8', 0, 'CI4', 'CI8', 'CI14x2', 0, 0, 0, 'CMPR']
wrap = ["clamp to edge", "repeat", "mirror"]
for filename in os.listdir('./'):
    if not os.path.exists(filename) or not os.path.isfile(filename):
        continue
    if os.path.getsize(filename) < 30:
        continue
    with open(filename, "rb") as file:
        colour = bti.read(1)[0]
        bti.seek(0x10)
        nooll = bti.read(12)
        if 0 <= colour < 15 and colour not in [7, 11, 12, 13] and nooll[0:4] == b"\x00\x00\x00\x00" and nool[6:8] == b'\x00\x00' and nool[9:12] == b'\x00\x00\x00':
            i = file.read(1)[0]
            alpha = file.read(1)[0]
            tex_dim = file.read(4)
            wrap_s = file.read(1)[0]
            wrap_t = file.read(1)[0]
            file.seek(24)
            mip = file.read(1)[0]
        if alpha == 0:
            alpha = "disabled"
        else:
            alpha = "enabled"
    print(f'{filename} - ({tex_dim[0] * 256 + tex_dim[1]}x{tex_dim[2] * 256 + tex_dim[3]}) - BTI.{colourenc[i]} format - has {mip} mipmaps - alpha {alpha} - Wrap horizontal "{wrap[wrap_s]}" - Wrap Vertical "{wrap[wrap_t]}"\n')
print()
input("Press enter to exit.")
