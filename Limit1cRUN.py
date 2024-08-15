import psutil
import sys
import ctypes
import os
import time

# Если хотим засечь время выполнения скрипта, убираем комент 
#start_time = time.time()

# Наша процедура с открытием 1С-ки
def OpenCount1C(Num):

    List1cv8c = [] # Список сколько 1С программ запущено у пользователя
    List1cestart = [] # Список сколько 1С стартеров запущено у пользователя
    for p in psutil.process_iter(attrs=['username', 'name']):
        if p.info['name'] == "1cv8c.exe" and p.info['username'] is not None:
            List1cv8c.append(p.info['name'])
        elif p.info['name'] == "1cv8s.exe" and p.info['username'] is not None:
            List1cestart.append(p.info['name'])
    CountList1cv8c = List1cv8c.count("1cv8c.exe")  # Считаем количество совпадений в списке
    CountList1cestart = List1cestart.count("1cv8s.exe") # Считаем количество совпадений в списке

    if CountList1cestart < 1: # Нельзя запускать сразу миллион стартеров
        if CountList1cv8c < Num: 
            os.startfile(r'C:\Program Files (x86)\1cv8\common\1cestart.exe')
        else:
            message = "Администратором запрещено запускать более " + str(Num) + " процессов 1С"
            ctypes.windll.user32.MessageBoxW(0, message , "Уведомление о блокировке", 1)
            sys.exit(0) # Stop
    else:
        sys.exit(0) # Stop

#Настраиваем ограничения по пользователям
USERNAME = os.environ.get( "USERNAME" )
if USERNAME == 'Собственник': #для Собственника вообще не будет отрабатывать ограничение
    os.startfile(r'C:\Program Files (x86)\1cv8\common\1cestart.exe')
elif USERNAME == 'Бухгалтер1': #для Бухгалтер1 это будет 8 баз
    OpenCount1C(8)
elif USERNAME == 'Бухгалтер2': #для Бухгалтер2 это будет 12 баз
    OpenCount1C(12) 
else:
    OpenCount1C(4) # для всех остальных 4 базы

# Если хотим вывести время выполнения скрипта, убираем комент 
#print("--- %s seconds ---" % (time.time() - start_time))