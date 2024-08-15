import os
import traceback
from glob import glob
from rich import print as rpn
CustPathV8i = os.path.dirname(__file__)
rpn(CustPathV8i)
tmplcfg = '*.py'#,root_dir=CustPathV8i, recursive=True{CustPathV8i}\
if listcfg := glob(tmplcfg,root_dir=CustPathV8i, recursive=True):
    for ni,icfg in enumerate(listcfg):
        rpn(f'{ni:3}: [green1] {icfg}')
        rpn(f'{ni:3}: [yellow] {os.path.join(CustPathV8i,icfg)}')