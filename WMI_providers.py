from rich import print
from wmi import WMI
import os 

UserPath = 'OMC170GE26'
#UserPath = 'KirillovO'
TermServer = 'baikal'
pc = WMI(TermServer)
wql = "SELECT * FROM Win32_UserProfile WHERE '%" + UserPath + "' like LocalPath and Loaded = TRUE and Special = FALSE"
wql = "SELECT * FROM win32_loggedonuser "
wql = "SELECT * FROM Win32_TerminalService"
wql = "SELECT ActiveSessions FROM Win32_PerfFormattedData_LocalSessionManager_TerminalServices"
wql = "SELECT * FROM Win32_PerfFormattedData_LocalSessionManager_TerminalServices"
wql = "SELECT * FROM Win32_LogonSession "
wql = "SELECT LogonId FROM Win32_LogonSession "
#wql = "SELECT * FROM win32_computersystem"
wql = "SELECT * FROM Win32_LoggedOnUser"
#wql = "SELECT * FROM win32_computersystem"
# wql = "SELECT * FROM Win32_UserProfile WHERE Special = FALSE" 
#'%" + UserPath + "' like LocalPath and Loaded = TRUE and Special = FALSE"
#wql = "Select * from Win32_SID where SID='S-1-5-21-3469434719-2898995916-231618229-4718'"
qrt = pc.query(wql)
# print(qrt)
for tr in qrt:
    print(tr)
    # print(tr.LogonId)
    # print(f'User  :{os.path.basename(tr.LocalPath)}')
    # print(f'Loaded:{tr.Loaded}')
    # print(tr.Status)
    # print(tr.Special)
    # print(tr.Status)
# if len(qrt) == 1:
    # print(qrt[0].LocalPath) 

#'%" + UserPath + "' like LocalPath and

# for u in w.Win32_UserAccount(["Name"]): #Net
#Win32_PerfRawData_TermService_TerminalServicesSession
#Win32_NetworkLoginProfile
#Win32_ServerConnection
#Win32_ServerSession
#Win32_SessionConnection
#Win32_SystemUsers
#Win32_UserInDomain
#Win32_UserAccount
#Win32_UserProfile
