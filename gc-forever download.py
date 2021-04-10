done = False
try:
    import requests

    done = True
except:
    html = input("you should install requests module in cmd by typing 'pip install requests'\n or specify a html file version of the page here: ")

j = 1
if done:
    link = input("paste a gc-forever forum link here : ")
    link = link.split("&start")[0]
    req = requests.get(link)
    data = req.content
else:
    with open(html, 'rb') as file:
        data = file.read()
post = b' posts\n\t\t\t\t\t\t\t'
for i in range(len(data)):
    if data[i:i + 14] == post:
        while data[i - j] != 9:
            j += 1
        size = int(data[i - j + 1:i])
        print("The total number of posts is " + str(size))
        break
current_post = size // 25 + 2


def writecodes():
    gecko = False
    with open('GameID.ini', "r+b") as config:
        config.seek(0, 2)
        for indice in range(len(data)):
            k = 1
            if data[indice:indice + 114] == b'<div class="codebox"><p>Code: <a href="#" onclick="selectCode(this); return false;">Select all</a></p><pre><code>\n':
                # print('found')
                while b'</code>' not in data[indice:indice + k]:
                    k += 1
                code = data[indice + 114:indice + k - 7]#)[2:-1]
                codelines = code.splitlines()
                # if n ==0:
                #    print(codelines)
                current = -1
                for line in codelines:
                    current += 1
                    if b'[' in line:  # and (len(codelines[current + 1]) == len(codelines[current + 2]) or len(codelines[current + 2]) < 2):
                        config.write(b'\r\n$' + line + b'\r\n')
                        gecko = True
                    elif gecko:
                        if len(line) < 2:
                            gecko = False
                            continue
                        config.write(line + b'\r\n')
                    else:
                        if len(line) < 2:
                            continue
                        config.write(b'*' + line + b'\r\n')

print("creating GameID.ini ...")

with open('GameID.ini', "wb") as ini:
    ini.write(b"# some codes may be duplicates (because they don't have the same name)\r\n\r\n")
    if b'(GCN/AR/' in data:
        ini.write(b'[ActionReplay]')
    else:
        ini.write(b'[Gecko]')

if not done:
    writecodes()
    exit()

for n in range(current_post):
    req = requests.get(link + f"&start={n * 25}")
    data = req.content
    writecodes()

input('\ndone!\npress enter to exit...\n')