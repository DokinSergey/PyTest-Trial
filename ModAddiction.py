# pylint: disable-msg=W0602
import os,traceback,platform
from rich import print as rpn
from glob import glob
# from time import sleep#perf_counter,
# from subprocess import Popen, PIPE,TimeoutExpired#,SubprocessError
from datetime import datetime,timezone,date,timedelta
###########################################################################################################################
_author  = 't.me/dokin_sergey'
_version = '1.1.0'
_verdate = '2024-07-29 22:04'
_LogLocPath = os.path.dirname(__file__)
_GlobaLen = 120
#----------------------------------------------------------------------------------
modexset = set()
modinset = set()
def_dict:dict  = {}
loclmod:tuple = ()
#----------------------------------------------------------------------------------
try:
    _LogFile  = fr'{_LogLocPath}\ModAddict_{str(date.today())}.txt'
    _ListModl = fr'{_LogLocPath}\ModuList.txt'
except Exception as EMess:
    rpn(f'Ошибка: [orchid]{EMess}')
    rpn(f'Ошибка: [orchid]{traceback.format_exc()}')
#----------------------------------------------------------------------------------
class DokExcept(Exception):
    def __init__(self, message:str):
        super().__init__(message)
#-------------------------------------
debug = False
#####################################################################################################################################################
def WordRead(Wrd:str)->bool:
    Wres = False
    if   Wrd.isalnum():
        Wres = True
    else:
        for iw in Wrd:
            if (ord(iw) in range(33,125)) or (ord(iw) in range(192,255)):
                Wres = True
                break
    return Wres
################################################################################################################################################################
def FileWrite(FlName:str,NetStr:str,WMess:tuple[str,...])->bool:# = '',LMess:tuple[str] = ())->bool:
    try:
        with open(FlName, mode = 'a', encoding = 'utf_8') as fwl:
            for istr in WMess:
                print(f'{NetStr}{istr}', file = fwl)
    except Exception as FMess:
        LogErrDebug('Failure',f'{FMess}','FileWrite')
        LogErrDebug('Failure',f'{traceback.format_exc()}','FileWrite')
        print(f'Ошибка: {FMess}')
        print(f'Ошибка: {traceback.format_exc()}')
        return False
    return True
################################################################################################################################################################
def LogErrDebug(Mess1:str,Mess2:str, Mess3:str = '')->bool:
    TypeMess = ('Warning','Failure','Update_','Install','Message','ErroCMD')#Caution
    if len(Mess1) == 7 and Mess1 in TypeMess:
        TMess = Mess1#+' '
        RMess = Mess2
        Funct = Mess3
    else:
        TMess = 'Message'
        RMess = Mess1
        Funct = Mess2
    ListMess = []
    try:
        dtnow = datetime.now(timezone.utc) + timedelta(hours=3)
        dtstr = dtnow.strftime("%H:%M:%S")
        PrnStr = f'{dtstr};{TMess};'
        lFN = 12
        FN = f'{Funct:{lFN}} ;' if Funct else f'{" ":{lFN}} ; '
        PrnStr += FN
        ListStr = str(RMess).splitlines()
        tstr = ''
        for iStr in ListStr:
            if iStr and not iStr.isspace():
                ListWr = iStr.split()
                for iLW in ListWr:
                    if iLW:# and WordRead(iLW):
                        tstr += f' {iLW}'
                    if len(tstr) >_GlobaLen+1:
                        ListMess.append(tstr)
                        tstr = ''
        if tstr: ListMess.append(tstr)
    #---------------------------------------------------------------------------------------------------------------------------
        TupleMess = tuple(ListMess)
        if _LogFile:
            FileWrite(_LogFile,PrnStr,TupleMess)
        #------------------------------------------------------------------------------------------------
        if debug: rpn(f'{dtstr} ; [yellow]{RMess}')
    except Exception as Err:
        Led = False
        rpn(f'Ошибка: [orchid]{Err}')
    else:
        Led = True
    return Led
####################################################################################################################################
def parseimport(imstr:str):
    global modexset,modinset
    _tlist = imstr.split()[1].split(',')
    for _str in _tlist:
        if _str in loclmod:
            modinset.add(_str)
        else:
            modexset.add(_str)
###################################################################################################################################
def parsedef(instr:str,modname:str):
    global def_dict
    _str = instr.split(' ',1)[1]
    if _str.startswith('_'):return
    _tlist = _str.split(sep = r')')[0].split(sep = r'(')
    def_dict[_tlist[0]] = [modname,]
    def_dict[_tlist[0]] += (_tlist[1].split(','))
    return
###################################################################################################################################
def ModulPars(parsfile:str):
    rpn(parsfile)
    try:
        #----------------------------------------------------------------
        with  open(parsfile, mode = 'r', encoding = 'utf_8') as sfl:
            filetxt = sfl.readlines()
        #----------------------------------------------------------------
        for ist in filetxt:
            tstr = ist.strip()
            if tstr:
                if tstr.startswith('#'):continue
                if tstr.startswith('import') or tstr.startswith('from'):parseimport(tstr)
                if tstr.startswith('def'):parsedef(tstr,parsfile)
                    # rpn(f'\tfunct:{tstr}')
    except Exception as MErs:
        LogErrDebug('Failure',f'{MErs}','cmdexecNoOut')
        LogErrDebug('Failure',f'{traceback.format_exc()}','cmdexecNoOut')
        print(f'{MErs}')
        print(f'{traceback.format_exc()}')
####################################################################################################################################
if __name__ == '__main__':
    print(f'установки связностей проектов вер.{_version} для Python ver.{platform.python_version()}')
    #----------------------------------------------------------------------------------------------------------------------
    FileWrite(_LogFile,'',('*'*(_GlobaLen+20),))
    LogErrDebug('Message',f'Программы установки связностей проектов: {_version} ; от {_verdate} ; Автор {_author} ; ', os.path.basename(__file__))
    LogErrDebug('Message',f'Установлен Python ver.{platform.python_version()} ; {platform.python_build()[1]} ; {platform.python_compiler()}', os.path.basename(__file__))
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    projpath = r'C:\Dev\Py_OMC_Customer'
    os.chdir(projpath)
    filist = glob('*.py', root_dir=projpath)
    loclmod = tuple(os.path.splitext(fn)[0] for fn in filist)
    # rpn(filist)
    # rpn(type(loclmod),loclmod)
    #--------------------------------------------------------------------------------------------------------------

    for tfile in filist:
        ModulPars(tfile)
    rpn(f'{modexset = }')
    rpn(f'{modinset = }')
    for _idd, _ivv in def_dict.items():
        rpn(f'{_idd:20}: {_ivv}')
    #----------------------------------------------------------------------
    input('\nВыход :-> ')
    os._exit(0)
