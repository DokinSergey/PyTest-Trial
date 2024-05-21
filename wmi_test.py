# import wmi
from wmi import WMI
# TermServer = 'Bali'
# CustUser = ''
# TestInServ = 0
# """ Получение домашней папки юзверя на терминальном сервере"""
# UserPath = ''
# pc = wmi().WMI(TermServer)
pc = WMI('localhost')
wql = "SELECT LocalPath, Loaded FROM Win32_UserProfile WHERE SID like 'S-1-5-21%'"
qrt = pc.query(wql)
for iq in qrt:
    print(iq.LocalPath,iq.Loaded)


# if TestInServ:
    # wql = f"SELECT LocalPath FROM Win32_UserProfile WHERE '%{CustUser}' like LocalPath and Loaded = TRUE"
# else:
    # wql = f"SELECT LocalPath FROM Win32_UserProfile WHERE '%{CustUser}' like LocalPath"

    # if len(qrt) == 1:
        # UserPath = qrt[0].LocalPath
# wql = f"SELECT LocalPath FROM Win32_UserProfile WHERE Loaded = TRUE"
