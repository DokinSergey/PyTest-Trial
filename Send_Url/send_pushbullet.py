import os
import json
import urllib.request
import urllib.error
import niquests
from rich import print as rpn
from time import perf_counter#,sleep
# from urllib import request

access_token = 'o.4wQfYVsk61ILJud1qUIDnKMeLR1kq6UK'

def send_pushbullet(_title:str, _body:str)->None:
    url = "https://api.pushbullet.com/v2/pushes"
    headers = {"Access-Token": access_token}
    data = {
        "type": "note",
        "title": _title,
        "body": _body
    }
    res =  niquests.post(url, json=data, headers=headers)
    rpn(res)

def send_pushbullet_note(_title:str, _body:str)->bool:
    """
    Отправляет уведомление типа 'note' через Pushbullet.
    Возвращает True в случае успеха, иначе False.
    """
    url = "https://api.pushbullet.com/v2/pushes"
    headers = {
        "Access-Token": access_token,
        "Content-Type": "application/json"
    }
    data = {
        "type": "note",
        "title": _title,
        "body": _body
    }
    json_data = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(url, data=json_data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            # Успешно: код 200 (или 201 Created).getheaders().read()
            rpn(f'{response.read().decode('utf-8')}')
            return True
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
    body  = ' Мой дядя самых честных правил,\n когда не в шутку занемог\n он уважать себя заставил\n и лучше выдумать не мог\n'
    t0 = perf_counter()
    # send_pushbullet(title, body)
    t1 = perf_counter()
    send_pushbullet_note(title, body)
    t2 = perf_counter()
    rpn(f'{t1 - t0:.5f}  {t2 - t1:.5f}')
    input(' :-)> ')
