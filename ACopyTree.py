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
__version__ = '0.0.7'
__verdate__ = '2025-03-11 13:32'
#pylint: disable-msg=W0603
LogUsrPath = os.path.join(os.environ['USERPROFILE'],'Documents')
LogUsrFile = ''
SourcePath = r'D:\DevPath'
Destination = r'\\tandadev\D\DevPath'
FileList:list[str] = []
FileListLock = asyncio.Lock()
FileLogLock = asyncio.Lock()
semaphore = asyncio.Semaphore(1000)
WaitPrBar = True#ProgressBar Stop
ExtBlackList = ('mp3','lnk')
Replace = False
#########################################################################################################################################
async def ProgressBar()-> None:
    i=0
    Delay = 1
    # Step = 10
    start_PrBr = perf_counter()
    rpn('[',end = '')
    try:
        while WaitPrBar:
            i += 1
            # if   not i % Step:rpn(f'{int(i*Delay):0>3d}',end = '')
            if not i % 2:rpn('[green1]+',end = '')
            else:rpn('[green1]-',end = '')
            await asyncio.sleep(Delay)
    finally:
        stop_PrBr = perf_counter()
        slep_time = round(stop_PrBr - start_PrBr,3)
        rpn(']', f'{slep_time}')
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
async def LogMessage(Message:str)->bool:
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
async def Loglines(MessLine:list[str])->bool:
    await asyncio.sleep(0)
    if not LogUsrFile or not MessLine:return False
    try:
        async with FileLogLock:
            async with aiofiles.open(LogUsrFile, mode='a', encoding = 'utf-8') as fn:
                await fn.writelines(MessLine)
                await asyncio.sleep(0)
    except Exception as _err:
        rpn(f'[red1]RF:{_err}')
        rpn(f'[red1]RF:{traceback.format_exc()}')
    return True
#########################################################################################################################################
async def CopyFile(NameFile:str)->str:
    NewFile = NameFile.replace(SourcePath,Destination,1)
    _,FileExt = os.path.splitext(NameFile)
    dtnow = (datetime.now(timezone.utc) + timedelta(hours=3)).strftime('%H:%M:%S')
    if FileExt[1:] in ExtBlackList:
        return f'{dtnow};Blist;{NewFile}\n'
    try:
        NewPath = os.path.dirname(NewFile)
        if not os.path.isdir(NewPath):
            await aos.makedirs(NewPath,exist_ok=True)
        if os.path.isfile(NewFile) and not Replace:
            await asyncio.sleep(0)
            return f'{dtnow};Exist;{NewFile}\n'
        async with semaphore:
            await Acopy2(NameFile, NewFile)
            # await asyncio.sleep(0)
    except Exception as _err:
        rpn(f'[red1]RF:{_err}')
        rpn(f'[red1]RF:{traceback.format_exc()}')
        return f'{dtnow};Error;{NewFile}\n'
    #-----------------------------------------------------
    return f'{dtnow};Copy;{NewFile}\n'
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
async def ParsingPath(CurrentPath:str)->tuple[list[str], list[str]]:
    nextpaths = []
    nextfiles = []
    await asyncio.sleep(0.01)
    try:
        for item in await aos.listdir(CurrentPath):
            item1 = os.path.join(CurrentPath,item)
            if os.path.isfile(item1):
                nextfiles.append(item1)
                # async with FileListLock:
                    # FileList.append(item1)
                await asyncio.sleep(0.1)
            elif os.path.isdir(item1):# Добавляем папку в список файлов следующего уровня
                # rpn(f'\tItem = {item1}')
                nextpaths.append(item1)
    #--------------------------------------------------------
    except Exception as _err:
        rpn(f'[red1]PP:{_err}')
        rpn(f'[red1]PP:{traceback.format_exc()}')
    return nextpaths,nextfiles
##############################################################################################################
async def main()-> None:
    global WaitPrBar,FileList
    await LogInit()
    # input(' :-)> ')
    st = 0
    try:
        rpn('Подготовка списка файлов')
        # start_Src = perf_counter()
        StepPath = [SourcePath]#Список файлов текущего шага Destination
        WaitPrBar = True
        tsc = asyncio.create_task(ProgressBar(),name='ProgressBar')
        while StepPath:
            st += 1
            await asyncio.sleep(0.1)
            tasks = [asyncio.create_task(ParsingPath(Item)) for Item in StepPath]
            await asyncio.gather(*tasks)
            StepPath = []
            #---------------------------------------------------------------
            for task in tasks:
                StepPath += task.result()[0]
                async with FileListLock:
                    FileList += task.result()[1]
        FileList.sort()
        WaitPrBar = False
        await tsc
        if not tsc.done():tsc.get_coro().close()
        # await asyncio.sleep(0.1)
        stop_Src = perf_counter()
        # FileListTime = round(stop_Src - start_Src,3)
        # rpn(f'Составление списка файлов заняло {FileListTime}c')
    #--------------------------------------------------------------------------------------
        rpn(f'Копирование {len(FileList)} файлов')
        WaitPrBar = True
        PrBar = asyncio.create_task(ProgressBar())
        copytasks = [asyncio.create_task(CopyFile(Fl)) for Fl in FileList]
        await asyncio.gather(*copytasks)
        WaitPrBar = False
        await PrBar
        if not PrBar.done():PrBar.get_coro().close()
        stop_copy = perf_counter()
        copy_time = round(stop_copy - stop_Src,3)
        rpn(f'Копирование {len(FileList)} файлов заняло {copy_time} c')
    #--------------------------------------------------------------------------------------
        rpn(f'Запись протокола в {LogUsrFile}')
        WaitPrBar = True
        PrBar = asyncio.create_task(ProgressBar())
        LogLines:list[str] = []
        for Ctsk in copytasks:
            LogLines += Ctsk.result()
        await Loglines(LogLines)
        WaitPrBar = False
        await PrBar
        if not PrBar.done():PrBar.get_coro().close()
        await asyncio.create_task(LogMessage(f'Копирование завершено. Скопировано {len(FileList)} файлов. Время копирования {copy_time} c'))
        await asyncio.sleep(0.1)
    #-------------------------------------------------------------------------------------
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
