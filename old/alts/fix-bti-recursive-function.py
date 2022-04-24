import os

dirlist = []


def fix(directory):
    for name in os.listdir('./'):
        if not os.path.exists(name):
            return
        if os.path.isdir(name) and name not in dirlist:
            directory += 1
            dirlist.append(name)
            os.chdir(f'./{name}/')
            fix(directory)
        if os.path.isfile(name) and os.path.splitext(name)[-1] == ".bti":
            with open(name, "r+b") as bti:
                bti.seek(6)
                bti.write(b'\x00\x00')
    directory -= 1
    os.chdir('../')
    if directory >= 0:
        fix(directory)
    else:
        exit()

fix(0)