import os
import traceback
from rich import print as rpn
# from Mod_Common import FRes,fusr,OmcError,SeartDomain,GetListHomePath,PSExec,Get_Domus,AReadSQLini
from Logg import LogErrDebug#, Logging
# from Mod_Logging import LogErrDebug,LoggingInit,ReportSql
from ldap3 import Connection, Server,ALL,NTLM,ALL_ATTRIBUTES#,MODIFY_REPLACE,MODIFY_DELETE#, ANONYMOUS, SIMPLE, SYNC, ASYNC,Tls
# from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups as addUsersInGroups
# from ldap3.extend.microsoft.removeMembersFromGroups import ad_remove_members_from_groups as removeUsersGroups
#,ParsingLogin,UserHomePath,TestUserAD,copy2,DetectCodec,PowerShell
from ldap3.core.timezone import OffsetTzInfo
from datetime import datetime as dt#timedelta,date,
# pylint: disable-msg=W0603,W0602
__author__  = 't.me/dokin_sergey'
__version__ = '0.0.0'
__verdate__ = '2025-05-28 14:57'
###########################################################################################################################################
def GetADBlockedUser(dm1:str = '1more',dm0:str = 'cloud',dbg:bool = False):
# def get_UserAD()->tuple[dict[str,str]]:
    LogErrDebug('Message',f'Start {dm1}.{dm0}')
    if dbg:rpn(f'Start debug get_UserAD {dm1}.{dm0}')
    ADServer = Server(rf'ldap://{dm1}.{dm0}', get_info=ALL)
    try:
        # Domus = Get_Domus()
        with Connection(ADServer, user = r'1more.cloud\script4service', password = r'MhNn@wQDIYmZ',
            authentication=NTLM, auto_bind=True) as conn:
            ADuser = r'omc222071*'
            # ddt = dt(2025, 6, 25, 0, 0, 0, 0, +2)#'lastLogon',(cn={ADuser})(!(accountExpires=b'9223372036854775807'))
            # ddt =  dt(9999, 12, 31, 23, 59, 59, 999999, tzinfo=OffsetTzInfo(offset=0, name='UTC'))(!(accountExpires=20250625181408Z))
            # ddt = '20250625181408Z'
            ddt = b'0'
            conn.search(f'dc={dm1},dc={dm0}', f"(&(objectclass=person)(cn={ADuser})(!(accountExpires={ddt})))",attributes=ALL_ATTRIBUTES)
                #['cn','distinguishedName','objectCategory','company','memberOf','accountExpires', 'Enabled',])
        ##----------------------------------------------------------------------------------------
        _alist:list[dict[str,str]] = []
        for _ia in conn.response: # type: ignore
            if 'attributes' in _ia:
                rpn(_ia)
                _ib:dict[str,str] = _ia['attributes']
                _alist.append(_ib)
        _res = tuple(_alist)
    ##--------------------------------------------------------------------------------------------
        LogErrDebug('Message',f'{_res}')
        if dbg and bool(_res):
            for _gr in _res:
                rpn('-'*80)
                rpn(f'               cn : {_gr['cn']}')
                rpn(f'distinguishedName : {_gr['distinguishedName']}')
                rpn(f'   objectCategory : {_gr['objectCategory']}')
                rpn(f'          company : {_gr['company']}')
                # rpn(f'          Enabled : {_gr['Enabled']}')
                rpn(f'   accountExpires : {_gr['accountExpires']}')
                for _mof in _gr['memberOf']:
                    rpn(f'         memberOf : {_mof}')
            rpn('-'*80,'\n')
    ##----------------------------------------------------------
    except Exception as Mess:
        LogErrDebug('ErrMess', f'{Mess}')
        LogErrDebug('ErrTrac', f'{traceback.format_exc()}')
        if dbg:rpn(f'[yellow]{traceback.format_exc()}')
        if dbg:rpn(f'[orchid]{Mess}')
    # if dbg:rpn(f'[yellow]{_res = }')
    return _res # type: ignore
###########################################################################################################################################
def RpnBlockedUser():
    pass
###########################################################################################################################################
def SaveReportBU():
    pass
###########################################################################################################################################
if __name__ == '__main__':
    import time
    dtnow = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    start_time = time.perf_counter()
    _mess = f"Поиск {dtnow} заблокированных ползователей ver: {__version__}; от: {__verdate__}"
    PROJECT = 'ADBlockedUser'
    UserProject = os.getlogin()
    # LoggingInit(PROJECT,UserProject)
    rpn(_mess)
    LogErrDebug('Message',f'{_mess};',os.path.basename(__file__))
    time_0 = time.perf_counter()
    ##-------------------------------------------------------------------------------------------------
    while not (reply := input('Выполнить? :-)> ')):
        GetADBlockedUser(dbg = True)
    ##-------------------------------------------------------------------------------------------------
    stop_time = time.perf_counter()
    Inetrval = stop_time - start_time
    input(f'{Inetrval:.7f} :-> ')
    os._exit(0)
