import os,traceback,ctypes#,,sys

from rich import print as rpn

rpn(f'UserName = {os.environ['USERNAME'].lower()}')
rpn(f'Domain   = {os.environ['USERDNSDOMAIN'].lower()}')
rpn(f'С правми админа = {ctypes.windll.shell32.IsUserAnAdmin()}')
#----------------------------------------------------------------------------------------
ServerName = 'sh-vds-fran01.shumeiko.local'
omcid = 'dev25005'
usrid = 'dev2500501'
usrdsc = 'E:'
ibaspath = r'\\sh-vds-fran01.shumeiko.local\ibases'
usrprof  = fr'{usrdsc}\{usrid}'
rpn(f'usrprof = {usrprof}')
netprofile = fr"\\{ServerName}\{usrprof.replace(':','$')}"
rpn(f'netprofile = {netprofile}')
usrcfgpath = os.path.join(netprofile,r'AppData\Roaming\1C\1CEStart')
rpn(f'usrcfgpath = {usrcfgpath}')
try:
    if not os.path.isdir(usrcfgpath):os.makedirs(usrcfgpath,exist_ok=True)
    usrcfgfile = os.path.join(usrcfgpath,'1cestart.cfg')
    rpn(f'usrcfgfile = {usrcfgfile}')
    ta = os.path.join(ibaspath,omcid)
    netcfgfile = os.path.join(ta,f'1cestart_{usrid}.cfg')
    rpn(f'netcfgfile = {netcfgfile}')
    # a = os.symlink(r"\\moscow\ibases\dev25001\1cestart_dev2500102.cfg",
        # r"\\tandadev\E$\dev2500102\AppData\Roaming\1C\1CEStart\1cestart.cfg")
    a = os.symlink(netcfgfile,usrcfgfile)
    rpn(a)
except FileExistsError as FEEMess:
    rpn('Ссылочка то уже есть')
    rpn(f'{FEEMess}')
except Exception as ErrMs:
    rpn(f'{ErrMs}')
    rpn(f'{traceback.format_exc()}')
input(' :-)> ')
os._exit(0)
