import os
# import sqlite3
import traceback
import chardet
# from glob import glob
from rich import print as rpn
###################################################################################################
_author = 't.me/dokin_sergey'
_version = '1.0.1'
_verdate = '2024-10-30 13:07'
###################################################################################################
###################################################################################################
if __name__ == '__main__':
    rpn(f'[bright_blue]Перегрузка адресных книг из CSV в SQL Lite [green1]{_version} ')
    try:
        list_file=('Test_ANSI.txt','Test_UTF-8.txt','Test_UTF-8-BOM.txt',
        'Test_UTF-16 LE BOM.txt','Test_UTF-16 BE BOM.txt',)
        for filetst in list_file:
            rpn(f'\n[cyan1]Файл {filetst}')
            with open(filetst,  mode='rb') as gc:
                rawdata = gc.read()
            rkraw = chardet.detect_all(rawdata)
            rk = rkraw[0]['encoding']
            for rki in rkraw:
                rpn(f'\t[bright_blue]Определена кодировка = [green1]{rki['encoding']} [bright_blue]С вероятность = \
[green1]{rki['confidence']:.3f} [bright_blue]язык = [green1]{rki['language']}')
            #----------------------------------------------------------------------
            rpn()
            with open(filetst, mode ='r', encoding = rk) as Hcfg:
                onestr = Hcfg.readlines()
            cl = '[light_green]'
            for istr in onestr:
                if '[dark_orange]' in istr.strip():cl = ''
                rpn(f'\t\t{cl}{istr.strip()}')
    except Exception as ErrMs:
        rpn(f'[red1]{ErrMs = }')
        rpn(f'[red1]{traceback.format_exc()}')
###################################################################################################
input('Выход:-> ')
os._exit(0)
