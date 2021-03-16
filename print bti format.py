import os

colourenc = ['I4', 'I8', 'IA4', 'IA8', 'RGB565', 'RGB5A3', 'RGBA8', 0, 'CI4', 'CI8', 'CI14x2', 0, 0, 0, 'CMPR']
for filename in os.listdir('./'):
    if not os.path.isfile(filename):
        continue
    with open(filename, "rb") as file:
        if os.path.splitext(filename)[-1] != ".bti":
            continue
        i = file.read(1)[0]
    print(f"{filename} is in {colourenc[i]} format")
print()
input("Press enter to exit.")
