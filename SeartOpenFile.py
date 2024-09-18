import psutil
from rich import print as rpn
def lsof(path=None):
    users = []
    rpn('[green1][',end='')
    for p in psutil.process_iter():
        files = []
        rpn('[cyan1]#',end='',flush=True)
        try:
            # rpn(p.open_files())
            files = p.open_files()
        except:
            # rpn(p)
            pass
        # print(files)
        if path:
            users.extend([(f.path,p.name(),p.pid,p.username()) for f in files if f.path in path])
        else:
            users.extend([(f.path,p.name(),p.pid,p.username()) for f in files])
            # for f in files
                # f.path,p.name()
    rpn('[green1]]')
    return users
print(lsof(r'C:\Users\dokin\Documents'))
