import os
from windows import system
from rich import print

pfw = system.wmi.query("SELECT LocalPath, Loaded FROM Win32_UserProfile WHERE '%' like LocalPath")
for ist in pfw:
    print(ist(LocalPath, Loaded))
    #----------------------------------------------------------------------
input('\nВыход :-> ')
os._exit(0)
