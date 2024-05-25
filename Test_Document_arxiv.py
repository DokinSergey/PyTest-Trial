import os
from shutil import rmtree,make_archive,copytree,ignore_patterns#copy2,
from time import perf_counter,sleep
from rich import print
import traceback
#--------------------------------------------------------------
start_time = tick_time_1 = tick_time_2 = perf_counter()
Profile = r'C:\Users\dokin'
CurPath = os.path.realpath('')
Ts1Path = os.path.join(os.path.dirname(CurPath),'TestDir1')
Ts2Path = os.path.join(Ts1Path,'TestDir2')
try:
    if not os.path.isdir(Ts2Path):
        os.makedirs(Ts2Path,exist_ok=True)
    Documnt = os.path.join(Profile,'Documents')
    Docutmp = os.path.join(Profile,'Docum_tmp')
    ipatt = ignore_patterns('*.lnk', '*.url', '*.ini','Мои видеозаписи','мои рисунки', 'Моя музыка', 'Visual Studio*','WindowsPowerShell','SQL Server*' )
    copytree(Documnt,Docutmp,ignore=ipatt,dirs_exist_ok=True)
    tick_time_1 = perf_counter()
    print(intr1 := tick_time_1 - start_time)
    print(base_name := os.path.join(Ts2Path, 'zip'))
    # make_archive(base_name, 'zip', Docutmp)
    # rmtree(Docutmp,ignore_errors = True)
    tick_time_2 = perf_counter()
    print(intr2 := tick_time_2 - tick_time_1)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
except Exception as DErr:
    print(f'\t[orchid]{DErr}')
    print(f'\t[bright_yellow]{traceback.format_exc()}')
#--------------------------------------------------------------------------------------
input(':-> ')
# rmtree(Ts1Path)
os._exit(0)
