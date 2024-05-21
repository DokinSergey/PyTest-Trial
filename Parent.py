import wmi, os 
pc = wmi.WMI()
ParentPID = pc.query("SELECT * FROM Win32_Process WHERE ProcessId = " + str(os.getpid()))[0].ParentProcessId
qrt = pc.query("SELECT Caption FROM Win32_Process WHERE ProcessId = " + str(ParentPID))[0].Caption

print(qrt)