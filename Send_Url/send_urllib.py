import os
import json
import urllib.request
import urllib.parse
import urllib.error
from rich import print as rpn
from time import perf_counter#,sleep
## ---------------------------------------------------------------------------------------------------------------------
TOKEN = "6633397926:AAFIYCuBEXG09_n1kTyV-PxE7SiLi_1YU2s"
group_id = "-1002152529179"
CHAT_ID  = "839545749"
## ---------------------------------------------------------------------------------------------------------------------
def send_telegram_message(token:str, chat_id:str, message:str)->bool:
    # Формируем URL для запроса к Telegram API
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    # Подготавливаем данные для отправки
    data = {
        'chat_id': chat_id,
        'text': message
    }

    # Кодируем данные в формат, подходящий для POST‑запроса
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')

    # Создаём запрос
    request = urllib.request.Request(url, data=encoded_data)

    try:
        # Отправляем запрос и получаем ответ
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode('utf-8'))

        # Проверяем успешность отправки
        if result.get('ok'):
            print("Сообщение успешно отправлено!")
            return True
        else:
            print(f"Ошибка: {result.get('description')}")
            return False
    ## -----------------------------------------------------------------------------------------------------------------
    except urllib.error.HTTPError as e:
        print(f"HTTP ошибка при отправке в Pushbullet: {e.code} - {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"URL ошибка: {e.reason}")
        return False
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return False
###########################################################################################################
if __name__ == '__main__':
    title = f'Messeges_{os.getpid()}'
    MESSAGE  = ' Мой дядя самых честных правил,\n когда не в шутку занемог\n он уважать себя заставил\n и лучше выдумать не мог\n'
    t0 = perf_counter()
    # send_pushbullet(title, body)
    t1 = perf_counter()
    send_telegram_message(TOKEN, CHAT_ID, MESSAGE)
    t2 = perf_counter()
    rpn(f'{t1 - t0:.5f}  {t2 - t1:.5f}')
    input(' :-)> ')
