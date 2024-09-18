from datetime import datetime
from psutil import users,process_iter,Process
# print(users())
for usr in users():
    if usr.host:
        print(f'{str(usr.name):12} {str(usr.host):15}  {datetime.fromtimestamp(usr.started):%Y-%m-%d %H:%M}')

for proc in process_iter(['name', 'cmdline', 'username','create_time']):
    if proc.info['name'] not in ('1cv8c.exe','1cv8s.exe','1cv8.exe'):continue
#, 'username', "exe"'pid',
    # print(proc.info)
    print(f'{str(proc.info['username']):19}: {datetime.fromtimestamp(proc.info['create_time']):%Y-%m-%d %H:%M} : {proc.info['cmdline'][2:3]}')
    # print(Process())
print()
# Process.pid               #PID процесса,
# Process.ppid() 		    #родительский PID процесса,
# Process.name() 		    #имя процесса,
# Process.exe() 		    #абсолютный путь процесса,
# Process.cmdline() 		#командная строка процесса,
# Process.environ()     	переменные окружения процесса,
# Process.create_time() 	#время создания процесса,
# Process.as_dict() 		#извлекает информацию о нескольких процессах,
# Process.parent() 		    #родительский процесс,
# Process.parents() 		#родители этого процесса,
# Process.status() 		    #текущее состояние процесса,
# Process.cwd() 		    #рабочий каталог процесса,
# Process.username() 		#имя пользователя, которому принадлежит процесс,
# Process.uids() 		    #идентификатор пользователя этого процесса,
# Process.gids() 		    #идентификатор группы этого процесса,
# Process.terminal() 		#терминал, связанный с этим процессом,
# Process.nice() 		    #получает или устанавливает приоритет процесса,
# Process.ionice() 		    #получает или устанавливает приоритет ввода-вывода процесса,
# Process.rlimit() 		    #получает или устанавливает лимиты ресурсов процесса,
# Process.io_counters() 	#статистика ввода-вывода процесса,
# Process.num_ctx_switches()#количество переключений контекста,
# Process.num_fds() 		#количество открытых файловых дескрипторов,
# Process.num_handles() 	#количество используемых файловых дескрипторов,
# Process.num_threads() 	#количество используемых потоков,
# Process.threads() 		#потоки, открытые процессом,
# Process.cpu_times() 		#суммарное время обработки в секундах,
# Process.cpu_percent() 	#использование ЦП процессом в процентах,
# Process.cpu_affinity() 	#получает или устанавливает привязку процессора к процессу,
# Process.cpu_num() 		#на каком ЦП в данный момент работает этот процесс,
# Process.memory_info() 	#информацию о памяти, которую занимает/использует процесс,
# Process.memory_full_info()#предоставляет дополнительные показатели (USS, PSS и swap),
# Process.memory_percent() 	#сравнивает память процесса с общей физической памятью,
# Process.memory_maps() 	#возвращает сопоставленные области памяти процесса,
# Process.children() 		#дочерние элементы этого процесса,
# Process.open_files() 		#файлы, открытые процессом,
# Process.connections() 	#соединения сокетов,
# Process.is_running() 		#проверяет, выполняется ли текущий процесс,
# Process.send_signal() 	#отправляет сигнал процессу,
# Process.suspend() 		#приостанавливает выполнение процесса,
# Process.resume() 		    #возобновляет выполнения процесса,
# Process.terminate() 		#завершает процесс,
# Process.kill() 		    #уничтожает текущий процесс,
