import os
import asyncio
import traceback
from time import perf_counter
from rich import print as rpn
##-----------------------------------
WaitPrBar = True#ProgressBar Stop
#######################################################################################
async def ProgressBar():
    sim = 0
    start_PrBr = perf_counter()
    try:
        while WaitPrBar:
            await asyncio.sleep(0.5)
            if not sim:
                rpn('[',end = '')
                sim += 1
                continue
            if not sim % 120:rpn(f'[cyan1] {sim//120:2}')
            elif not sim % 2:rpn('[green1]+',end = '')
            else:rpn('[green1]-',end = '')
            sim += 1
    finally:
        stop_PrBr = perf_counter()
        slep_time = round(stop_PrBr - start_PrBr,3)
        rpn(f'] по таймеру {slep_time}')
        # rpn(f'Задержка по таймеру {slep_time}')
##############################################################################################################
async def main(long_time:int)->None:
    global WaitPrBar
    try:
        WaitPrBar = True
        tsc = asyncio.create_task(ProgressBar(),name='ProgressBar')
        await asyncio.sleep(long_time)
        WaitPrBar = False
        await asyncio.sleep(0.5)
        if not tsc.done():
            rpn('Аварийная от')
            tsc.cancel()
    except Exception as _err:
        rpn(f'[red1]RF:{_err}')
        rpn(f'[red1]RF:{traceback.format_exc()}')
###################################################################################################################################
if __name__ == '__main__':
    while True:
        asyncio.run(main(15))
        if input(':-> '):break
    os._exit(0)
