import os
from rich import print
from shutil import ignore_patterns,rmtree
from pprint import pp
MyPath = r'E:\DokinSergey\AppData\Local\Temp'
pathlist = []
if os.path.isdir(MyPath):
    for bpath in os.listdir(MyPath):
        print(bpath)
        pathlist.append(f'{MyPath}\\{bpath}')
        # if os.path.isdir(f'{MyPath}\\{bpath}'):
            # print(f'\tPath:>{bpath}')
        # elif os.path.isfile(f'{MyPath}\\{bpath}'):
            # print(f'\tfile:>{bpath}')
        # else: print(f'what is it:>{f'{MyPath}\\{bpath}'}')
#-----------------------------------------------------------
for ri in pathlist:
    if os.path.isdir(ri):
        print(f'Path:>{ri}')
    elif os.path.isfile(ri):
        pp(ri, width=160)
    else: print(f'what is it:>{ri}')
    # rmtree(ri, ignore_errors=True)