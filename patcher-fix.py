import os


def rename(name):
    if not os.path.exists(name) or not os.path.isfile(name):
        return
    ext = os.path.splitext(name)
    size = os.path.getsize(name)
    if ext[-1] == '.arc':
        if ext[0][-1] == 'L':
            os.rename(name, "track_mp.arc")
        else:
            os.rename(name, "track.arc")

    elif ext[-1] == '.json':
        os.rename(name, "minimap.json")

    elif ext[-1] == '.ght':
        os.rename(name, "staffghost.ght")

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
        if os.path.exists('lap_music_normal.ast'):
            if os.path.getsize('lap_music_normal.ast') < size:
                os.rename('lap_music_normal.ast', 'lap_music_fast.ast')
        os.rename(name, "lap_music_normal.ast")


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
                                                                            rename(file)
                                                                        os.chdir('../')
                                                                    rename(file)
                                                                os.chdir('../')
                                                            rename(file)
                                                        os.chdir('../')
                                                    rename(file)
                                                os.chdir('../')
                                            rename(file)
                                        os.chdir('../')
                                    rename(file)
                                os.chdir('../')
                            rename(file)
                        os.chdir('../')
                    rename(file)
                os.chdir('../')
            rename(file)
        os.chdir('../')
    rename(file)
# 9 subfolders
