import os, locale
import pythonnet
import clr
from System.Diagnostics import ProcessStartInfo,Process
from System.Text import Encoding #

print('Стартовое окно')
try:
    filerun = 'N_Create_v8i'
    PSI = ProcessStartInfo()
# !!!! Ахтунг !!!! Здесь и в ярлыке должны быть РАЗНЫЕ программы запуска
# !!!! например py  python 
    PSI.WorkingDirectory = os.path.realpath('') # Папка проекта????
    print(PSI.WorkingDirectory)
    # PSI.FileName = "python.exe"
    # PSI.Arguments = os.path.join(os.path.realpath(''),'RunAsRun.py')-Verb 'RunAs' 
    PSI.FileName  = 'powershell.exe'
    # PSI.Verb = ' -i -d -c'
    # PSI.Verb = 'RunAs'
    PSI.LoadUserProfile = False
    # PSI.Arguments = r'''-command "Start-Process 'py.exe' -Verb RunAs -WorkingDirectory 'C:\Dev\Py_OMC_Customer\PSRunAs' -ArgumentList ' -i RunAdmin.py\' \n pause"'''
    # PSI.Arguments = r'-command "Start-Process \'py.exe\' -Verb RunAs -WorkingDirectory \'C:\\Dev\\Py_OMC_Customer\\PSRunAs\' -ArgumentList \' -i RunAdmin.py\'" pause'
    PSI.Arguments = f''' -noexit -command "Start-Process py.exe -Verb RunAs -ArgumentList ' -i -m {filerun}'"'''
    print(PSI.Arguments)
# Pause"""
    #-------------------------------------------------
    PSI.CreateNoWindow = False#True #
    # PSI.RedirectStandardOutput = True#False#
    # PSI.RedirectStandardError = True#False#
    # PSI.RedirectStandardInput = True
    #--------------------------------------------------------
    PSI.UseShellExecute = False
    PSI.Domain = '1more.cloud'
    PSI.UserName = "script4service" #@1more.cloud
    PSI.PasswordInClearText = "MhNn@wQDIYmZ"
    # PSI.Password = SecureString("MhNn@wQDIYmZ")
    #-----------------------------------------------
    # PSI.StandardOutputEncoding = Encoding.GetEncoding(1251)
    # PSI.StandardInputEncoding = Encoding.GetEncoding(1251)
    # PSI.StandardErrorEncoding = Encoding.GetEncoding(1251)
    PSI.ErrorDialog = True
    #-----------------------------------------------
    Prc = Process()
    Prc.StartInfo = PSI
    Prc.Start()
    print(Prc.ToString())
    # Prc.WaitForExit()
    # res = Prc.StandardOutput.ReadToEnd()
    print("Перехватываемые сообщения")
    # print(res)
except Exception as Mess:
    print(f'MainErr: {str(Mess)}')
#----------------------------------------------------------------------------
# startInfo.FileName = "cmd.exe";
# startInfo.Arguments = "/C md " + target.FullName;

