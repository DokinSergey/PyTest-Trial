import os
import atexit
import time
from rich import print as rpn
from datetime import datetime,timezone,timedelta#,date

exit_file = os.path.join(os.path.dirname(__file__),'some_state.txt')
print(f'{exit_file}')

def on_stop(*args):
    dtnow = datetime.now(timezone.utc) + timedelta(hours=3)
    dtstr = dtnow.strftime("%H:%M:%S")
    with open(exit_file, 'a', encoding='utf_8') as fa:
        print(dtstr, *args,file = fa)
    # os._exit(0)

atexit.register(on_stop,'Убили прогу', 'окно закрыли')

i = 0
while True:
    i += 1
    # if   not i % Step:rpn(f'{int(i*Delay):0>3d}',end = '')
    if not i % 2:rpn('[green1]+',end = '')
    else:rpn('[green1]-',end = '')
    time.sleep(0.5)
# on_stop(25,15)




# try:
    # while True:
        # try:
            # if (ex := input(' :-)> ')) in ('.',','):
                # break
        # except GeneratorExit as Ge:
            # print(f'GeneratorExit = {Ge}')
        # except KeyboardInterrupt as Ki:
            # print(f'KeyboardInterrupt = {Ki}')
        # except SystemExit as Se:
            # print(f'SystemExit = {Se}')
        # except Exception as Ex:
            # print(f'Exception = {Ex}')
# except BaseException as ErrBase:
    # print(f'Поймали = {ErrBase}')
input('Exit:-)>')
