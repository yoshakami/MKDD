import os

colourenc = ['I4', 'I8', 'IA4', 'IA8', 'RGB565', 'RGB5A3', 'RGBA8', 0, 'CI4', 'CI8', 'CI14x2', 0, 0, 0, 'CMPR']


def fix(name):
    if not os.path.exists(name) or not os.path.isfile(name):
        return
    if os.path.getsize(name) < 30:
        return
    with open(name, 'r+b') as bti:
        colour = bti.read(1)[0]
        bti.seek(0x10)
        nooll = bti.read(12)
        if 0 <= colour < 15 and colour not in [7, 11, 12, 13] and nooll[0:4] == b"\x00\x00\x00\x00" and nool[6:8] == b'\x00\x00' and nool[9:12] == b'\x00\x00\x00':
            bti.seek(6)
            bti.write(b'\x00\x00')


for file in os.listdir('./'):
    if os.path.isdir(file):
        os.chdir(f'./{file}/')
        for file in os.listdir('./'):
            if os.path.isdir(file):
                os.chdir(f'./{file}/')
                for file in os.listdir('./'):
                    if os.path.isdir(file):
                        os.chdir(f'./{file}/')
                        for file in os.listdir('./'):
                            if os.path.isdir(file):
                                os.chdir(f'./{file}/')
                                for file in os.listdir('./'):
                                    if os.path.isdir(file):
                                        os.chdir(f'./{file}/')
                                        for file in os.listdir('./'):
                                            if os.path.isdir(file):
                                                os.chdir(f'./{file}/')
                                                for file in os.listdir('./'):
                                                    if os.path.isdir(file):
                                                        os.chdir(f'./{file}/')
                                                        for file in os.listdir('./'):
                                                            if os.path.isdir(file):
                                                                os.chdir(f'./{file}/')
                                                                for file in os.listdir('./'):
                                                                    if os.path.isdir(file):
                                                                        os.chdir(f'./{file}/')
                                                                        for file in os.listdir('./'):
                                                                            fix(file)
                                                                        os.chdir('../')
                                                                    fix(file)
                                                                os.chdir('../')
                                                            fix(file)
                                                        os.chdir('../')
                                                    fix(file)
                                                os.chdir('../')
                                            fix(file)
                                        os.chdir('../')
                                    fix(file)
                                os.chdir('../')
                            fix(file)
                        os.chdir('../')
                    fix(file)
                os.chdir('../')
            fix(file)
        os.chdir('../')
    fix(file)
# 9 subfolders
