import wmi, os, sys #as WMI

# $Lpid = $PID
# $QueryTXT = "select * from Win32_Process where ProcessId = $Lpid "

# $RQ = Get-WmiObject -Query $QueryTXT
# $ParentPID = $RQ.ParentProcessId
PID = os.getpid()
print(PID, str(PID)) 



# if len(qrt) == 1:
    # ParentPID = qrt[0].ParentProcessId
print(sys.argv)
ParentPID = os.getppid()
wql = "SELECT Caption FROM Win32_Process WHERE ProcessId = " + str(ParentPID)
pc = wmi.WMI()
qrt = pc.query(wql)
if qrt[0].Caption != 'notepad++.exe':
    input('Нажмите "Enter" для закрытия окна')