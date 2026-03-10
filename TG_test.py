import os,sys
import traceback
import requests
from rich import print as rpn

TOKEN = "6633397926:AAFIYCuBEXG09_n1kTyV-PxE7SiLi_1YU2s"
# group_id = "-1002152529179"
chat_id  = "839545749"
# debug = False
#pylint: disable-msg=R1719
if (debug := True if len(sys.argv) > 1 and str(sys.argv[1]) in ('True','cons') else False):
    rpn(f'debug is [orange_red1]{debug}')
#pylint: enable-msg=R1719
##################################################################################################################
def TgBotMess(_TgStr:str)->bool:
    res = True
    try:
        if debug:#При отладке отправляем только себе, при ошибке - в группу
            _chat_id = chat_id
            rpn('[cyan3]Сообщение в ТГ отправлено в чат-бот')
        else:
            _chat_id = group_id
            rpn('[cyan3]Сообщение в ТГ отправлено в общий чат')
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={_chat_id}&text={_TgStr}"
        requests.get(url, timeout=15).json()
    except Exception as _ErrMs:
        res = False
        rpn(f'[orange_red1]{_ErrMs}')
        rpn(f'[orange_red1]{traceback.format_exc()}')
    return res
##################################################################################################################
def tg_group_test(_TgStr:str,)->bool:
    res = True
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={group_id}&text={_TgStr}"
        _ar = requests.get(url, timeout=15).json()
        # rpn(_ar)
    except Exception as _ErrMs:
        res = False
        rpn(f'[orange_red1]{_ErrMs}')
        rpn(f'[orange_red1]{traceback.format_exc()}')
    return res


##################################################################################################################
if __name__ == '__main__':
    debug = True
    ancl = " Мой дядя самых честных правил,\n когда не в шутку занемог\n он уважать себя заставил\n и лучше выдумать не мог\n"
    TgBotMess(ancl)
    # tg_group_test(ancl)
    input(':-)>')
    os._exit(0)
