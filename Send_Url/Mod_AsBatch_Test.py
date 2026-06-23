import os
import time
import traceback
# import chardet
import asyncio
import aiofiles
# import aiosqlite
import csv
from shutil import copytree,ignore_patterns,Error as ShuError#,disk_usage,copy2#,rmtree
from aiocsv import AsyncDictReader
from rich import print as rpn
#-------------------------------------------
__author__  = 't.me/dokin_sergey'
__version__ = '0.3.2'
__verdate__ = '2025-02-21 15:30'
#-------------------------------------------
CSVfile = os.path.join(os.path.dirname(__file__),'Change_Shum.csv')
WaitPrBar = True
debug = True
rpn(CSVfile)
#########################################################################################################################################
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

#######################################################################################################################
async def Copy_Profile(OldProfile:str,NewProfile:str)->bool:
    _dbg = debug
    _res = True
    # LogErrDebug('Message',f'Start {OldProfile = } {NewProfile = }')
    PathTyple = ('Documents','Desktop','Downloads',)
    if _dbg:rpn(f'\t\t\tCUD:10:[cyan]{OldProfile = } {NewProfile = }')
    #----------------------------------------------------------
    for _ipath in PathTyple:
        src = os.path.join(OldProfile,_ipath)
        dst = os.path.join(NewProfile,_ipath)
        # LogErrDebug('Message',f'{src = } {dst = }')
        if _dbg:rpn(f'\t\t\tCUD:21:[cyan]{src = } {dst = }')
        ipatt = ignore_patterns('*.lnk', '*.url', '*.ini','Мои видеозаписи','мои рисунки', 'Моя музыка' )
        try:
            copytree(src, dst, ignore=ipatt,dirs_exist_ok=True)
            await asyncio.sleep(0.)
            # LogErrDebug('Message',f'Папка {_ipath} скопирована на {NewProfile}')
            if _dbg:rpn(f'\t\t\tCUD:23: [cyan]Папка {_ipath} скопирована на {NewProfile}')
        except ShuError as Sherr:
            # LogErrDebug('ErrMess',f'{type(Sherr)} = {Sherr}!')
            rpn(f'\t\t\t\t[bright_yellow]Ошибка при копирования папки {_ipath} на {NewProfile}')
            rpn(f'\t\t\t\t[cyan]{Sherr}')
            # for _e in Sherr:rpn(f'\t\t\t\t[cyan]{_e}')
        except Exception as ErrMs:
            _res = False
            # LogErrDebug('ErrMess',f'{ErrMs}')
            # LogErrDebug('ErrTrac',f'{traceback.format_exc()}')
            rpn(f'\t\t\t\t[cyan]Ошибка при копирования папки {_ipath} на {NewProfile}')
            rpn(f'[orchid]{ErrMs}')
            rpn(f'[orchid]{traceback.format_exc()}')
#######################################################################################################################
#########################################################################################################################################
async def PSExec(psstr:str,_dbg:bool = False)->str:
    res = ''
    # LogErrDebug('psstrlg',f'{psstr}')
    if _dbg:rpn(f'{psstr}\n')
    # psstr = 'powershell.exe ' + psstr
    try:
        proc = await asyncio.create_subprocess_exec('powershell',psstr, stdout = asyncio.subprocess.PIPE, stderr = asyncio.subprocess.PIPE)
        await asyncio.sleep(0.1)
        pls,ers = await proc.communicate()
        if _dbg and ers:rpn(f'ers = {ers.decode('cp866')}')
        elif  _dbg and pls:rpn(pls.decode('cp866'))
        # if dbg:
        # if bool(pls.strip()):LogErrDebug('Message',f'{pls.decode('cp866').strip()}')
        # if bool(ers.strip()):LogErrDebug('ErrPoSh',f'{ers.decode('cp866').strip()}')
    # except TimeoutExpired as Mess:
        # res.Mess1 = str(Mess)
        # res = str(Mess)
        # LogErrDebug('ErrMess',f'Timeout: {Mess}')
    except Exception as Exp:
        rpn(res := str(Exp))
        rpn(ers.decode('cp866'))
        # LogErrDebug('ErrMess',f'{Mess}','PSExec')
        # LogErrDebug('ErrTrac',f'{traceback.format_exc()}')
    # else:
    if bool(pls): res = str(pls.decode('cp866'))
        # LogErrDebug('Success','Скрипт PS выполнен успешно','PSExec','1')
    return res
#######################################################################################################################
async def GetProfile(User,Server):
    _dbg = debug
    # Server = 'SH-VDS-TEMP.shumeiko.local';User = 'DokinSergey'
    psstr  =  "$new_pwd = ConvertTo-SecureString -AsPlainText 'Vx964&iugo7w' -Force\n"
    psstr +=  "$Cred = New-Object System.Management.Automation.PSCredential 'script4service@shumeiko.local', $new_pwd\n"
    psstr += f"""$Query = 'Select LocalPath from Win32_UserProfile where LocalPath LIKE "%{User}"'\n"""
    psstr += f"Get-WmiObject -Credential $Cred -ComputerName '{Server}'  -Query $Query | FT LocalPath -HideTableHeaders"
    rre = await asyncio.create_task(PSExec(psstr,True))
    res = rre.strip()
    rpn(f'[yellow]{User = }  {res = }')
    return res
#######################################################################################################################
async def GreateProfile(User:str,Psswrd:str,Server:str, Domain:str)->str:
    _dbg = debug
    Profiles = ''
    #-------------------------------------------------------------------------------------------------------------------
    Cred  =  "$new_pwd = ConvertTo-SecureString -AsPlainText 'Vx964&iugo7w' -Force\n"
    Cred +=  "$Cred = New-Object System.Management.Automation.PSCredential 'script4service@shumeiko.local', $new_pwd\n"
    psstr = Cred
    #-------------------- Добавляем пользователя в группу
    psstr += "Import-Module ActiveDirectory \n"
    psstr += f"Add-AdGroupMember 'CreateProfileRemote' -Credential $Cred -Members '{User}' -server '{Domain}' -PassThru \n"# -PassThru
    rre = await asyncio.create_task(PSExec(psstr))
    # res = rre.strip()
    # if (res := rre.strip()):
    if rre.strip():
    #----------------- Создание профиля ----------------------------------------------------------------------------------
        # if _dbg:rpn(f'AdGr:{res = }')
        UserNm = f'{User}@{Domain}'
        ServNm = f'{Server}.{Domain}'
        if _dbg:rpn(f'GrPr:{UserNm = } {ServNm = }')
        psstr  = f"$new_pwd = ConvertTo-SecureString -AsPlainText '{Psswrd}' -Force \n"
        psstr += f"$Cred = New-Object System.Management.Automation.PSCredential '{UserNm}', $new_pwd \n"
        psstr += f"$NS = New-PSSession -ComputerName '{ServNm}' -Credential $Cred \n"
        psstr +=  "if( $NS ){Invoke-Command -Session $NS -ScriptBlock {$env:USERPROFILE} \n"
        psstr +=  "Remove-PSSession -Session $NS} \n"
        rre = await asyncio.create_task(PSExec(psstr))
        Profiles = rre.strip()
        # if _dbg:rpn(f'GrPr:{Profiles = }')
    #----------------- Добавление прав на папку
        TrServ = fr'\\{Server}\{Profiles.replace(':','$')}'
        if _dbg:rpn(f'TrServ = {TrServ}')
        psstr  = Cred
        psstr +=  'Import-Module ActiveDirectory\n'
        psstr += f'$NS = New-PSSession -ComputerName "{Server}" -Credential $Cred \n '
        psstr += 'if($NS){Invoke-Command -Session $NS -ScriptBlock {Import-Module NTFSSecurity \n '
        psstr += f'Add-NTFSAccess -Path "{TrServ}" -Account "1MORECLOUD@1more.cloud" -AccessRights "FullControl" -AccessType "Allow" '
        psstr += '-AppliesTo "ThisFolderSubfoldersAndFiles"} \n  Remove-PSSession -Session $NS} \n'
        rre = await asyncio.create_task(PSExec(psstr))
        # res = rre.strip()
        # if _dbg:rpn(f'ntfs:{res = }')
    #----------------- Убираем пользователя из группы
        psstr  = Cred
        psstr += 'Import-Module ActiveDirectory\n'
        psstr += f'Remove-AdGroupMember "CreateProfileRemote" -Credential $Cred -Members "{User}" -Server "{Domain}" -PassThru -Confirm:$false\n'
        rre = await asyncio.create_task(PSExec(psstr))
        # res = rre.strip()
        # if _dbg:rpn(res)
    return Profiles

#######################################################################################################################
async def Profile_Trans(UsrD:dict)->bool:
    global WaitPrBar
    _dbg = debug
    # 'N': '1','OMCID': 'IAS20181','UserID': 'IAS2018101','Password': 'Yyx82-a68JGm','OldTerm': 'sh-vds-01',
    #'NewTerm': 'sh-vds-temp','dm1': 'shumeiko','dm1': 'local','result': '0'
    if int(UsrD['result']):return False
    # if _dbg:rpn(UsrD)
    Domain = f'{UsrD['dm1']}.{UsrD['dm0']}'.lower()
    User = UsrD['UserID'].lower()
    Serv = UsrD['NewTerm'].lower()
    OSrv = UsrD['OldTerm'].lower()
    Pass = UsrD['Password']
    OPrf = await asyncio.create_task(GetProfile(User,OSrv))
    NPrf = await asyncio.create_task(GetProfile(User,Serv))
    # await asyncio.gather(OPrf,NPrf)
    if WaitPrBar:WaitPrBar = False
    await asyncio.sleep(0.1)
    rpn(f'[cyan1]{OPrf = } {OPrf = }')

    # if not (ProFile := NPrf.strip()):
        # rre = await asyncio.create_task(GreateProfile(User,Pass,Serv,Domain))
        # ProFile = rre.strip()
        # await asyncio.sleep(0.5)
        # if _dbg:rpn( f'На сервере {Serv} для пользователя {User} создан профиль {ProFile}')
    #-------------------------------------------------------------------------------------
    # NetProfile = fr'\\{Serv}\{ProFile.replace(':','$')}'
    # CfgPath = os.path.join(NetProfile,r'AppData\Roaming\1C\1CEStart')
    # CfgLink = os.path.join(CfgPath,'1cestart.cfg')
    # CfgFile = os.path.join('I:',f'1cestart_{User}.cfg')
    # CfgFile = os.path.join(r'\\sh-vds-01\ibases',f'1cestart_{User}.cfg')
    # if _dbg:rpn(f'ProFile = {NetProfile}')#\sh-vds-01\ibases\\1cestart_ias20181XX.cfg
    # if _dbg:rpn(f'CfgLink = {CfgLink}')
    # if _dbg:rpn(f'CfgFile = {CfgFile}')
    # input(' :-)> ')
    # try:
        # if not os.path.islink(CfgLink):
            # if os.path.isfile(CfgLink):os.remove(CfgLink)
            # if not os.path.isdir(CfgPath):os.makedirs(CfgPath,exist_ok=True)
            # if os.path.isfile(CfgFile):
                # # Cred   =  "$new_pwd = ConvertTo-SecureString -AsPlainText 'Vx964&iugo7w' -Force\n"
                # # Cred  +=  "$Cred = New-Object System.Management.Automation.PSCredential 'script4service@shumeiko.local', $new_pwd\n"
                # # psstr  = Cred
                # # psstr += f"New-Item -Credential $Cred -ItemType SymbolicLink -Path '{CfgFile}' -Target '{CfgLink}'"
                # # Link  = await asyncio.create_task(PSExec(psstr,True))
                # # rpn(Link)
                # os.symlink(CfgFile,CfgLink)
                # rpn(f'[cyan1]Симлинк [green1]{CfgLink} [cyan1]успешно создан')
        # else:rpn(f'[yellow]СимЛинк уже создан {CfgLink}')
    # except Exception as ErrMs:
        # rpn(f'[orchid]{ErrMs = }')
    # await asyncio.sleep(0)
#----------------------------------------------------------------------------------------------------------------------
    # SoursPath = fr'\\{UsrD['OldTerm']}\{OPrf.replace(':','$')}'
    # if _dbg:rpn(f'SoursPath = {SoursPath}')
    # await asyncio.create_task(Copy_Profile(SoursPath,NetProfile))
#######################################################################################################################
async def Transfer_Profiles()->None:
    global WaitPrBar
    WaitPrBar = True
    tascs = []
    try:
        tascs.append(asyncio.create_task(ProgressBar(),name='PrBar'))
        async with aiofiles.open(CSVfile, mode="r", encoding="utf-8") as afp:
            async for row in AsyncDictReader(afp, delimiter="\t",quotechar = "'",doublequote = True,skipinitialspace = True,quoting = csv.QUOTE_MINIMAL):
                tascs.append(asyncio.create_task(Profile_Trans(row)))
                await asyncio.sleep(0)
                # rpn(row)
        await asyncio.gather(*tascs)
        await asyncio.sleep(0)
    except Exception as err:
        rpn(f'[red1]Main:{err}')
        rpn(f'[red1]Main:{traceback.format_exc()}')
#######################################################################################################################
def Transfer_Main():
    _start_time = time.perf_counter()
    asyncio.run(Transfer_Profiles())
    _all_time = time.perf_counter()
    _alltime = _all_time - _start_time
    rpn(f'Выполнено за {_alltime:.7f} секунд.')
#######################################################################################################################
if __name__ == '__main__':
    # PROJECT = 'Test_OMC_Customer'
    # UserProject = os.getlogin()
    # LoggingInit(PROJECT,UserProject)
    # Logging('Message',f'Start parsing log 1C ver.{__version__} от {__verdate__}',os.path.basename(__file__))

    start_time = time.perf_counter()
    # asyncio.run(Transfer_Profiles())
    asyncio.run(GetProfile('IAS2018151','sh-dc-01'))
    all_time = time.perf_counter()
    alltime = all_time - start_time
    rpn(f'Выполнено за {alltime:.7f} секунд.')
    # Logging('Message',f'Выполнено за {alltime:.7f} секунд. Записано {nstrok} строк',os.path.basename(__file__))
else:
    print('')
    os._exit(0)
