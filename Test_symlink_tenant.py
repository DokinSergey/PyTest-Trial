import os
import traceback
try:
    usercfg   = r'\\tenant-fs-01\ibases\omp26113\1cestart_omp2611301.cfg'
    UserGfg1C = r'\\zir-vds-01.tenant.local\E$\omp2611301\AppData\Roaming\1C\1CEStart\1cestart.cfg'
    os.symlink(usercfg,UserGfg1C)
except Exception as ErrMs:
    print(f'{ErrMs}')
    print(f'{traceback.format_exc()}')
input(' :-)> ')
