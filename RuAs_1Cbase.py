import os,traceback,uuid,sys
import asyncio, aiosqlite
from glob import glob
from rich import print as rpn
from shutil import copytree
from Mod_Common import DetectCodec,FRes,fusr,C1c,OmcError,UserHomePath,AChangeIni,Get_Domus,PSExec
from Mod_Logging import LogErrDebug,ReportSql
__author__  = 't.me/dokin_sergey'
__version__ = '1.3.2'
__verdate__ = '2025-03-15 11:00'
#################################################################################################################
tv8i:str#  = '\n'.join(templ_v8i)#Преобразуем лист в многострочный текс
ConnS:str# = templates['tConnS']
ConnF:str# = templates['tConnF']
Arch = 'x86_prt'
templ_cfg:dict[str,str]#  = templates['Templ_cfg']
###################################################################################################################
async def AReadSQL1C()->None:
    global tv8i,ConnS,ConnF,templ_cfg
    try:
        FileSQL = os.path.join(os.path.dirname(__file__),'OMC_Customer.db3')
        async with aiosqlite.connect(FileSQL) as SQL:
            templ_v8i = []
            async with SQL.execute("SELECT Value FROM Settings Where Key = 'V8iTempl'") as cursor:
                async for row in cursor:
                    if row[0]:templ_v8i.append(row[0])
            tv8i = '\n'.join(templ_v8i)
            # rpn(tv8i)
    #---------------------------------------------------------------------------------------------------
            async with SQL.execute("SELECT Value FROM Settings Where Key = 'ConnS'") as cursor:
                async for row in cursor:
                    ConnS = row[0]
            # rpn(f'{ConnS = }')
    #---------------------------------------------------------------------------------------------------
            async with SQL.execute("SELECT Value FROM Settings Where Key = 'ConnF'") as cursor:
                async for row in cursor:
                    ConnF = row[0]
            # rpn(f'{ConnF = }')
    # ---------------------------------------------------------------------------------------------------
            templ_cfg = {}
            async with SQL.execute("SELECT Value FROM Settings Where Key = 'TemplCfg'") as cursor:
                async for row in cursor:
                    k,v = row[0].split('=')
                    templ_cfg[k] = v
            # rpn(f'{templ_cfg = }')
    #---------------------------------------------------------------------------------------------------
    except Exception as err:
        rpn(f'[red1]Main:{err}')
        rpn(f'[red1]Main:{traceback.format_exc()}')
###################################################################################################################
def RecoverAllCfg(CfgPath:str)->bool:
    CfgName = f'{CfgPath}\\OMC_ibases\\1cestart.cfg'
    BaseList:dict[str,str] = {}
    # rpn(f'[cyan2]Проверка файла [bright_green]{CfgName}[cyan2] на валидность')
    try:
        with open('D:\\ibases\\error_cfg.txt', mode = 'w', encoding = 'utf_8') as ecfg:
            if os.path.isfile(CfgName):
                rk = DetectCodec(CfgName)
                with open(CfgName, mode ='r', encoding = rk) as Hcfg: #, encoding='utf_16_le'
                    filetxt = Hcfg.readlines()
            #------------------------------------------------------------------------------------
                for istr in filetxt: # а теперь принимаемся за 1cestart.cfg
                    if istr.startswith('CommonInfoBases='):
                        ifile = istr.split('=')[1].strip()
                        if os.path.isfile(ifile):
                            vpath,vfile = os.path.split(ifile)
                            BaseList.setdefault(vfile,vpath)
                        else:
                            rpn(f'[orange1]{ifile} [cyan2]Файл отсутсвует по указанному пути')
                            print(f'{ifile}; Файл отсутсвует по указанному пути' ,file = ecfg )
#------------------------------------------------------------------------------
            PathNotList = ('OMC_ibases','_OMC_temp','_OMC_temp','test')
            for vpath, _, files in os.walk(CfgPath):
                if len(vpath.split('\\')) > 4 and (vpath.split('\\')[4] in PathNotList):continue
                # rpn(f'{root = }')
                for vfile in files:
                    if os.path.basename(vfile)[-3:] != 'v8i':continue
                    # res = IIList.setdefault(vfile,vpath))
                    if vfile in BaseList:#.keys():
                        rpn(f'[green1]{os.path.realpath(os.path.join(vpath,vfile))}В словаре ')
                    else:
                        BaseList[vfile] = vpath
                        rpn(f'[orange1]{os.path.realpath(os.path.join(vpath,vfile))}[cyan2] ссылка на файл отсутсвует ')
                        print(f'{os.path.realpath(os.path.join(vpath,vfile))}; ссылка на файл отсутсвует' ,file = ecfg )
        # rpn(IIList)
        # получаем словар .v8i  с путями
        # V8iPath = f"{CfgPath}\\*\\*.v8i"
        # V8itempl = '*.v8i'
        # filetxt = glob(V8itempl, root_dir=CfgPath, recursive=True)
        # rpn(f'{filetxt = }')
        # for istr in filetxt:
            # vPath,vfile = os.path.split(istr.strip())
            # BaseList.setdefault(vfile,vPath)
        # rpn(BaseList)
    #---------------------------------------------------------------
        ab = True
    except Exception as DErr:
        LogErrDebug('ErrMess',f'{str(DErr)} ; {CfgPath = }','RecoverAllCfg')
        ab = False
    return ab
###################################################################################################################################
def ServiceStrTempl(ServStr:str,dbg:bool = False)->str:
    LogErrDebug('Message',f'Start {ServStr = }','ServiceStrTempl')
    Lstr = ServStr.split();rstr:str = ''
    if dbg:rpn(f'SST:10:[purple]{ServStr =}')
    il = [ext.split('=')[0] for ext in Lstr]
    for itmp in templ_cfg.items():
        if dbg:rpn(f'SST:20:[purple]{itmp = }')
        if itmp[0] in il:continue
        Lstr.append(f'{itmp[0]}={itmp[1]}')
    rstr = ''.join(f'{tstr}\n' for tstr in Lstr)
    if dbg:rpn(f'SST:30:[purple]{rstr = }')
    return rstr
###################################################################################################################################
def DelcfgV8i(FileCfg:str,DellV8i:list[str],dbg:bool = False)->FRes:
    """Удаление ссылок на базы из файла \\OMC_ibases\\1cestart.cfg Может быть указан как:
    FileCfg имя файла с полным путем
    DellV8i список имен файлов *.v8i"""
    aa = FRes()
    LogErrDebug('Message',f'Start {FileCfg = } {DellV8i = }','DelcfgV8i')
    CfgAllName = FileCfg
    if dbg:rpn(f'DCV:10:[purple]{CfgAllName =}')
    # ArxCfgName = fr'{BasePath}\OMC_ibases\1cestart.txt'
    ArxCfgName = os.path.join(os.path.dirname(FileCfg),'1cestart.txt')
    if dbg:rpn(f'DCV:20:[purple]{ArxCfgName =}')
    LogErrDebug('Message',f'{ArxCfgName = }','DelcfgV8i')
    #---------------------------------------------------------------------------------------------
    lst = []
    for pst in DellV8i:#в нижний регистр + осталяем только имя файла
        namefl = os.path.basename(pst).lower() if '\\' in pst else pst.lower()
        if dbg:rpn(f'DCV:30:[purple]{namefl =}')
        lst.append(namefl)
    NewFile = False
    #---------------------------------------------------------------------------------------------
    try:
        newtxt = '';servtxt = ''
        if os.path.isfile(CfgAllName):
            rk = DetectCodec(CfgAllName)
            with open(CfgAllName, mode ='r', encoding = rk) as Allcfg:   #, encoding='utf_8'
                filetxt = Allcfg.readlines()
            #--------------------------------------------------------------------------------
            for line in filetxt:
                if not line:continue
                if line.strip().startswith('CommonInfoBases='):
                    _,filename = os.path.split(line.strip().lower())
                    if filename in lst:
                        LogErrDebug('Message',f'Удалено ; {filename = }','DelcfgV8i')
                        NewFile = True
                        continue
                    newtxt += line
                else:servtxt += line
        else:raise OmcError(f'Файл {CfgAllName} не найден')
    #------------------------------------------------------------------------------
        #Выравниваем сервисную часть по шаблону из настроек
        Tservtxt = ServiceStrTempl(servtxt,dbg)
    #------------------------------------------------------------------------------
        if NewFile:
            os.replace(CfgAllName,ArxCfgName)
            with open(CfgAllName, mode ='w', encoding = 'utf_8') as Hcfg:
                Hcfg.writelines(Tservtxt)
                Hcfg.writelines(newtxt)
    #------------------------------------------------------------------------------
    except OmcError as Mess:
        LogErrDebug('Warning',f'{Mess}','DelcfgV8i')
        aa.err = 1
        aa.Mess1 = f'{Mess}'
    except Exception as AErr:
        aa.err = 1
        LogErrDebug('ErrMess',f'{AErr}','DelcfgV8i')
        aa.Mess1 = f'{AErr}'
        LogErrDebug('ErrTrac',f'{traceback.format_exc()}','DelcfgV8i')
    else:
        aa.res = 1
        aa.Mess1 = 'Строки удалены успешно'
    return aa
####################################################################################################################
def AllBases_v8i(V8iFullName:str)->str:
    """Добавление сроки инф. базы в общий 1cestart.cfg"""
    try:
        v8iNetPat, v8iName =  os.path.split(V8iFullName)
        v8iNetPat, _ =  os.path.split(v8iNetPat)
        IbaseAll = f'{v8iNetPat}\\OMC_ibases\\1cestart.cfg'
        if os.path.isfile(IbaseAll):
            rk = DetectCodec(IbaseAll)
            with open(IbaseAll, mode ='r', encoding = rk) as Allcfg:   #, encoding='utf_8'
                filetxt = Allcfg.readlines()
            for line in filetxt:
                if v8iName.strip() in line.strip(): break
            else:
                with open(IbaseAll, mode ='a', encoding = rk) as Allcfg: #, encoding='utf_16_le'
                    print(f'CommonInfoBases={V8iFullName}',file=Allcfg)
        else:
            with open(IbaseAll, mode ='w', encoding = 'utf_8') as Hcfg:
                print('UseHWLicenses=0', file = Hcfg)
                print('AppAutoInstallLastVersion=1', file = Hcfg)
                print(f"CommonInfoBases={V8iFullName}", file = Hcfg)
    #---------------------------------------------------------------
        ab = os.path.realpath(IbaseAll)
    except Exception as DErr:
        LogErrDebug('ErrMess',f'{str(DErr)} ; {V8iFullName = }','AllBases_v8i')
        ab = ''
    return ab
###################################################################################################################################
def FileListV8i(path1c:str)->list[str]:
    r"""Получение списка ID файловых баз юзера
         из файла \AppData\Roaming\1C\1CEStart\ibases.v8i"""
    exclist = []
    try:
        if os.path.isfile(path1c):
            rk = DetectCodec(path1c)
            with open(path1c, mode ='r', encoding = rk) as Hcfg:
                filetxt = Hcfg.readlines() #Читаем файл одним куском
            #------------------------------------------------------------------------------------
            itertxt = iter(filetxt)  #преобразуем многострочный текс в итератор
            for istr in itertxt: # пошли по строкам
                if istr.startswith('Connect=File'): # нужнам нам строка в наличии
                    a = next(itertxt).split('=')[1].strip()
                    exclist.append(a) # ID из строки +1
                    # b = path1c.split('\\')
                    # LogErrDebug(f'{b[4]} ; ID={a}','FileListV8i')
                    # exclist.append(next(itertxt).split('=')[1].strip()) # ID из строки +1
        else:exclist.append('')
    except Exception as DErr:
        LogErrDebug('ErrMess',f'{path1c = } ; {DErr}','FileListV8i')
        LogErrDebug('ErrTrac',f'{traceback.format_exc()}','FileListV8i')
    # finally:
    return exclist
###################################################################################################################################
def GetTypeV8i(FileV8i:str)->list[str]:
    """Получение типа базы из v7i"""
    LogErrDebug('Message',f'{FileV8i}','GetTypeV8i')
    rbt:list[str] = []
    try:
        if os.path.isfile(FileV8i):
            rk = DetectCodec(FileV8i)
            with open(FileV8i, mode ='r', encoding = rk) as Hv8i:
                filetxt = Hv8i.readlines() #Читаем файл одним куском
            #------------------------------------------------------------------------------------
            itertxt = iter(filetxt)
            for istr in itertxt: # пошли по строкам Connect=File=
                # Connect=Srvr="web4test1c";Ref="dev25001-acc-fxnxufcy";
                # Connect=File="D:\OMC21230\Accounting30";
                if istr.startswith('Connect='): # нужнам нам строка в наличии Connect=Srvr=
                    rtf = istr.split('=')
                    ibt = rtf[1]
                    rbt.append(ibt)
                    if ibt =='Srvr':
                        rbt.append(rtf[3].strip('\n";'))
                        rbt.append(rtf[2].split(';')[0].strip('";'))
                    else:
                        rbt.append(rtf[2].strip('\n";'))
        else:raise OmcError(f'Файл {FileV8i} отсутсвует')
    except OmcError as Mess:
        LogErrDebug('Warning',f'{Mess}','GetTypeV8i')
    except Exception as DErr:
        LogErrDebug('ErrMess',f'{FileV8i = } ; {DErr}','GetTypeV8i')
        LogErrDebug('ErrTrac',f'{traceback.format_exc()}','GetTypeV8i')
    else:
        LogErrDebug('Success',f'TypeBase={rbt}','GetTypeV8i')
    return rbt
###################################################################################################################################
def GetListIB(Cu:fusr)->list[list[str]]:
    """Получение типа базы из v7i"""
    res:list[list[str]] = []
    ert:list[str] = []
    LogErrDebug('Message',f'{Cu}','GetListIB')
    CuPath = os.path.join(Cu.iph,Cu.omc)
    try:
        if os.path.isdir(CuPath):
            V8iPath = f"{CuPath}\\*.v8i"
            filetxt = glob(V8iPath)
            for istr in filetxt:
                ert = GetTypeV8i(istr)
                res.append(ert)
    except OmcError as Mess:
        LogErrDebug('Warning',f'{Mess}','GetListIB')
    except Exception as DErr:
        LogErrDebug('ErrMess',f' {DErr}','GetListIB')
        LogErrDebug('ErrTrac',f'{traceback.format_exc()}','GetListIB')
    else:
        LogErrDebug('Success',f'{CuPath = } ; CountBase={len(ert)}','GetListIB')
    return res
###################################################################################################################################
def GetListFolder1C(IbasesPath:str)->list[str]:
    """Получение списка 'Folder' для 1с"""
    res = []
    V8iPath = fr"{IbasesPath}\*.v8i"
    LogErrDebug('Message',f'{IbasesPath}','GetListFolder1C')
    BaseList = glob(V8iPath)
    #------------------------------------------------------------------------------------
    for val in BaseList:
        try:
            rk = DetectCodec(val)
            # rpn(f"{rk = }  {val} ")
            with open(val, mode ='r', encoding = rk) as Hcfg:
                filetxt = Hcfg.readlines()
            #------------------------------------------------------------------------------------
            for istr in filetxt:# пошли по строкам
                if istr.startswith('Folder=/'): # нужнам нам строка в наличии
                    # a = istr.split('/')[1].strip()
                    # if a not in res:
                    if (a := istr.split('/')[1].strip()) not in res:
                        res.append(a)
        except Exception as DErr:
            LogErrDebug('ErrMess',f'{rk =} {os.path.basename(val)}','GetListFolder1C')
            LogErrDebug('ErrMess',f'{DErr}','GetListFolder1C')
            LogErrDebug('ErrTrac',f'{traceback.format_exc()}','GetListFolder1C')
    return res
#######################################################################################
def Create_v8i(omcid:str,omcsrv:str,omclev:int,omciph:str,BaseID:str,BaseUsrFldr:str,Server1C:str,TypeIB:str,BaseUsrName:str,
                TemplFl1C:str,dbg:bool = False) ->FRes:
    """Создание файла v8i """
    LogErrDebug('Message',f'{omcid = } ; {omclev = } ; omciph = {omciph} ; {omcsrv = }')
    LogErrDebug('Message',f'{BaseID = } ; {BaseUsrName =} ; BaseUsrFldr = {BaseUsrFldr} ; {Server1C = }')
    if dbg:rpn(f'{omcid = } ; {omclev = } ; omciph = {omciph} ; {omcsrv = }')
    if dbg:rpn(f'{BaseID = } ; {BaseUsrName = } ; BaseUsrFldr = {BaseUsrFldr} ; {Server1C = }')
    IB = FRes();rr1=rr2=rr3=''
    GuID = str(uuid.uuid4())
    #------------------------------------------------
    try:
        PathV8iLkl = os.path.join(omciph,omcid) if omclev else omciph
        if dbg:rpn(f'C8i:20 [yellow]{PathV8iLkl = }')
        PathV8iNet = os.path.join(omcsrv,PathV8iLkl.replace(':','$')) if ':' in PathV8iLkl else PathV8iLkl
        if not os.path.isdir(PathV8iNet):
            os.makedirs(PathV8iNet.lower(), exist_ok=True)
    #-----------------------------------------------------------------
        if TypeIB == 'Serv':
            Connect = ConnS.format(tServer1C = Server1C, tBaseID = BaseID)
            V8iN = f'ibases_{BaseID}.v8i'
        else:#файловая база
            BasePathNet = fr'\\{omcsrv}\D$\{omcid.lower()}'
            BasePathLkl = fr'D:\{omcid.lower()}\{BaseID.lower()}'
            V8iN = f'ibases_{omcid.lower()}_{BaseID.lower()}.v8i'
            Connect = ConnF.format(tBasePath = BasePathLkl)
            if os.path.isdir(BasePathNet):
                BasePathNet = os.path.join(BasePathNet,BaseID.lower())
                if not os.path.isdir(BasePathNet):os.makedirs(BasePathNet,exist_ok=True)
                if TemplFl1C:copytree(TemplFl1C,BasePathNet,symlinks=False,dirs_exist_ok=True)
            else: rr3 = fr'На терминале {omcsrv} отсутвует папка D:\{omcid.lower()} для файловых баз'
    #---------------------------------------------------------------------------------------------------------------
        V8iName = os.path.join(PathV8iNet,V8iN)
        cfgname = os.path.join(PathV8iNet,'1cestart.cfg')
        LogErrDebug('Message',f'{V8iName = };{PathV8iLkl = }')
        #-------------------- если файл уже существует создаём <old> копию ----------------
        if os.path.isfile(V8iName):
            os.replace(V8iName,f'{V8iName[:-3]}old.txt')
        #----------------------------------------------------------------------------------------------------------------
        with open(V8iName, mode ='w', encoding='utf_8') as V8i:
            V8i.write(tv8i.format(tBaseUsrName = BaseUsrName, tConnect = Connect, tGuID = GuID, tBaseUsrFldr = BaseUsrFldr,tArch=Arch))
    #---------------------------------------------------------------------------------------------------------------------
        # rr1 = Customer_v8i(PathV8iLkl, PathV8iNet)
        if Addv8iUsrCfg(cfgname, V8iName):LogErrDebug('Message',rr1 := f'В файл {cfgname} добавлено успешно')
        else: LogErrDebug('Warning',rr1 := f'Ошибка добавления в файл {cfgname}')
    #---------------------------------------------------------------------------------------------------------------------
        rr2 = AllBases_v8i(V8iName) if omclev else '' # :->
    #-------------------------------------------------------------------------------------------
    except OmcError as Mess:
        IB.Mess1 = str(Mess)
        LogErrDebug('Warning',f'{Mess}')
    except Exception as DErr:
        LogErrDebug('ErrMess',f'{DErr}')
        IB.err = 1
        IB.Mess1 = str(DErr)
        IB.Mess2 = traceback.format_exc()
        LogErrDebug('ErrTrac',f'{traceback.format_exc()}')
    else:
        ReportSql(omcid,V8iN,'Create_v8i')
        IB.res = 1
        # IB.Mess1 = V8iName
        IB.Mess1 = rr1
        IB.Mess2 = rr2 if rr2 else ''
        IB.Mess3 = rr3 if rr3 else ''
        LogErrDebug('Success',f'{IB = }')
    return IB
#######################################################################################
def Addv8iUsrCfg(UserIdCfg:str, V8iFullName:str,dbg:bool = False)->bool:
    ''' Добавление ссылки на файл ibases_ххх.v8i -> V8iFullName
        в файл 1cestart_<OMCID>.cfg -> UserIdCfg'''
    LogErrDebug('Message',f'{UserIdCfg = } ; {V8iFullName = }','Addv8iUsrCfg')
    uc = False;servicetxt = '';NewFile = True
    BaseList:dict[str,str] = {}
    try:
        if os.path.isfile(UserIdCfg):
            NewFile = False
            rk = DetectCodec(UserIdCfg)
            with open(UserIdCfg, mode ='r', encoding = rk) as rcfg1:
                filetxt = rcfg1.readlines()
            #--------------------------------------------------------------
            for istr in filetxt:
                if dbg:rpn(f'A8C:10:[purple]{istr = }')
                if not istr:continue
                if istr.startswith('CommonInfoBases='):
                    vpath,vfile = os.path.split(istr[16:].strip())
                    BaseList.setdefault(vfile.lower(),vpath.lower())
                else:servicetxt += istr
            if dbg:rpn(f'A8C:20:[purple]{BaseList = }')
    #------------------------------------------------------------------------------------
        with open(UserIdCfg, mode ='w', encoding = 'utf_8') as wcfg:
            if NewFile:
                #Служебные строки берем из справочника шаблона, сложив м многострочный текст
                rstr = ''.join(f'{tstr[0]}={tstr[1]}\n' for tstr in templ_cfg.items())
                if dbg:rpn(f'A8C:30:[purple]{rstr = }')
                wcfg.writelines(rstr)
            else:#файл старый, пишем что было
                #Новые значения добавляем по дефолту, старые оставляем как есть
                Tservtxt = ServiceStrTempl(servicetxt,dbg)
                wcfg.writelines(Tservtxt)
            for ifl,ipt in BaseList.items():
                if dbg:rpn(f'A8C:40:[purple]FileV8i = {os.path.join(ipt,ifl).lower()}')
                print(f"CommonInfoBases={os.path.join(ipt,ifl).lower()}", file = wcfg)
            if os.path.basename(V8iFullName).lower() not in BaseList:
                print(f'CommonInfoBases={V8iFullName.lower()}', file = wcfg)
        uc = True
    except Exception as DErr:
        LogErrDebug('ErrMess',f'{DErr} ; {UserIdCfg = } ; {V8iFullName = }','Addv8iUsrCfg')
        LogErrDebug('ErrTrac',f'{traceback.format_exc()}','Addv8iUsrCfg')
        uc = False
    return uc
#########################################################################################################################################
def AddUserIB(UserName:str, ServerName:str, v8iFile:str,dbg:bool = False)->FRes:
    '''Добавление базы (ibases) пользователю
    '''
    LogErrDebug('Message',f'{UserName = } ; {ServerName} ; {v8iFile = }')
    if dbg:rpn(f'AUIB:10:[yellow]UserName = {UserName} ; ServerName = {ServerName} ; v8iFile = {v8iFile}')
    AA = FRes()
    v8ipath = os.path.dirname(v8iFile)
    if dbg:rpn(f'AUIB:20:[yellow]v8ipath = {v8ipath}')
    # v8iFile = BaseName
    UserPath = ''
    try:
        if not os.path.isfile(v8iFile):raise OmcError("Отсутсвует файл .v8i")
        #--------------------------------------------------------------
        RUPth = UserHomePath(UserName, ServerName,dbg)
        if dbg:rpn(f'AUIB:30:[yellow]{RUPth = }')
        if RUPth.res:
            UserPath = RUPth.Mess1
            #---------------------------------------------------------------
            UserPath1C = os.path.join(UserPath,r'AppData\Roaming\1C\1CEStart')
            UserGfg1C  = os.path.join(UserPath1C,'1cestart.cfg')
            netuserpath = fr"\\{ServerName}\{UserPath1C.replace(':','$')}"
            LogErrDebug('Message',f'{UserPath1C = } ; {netuserpath = }')
            if dbg:rpn(f'AUIB:40:[yellow]{UserPath1C = } ; {netuserpath = }')
            #Сомнительная операция, может не хватить прав, путь должен существовать наперво
            if not os.path.exists(netuserpath):os.makedirs(netuserpath, exist_ok = True)
        #-------------------------------------------------------------------------------
            # cfgname = fr'{netuserpath}\1cestart.cfg'
            # usr_v8i = fr'{netuserpath}\ibases.v8i'
            usercfg = os.path.join(v8ipath,f'1cestart_{os.path.basename(UserName)}.cfg')
            LogErrDebug('Message',f'usercfg = {usercfg}')#cfgname = {cfgname}
            # if dbg:rpn(f'AUIB:41:[yellow]cfgname = {cfgname}')
            if dbg:rpn(f'AUIB:42:[yellow]usercfg = {usercfg}')
            # if dbg:rpn(f'AUIB:43:[yellow]usr_v8i = {usr_v8i}')
            #------------------------------------------------------------------------
            Addv8iUsrCfg(usercfg, v8iFile)
            # ---------------------------------------------------------------------------
            # if os.path.isfile(cfgname): os.rename(cfgname,f'{netuserpath}\\1cestart_cfg.txt')
            Domus = Get_Domus()
            psstr  = f"$new_pwd = ConvertTo-SecureString -AsPlainText '{Domus.pus}' -Force\n"
            psstr += f"$Cred = New-Object System.Management.Automation.PSCredential '{Domus.cus}', $new_pwd\n"
            psstr += f'$NS = New-PSSession -ComputerName "{ServerName}" -Credential $Cred \n '
            psstr +=  'if( $NS ){Invoke-Command -Session $NS -ScriptBlock { \n '
            psstr += f'New-Item -ItemType SymbolicLink -Path {UserGfg1C} -Target {usercfg} '
            psstr +=  '-Force }}\n'
            if dbg:rpn(f'[yellow]{psstr}')
            UP = PSExec(psstr)
            serr = 'Сбой подключения к удаленному серверу'
            if UP.err and (serr not in UP.Mess1):raise OmcError(UP.Mess1)
            #----------------------------------------------------------------
            if not UP.res:raise OmcError('Симлинк не создан, подробности в лог файле')
            # if os.path.isfile(usr_v8i):
                # os.remove(usr_v8i)
            # copy2(cfgpath_bak, cfgname)
        else:
            raise OmcError("Домашняя папка пользователя не найдена")
    #-------------------------------------------------------------------------------------------------------------------------------
    except OmcError as Mess:
        LogErrDebug('Warning',f'{Mess}')
        for tstr in str(Mess).split():
            if   len(AA.Mess1) < 50 : AA.Mess1 += f' {tstr}'
            elif len(AA.Mess2) < 50 : AA.Mess2 += f' {tstr}'
            else: AA.Mess3 += f' {tstr}'
    except Exception as Mess:
        LogErrDebug('ErrMess',f'{Mess}')
        LogErrDebug('ErrTrac',f'{traceback.format_exc()}')
        rpn(f'[orchid]{Mess}')
        rpn(f'[orchid]{traceback.format_exc()}')
        AA.err = 1
        AA.Mess1 = str(Mess)
        AA.Mess2 = traceback.format_exc()
    else:
        ReportSql(UserName,os.path.basename(v8iFile),'Add symlink v8i')
        AA.res = 1
        AA.Mess1 = 'Ok'
        AA.Mess2 = usercfg
        AA.Mess3 = v8iFile
        LogErrDebug('Success',f'{AA.Mess1} ; {AA.Mess2} ; {AA.Mess3}')
    return AA
####################################################################################################
def DelIB_fromUser(Tsr:fusr, BaseId:list[str],dbg:bool = False)->FRes:
    '''Удаление базы (ibases) у пользователя'''#,UserPath:str
    CustPathV8i = os.path.join(Tsr.iph,Tsr.omc) if Tsr.lev else Tsr.iph
    if dbg:rpn(f'DibFu:10:[yellow]{CustPathV8i = }')
    cfg0File    = os.path.join( CustPathV8i, f'1cestart_{Tsr.usn}.cfg')
    if dbg:rpn(f'DibFu:20:[yellow]{cfg0File = }')
    # UserPathNet = fr"\\{Tsr.srv}\{UserPath.replace(':','$')}"
    # if dbg:rpn(f'DibFu:30:[yellow]{UserPathNet = }')
    # cfg1File = f'{UserPathNet}\\AppData\\Roaming\\1C\\1CEStart\\1cestart.cfg'
    BaseList:list[str] = []
    IB = FRes();servicetxt = ''
    LogErrDebug('Message',f'{cfg0File = }','DelIB_fromUser')
    try:
        if not os.path.isfile(cfg0File): raise OmcError(f'Файл {cfg0File = } отсутсвует')
        rk = DetectCodec(cfg0File)
        with open(cfg0File, mode = 'r',encoding = rk) as edfl:
            filetxt = edfl.readlines()
        #--------------------------------------------------------------
        for istr in filetxt:# а теперь принимаемся за 1cestart
            if not istr:continue
            if istr.startswith('CommonInfoBases='):
                vfile = istr.split('=')[1].strip().lower()
                if dbg:rpn(f'DibFu:40:[yellow]Проверям {vfile}')
                if vfile in BaseId:
                    if dbg:rpn(f'DibFu:50:[green1]удаляем {vfile}')
                    continue
                BaseList.append(istr)
            else:servicetxt += istr
        #----------------------------------------------------------------------------------------------
        Tservtxt = ServiceStrTempl(servicetxt,dbg)
        if dbg:rpn(f'DibFu:60:[yellow] {BaseList = }')
    #--------------------------------------------------------------------------------------------------
        LogErrDebug('Message',f'{BaseList = }','DelIB_fromUser')
        with open(cfg0File, mode ='w', encoding = 'utf_8') as wcfg:
            wcfg.writelines(Tservtxt)
            for ifl in BaseList:
                wcfg.write(ifl)
    #--------------------------------------------------------------------------------------------------
    except OmcError as ErrMs:
        IB.Mess1 = str(ErrMs)
        LogErrDebug('Warning',f'OmcError {str(ErrMs)}','DelIB_fromUser')
    except Exception as ErrMs:
        IB.err = 1
        IB.Mess1 = str(ErrMs)
        LogErrDebug('ErrMess',f'{ErrMs};{IB.Mess1}','DelIB_fromUser')
        LogErrDebug('ErrTrac',f'{traceback.format_exc()}','DelIB_fromUser')
    else:
        IB.res = 1
        IB.Mess1 = 'Выполненно успешно'
        LogErrDebug('Success',IB.Mess1,'DelIB_fromUser')
    return IB
####################################################################################################
def Restore_v8i(Rsr:fusr,UserDict:dict[str,str],dbg:bool=False)->list[str]:
    clearext:list[str] = []
    for usri in UserDict:
        try:
        # Если профиль существует и пользователь не залогинен продолжить
            if UserDict[usri]: # and not UserDict[usri][1]:
                PathUsr = fr"\\{Rsr.srv}\{UserDict[usri].replace(':','$')}"
                UsrV8i = fr'{PathUsr}\AppData\Roaming\1C\1CEStart\ibases.v8i'
                UsrCfg = fr'{PathUsr}\AppData\Roaming\1C\1CEStart\1cestart.cfg'
                NetCfg = fr'{Rsr.iph}\{Rsr.omc}\1cestart_{usri}.cfg' if Rsr.lev else fr'{Rsr.iph}\1cestart_{usri}.cfg'
                LogErrDebug('Message',f'{usri = } ; {NetCfg =}')
                LogErrDebug('Message',f'{UsrV8i} ; {UsrCfg} ')
            # Если файл ibases.v8i в наличии ------------------------------------------------
                if os.path.isfile(UsrV8i):
                    os.remove(UsrV8i)
                ReportSql(usri,PathUsr,'Restore_v8i')
                clearext.append(usri)
            else:
                LogErrDebug('Message',f'На {Rsr.srv} отсутсвует профиль {usri}')
            #--------------------------------------------------------------------------------
        except Exception as ErrMs:
            LogErrDebug('ErrMess',f'{ErrMs}')
            LogErrDebug('ErrTrac',f'{traceback.format_exc()}')
            if dbg:rpn(f'[bright_red]Ошибка:{ErrMs}')
            if dbg:rpn(f'[bright_red]Ошибка:{traceback.format_exc()}')
    return clearext
####################################################################################################
asyncio.run(AReadSQL1C())
if __name__ == '__main__':
    for arg in sys.argv:
        rpn(arg)
    if len(sys.argv) > 3:
        FuName = getattr(sys.modules[__name__],sys.argv[1])
        rrs = FuName(*sys.argv[2:])
        # match sys.argv[1]:
            # case 'Create_v8i':
            # Create_v8i(omc:fusr,Arb:C1c,dbg:bool = False)

    else:
        _mess = f"Автономный тест модуля работы с файлами 1С ver: {__version__}; от: {__verdate__}; файл: {__file__}"
        LogErrDebug('Message',f'{_mess};',os.path.basename(__file__))
    # ------------------------------------------------------------------------------------------------------------
        TC1c = C1c()
        TC1c.BaseID = 'dev25003-acc-fxnxufcy'
        #--------------
        Test = fusr()
        Test.omc = 'dev25005' # OMCID dev23001
        # Test.omc = 'omc170ge'
        Test.usn = 'dev2500501' # User name dev2300101
        Test.dm1 = 'shumeiko' # 1more
        Test.dm0 = 'local' # cloud
        Test.srv = 'Bali'
        Test.lev = 1
        Test.grt = 'Clients-test' # standard-tarif
        Test.uou = 'OU=dev25005-ou,OU=Clients-dev,DC=1more,DC=cloud'
        Test.uph = r'\\moscow\FILES'
        Test.iph = r'\\moscow\ibases'
        # rpn(Test)
        asyncio.run(AChangeIni(Test))
    # rpn(Test)
    input(' :-)> ')
# Create_v8i
# {'Gu':
# omc=dev25005
# usn=
# domain=shumeiko.local
# srv=sh-vds-fran01
# grt=shumeikousersfran01
# uou=OU=dev25005-ou,OU=ShumeikoUsersFran01,DC=shumeiko,DC=local
# cmp=dev25005
# lev=1-\\sh-vds-fran01.shumeiko.local\ibases-\\sh-vds-fran01.shumeiko.local\Files,
# 'Gib':
# BaseID=dev25005-acc-abcd
# TypeIB=Serv
# Server1C=('38103',
# 'Sh-vds-01sh-1c-01')
# ServerBD=('',
# '')
# ServerSR=('',
# ''),
# 'deb':
# True}

    # AddUserIB(r'shumeiko.local\dev2500301', 'sh-vds-fran01.shumeiko.local', r'\\sh-vds-fran01.shumeiko.local\ibases\dev25003\ibases_dev25003-acc-XXXXXXXX.v8i',True)
    # Addv8iUsrCfg(r'\\moscow\ibases\OMC170GE\1cestart_omc170ge26.cfg',r'\\moscow\ibases\OMC170GE\ibases_omc170ge-dmg-demo.v8i')
    # Create_v8i(Test,TC1c,True)
    # Addv8iUsrCfg(r'\\moscow\ibases\DEV24004\1cestart_DEV2400404.cfg',r'\\moscow\ibases\DEV24004\ibases_dev25001-zup-dfhfdhdf.v8i',True)
    # DelcfgV8i(r'\\moscow\ibases\dev25004\1cestart.cfg',['ibases_dev25001-zup-dfhfdhdf.v8i',],True)
    # Customer_v8i(r'D:\ibases',r'\\tandaterm\ibases\ibases_dev23002-acc-fxnugt.v8i')
    # RecoverAllCfg( r'D:\ibases')
    input(':-> ')
    sys.exit(0)
else:
    LogErrDebug('Message',f'Импорт модуля работы с файлами 1С ver: {__version__} ; от {__verdate__}',os.path.basename(__file__))
