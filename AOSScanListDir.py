import os
import time
import traceback
import asyncio
from psycopg import AsyncConnection,Error as PGerr#IsolationLevel
import aiofiles.os as aos
from rich import print as rpn
PGconSTR = "dbname=dokin user=postgres password=postgres host=klin"
###########################################################################################################
###########################################################################################################
async def mainloop()->None:
    # apath = r'\\sapsan\C$\1c_tech_log\sys'
    pwr = 0
    T0 = time.perf_counter()
    try:
        # async with PGsemaph:pg_size_pretty(
        async with await AsyncConnection.connect(PGconSTR,autocommit=True) as _aconn:
            sqltxt = "SELECT pg_database_size(current_database())"
            async with _aconn.cursor() as _PGSQL:
                await _PGSQL.execute(sqltxt)
                if (SBase := await _PGSQL.fetchone()):
                    SizeBase = SBase[0]
                    target_size = 1073741824 * 0.05#Gb
                    pwr = int((SizeBase - target_size) / 410)
                if pwr > 0:
                    rpn(f'{SizeBase:12_} <> {int(SizeBase - target_size)} <> {pwr:12_}')
                    sqltxt = f"DELETE FROM public.logs1c WHERE IDLOG in (SELECT IDLOG FROM logs1c ORDER BY datetimelg LIMIT {pwr})"
                    await _PGSQL.execute(sqltxt)
                    rpn(sqltxt)
            # await _aconn.commit()
            rpn('VACUUM')
            async with _aconn.cursor() as _GSQL:
                sqltxt = "VACUUM FULL public.logs1c"
                await _GSQL.execute(sqltxt)
            await _aconn.commit()
        await _aconn.close()
    except PGerr as pgerr:
        rpn('ErrMess',f'[khaki1]{pgerr}')
        rpn('ErrMess',f'[khaki1]sqltxt = {sqltxt}')
        rpn('ErrTrac',f'[khaki1]{traceback.format_exc()}')

    except BaseException as _err:
        rpn(f'[yellow1]{_err}')
        rpn(f'[yellow1]{traceback.format_exc()}')
        T1 = time.perf_counter()
        rpn(f'Файлов за {T1-T0:7.5}')
###########################################################################################################
if __name__ == '__main__':
    rpn('Start parsing log 1C ver.')
    start_time = time.perf_counter()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(mainloop())
    all_time = time.perf_counter()
    alltime = all_time - start_time
    rpn(f'Обмен выполнен за {alltime:.7f} секунд. ')
    input(' :-)> ')
    os._exit(0)
