import os
a = b"\x00"
for g in os.listdir('./'):
    if not os.path.isfile(g):
        continue
    if (g.split('.')[-1] != "bti"):
        continue
    fh = open(g, "r+b")
    fh.seek(0x06)
    fh.write(a)
    fh.seek(0x07)
    fh.write(a)
    fh.close()