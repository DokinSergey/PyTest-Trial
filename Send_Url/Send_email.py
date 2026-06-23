import os
import base64
import smtplib
from platform import python_version
from email.message import EmailMessage

msg = EmailMessage()
msg["From"] = "pushkin@1more.cloud"
# msg["To"]   = "gt@1more.cloud" #"es@1more.cloud"
msg["To"]   = "sd@1more.cloud"
# msg["Bcc"]  = "av@1more.cloud"
# msg["Cc"]   = "sd@1more.cloud"
msg["Subject"] = f"Sent from Python {python_version()} {os.getpid()}"
# msg.set_content(' ')
msgtxt = '''«Мой дядя самых честных правил,
Когда не в шутку занемог,
Он уважать себя заставил
И лучше выдумать не мог.
Его пример другим наука;
Но, боже мой, какая скука
С больным сидеть и день и ночь,
Не отходя ни шагу прочь!
Какое низкое коварство
Полуживого забавлять,
Ему подушки поправлять,
Печально подносить лекарство,
Вздыхать и думать про себя:
Когда же черт возьмет тебя!»
'''
msg.set_content(msgtxt)
print(msg.as_string())

# input(' :-)> ')
# Данные отправителя
smtp_server = "mail.nic.ru"
port = 587
sender = "script4service@1more.cloud"
# password = base64.b64decode(b'eVZvMzhkeXE=').decode("utf-8")
password = base64.b64decode(b'QXdvMTV6ZXY=').decode("utf-8")
# recipient = "sd@1more.cloud" b'QXdvMTV6ZXY='


# Отправляем
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, password)
    server.send_message(msg)

input(' :-)> ')
