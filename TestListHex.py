import os

_VERDATE = '2024-09-23 22:48'
a = {'a12301':'True','a12302':'True','a12303':'True','a12304':'True','a12305':'True','a12306':'True','05':'True',}#'a123aa':'True','a123ff':'True',]
b = tuple(a.keys())
print(type(b))
for ni,ii,iv in enumerate(a.items()):
    print(ni,ii,iv)
    # print(f'{ii} {ii[-2:]} {int(ii[-2:],16)} {ii[-2:].isdigit() = }')
print(all(jj[-2:].isdigit() for jj in a))