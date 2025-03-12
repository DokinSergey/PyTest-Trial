import os
# import sqlite3
import traceback
import chardet
# from glob import glob
from rich import print as rpn
###################################################################################################
_author = 't.me/dokin_sergey'
_version = '1.0.0'
_verdate = '2024-10-30 13:07'
###################################################################################################
###################################################################################################
if __name__ == '__main__':
    rpn(f'[bright_blue]Перегрузка адресных книг из CSV в SQL Lite [green1]{_version} ')
    try:
        list_file=('Test_ANSI.txt','Test_UTF-8.txt','Test_UTF-8-BOM.txt',
        'Test_UTF-16 LE BOM.txt','Test_UTF-16 BE BOM.txt',)
        for filetst in list_file:
            with open(filetst,  mode='rb') as gc:
                rawdata = gc.read()
            rk = chardet.detect(rawdata)['encoding']
            rpn(f'\n[cyan1]Файл {filetst} Кодировка {rk = }')
            #----------------------------------------------------------------------
            with open(filetst, mode ='r', encoding = rk) as Hcfg:
                onestr = Hcfg.readlines()
            for istr in onestr:
                rpn(f'\t{istr.strip()}')
    except Exception as ErrMs:
        rpn(f'[red1]{ErrMs = }')
        rpn(f'[red1]{traceback.format_exc()}')
###################################################################################################
input('Выход:-> ')
os._exit(0)
