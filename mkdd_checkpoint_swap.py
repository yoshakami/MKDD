def integerize(num):
    if num[:2] == "0x":
        num = int(num, 16)
    else:
        num = int(num)
    return num


# swap all left and right checkpoint coordinates
filename = input("bol file name : ")
start = input("start offset of first checkpoint in hex or decimal : ")
end = input("end offset of last checkpoint in hex or decimal : ")

with open(filename, "r+b") as file:
    while start < end:
        file.seek(start)
        j = file.read(12)
        file.seek(start + 12)
        k = file.read(12)
        file.seek(start + 12)
        file.write(j)
        file.seek(start)
        file.write(k)
        start = start + 28
    b = b"\x00\x00\x00\x00"
    while start < end:
        file.seek(start + 4)
        file.write(b)
        file.seek(start + 16)
        file.write(b)
        start = start + 28
