import os

dirlist = []
defaultcwd = os.getcwd()

def rename(depth):
    print(os.getcwd(), depth)
    for name in os.listdir('./'):
        if not os.path.exists(name):
            continue
        if os.path.isdir(name) and name not in dirlist:
            dirlist.append(name)
            os.chdir(f'./{name}/')
            rename(depth+1)
        if os.path.isfile(name):
            size = os.path.getsize(name)
        ext = os.path.splitext(name)
        if ext[-1] == '.arc':
            if ext[0][-1] == 'L' and not os.path.exists('track_mp.arc'):
                os.rename(name, "track_mp.arc")
            elif not os.path.exists('track.arc'):
                os.rename(name, "track.arc")

        elif ext[-1] == '.json':
            if not os.path.exists("minimap.json") and name != 'minimap.json':
                os.rename(name, "minimap.json")

        elif ext[-1] == '.ght':
            if not os.path.exists("staffghost.ght") and name != "staffghost.ght":
                os.rename(name, "staffghost.ght")
            
        elif ext[-1] == '.ini':
            if os.path.exists('trackinfo.ini') and name != 'trackinfo.ini':
                continue
            os.rename(name, "trackinfo.ini")
            cwd = os.getcwd()
            cwd = bytes(cwd.split('\\')[-1], 'latin-1')
            with open('trackinfo.ini', 'r+b') as ini:
                pointer = 0x29
                ini.seek(pointer)
                part2 = ini.read()
                ini.seek(pointer)
                ini.write(cwd+part2)
                while pointer != -1:
                    ini.seek(pointer)
                    pointer += 1
                    part3 = ini.read(11)
                    ini.seek(pointer)
                    part4 = ini.read(17)
                    if part3 == b'replaces = ':
                        ini.seek(pointer+11)
                        last_part = ini.read()
                        ini.seek(pointer+11)
                        ini.write(cwd+last_part)
                    elif part4 == b'replaces_music = ':
                        ini.seek(pointer+17)
                        last_part = ini.read()
                        ini.seek(pointer+17)
                        ini.write(cwd+last_part)
                        pointer = -1
                        

        elif ext[-1] == '.bti':
            if size == 43296:
                os.rename(name, "track_big_logo.bti")
            elif size == 5216:
                os.rename(name, "track_small_logo.bti")
            elif size == 23584:
                os.rename(name, "track_image.bti")
            else:
                os.rename(name, "track_name.bti")
        elif ext[-1] == '.ast':
            if os.path.exists(normal):
                if os.path.exists(fast):
                    if os.path.getsize(normal) < os.path.getsize(fast):
                        os.rename(normal, 'temp.bak')
                        os.rename(name, normal)
                        os.rename('temp.bak', fast)
                elif os.path.getsize(normal) < size:
                    os.rename(normal, fast)
                    os.rename(name, normal)
            else:
                os.rename(name, normal)
    os.chdir('../')
    if os.getcwd() != defaultcwd:
        rename(depth-1)

normal = 'lap_music_normal.ast'
fast = 'lap_music_fast.ast'

rename(0)
