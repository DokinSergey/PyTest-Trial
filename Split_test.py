import os
a = r'\\moscow\pupas\dev25001\trubas'
server = [b for b in a.split('\\') if b][0]
# for curs in a.split('\\'):
    # print(f'{curs = }')
    # if curs:
        # server = curs
        # break


print(f'Ура нашли {server}')
input(' :-)> ')
