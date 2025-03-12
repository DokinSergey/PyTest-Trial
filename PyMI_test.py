import os,traceback
# import mi
from wmi import WMI
from rich import print as rpn
# pfw = dir(mi)
# pfw = system.wmi.query("SELECT LocalPath, Loaded FROM Win32_UserProfile WHERE '%' like LocalPath and 'S-1-5-21%' like sid")
# for ist in pfw:
    # print(ist)
# pc = WMI()
# wql = "SELECT Antecedent,Dependent FROM Win32_LoggedOnUser"# WHERE '%' like Antecedent.SID"# and '%' like LocalPath"S-1-5-21
# wql = "
# qrt = pc.query(wql)#[0].properties.keys()
try:
    # TermSrv = 'sh-vds-01.shumeiko.local'
    # TermSrv = 'sh-dc-01.shumeiko.local'
    # TermSrv = 'SH-VDS-FRAN01.shumeiko.local'
    # DmnUser = 'script4service@shumeiko.local'
    # DmnPssd = 'Vx964&iugo7w'
    TermSrv = 'baikal.1more.cloud'#computer=TermSrv
    DmnUser = 'script4service@1more.cloud'
    DmnPssd = 'MhNn@wQDIYmZ'
    pc = WMI(computer=TermSrv,user=DmnUser, password=DmnPssd)
    wql = "SELECT LocalPath, Loaded, Documents FROM Win32_UserProfile WHERE SID like 'S-1-5-21%' and '%' like LocalPath"
    qrt = pc.query(wql)
    # rpn(type(qrt))
    # rpn(qrt)

    for ius in qrt:
        # rpn(ius)
        rpn(f'LocalPath = {ius.LocalPath:30} {ius.Loaded}')#, end = '\t') 
        # rpn(f'Documents = {ius.Documents}')
    # print()Loaded
    # try:
        # print(f'Caption = {ius.Antecedent.SID}')LocalPath, Loaded
        # print(f'Caption = {ius.Antecedent.Caption}')
        # print(f'Description = {ius.Antecedent.Description}')
        # print(f'Domain = {ius.Antecedent.Domain}')
        # print(f'Name = {ius.Antecedent.Name}')
        # print(f'FullName = {ius.Antecedent.FullName}')
        # print(f'LocalAccount = {ius.Antecedent.LocalAccount}')
        # print(f'LogonId = {ius.Dependent.LogonId}')
        # print(f'LogonType = {ius.Dependent.LogonType}')
    # except Exception as EMess:
        # pass
        # print(f'Ошибка: {EMess}')
    # for uis in  ius:
        # print(uis)
    # print(ius.Antecedent)#.Caption).SID
    # 
    # print(ius.Loaded)
except Exception as EMess:
    rpn(f'[orchid]{EMess}')
    rpn(f'[yellow]{traceback.format_exc()}')
#----------------------------------------------------------------------
input('\nВыход :-> ')
os._exit(0)
