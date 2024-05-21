import os, uuid, subprocess
from rich import print, inspect

UserID = 'DEV2200101'
DC1 = '1moredev'
DC0 = 'local'

psstr  =  'Import-Module ActiveDirectory\n'
# psstr += f'Get-ADUser -Filter "sAMAccountName -like \'{UserID}\'" -SearchBase "DC=1more,DC=cloud"'-Properties *
# psstr += f'Get-ADObject -Filter "Name -like \'{UserID}\'" -SearchBase "DC={DC1},DC={DC0}" -Properties ObjectClass | FL ObjectClass, Name\n'#
psstr += f'Get-ADObject -Filter "Name -like- \'{UserID}\'" -server {DC1}.{DC0} | FL'
pls = subprocess.Popen(['powershell', psstr], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()#[0]
print(pls[0].decode('cp866'))
longstr = pls[1].decode('cp866').splitlines()[0]
ig =[];ik = 0
for tstr in longstr.split():
    if ik == len(ig):ig.append('')
    ig[ik] += f' {tstr}'
    if ik < 2 and len(ig[ik]) > 50: ik +=1

        
# else:
    # ig.append(longstr)
    
print(len(ig))
print(ig)
# print(pls[0].decode('utf-8').splitlines())
resDict={} # тут дикт созданного Юзера, проверяем по ObjectGUID[0]
# for strline in pls[0].decode('utf-8').splitlines():
    # if strline: #.startswith('DistinguishedName'):
        # ADpath = strline.lstrip('DistinguishedName :')
        # resDict.setdefault(strline.split(':')[0].strip(), strline.split(':')[1].strip())
# ADpath = ADpath.split(',',1)[1]
# print(ADpath)
# print(resDict)
Message3 = 'Get-ADObject : Ошибка анализа запроса: "Name -like- \'DEV23001\'" Сообщение об ошибке: "Operator Not supported: -like-" с расположением в: "6".'
# print(str(Message3))

# psstr  = 'Import-Module ActiveDirectory \n'
# psstr += f'Get-ADGroup -Filter "Name -like \'{OMCID}\'"'
# pls = subprocess.Popen(['powershell', psstr], stdout=subprocess.PIPE).communicate()

psstr  = 'Import-Module NTFSSecurity\n'
psstr += f'Add-NTFSAccess -Path {userfolder} -Account {username} -AccessRights "Fullcontrol" -PassThru'
pls = subprocess.Popen(['powershell', psstr], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
if bool(pls[1]): 
    raise PowerShell (pls[1].decode('cp866').splitlines()[0])