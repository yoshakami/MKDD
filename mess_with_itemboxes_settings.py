import os
import random

with open("./track/babyluigi_course.bol", "r+b") as bol:
    count = -1
    bol.seek(0x54)
    byte = bol.read(4)
    cursor = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
    byte = bol.read(4)
    max_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
    while cursor < max_offset:  # number of itemboxes
        bol.seek(cursor + 8)
        bol.seek(cursor + 0x24)
        object_type = bol.read(2)
        # print(object_type)
        if object_type != b'\x00\x01':  # the object isn't an itembox
            cursor += 0x40
            continue
        count += 1
        bol.seek(cursor + 0x30)
        # print(cursor)
        bol.write(bytes(chr(0), 'latin-1'))
        bol.write(bytes(chr(0x87), 'latin-1'))
        print(f"changed {count} itemboxes at offset {cursor}")
        bol.write(bytes(chr(0), 'latin-1'))
        #bol.write(bytes(chr(random.choice((1, 3))), 'latin-1'))
        bol.write(bytes(chr(1), 'latin-1'))
        bol.write(bytes(chr(0), 'latin-1'))
        bol.write(bytes(chr(0), 'latin-1'))
        bol.write(bytes(chr(count//256), 'latin-1'))
        bol.write(bytes(chr(count%256), 'latin-1'))
        for i in range(8):
            bol.write(bytes(chr(0), 'latin-1'))

        """
        bol.write(bytes(chr(0), 'latin-1'))
        bol.write(bytes(chr(0), 'latin-1'))
        bol.write(bytes(chr(0), 'latin-1'))
        number = bytes(chr(random.randint(0, 255)), 'latin-1')
        bol.write(number * 13)
        print(f"changed {count} itemboxes at offset {cursor}")
        bol.write(bytes(chr(random.randint(0, 255)), 'latin-1'))
        for i in range(12):
            bol.write(bytes(chr(random.randint(0, 255)), 'latin-1'))"""
        cursor += 0x40