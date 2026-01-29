import os,sys,time,traceback#,inspect
import asyncio
from rich import print as rpn
from psycopg import AsyncConnection,version as PGversion,Error as PGerr
from platform import python_version#,node
from datetime import datetime as dt#,date as ddate,time as dtime
#pylint: disable-msg=R1719
if (debug := True if len(sys.argv) > 1 and str(sys.argv[1]) in ('True','cons') else False):
    rpn(f'debug is [orange_red1]{debug}')
project = os.path.basename(__file__)
#pylint: enable-msg=R1719

##------------------------------------------
__author__  = 't.me/dokin_sergey'
__version__ = '0.0.1'
__verdate__ = '2025-09-23 17:14'
##-------------------------------------
PGconSTR:str = "dbname=dokin user=postgres password=postgres host=klin"
##-----------------------------------------------------------------------------------------
#######################################################################################################################
async def mainloop()->None:
    try:
        async with await AsyncConnection.connect(PGconSTR) as _aconn:
            sqltxt  =  "UPDATE public.fileid SET parsed=false, change=CURRENT_TIMESTAMP "
            sqltxt +=  "WHERE parsed AND typefile = 'json'and to_date(files,'YYMMDDHH24') < CURRENT_DATE - INTERVAL '0 days';"
            async with _aconn.cursor() as _PGSQL:
                rw = await _PGSQL.execute(sqltxt)
                await _aconn.commit()
                rl = rw.statusmessage.strip().split()
                rpn(rl)
                res = int(rl[1]) if len(rl) > 1 and rl[1].isdecimal() else 0
                rpn(f'2:{res = } {rw.statusmessage}')
            await _aconn.close()
    except PGerr as pgerr:
        rpn(f'ErPD1:{pgerr}')
        # rpn(f'ErPD12:{traceback.format_exc()}')
    except Exception as _err:
        rpn(f'Er1:{_err}')
        rpn(f'Er2:{traceback.format_exc()}')
        return False
    return True
###########################################################################################################
if __name__ == '__main__':
    if debug:
        dtnow = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        rpn(f'[cyan1]Start [green1]{dtnow} [cyan1]DeepKlin log 1C ver.[green1]{__version__} [cyan1]от [green1]{__verdate__}')
        rpn(f'[cyan1]Точка подключения [green1]{PGconSTR}')
        rpn(f'[cyan1]Start [green1]{project} [cyan1]Python: [green1]{python_version()}    [cyan1]psycopg: [green1]{PGversion.__version__}')
    try:
        start_time = time.perf_counter()
        if sys.platform == "win32":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(mainloop())
        stop_time = time.perf_counter()
        alltime = stop_time - start_time
        if debug:rpn(f'Работа приложения завершена за {alltime:>7.3f} секунд.')
    except BaseException as _err:
        if debug:rpn(f'{_err}')
        if debug:rpn(f'{traceback.format_exc()}')
    input('__main__ :-)> ')
    os._exit(0)
