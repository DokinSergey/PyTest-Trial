import base64

# PSI.Domain = "1more.cloud"
# PSI.UserName = base64.b64decode(b'c2NyaXB0NHNlcnZpY2U=').decode('utf-8')
# PSI.PasswordInClearText = base64.b64decode(b'TWhObkB3UURJWW1a').decode("utf-8")

string = "GreeksforGreeks"
s4suser = r'shumeiko.local\script4service'
# s4suser = r'1more.cloud\script4service'
s4spass = 'Vx964&iugo7w'

# Encoding the string
e4suser = base64.b64encode(s4suser.encode("utf-8"))

e4spass = base64.b64encode(s4spass.encode("utf-8"))
print(f'Пользователь: = {e4suser}!')
print(f'Пароль: !{e4spass = }!')

# Decoding the string
print('\nПроверка ')
Udecode = base64.b64decode(e4suser).decode("utf-8")
Pdecode = base64.b64decode(e4spass).decode("utf-8")

print(f'Пользователь: !{Udecode = }!')
print(f'Пароль: !{Pdecode = }!')
input(' :-)> ')
