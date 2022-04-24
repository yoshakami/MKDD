import os
for g in os.listdir('./'):
    if os.path.isdir(g):
        os.chdir(f'./{g}/')
        for g in os.listdir(f'./'):
            if os.path.isfile(g) and os.path.splitext(g)[-1] == ".bti":
                with open(g, "r+b") as bti:
                    bti.seek(6)
                    bti.write(b'\x00\x00')
        os.chdir('../')
    if os.path.isfile(g) and os.path.splitext(g)[-1] == ".bti":
        with open(g, "r+b") as bti:
            bti.seek(6)
            bti.write(b'\x00\x00')
