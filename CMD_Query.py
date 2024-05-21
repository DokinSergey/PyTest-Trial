import os
import time
import traceback
from subprocess import Popen, PIPE,SubprocessError,TimeoutExpired
from rich import print
#---------------------------------------------------
_AUTHOR  = 't.me/dokin_sergey'
_VERSION = '1.1.1'
_VERDATE = '2024-01-22 11:58'
######################################################################################
def GetqueryUser(ServerTerm:str, UserTrm:str = ''):
    res = {}
    psstr = f'query user {UserTrm} /server:{ServerTerm}'
    # print(psstr)
    try:
        with Popen(['cmd','/C', psstr], stdout = PIPE, stderr = PIPE) as popps:
            pls = popps.communicate(timeout=15)
        if bool(pls[1]):
            print(pls[1].decode('cp866'))
        else:
            # print(pls[0].decode('cp866'))
            lstr = pls[0].decode('cp866').splitlines
            for nl,il in enumerate(lstr()):
                if nl:
                    print(il)
                    # print(f'{il[:22].strip()}-{il[23:39].strip()}-{il[40:45].strip()}-{il[46:53]}-{il[54:64]}-{il[65:]}-' )
                    print(f'{il[:22].strip()}-{il[40:45].strip()}-{il[46:53].strip()}-{il[65:].strip()}-' )
                    res[il[:22].strip()] = (il[40:45].strip(),il[46:53].strip(),il[65:].strip())
            print(res)
    except TimeoutExpired as Mess:
        print(str(Mess))
        print(pls)
        print(str(Mess))
    except Exception as Mess:
        print(str(Mess))
    return res
#-------------------------------------------------------------------------------------------------------
def GetqueryProc(ServerTerm:str, UserTrm:str = ''):
    res = {}
    psstr = f'query process {UserTrm} /server:{ServerTerm}'
    # print(psstr)
    try:
        with Popen(['cmd','/C', psstr], stdout = PIPE, stderr = PIPE) as popps:
            pls = popps.communicate(timeout=15)
        if bool(pls[1]):
            print(pls[1].decode('cp866'))
        else:
            # print(pls[0].decode('cp866'))
            lstr = pls[0].decode('cp866').splitlines
            for nl,il in enumerate(lstr()):
                if nl:
                    # print(il)
                    # print(f'{il[:22].strip()}-{il[23:39].strip()}-{il[40:45].strip()}-{il[46:53]}-{il[54:64]}-{il[65:]}-' )
                    print(f'{il[:22].strip()}-{il[40:45].strip()}-{il[46:53].strip()}-{il[65:].strip()}-' )
                    res[il[:22].strip()] = (il[40:45].strip(),il[46:53].strip(),il[65:].strip())
            print(res)
    except TimeoutExpired as Mess:
        print(str(Mess))
        print(pls)
        print(str(Mess))
    except Exception as Mess:
        print(str(Mess))
        # res.err = 1
        # LogErrDebug(f'Ошибка ; {Mess} ; {traceback.format_exc()}','')
    return res
#-------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    _mess = f"Автономный тест общего модуля ver: {_VERSION}; от: {_VERDATE} ; автор {_AUTHOR}"
    print(_mess)
    resq = GetqueryUser('cloud')
    # print(resq)
