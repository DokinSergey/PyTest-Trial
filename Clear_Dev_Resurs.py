import os,traceback,time
from wmi import WMI
from rich import print as rpn
from glob import glob
from ldap3 import Connection, Server,OFFLINE_AD_2012_R2,NTLM#,ALL_ATTRIBUTES, ANONYMOUS, SIMPLE, SYNC, ASYNC,Tls
__author__  = 't.me/dokin_sergey'
__version__ = '1.0.12'
__verdate__ = '2024-12-25 17:09'
#######################################################################################################################
flspath = r'\\moscow\FILES'
ibapath = r'\\moscow\ibases'
SRKpath = r'\\more\COPY\_log\psql-dump-enabled'
ArxPath = r'\\moscow2\RESERVS2_MANUAL'
ServerList =("cl-15", "cl-25", "cl-33","cl-34","cl-35","cloud", "cloud-vip",'OMC22207', 'bali','Baikal','MGU','tandadev',)
CustUser = r'dev%'
#----------------------------------------------------------------------------------------------------
try:
    rpn(f'[cyan1]Программа контроля ресурсов DEV.Версия [green1]{__version__} [cyan1]от {__verdate__}')
    while True:
        time_start = time.perf_counter()
        os.system('cls')
        rpn('[green1]*'*80)
        rpn('Ресурсы AD')
    #------------------------------------------------------------------------------------------------------------------
        server = Server('1more.cloud', get_info=OFFLINE_AD_2012_R2)
        try:
            with Connection(server, user = r'1more.cloud\script4service', password='MhNn@wQDIYmZ',
                authentication=NTLM, auto_bind=True) as conn:
                conn.search('dc=1more,dc=cloud', '(cn=dev*)',attributes=['cn','distinguishedName','objectCategory',])
            #----------------------------------------------------------------------------------------------------------
            _adl={}
            for _ia in conn.response: # type: ignore
                if 'attributes' in _ia:
                    _ib:dict[str,str] = _ia['attributes']
                    ou = _ib['distinguishedName'].split(',')[-3].split('=')[1]
                    _adl.setdefault(ou,{})
                    # _adl[ou].append({_ib['cn']:_ib['objectCategory'].split(',')[0].split('=')[1]})
                    _adl[ou][_ib['cn']] = _ib['objectCategory'].split(',')[0].split('=')[1]
            # rpn(_adl)
    #--------------------------------------------------------------------------------------------
            if bool(_adl):
                for _gr,_vr in _adl.items():
                    rpn(f'\n\t[bright_blue]{_gr}')
                    for _ra,_rb in _vr.items():
                        if 'Group' in _rb:rpn(f'\t\t[cyan1]{_ra:12}[bright_blue]{_rb}')
                        else:rpn(f'\t\t[cyan1]{_ra:12}[green1]{_rb}')
            rpn()
    #----------------------------------------------------------
        except Exception as Mess:
            rpn(f'[orchid]{Mess}')
            rpn(f'[orchid]{traceback.format_exc()}')
    #----------------------------------------------------------------------------------------------------------------------------------------------
        time_1 = time.perf_counter()
        Inetrval = time_1 - time_start
        rpn(f'[yellow]Время выполнения [bright_yellow]{Inetrval:.7f}\n')
        rpn('Наличие профайлов на терминальных серверах')
        for sl in ServerList:
            rpn(f'\t[bright_blue]Сервер [bright_green]{sl}')
            pc = WMI(computer=sl)
            # wql = "SELECT LocalPath FROM Win32_UserProfile WHERE '%" + CustUser + "' like LocalPath"
            wql = "SELECT LocalPath FROM Win32_UserProfile WHERE '%dev%' like LocalPath"
            qrt = pc.query(wql)
            for LP in qrt:
                rpn(f'\t\t[bright_cyan]{LP.LocalPath}')
            if qrt:rpn()
        # rpn(f'[green1]{"-"*50}')
        time_2 = time.perf_counter()
        Inetrval = time_2 - time_1
        rpn(f'[yellow]Время выполнения [bright_yellow]{Inetrval:.7f}\n')
        #------------------------------------------------------------------------------------
        flsmask = fr'{flspath}\dev*'
        if tmplst:=glob(flsmask):
            rpn('Папки для дисков "U"')
            for ifl in tmplst:
                rpn(f'\t[cyan1]{ifl}')
        #-------------------------------
        flsmask = fr'{ibapath}\dev*'
        if tmplst:=glob(flsmask):
            rpn('Папки для "Ibases"')
            for ifl in tmplst:
                rpn(f'\t[cyan1]{ifl}')
        #-------------------------------
        flsmask = fr'{ibapath}\*\ibases_dev*'
        if tmplst:=glob(flsmask, recursive=True):
            rpn('Базы данных')
            for ni,ifl in enumerate(tmplst):
                rpn(f'\t[green1]{ni+1:3}: [cyan1]{ifl}')
        #-------------------------------
        flnomc = r'\\moscow\ibases\OMC_ibases\1cestart.cfg'
        ni= 1
        if os.path.isfile(flnomc):
            rpn('Наличие в общем списке баз 1С')
            with open(flnomc, mode = 'r', encoding = 'utf_8') as sn:
                filetxt = sn.readlines()
            for lsts in filetxt:
                fln =lsts.strip().split('=',1)[1]
                pfln,nfln = os.path.split(fln)
                if 'dev' in pfln or '_dev' in nfln:
                    rpn(f'\t[green1]{ni:3}: [cyan1]{pfln} ; {nfln}')
                    ni +=1
        #-------------------------------
        flsmask = fr'{SRKpath}\dev*'
        if tmplst:=glob(flsmask):
            rpn('Задания для "СРК"')
            for ifl in tmplst:
                rpn(f'\t[cyan1]{ifl}')
        #-------------------------------
        flsmask = fr'{ArxPath}\dev*'
        rpn('Архивы удаленных учеток')
        if tmplst:=glob(flsmask):
            for ifl in tmplst:
                rpn(f'\t[cyan1]{ifl}')
        #------------------------------------------------------------------------
        time_stop = time.perf_counter()
        Inetrval = time_stop - time_start
        rpn(f'[yellow]Общее время выполнения [bright_yellow]{Inetrval:.7f}\n')
        if input('Повторить:-> '):break
# except TimeoutExpired as Mess:
    # rpn(f'[orchid]Timeout: {Mess}')
except Exception as Mess:
    rpn(f'[orchid]Ошибка: {Mess = }')
    rpn(f'[orchid]{traceback.format_exc()}')
else:
    rpn(f'[green1]Выход{"-"*20}')
