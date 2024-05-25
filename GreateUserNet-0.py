import wmi
import os
ID_cm  = 'OMC170GE26'
ID_cm = 'DokinSergey'
server = 'bali'
server = 'tandaterm'
#server = 'cloud'
#print (os.getlogin())





pc = wmi.WMI(server) 
#pc = wmi.WMI() 
# usrs = pc.Win32_UserProfile(["LocalPath", "Special"], Special = 'FALSE')
# wql = "SELECT LocalPath FROM Win32_UserProfile WHERE '%" + CustUser + "' like LocalPath"
wql = "SELECT LocalPath FROM Win32_UserProfile WHERE (Special = 'FALSE') and not(LocalPath like '%[.#]%' )" 
qrt = pc.query(wql)

# UsersPath = {}
# print(*qrt)
#print(usrs.LocalPath)
# exit(1)
for usr in qrt:
    #pass
    print(os.path.basename(usr.LocalPath).ljust(15), usr.LocalPath)
    #print(usr.LocalPath)
    #print('-----------------------------------------')
    #UsersPath[os.path.basename(usr.LocalPath)] = usr.LocalPath
    #print(os.path.basename(usr.LocalPath), '\t', usr.LocalPath)
    
    #help(usr)