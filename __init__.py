import os
import sys
import time
import traceback
import chardet

from datetime import datetime as dt
from rich import print as rpn
from glob import glob

__author__  = 't.me/dokin_sergey'
__version__ = '0.0.1'
__verdate__ = '2025-02-15 16:11'
mainpath = r'C:\1C_tech_log\sys'
tonetpath = r'C$\1C_tech_log\sys'
#############################################################################################################
def readfile(namefile):
    _txtbloc = ''
    try:
        with open(namefile,  mode='rb') as gc:
            rawdata = gc.read()
            rk = chardet.detect(rawdata)['encoding']
        with open(namefile, mode = 'r', encoding = rk) as fn:
            _txtbloc = fn.read()
    except Exception as ErrMs:
        rpn(f'\t[orchid]{ErrMs}')
        rpn(f'\t[orchid]{traceback.format_exc()}')
    return _txtbloc
#############################################################################################################
def readblok(_txtbloc):
    try:
        _listtxt = _txtbloc.splitlines()
        for strtxt in _listtxt:
            #rpn(strtxt.strip(','))
            yield strtxt.strip().split(',')
    except Exception as ErrMs:
        rpn(f'\t[orchid]{ErrMs}')
        rpn(f'\t[orchid]{traceback.format_exc()}')
#############################################################################################################
def main_proc():
    if listlog := glob(rf'{mainpath}\*\*.log', recursive=True):#,root_dir=mainpath
        try:
            for filename in listlog:
                reslist = []
                a,name = os.path.split(filename)
                reslist.append(a)
                b,_ = os.path.splitext(name)
                rpn(f'[khaki1]{filename}')
                ye = int(f'20{b[:2]}')
                mo = int(b[2:4])
                dn = int(b[4:6])
                ho = int(b[6:8])
                d = dt(int(b[:2]),int(b[2:4]),int(b[4:6]),int(b[6:]))
                # reslist.append(d)
                txtbloc = readfile(filename)
                for istr in readblok(txtbloc):
                    if all(stt in istr[0] for stt in ':-'):
                        c = istr[0].split('-')[0]
                        if c:
                            mm = int(c.split(':')[0])
                            ss = int(c.split(':')[1].split('.')[0])
                            ms = int(c.split(':')[1].split('.')[1])
                            print(dt(ye,mo,dn,ho,mm,ss,ms))
                        rpn(istr[1:])
                    else:
                        pass
                    # rpn(i[0])
                    input(' :-> ')
                # print(txtbloc)
                input(' :-> ')
        except Exception as ErrMs:
            rpn(f'\t[orchid]{c = }')
            rpn(f'\t[orchid]{ErrMs}')
            rpn(f'\t[orchid]{traceback.format_exc()}')
#############################################################################################################
if __name__ == '__main__':
    mess = f'Автономный тест модуля работы с файлами ver {__version__} от {__verdate__} файл {__file__}'
    PROJECT = 'Test_OMC_Customer'
    UserProject = os.getlogin()
    # LoggingInit(PROJECT,UserProject)
    # LogErrDebug('Message',f'{_mess}',__name__)
    #-----------------------------------------------------------------------------------------
    start_time = time.perf_counter()
    # asyncio.run(main())
    main_proc()
    stop_time =  time.perf_counter()
    Inetrval = stop_time - start_time
    print(f'\nОбщее время выполнения {Inetrval:.7f}')
else:
    pass
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
