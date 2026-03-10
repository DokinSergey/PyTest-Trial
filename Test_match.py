import os
from rich import print as rpn

b = ('первый','второй','третий','четвертый','пятый',)
c = r'C:\Exe\Customer_csv\Batch.csv'

while True:
    d = ''
    a = input('ввод паттерна :-)> ').strip()
    match a:
        case '0':
            rpn('Выход !')
            break
        case '':
            rpn('Повтор')
            d = c
        case 'M'|'m'|'М'|'м':
            d = input('ввод file name :-)> ').strip()
        case _:
            if a.isnumeric() and (0 < int(a)-1 <= len(b)):
                rpn(b[int(a)-1])
            else:
                rpn('Черте чё')
            continue
    if os.path.isfile(d):
        rpn(d)
        break

input('Выход :-> ')
