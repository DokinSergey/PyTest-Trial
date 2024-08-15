import os
# import mi
from wmi import WMI
from rich import print
# pfw = dir(mi)
# pfw = system.wmi.query("SELECT LocalPath, Loaded FROM Win32_UserProfile WHERE '%' like LocalPath and 'S-1-5-21%' like sid")
# for ist in pfw:
    # print(ist)
pc = WMI()
wql = "SELECT Antecedent,Dependent FROM Win32_LoggedOnUser"# WHERE '%' like Antecedent.SID"# and '%' like LocalPath"S-1-5-21
qrt = pc.query(wql)#[0].properties.keys()
print(type(qrt))
# if qrt:
for ius in qrt:
    # print(ius)
    print()
    try:
        print(f'Caption = {ius.Antecedent.SID}')
        print(f'Caption = {ius.Antecedent.Caption}')
        print(f'Description = {ius.Antecedent.Description}')
        print(f'Domain = {ius.Antecedent.Domain}')
        print(f'Name = {ius.Antecedent.Name}')
        print(f'FullName = {ius.Antecedent.FullName}')
        print(f'LocalAccount = {ius.Antecedent.LocalAccount}')
        print(f'LogonId = {ius.Dependent.LogonId}')
        print(f'LogonType = {ius.Dependent.LogonType}')
    except Exception as EMess:
        pass
        print(f'Ошибка: {EMess}')
    # for uis in  ius:
        # print(uis)
    # print(ius.Antecedent)#.Caption).SID
    # 
    # print(ius.Loaded)
#----------------------------------------------------------------------
input('\nВыход :-> ')
os._exit(0)
