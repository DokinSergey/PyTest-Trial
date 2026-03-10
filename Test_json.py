import sys,time,traceback
# import datetime
from json import loads,dumps
# from ujson import loads,dumps
from rich import print as rpn
from typing import Any
## -------------------------------------------------------
File_str_json = r'D:\Work\Data\rphost_13320_25100211.log'
#######################################################################################################################
def LinePrs_JSON(_jline:str,_stn:int)->None:
    _tmstr:list[Any] = []
    try:
        _t0 = time.perf_counter()
        _ldict = loads(_jline)
        _t1 = time.perf_counter()
        dumps(_ldict)
        _t2 = time.perf_counter()
        # rpn(f'\t[cyan1]Строка [spring_green3]{_stn} [cyan1]длина [spring_green3]{len(_jline)} [cyan1]Время loads \
# [spring_green3]{_t1 -_t0:>7.7f} [cyan1]dumps [spring_green3]{_t2 -_t1:>7.7f}')
    except json.JSONDecodeError as Jerr:
        rpn(f'[orange_red1]{Jerr}')
        rpn(f'[orange_red1]{_stn}')
    except Exception as Expt:
        rpn(f'[orange_red1]{Expt} {_stn}')
        rpn(f'[orange_red1]{traceback.format_exc().splitlines()[-1]}')
##################################################################################################################
def FlPrs_SMB_jsn()->None:
    """Разбор файла чтние по протоколу samba но файлы тип json
    _fKey ключ _fVal значение из словаря FilePrs?"""
    _ResMain:list[Any] = []
    _t0 = time.perf_counter()
    _Nline = 0
    try:
        ##---------------------------------------------------------------------------------------------------------
        with open(File_str_json, mode='r', encoding = 'utf-8-sig',newline = '\r\n',buffering=1) as fn:
            for _row in fn:
                _Nline += 1
                ##-----------------------------------------------------------------
                LinePrs_JSON(_row,_Nline)
        ##-------------------------------------------------------------------------------------------------------------
        _t1 = time.perf_counter()
        rpn(f'{_Nline:7_} строк за ;{_t1 -_t0:>7.7f}')

    ##-----------------------------------------------------------------------------------------------------------------
    except Exception:
        rpn(f'{traceback.format_exc().splitlines()[-1]}')
##################################################################################################################
if __name__ == '__main__':
    debug = True
    _t0 = time.perf_counter()
    FlPrs_SMB_jsn()
    input(' :-)> ')
    sys.exit()
