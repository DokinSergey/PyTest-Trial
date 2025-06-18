import os,sys,uuid
import traceback
import asyncio
import aiofiles
import aiofiles.os as aos
from datetime import datetime,timezone,timedelta
from time import perf_counter
from aioshutil import copy2 as Acopy2
from rich import print as rpn
#------------------------------------------
__author__ = 't.me/dokin_sergey'
__version__ = '0.0.4'
__verdate__ = '2025-03-10 12:26'
#pylint: disable-msg=W0603
LogUsrPath = os.path.join(os.environ['USERPROFILE'],'Documents')
LogUsrFile = ''
SourcePath = r'D:\DevPath'
Destination = r'E:\auto'
FileList = []
FileListLock = asyncio.Lock()
FileLogLock = asyncio.Lock()
semaphore = asyncio.Semaphore(3000)
WaitPrBar = True#ProgressBar Stop
ExtBlackList = ('mp3',)
#########################################################################################################################################
async def ProgressBar()-> None:
    i=0
    Delay = 1
    Step = 10
    rpn('[',end = '')
    try:
        while WaitPrBar:
            i += 1
            if   not i % Step:rpn(f'{int(i*Delay):0>3d}',end = '')
            elif not i % 2:   rpn('[green1]+',end = '')
            else:rpn('[green1]-',end = '')
            await asyncio.sleep(Delay)
    finally:
        rpn(']', f'\t{i*Delay}')
#########################################################################################################################################
async def LogInit(Project:str = 'AcynCopyFiles')->bool:
    global LogUsrFile
    try:
        LogFileUsr = os.path.join(LogUsrPath,Project)
        if not os.path.isdir(LogFileUsr):os.makedirs(LogFileUsr,exist_ok=True)
        LogUsrFile = os.path.join(LogFileUsr,f'{datetime.today().strftime('%Y%m%d')}.txt')
        dtnow = (datetime.now(timezone.utc) + timedelta(hours=3)).strftime('%H:%M:%S')
        async with FileLogLock:
            async with aiofiles.open(LogUsrFile, mode='a', encoding = 'utf-8') as fn:
                await fn.write(f'{'-' * 120}\n')
                await fn.write(f'{dtnow} Версия:{__version__} от:{__verdate__} Автор:{__author__}\n')
    except Exception as _err:
        rpn(f'[red1]RF:{_err}')
        rpn(f'[red1]RF:{traceback.format_exc()}')
        rpn(LogUsrFile)
        return False
    return True
#########################################################################################################################################
async def LogWriter(Message:str)->bool:
    await asyncio.sleep(0)
    if not LogUsrFile or not Message:return False
    dtnow = (datetime.now(timezone.utc) + timedelta(hours=3)).strftime('%H:%M:%S')
    try:
        async with FileLogLock:
            async with aiofiles.open(LogUsrFile, mode='a', encoding = 'utf-8') as fn:
                await fn.write(f'{dtnow}:{Message}\n')
    except Exception as _err:
        rpn(f'[red1]RF:{_err}')
        rpn(f'[red1]RF:{traceback.format_exc()}')
    return True
#########################################################################################################################################
async def CopyFile(NameFile:str)->bool:
    NewFile = NameFile.replace(SourcePath,Destination,1)
    _,FileExt = os.path.splitext(NameFile)
    if FileExt[1:] in ExtBlackList:return False
    try:
        NewPath = os.path.dirname(NewFile)
        async with semaphore:
            if not os.path.isdir(NewPath):
                await aos.makedirs(NewPath,exist_ok=True)
            await Acopy2(NameFile, NewFile)
            # await LogWriter(f'True {NewFile}')
            asyncio.create_task(LogWriter(f'True {NewFile}'))
            # await asyncio.sleep(0)
    except Exception as _err:
        asyncio.create_task(LogWriter(f'False {NewFile}'))
        # await LogWriter(f'False {NewFile}')
        rpn(f'[red1]RF:{_err}')
        rpn(f'[red1]RF:{traceback.format_exc()}')
        # rpn(NameFile)
        # rpn(NewFile)
        return False
    return True
#########################################################################################################################################
async def RenameFile(FileName:str)->bool:
    NewName = str(uuid.uuid4())[:8]
    PathName,FileOldName = os.path.split(FileName)
    _,FileExt = os.path.splitext(FileOldName)
    FileNewName = os.path.join(PathName,f'{NewName}{FileExt}')
    try:
        async with semaphore:
            os.replace(FileName,FileNewName)
            await asyncio.sleep(0)
    except Exception as _err:
        rpn(f'[red1]RF:{_err}')
        rpn(f'[red1]RF:{traceback.format_exc()}')
    return True
################################################################################################################
async def ParsingPath(CurrentPath:str)->list[str]:
    nextpaths = []
    await asyncio.sleep(0.01)
    try:
        for item in await aos.listdir(CurrentPath):
            item1 = os.path.join(CurrentPath,item)
            if os.path.isfile(item1):
                # await CopyFile(item1)
                # await RenameFile(item1)
                async with FileListLock:FileList.append(item1)
                await asyncio.sleep(0)
            elif os.path.isdir(item1):# Добавляем папку в список файлов следующего уровня
                # rpn(f'\tItem = {item1}')
                nextpaths.append(item1)
    #--------------------------------------------------------
    except Exception as _err:
        rpn(f'[red1]PP:{_err}')
        rpn(f'[red1]PP:{traceback.format_exc()}')
    return nextpaths
##############################################################################################################
async def main()-> None:
    global WaitPrBar
    await LogInit()
    # input(' :-)> ')
    St = 0
    Pt = 1
    try:
        start_Src = perf_counter()
        StepPath = [SourcePath]#Список файлов текущего шага Destination
        while StepPath:
            rpn(f'Уровень вложенности = {St = } {Pt = }')
            Pt = 1
            WaitPrBar = True
            # tsc = asyncio.create_task(ProgressBar(),name='ProgressBar')
            tasks = []
            for Item in StepPath:
                
                rpn(f'\tOldItem = {Item} ')
                #-----------------------------------------------------------
                PtName = os.path.dirname(Item)
                if St:
                # if St and os.path.basename(Item)[:7] != f'depth_{St}':
                    for ii in range(Pt,100000):
                        new = f'depth_{St}_folder_{ii}'
                        NewPath = os.path.join(PtName,new)
                        if os.path.isdir(NewPath):continue
                        await aos.rename(Item,NewPath)
                        Pt = ii + 1
                        break
                else:NewPath = Item
                #----------------------------------------------------------
                rpn(f'\tNewPath = {NewPath}')
                tasks.append(asyncio.create_task(ParsingPath(NewPath)))
                #-----------------------------------------------------------
            St += 1
            Pt = 1
            await asyncio.gather(*tasks)
            WaitPrBar = False
            # await asyncio.sleep(0.1)
            # await tsc
            StepPath = []
            #---------------------------------------------------------------
            for task in tasks:
                StepPath += task.result()# for task in tasks]
            input(' :-)> ')
        FileList.sort()
        stop_Src = perf_counter()
        rpn(f'Составление списка файлов заняло {round(stop_Src - start_Src,3)}c')
        #-------------------------------------------------------------------------------
        rpn(f'Копирование {len(FileList)} файлов')
        WaitPrBar = True
        tsc = asyncio.create_task(ProgressBar())
        tasks = [asyncio.create_task(CopyFile(Fl)) for Fl in FileList]
        await asyncio.gather(*tasks)
        WaitPrBar = False
        await tsc
        stop_copy = perf_counter()
        rpn(f'Копирование {len(FileList)} файлов заняло {round(stop_copy - stop_Src,3)}c')
    except Exception as err:
        rpn(f'[red1]Main:{err}')
        rpn(f'[red1]Main:{traceback.format_exc()}')
###############################################################################################################
start_time = perf_counter()
asyncio.run(main())
stop_time = perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
