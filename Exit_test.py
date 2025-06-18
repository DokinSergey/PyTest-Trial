import os
import atexit
import signal
from datetime import datetime,timezone,timedelta#,date

exit_file = os.path.join(os.path.dirname(__file__),'some_state.txt')
print(f'{exit_file}')

def on_stop(*args):
    dtnow = datetime.now(timezone.utc) + timedelta(hours=3)
    dtstr = dtnow.strftime("%H:%M:%S")
    with open(exit_file, 'a', encoding='utf_8') as fa:
        print(dtstr, *args,file = fa)
    # print(dtstr, *args)
    # input('Exit:-)>')
    os._exit(0)

for sig in (signal.SIGBREAK, signal.SIGINT, signal.SIGTERM):
    signal.signal(sig, on_stop)

while True:
    print('tick')
    # input(' :-)> ')
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
