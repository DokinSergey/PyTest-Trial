import os, uuid, subprocess
from rich import print, inspect

TermServ = 'tandaterm'
new_usr = '1moredev\dev2300202'
new_pwd = 'Lva85#pjcCU4'
new_pwd = 'Jgv49+sgcNYp'

psstr  = f'$new_pwd = ConvertTo-SecureString -AsPlainText {new_pwd} -Force\n'
psstr += f'$Cred = New-Object System.Management.Automation.PSCredential {new_usr}, $new_pwd\n'
psstr += f'$NS = New-PSSession -ComputerName {TermServ} -Credential $Cred\n'
psstr += 'if( $NS ){Invoke-Command -Session $NS -ScriptBlock {$env:USERPROFILE}\n'
psstr += 'Remove-PSSession -Session $NS}\n'
pls = subprocess.Popen(['powershell', psstr], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
if bool(pls[1]): 
    errlist = list()
    for strline in pls[1].decode('cp866').splitlines():errlist.append(strline.strip())
    raise errlist[0].split('.')[0], errlist[0].split('.')[1]
else:
    res = pls[0].decode('cp866')
    print(res)
