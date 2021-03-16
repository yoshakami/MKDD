import sys,os
for i in range(1, len(sys.argv)):
    os.system(f'wimgt decode "{sys.argv[i]}"')