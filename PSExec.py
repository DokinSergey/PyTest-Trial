#########################################################################################################################################
def PSExec(psstr:str)->FRes:
    res = FRes()
    LogErrDebug(f'{psstr = }','PSExec')
    try:
        with Popen(['powershell', psstr], stdout = PIPE, stderr = PIPE) as popps:
            pls = popps.communicate(timeout=15)
        if bool(pls[1]):
            LogErrDebug(pls[1].decode('cp866'),'PSExec')
            raise PowerShell (pls[1].decode('cp866'))
    except PowerShell as Mess:
        res.err = 1
        res.Mess1 = str(Mess)
        LogErrDebug(f'{Mess}','PSExec')
    except TimeoutExpired as Mess:
        res.err = 1
        res.Mess1 = str(Mess)
        LogErrDebug(f'{Mess}','PSExec')
    except Exception as Mess:
        res.err = 1
        LogErrDebug(f'Ошибка ; {Mess} ; {traceback.format_exc()}','PSExec')
        res.Mess1 = str(Mess)
        res.Mess2 = traceback.format_exc().splitlines()[1]
        res.Mess3 = traceback.format_exc().splitlines()[2:]
    else:
        res.res = 1
        res.Mess1 = pls[0].decode('cp866')
        res.Mess2 = ''
        res.Mess3 = ''
        LogErrDebug('Скрипт PS выполне умпешно','PSExec',1)
    return res
#########################################################################################################################################
   try:#--------------------------------------------------------------------------------------------
        psstr  = 'Import-Module ActiveDirectory\n'
        psstr += f"$npass = ConvertTo-SecureString -AsPlainText '{uspass}' -Force\n"
        psstr += f"Set-ADAccountPassword {aus.usn} -Reset -NewPassword $npass –PassThru\n"
        rps = PSExec(psstr)
        if rps.res:
            adu.err = 0
            adu.res = 1
            adu.Mess1 = acc = 'Выполнено успешно'
        else:
            adu.err = 1
            adu.res = 0
            adu.Mess3 = rps.Mess1
            acc = 'Ошибка выполнения скрипта PS'
    except OmcExcept as Mess:
        acc = 'OmcExcept'
        adu.err = 1
        adu.res = 0
        adu.Mess3 = str(Mess)
    LogErrDebug(f'{acc} ; {adu.Mess1} ; {a