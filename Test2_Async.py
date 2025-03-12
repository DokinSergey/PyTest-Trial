import sys,time
import asyncio
files = ['image.png', 'file.csv', 'file1.txt', 'file3.csv', 'file4.csv', 'file5.csv']
missed_files = ['file3.csv', 'file4.csv', 'file5.csv']
# Не менять функцию
async def download_file(file_name):
    await asyncio.sleep(1)
    if file_name in missed_files:
        raise FileNotFoundError(f'Файл {file_name} не найден')
    # else:
    await asyncio.sleep(1)
    return f'Файл {file_name} успешно скачан'

# ваш код пишите тут:
async def main():
    tasks = [asyncio.create_task(download_file(file_name)) for file_name in files]
    try:
        await asyncio.gather(*tasks)
    except FileNotFoundError as FnFE:
        print(FnFE)
    for task in tasks:
        pass
        # Получаем исключение из задачи, если оно возникло, и выводим информацию о нем
        mexcept = task.exception()
        # if exc:print(exc)



start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
