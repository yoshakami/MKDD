import os

bti_name, bti = [0], [0]
name, position, = [], []
add_png = keep = filetype = file = header = 0
colourenc = ['I4', 'I8', 'IA4', 'IA8', 'RGB565', 'RGB5A3', 'RGBA8', 0, 'CI4', 'CI8', 'CI14x2', 0, 0, 0, 'CMPR']
count = 0


def message():
    print("\n\na number was intended or there are less textures than your number,")
    print("count the texture position by dumping them.\n\nthe number can be negative if you start counting by the bottom\n")


def tex_list(file_jpa):
    print("Texture Name List :")
    with open(file_jpa, 'rb') as jpa:
        for n in range(1, len(bti)):
            jpa.seek((bti[n]) + 2)
            tex_dim = jpa.read(4)
            print(f'{n} - ({tex_dim[0] * 256 + tex_dim[1]}x{tex_dim[2] * 256 + tex_dim[3]}) - {bti_name[n]}')


def dump(jpa_file, number, filesize):
    if not os.path.exists("jpaeffect Dumped Textures"):
        os.mkdir("jpaeffect Dumped Textures")

    with open(jpa_file, 'rb') as jpa:
        for k in range(1, len(bti) - 1):
            jpa.seek(bti[k])
            with open(f'./jpaeffect Dumped Textures/{k} - {bti_name[k]}.bti', 'wb') as dmp:
                dmp.write(jpa.read(bti[k + 1] - bti[k] - 32))
        jpa.seek(bti[-1])
        with open(f'./jpaeffect Dumped Textures/{len(bti) - 1} - {bti_name[-1]}.bti', 'wb') as dmp_final:
            dmp_final.write(jpa.read(filesize - bti[-1]))

    os.chdir("./jpaeffect Dumped Textures")
    if not os.path.exists("png"):
        os.mkdir("png")
    input(f'\nDumped {number} bti in "jpaeffect Dumped Textures"\n\npress enter to convert them to png...')

    for x in range(1, len(bti)):
        os.system(f'wimgt decode "{x} - {bti_name[x]}.bti" -d "./png/{x} - {bti_name[x]}.png" -o')


mode = 1
for file in os.listdir('./'):
    if not os.path.isfile(file) or os.path.getsize(file) < 4:
        continue
    with open(file, 'rb') as stuff:
        header = stuff.read(3)
    if header == b"JPA":
        break

if header != b"JPA":  # the first "for" loop can ends after browsing a complete directory without finding any jpa file.
    keep2 = input('no jpa file found in current directory, type type 2 to continue and keep the encoded textures when the program ends.\n')
    if keep2 == 2:
        keep = True
    mode = 0

if mode != 0:
    mode = input(f"\nreplacing in {file}\n\npress enter to continue (don't keep encoded textures) or\n- type 1 if that's not the file you want\n- type 2 to continue and keep the encoded textures when the program ends\n- type 3 if that's not the file you want and you want to keep the encoded textures\n- type 4 to dump all bti images in the jpa file before continuing\n- type 5 to view a list of all bti names before continuing\n\nYour choice : ")

if mode in ['2', '3']:  # keep encoded textures
    keep = True
while mode in ["0", "1", "3"]:  # that's not the file you want, so type manually the filename
    file = input('jpa file name with extension : ')
    if not os.path.exists(file):
        continue
    with open(file, 'rb') as check:
        if check.read(3) != b"JPA":
            input('this file is not a jpa, press enter to continue or type anything else to choose another file.')
        else:
            mode = '0'

with open(file, 'r+b') as arc:  # arc = archive
    size = cursor = os.path.getsize(file)
    if '_' in file:
        short = file.rsplit('_', 1)[0]
    elif '.' in file:
        short = os.path.splitext(file)[0]
    else:
        short = file  # short has high probabilities to be the name used in the filesystem of the game
    print('Spotting all texture offsets in the file, please wait...')  # in case it's long
    for z in range(0, size - 17, 16):  # list of all the textures offsets
        arc.seek(z)
        header = arc.read(4)
        if header == b'TEX1':
            current_bti_name = ''
            count += 1
            arc.seek(z + 12)
            letter = arc.read(1)
            while letter != b'\x00':
                current_bti_name += str(letter)[2:-1]
                letter = arc.read(1)
            bti_name.append(current_bti_name)
            bti.append(z + 32)  # add a bti file offset to the texture list
    cmd_list = []
    if mode == "4":
        dump(file, count, size)
    if mode == "5":
        tex_list(file)
    while add_png != '1':  # while user enters a wrong name
        picture = input('png name with extension : ')  # remember quote is a forbidden character in windows
        picture = picture.strip('"')  # if you drag and drop it adds quotes and create a name that doesn't exists
        if not os.path.exists(picture):  # yes, python considers quotes as part of a file name
            print(f'{picture} was not found in the current working directory.\na png picture is intended.')
            continue
        with open(f'{picture}', 'r+b') as png:
            header = png.read(4)
        if header != b'\x89PNG':
            print("This file isn't a png.")
            continue
        while header != 1:  # while user enters a wrong number
            pos = input('texture position : ')
            if pos in ['0', '-0', '']:
                print("Error: the number can't be 0 (it can be -1 or -2 and more if you start counting by the bottom)")
            elif pos.lstrip('-').isdigit():
                if int(pos.lstrip('-')) > len(bti):  # if position entered is greater than the max number of bti found
                    message()
                    continue
                header = 1  # position entered is valid
                pos = int(pos)
            else:
                message()
        name.append(picture)
        position.append(pos)
        print()  # creates a blank line in cmd, else it looks too compressed
        offset = bti[pos] + 24
        arc.seek(offset)
        nmipmap = arc.read(1)[0] - 1  # the 24th byte of a bti file is the number of mipmaps +1
        #  print(f"number of mipmaps : {nmipmap}")
        arc.seek(offset - 24)  # a mipmap is a duplicate of a texture downscaled by 2, used when far away
        colour = arc.read(1)[0]  # to use less RAM, and also looks better visually when far away (not distorted)
        #  print(f'{colourenc[colour]} ++ {offset}')
        cmd_list.append(f'wimgt encode "{picture}" -x BTI.{colourenc[colour]} --n-mm {nmipmap} -o')
        print('press 1 then enter to encode all textures')
        add_png = input('or type anything else to add another png\n')
        if add_png == '1':
            for command in cmd_list:
                os.system(command)
    # ^ while add_png != 1 ^
    # wimgt will convert all png to encoded texture files called bti
    # print(cmd_list)
    for i in range(len(name)):  # replace textures in the file by the png given
        tex_name = name[i].rstrip('.png')
        pos = position[i]
        with open(tex_name, 'rb') as texture:
            if bti[i] == bti[-1]:
                tex_size = bti[pos] - size
            else:
                tex_size = bti[pos + 1] - bti[pos] - 32
            tex = texture.read()  # tex is actually the whole content of the custom bti
            texture.seek(2)  # the third byte of a bti file is the offset of dimensions
            dim_tex = texture.read(4)  # 2 bytes integer for width then height
            arc.seek(bti[pos] + 2)
            arc_tex_dim = arc.read(4)
        if dim_tex != arc_tex_dim:  # don't replace vanilla texture if the custom one doesn't have the same size
            input(f'{picture} is {dim_tex[0] * 256 + dim_tex[1]}x{dim_tex[2] * 256 + dim_tex[3]} while {file} texture is {arc_tex_dim[0] * 256 + arc_tex_dim[1]}x{arc_tex_dim[2] * 256 + arc_tex_dim[3]}\nDid you learned maths ???\n\nPress enter to replace all other textures.\n')
            continue
        arc.seek(bti[pos])
        arc.write(tex)  # custom texture data

commands = cmd_list[1:]
if not keep:
    for line in commands:
        if line.startswith("del "):
            continue
        texname = line.split('wimgt encode ')[1]
        texname = texname.split('.png')[0]
        os.system(f'del {texname}"')
print("done !")
