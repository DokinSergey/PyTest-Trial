import wmi
import os
import winrm

server = 'tandaterm'

NewUser = '1moredev\dev2300101'
NewPass = 'Lva85#pjcCU4'

print(server, NewUser, CUser, '\n')

wss = winrm.Session(server, auth=(NewUser, NewPass), transport='credssp')
#wss = winrm.Session('http://tandaterm:5985/wsman', auth=('1moredev\dev2300101', 'Lva85#pjcCU4'), transport='credssp')
#wss = winrm.Session(server, auth=('1moredev\DokinS', 'Gkt78j4eUSi'), transport='credssp')

#r = wss.run_cmd('dir')
r = wss.run_ps('$env:USERPROFILE')
#r = wss.run_ps('host')

#r = wss.run_cmd('ipconfig', ['/all'])
print(str(r.std_out,encoding='gbk'))  # Полученная информация о печати
print(str(r.std_err,encoding='gbk')) #Pprint ошибка информация

exit()
pc = wmi.WMI(server) 
wql = "SELECT LocalPath FROM Win32_UserProfile WHERE (Special = 'FALSE') and not(LocalPath like '%[.#]%' )" 
qrt = pc.query(wql)
for usr in qrt:
   # pass
    print(os.path.basename(usr.LocalPath).ljust(20), usr.LocalPath)
