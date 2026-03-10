# import os
from rich import print as rpn
################################################################################
def fact(a:int)->int:
    rs = 1
    for i in range(1,a + 1):rs *= i
    return rs
###############################################################################
if __name__ == '__main__':
    res = fact(100)
    rpn(f'[light_green]{res = }')

    input(':-)>')
