import sys,os
for i in range(1, len(sys.argv)):
    os.system(f'wimgt encode "{sys.argv[i]}" -x bti.cmpr --n-mm 0 -o -d "{os.path.splitext(sys.argv[i])[0]}.bti"')