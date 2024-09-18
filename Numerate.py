import os

from rich import print as prn
N = 52
base = {i+1:None for i in range(N)}
ik = 1
for k in range(1,27):
    if ik > N:ik = 3
    while base[ik]:
        ik += 2
        if ik > N:
            prn(f'всё не влезло 1 {k = }')
            break
    if ik > N:
        prn(f'всё не влезло 2 {k = }')
        break
    base[ik] = k
    prn(f'{ik =} {base[ik]=}')
    ik += 8
else:prn('всё влезло')
prn(base)
input(':-> ')
os._exit(0)
