import os
c = r'\\moscow\FILES\dev25001'
a = r'\\moscow\files\dev25001'
a = os.path.normcase(a)
print(f'a = {a}')
# a = os.path.join(a,'regsd')
# print(f'a = {a}')
while True:
    b = os.path.dirname(a)
    print(f'\tb = {b}')
    if b != a:
        a = b
        print(f'\ta = {a}')
    else:
        break
print(f'Ура нашли {b}')
input(' :-)> ')
os._exit(0)
