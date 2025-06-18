import os
import time
import traceback
# import chardet
import asyncio
from typing import Any
from psycopg import AsyncConnection#,Error as PGerr
# from datetime import datetime as dt#timedelta,date,
# from Logg import Logging
from rich import print as rpn
##############################################################################################################
async def ParsingPath (aconn:AsyncConnection[tuple[Any, ...]])->None:
    try:
        servers,paths,files = ('SH-1C-02','rphost_10600','25060908')
        ##----------------------------------------------------------------------------------------------
        async with aconn.cursor() as APGSQL:
            sqltxt1  = f"SELECT idf, parsed FROM filesindex WHERE servers like '{servers}' and paths like '{paths}' and files like '{files}';"
            await APGSQL.execute(sqltxt1)
            ft1 = await APGSQL.fetchall()
        rpn(f'[purple]{servers = } {paths = } {files =} ')
        rpn(f'[purple]{ft1 = }')
        input(' :-)> ')
        if len(ft1) == 1:#то что надо, одно значение
            fid = ft1[0][0]
            sqltxt = f"SELECT max(nline) FROM logs1c WHERE idfiles = {fid} group by idfiles;"
            rpn(sqltxt)
            async with aconn.cursor() as BPGSQL:
                rpn('1')
                await BPGSQL.execute(sqltxt)
                rpn('2')
                ft = await BPGSQL.fetchone()
                rpn('3')
            rpn(sqltxt)
            rpn(f'[yellow]{ft = }')
            input(' :-)> ')
    except BaseException as _err:
        # rpn('ErrMess',f'[khaki1]{dwt = }')
        rpn('ErrMess',f'[khaki1]sqltxt = {sqltxt}')
        rpn('ErrMess',f'[purple]{_err}')
        rpn('ErrTrac',f'[purple]{traceback.format_exc()}')
        input(' :-)> ')
#################################################################################
async def mainloop()->None:
    try:
        PGAconn = await AsyncConnection.connect("dbname=dokin user=postgres password=postgres host=klin")
        await ParsingPath(PGAconn)
        ##------------------------------------------------------------------------------------------------
    except asyncio.exceptions.CancelledError as _AECE:
        rpn('ErrMess',f'{_AECE}')
        rpn('ErrTrac',f'{traceback.format_exc()}')
    except KeyboardInterrupt as _KIM:
        rpn('ErrMess',f'{_KIM}')
        rpn('ErrTrac',f'{traceback.format_exc()}')
    except BaseException as _err:
        rpn('ErrMess',f'{_err}')
        rpn('ErrTrac',f'{traceback.format_exc()}')
    finally:
        await PGAconn.close()
###########################################################################################################
if __name__ == '__main__':
    # Logging('Message',f'Start parsing log 1C ver.{__version__} от {__verdate__}',os.path.basename(__file__))
    # if debug:rpn(f'Start parsing log 1C ver.{__version__} от {__verdate__}',os.path.basename(__file__))
    start_time = time.perf_counter()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(mainloop())
    all_time = time.perf_counter()
    alltime = all_time - start_time
    rpn(f'Обмен выполнен за {alltime:.7f} секунд. Записано строк',os.path.basename(__file__))
    input(' :-)> ')
    os._exit(0)
