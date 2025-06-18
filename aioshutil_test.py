import aioshutil
import asyncio
from rich import print as rpn
sourse = r'E:\ListNew'
destin = r'D:\!Flash'
WaitPrBar = True

####################################################################################################
async def ProgressBar():
    i=0
    rpn('[',end = '')
    try:
        while WaitPrBar:
            i += 1
            if i%5:rpn('[green1]#',end = '')
            else:rpn(f'{i}',end = '')
            await asyncio.sleep(0.1)
    finally:
        rpn(']')

####################################################################################################
async def Copy_Profile():
    ipatt= await aioshutil.ignore_patterns('*.mp3')
    await aioshutil.copytree(sourse, destin, ignore=ipatt,dirs_exist_ok = True)
    await asyncio.sleep(0.5)

###################################################################################################
async def main():
    global WaitPrBar
    WaitPrBar = True
    tasks = []
    tasks.append(asyncio.create_task(ProgressBar(),name='PrBar'))
    tasks.append(asyncio.create_task(Copy_Profile()))
    await asyncio.gather(*tasks)
    if WaitPrBar:WaitPrBar = False

asyncio.run(Copy_Profile())
input(' :-)> ')
