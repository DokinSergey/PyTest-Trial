# import time
from rich import print
# import shutil
from Mod_Common import os,Popen,PIPE,budget
bd = budget()
CustUser = 'DokinSergey'
UserPath = ''

TestInServ = 'True'
# True
#False
ServersTerm = "baikal"
psstr  = f'$pub_pwd = ConvertTo-SecureString -AsPlainText {bd.pwrd} -Force \n'
psstr += f'$Cred = New-Object System.Management.Automation.PSCredential {budget.user},$pub_pwd \n'
psstr += f'Get-WmiObject -Class Win32_UserProfile -Credential $Cred -ComputerName "{ServersTerm}" -Property LocalPath, Loaded | select LocalPath, Loaded'
with Popen(['powershell', psstr], stdout = PIPE, stderr = PIPE) as popps:
    pls = popps.communicate()
if bool(pls[1]):
    print('err:>',pls[1].decode('cp866'))
if bool(pls[0]):
    UsPf={}
    # for j,lstr in enumerate(pls[0].decode('cp866').splitlines()):
    for lstr in pls[0].decode('cp866').splitlines():
        ld = lstr[-7:].strip()
        ls = lstr[:-7].strip()
        if ld in ('True','False'):
            pass
            # print(f'{j:2} : {ld:5} : {ls} : {bool(ld)}')os.path.basename(
            print(f'{ld:5} : {ls} : {bool(ld)}')
            UsPf[os.path.basename(ls)] = (ls,ld)
print(UsPf)
if UsPf.get(CustUser) and UsPf.get(CustUser)[1] == str(TestInServ):
    res = UsPf[CustUser][0]
else:
    res = ''
# res = f[CustUser]  else 'No'

print(f'{res = }')
# print(str(True))
# qrt = pc.query(wql)
# if len(qrt) == 1:
    # UserPath = qrt[0].LocalPath
