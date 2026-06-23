import os
# import sys
import msvcrt  # Windows
import asyncio
import time
# from time import time,perf_counter
from rich import print as rpn
# from rich.console import Console
# from rich.progress import Progress
# from datetime import datetime,timezone,timedelta#,date
BTqueue:asyncio.Queue[str] = asyncio.Queue()
########################################################################################################################
async def ProgressBar()->None:
    """Отображает индикатор прогресса в консоли."""
    # dtnow = datetime.now(timezone.utc) + timedelta(hours=3)
    dtstr = time.strftime("%H:%M:%S")
    i=0
    rpn(f'[khaki1]{dtstr}[/khaki1] [',end = '')
    _t0 = time.perf_counter()
    try:
        r_key = ''
        for i in range(100):
        # while WaitPrBar:
            # i += 1
            if i%2:rpn('[green1]#',end = '')
            else:rpn('[green1]=',end = '')
            for _ in range(10):
                await asyncio.sleep(0.093)
                if msvcrt.kbhit():
                    match (r_key := msvcrt.getwche().strip().lower()):
                        case 'q':
                            await BTqueue.put(r_key)
                            break
                        case _:r_key = ''
            if r_key =='q':break
    # except asyncio.CancelledError:
        # _t1 = perf_counter()
        # rpn(f'] {_t1-_t0:>6.3f}')
        # await asyncio.sleep(0.1)
    finally:
        _t1 = time.perf_counter()
        rpn(f'] {_t1-_t0:>6.3f}')
########################################################################################################################
if __name__ == '__main__':
    asyncio.run(ProgressBar())
    # while BTqueue.empty():
        # rpn(BTqueue.get())

    input(':-> ')
    os._exit(0)
