import os,sys,traceback#,time
from datetime import datetime as dt
from rich import print as rpn
###########################################################################################################
def test_error()->None:
    try:
        _ = 2/0
    except BaseException as _err:
        rpn(f'[red1]{_err}')
        rpn(f'[dark_orange]{traceback.format_exc().splitlines()[-1]}')
###########################################################################################################
if __name__ == '__main__':
    dtnow = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    rpn(f'[cyan1]Start [green1]{dtnow} [cyan1]Test Exit')
    test_error()
    input('__main__ :-)> ')
    if sys.platform != "win32":
        os._exit(0)
    else:
        sys.exit()
