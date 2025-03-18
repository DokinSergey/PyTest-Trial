"""
Run the python script as adminstrator, which means anything evoked
from this script will have admin privilege

https://stackoverflow.com/questions/130763/request-uac-elevation-from-within-a-python-script/
"""


import ctypes
import sys
import subprocess


def main():
    """
    Test function to run as admin
    """
    p = subprocess.Popen(
        "start /wait cmd /k",
        shell=1,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    p.communicate()
    return


def is_admin():
    """
    Determine whether the current script has admin privilege

    @return: bool. whether the script is in admin mode
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def rerun_as_admin():
    """
    Re-run the current python script as admin using the python interpreter
    from `sys.excutable`
    
    Note: it is difficult to get output at the original console.
    """
    ctypes.windll.shell32.ShellExecuteW(
        None,
        u"runas",
        unicode(sys.executable),
        unicode(__file__),
        None,
        1
    )


if  __name__ == "__main__":
    if is_admin():
        main()
    else:
        rerun_as_admin()