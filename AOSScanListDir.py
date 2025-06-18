import os
import time
import traceback
import asyncio
# import aiofiles
import aiofiles.os as aos
from rich import print as rpn
###########################################################################################################
###########################################################################################################
async def mainloop()->None:
    apath = r'\\sapsan\C$\1c_tech_log\sys'
    _path_list = []
    try:
        T0 = time.perf_counter()
        # with await aos.scandir(apath) as it:
        for entry in await aos.scandir(apath):
            # pass
                # await asyncio.sleep(0)
            rpn(type(entry.path),entry.path)
        #await 
        aos.scandir(apath).close()
        T1 = time.perf_counter()
        rpn(f'{T1-T0:7.5}')
    except BaseException as _err:
        rpn(f'[yellow1]{_err}')
        rpn(f'[yellow1]{traceback.format_exc()}')
###########################################################################################################
if __name__ == '__main__':
    rpn('Start parsing log 1C ver.')
    start_time = time.perf_counter()
    asyncio.run(mainloop())
    all_time = time.perf_counter()
    alltime = all_time - start_time
    rpn(f'Обмен выполнен за {alltime:.7f} секунд. ')
    input(' :-)> ')
    os._exit(0)
