import os
# import sqlite3
import traceback
import chardet
# from glob import glob
from time import perf_counter
from rich import print as rpn
from charset_normalizer import detect
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
            t0 = perf_counter()
            rpn(f'\n[cyan1]Файл {filetst}')
            with open(filetst,  mode='rb') as gc:
                rawdata = gc.read()
            krk = chardet.detect(rawdata)
            t1 = perf_counter()
            rkraw = chardet.detect_all(rawdata)
            t2 = perf_counter()
            rk = rkraw[0]['encoding']
            trk1 = (t1 - t0) * 1000
            trk2 = (t2 - t1) * 1000
            for rki in rkraw:
                rpn(f'\t[bright_blue]Определена кодировка = [green1]{rki['encoding']} [bright_blue]С вероятность = \
[green1]{rki['confidence']:.3f} [bright_blue]язык = [green1]{rki['language']:11} [cyan1]{trk1:.3f}')
            rpn(f'\t{krk = } [cyan1]{trk2:.3f}')
        ## -------------------------------------------------------------------------------------------------------------
            t3 = perf_counter()
            # rpn(f'\n[cyan1]Файл {filetst}')
            with open(filetst,  mode='rb') as gc:
                rawdata = gc.read()
            rkr = detect(rawdata)
            t4 = perf_counter()
            # rk = rkr['encoding']
            trk3 = (t4 - t3) * 1000
            # rpn(f'\t[bright_blue]Определена кодировка = [green1]{rkr['encoding']} [bright_blue]С вероятность = \
# [green1]{rkr['confidence']:.3f} [bright_blue]язык = [green1]{rkr['language']:11} {trk2:.3f}')
            rpn(f'\t{rkr = } {trk3:.3f}')
            rpn()
        ## -------------------------------------------------------------------------------------------------------------
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
