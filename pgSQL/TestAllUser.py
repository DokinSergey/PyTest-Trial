import os
import traceback
import time
# from subprocess import Popen, PIPE#,SubprocessError,TimeoutExpired
from Mod_Common import FRes,fusr,OmcExcept,SeartDomain#,PowerShell,ParsingPowerShell
from Mod_Logging import LogErrDebug,LoggingInit#,ReportSql
from Mod_ADcontrol import ADGetGroup,PSExec#,ADTestUser,
#,ParsingLogin,UserHomePath,TestUserAD,copy2,DetectCodec,budget
# from rich import print
#--------------------------------
_AUTHOR  = 't.me/dokin_sergey'
_VERSION = '1.1.4.3'
_VERDATE = '2024-04-26 17:01'
#######################################################################################
def ADGetUserGroups(OMC:str, Dom1:str = '1more',Grets = 1)->FRes:
    LogErrDebug('Message',f'{OMC} ; {Dom1}','ADGetUserGroups')
    AA = FRes()
    # #--------------------------------------------------
    try:
        psstr  =  'Import-Module ActiveDirectory\n'
        psstr += f'''$ADO = Get-ADUser -Filter "Name -like '{OMC}*'" -server {Dom1} -Properties AccountExpirationDate,memberOf \n'''
        psstr +=  '$ADO | FT name,AccountExpirationDate -HideTableHeaders \n'
        if Grets:psstr +=  '$ADO | select -expand memberof\n'
        rr = PSExec(psstr)
        # print(rr)
        if rr.err:raise OmcExcept('Ошибка выполнения запроса')
        if rr.res:
            for ads in rr.Mess1.splitlines():
                # print(f'{ads = }')
                if ads.strip().lower()[:8] == OMC.lower()[:8]:
                    ss = ads.split()
                    ss0 = ss[0].strip()
                    ss1 = ss[1].strip() if len(ss) >1 else ''
                    AA.Mess1 += f'{ss0}:{ss1}\n'
                    continue
                if ads.strip().startswith('CN='):
                    AA.Mess3 += ads.strip().split(',')[0].split('=')[1] + '\n'
                    continue
                # if ads.strip():AA.Mess2 = ads.strip()
            AA.res   = 1 # объект
            # print(AA)
        else:raise OmcExcept(f'{OMC} не найден в AD')
    #--------------------------------------------------
    except OmcExcept as Mess:
        AA.Mess1 = 'OmcExcept'
        AA.Mess2 = str(Mess)
        LogErrDebug('Warning',f'{Mess}','ADGetUserGroups')
    except Exception as Mess:
        AA.err = 1
        AA.Mess1 = str(Mess)
        AA.Mess2 = traceback.format_exc()
        LogErrDebug('Failure', f'{Mess}','ADGetUserGroups')
        LogErrDebug('Failure', f'{traceback.format_exc()}','ADGetUserGroups')
    else:
        LogErrDebug('Success',f'{AA =}','ADGetUserGroups')
    return AA
#######################################################################################
def ADGetStruk(OMC:str, Dom1:str = '1more', Dom0:str = '')->FRes:
    LogErrDebug('Message',f'{OMC} ; {Dom1} ; {Dom0}','ADGetStruk')
    AA = FRes()
    # server = f'"{Dom1}.{Dom0}"' if Dom0 else f'"{Dom1}"'
    GrList = {};UsrLst = {};UsrBlkDct = {}
    #--------------------------------------------------
    try:
        rr0 = ADGetGroup(f'{OMC}*')
        if rr0.res:
        # if (rr0: = ADGetGroup(f'{OMC}*')).res:
            for ts in rr0.Mess1.splitlines():
                srvlst = []
                rr1 = ADGetGroup(f'{ts}')
                if rr1.res:
                    for st in rr1.Mess3.splitlines():
                        tnd = SeartDomain('Grt',st)
                        if tnd.srv:srvlst.append((st.lower(),tnd.srv.lower()))
                if ts in GrList:GrList[ts.lower()].append(srvlst)
                else:GrList[ts.lower()] = srvlst
        # else:
    #--------------------------------------------------
        rr2 = ADGetUserGroups(OMC,'1more',0)
        for dr0 in rr2.Mess1.splitlines():
            usrdr = dr0.strip().lower().split(':')[0]
            usblk = dr0.strip().lower().split(':')[1]
            UsrBlkDct[usrdr] = usblk
            # print(usrdr)#User
            rr3 = ADGetUserGroups(usrdr,'1more',1)
            if rr3.res:
                for dr1 in rr3.Mess3.splitlines():
                    UGrList={}
                    ts = dr1.strip().lower()
                    if ts[:8] == OMC.lower():
                        if ts in GrList:
                            UGrList[ts] = GrList[ts]
                            # print('\t',ts,UGrList[ts])#gr omcid
                            break
                        if dr1.strip().lower()[:8] == OMC.lower()[:8]:
                            rr4 = ADGetGroup(dr1)
                            if rr4.res:
                                for dr2 in rr4.Mess3.splitlines():
                                    if dr2.strip().lower()[:8] != OMC.lower():
                                        grtr = dr2.strip().lower()
                                        tnd = SeartDomain('Grt',grtr)
                                        if tnd.srv:srvlst.append((grtr.lower(),tnd.srv.lower()))
                        if ts in UGrList:UGrList[ts].append(srvlst)
                        else:UGrList[ts] = srvlst
            if usrdr in UsrLst:UsrLst[usrdr].append(UGrList)
            else:UsrLst[usrdr] = UGrList
    #-------------------------------------------------------------------------------------------------
        # for xi,yi in UsrLst.items():
            # print(xi,yi)
        print(UsrBlkDct)
    #-------------------------------------------------------------------------------------------------
    except OmcExcept as Mess:
        AA.Mess1 = 'OmcExcept'
        AA.Mess2 = str(Mess)
        LogErrDebug('Warning',f'{Mess}','ADGetStruk')
    except Exception as Mess:
        AA.err = 1
        AA.Mess1 = str(Mess)
        AA.Mess2 = traceback.format_exc()
        LogErrDebug('Failure', f'{Mess}','ADGetStruk')
        LogErrDebug('Failure', f'{traceback.format_exc()}','ADGetStruk')
    else:
        AA.res = 1
        AA.rDict = UsrLst
        LogErrDebug('Success',f'{AA =}','ADGetStruk')
    return AA
#################################################################################################################
def GetBlokDate(UsrID:str, Dom1:str = '1more',Dom0:str = 'cloud'):
# (get-date $_.AccountExpirationDate).AddDays(-1)}
    LogErrDebug('Message',f'{UsrID} ; {Dom1} ; {Dom0}','GetBlokDate')
    psstr  =  'Import-Module ActiveDirectory\n'
    psstr += f'''$ADO = Get-ADUser -Filter "Name -like '{UsrID}'" -server {Dom1} -Properties AccountExpirationDate,memberOf \n'''
    psstr +=  '$ADO.Name\n'
    psstr +=  'get-date $ADO.AccountExpirationDate\n'
    rr = PSExec(psstr)
    print(rr.Mess1)
#################################################################################################################
if __name__ == '__main__':
    start_time = time.perf_counter()
    debug = True
    PROJECT = 'Test_OMC_Customer'
    UserProject = os.getlogin()
    LoggingInit(PROJECT,UserProject)
    from platform import python_version
    print(f'Запушен из {__file__} ; версии: {_VERSION} ; от {_VERDATE} ; python ver: {python_version()}','Mod_Main',1)
    Test = fusr()
    Test.omc = 'omc18047'
    Test.omc = 'omc170GE'
    # Test.omc = 'dev24001'
    # Test.omc = 'dev24001'
    ADGetStruk(Test.omc)
    # GetBlokDate('OMP2303701')
    stop_time = time.perf_counter()
    Inetrval = stop_time - start_time
    input(f'{Inetrval}:-> ')
    os._exit(0)
#########################################################################################################################################
else:
    LogErrDebug('Message',f'Импорт модуля УВВ Main ; версии {_VERSION} ; от {_VERDATE}',os.path.basename(__file__))
