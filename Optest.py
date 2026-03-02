import traceback
from typing import Any
from rich import print as rpn

class fusr():
    """Тип данных user - domen."""
    __slots__ = ['omc','usn','dm1','dm0','srv','grt','uou','cmp','lev','iph','uph']
    def __init__(self)-> None:
        self.omc:str = '' # OMCID dev23001
        self.usn:str = '' # User name dev2300101
        self.dm1:str = '1more'
        self.dm0:str = 'cloud'
        self.srv:str = ''# bali
        self.grt:str = ''# standard-tarif
        self.uou:str = ''# OU=omc53467-ou,OU=Clients_CL-33,DC=1more,DC=cloud'
        self.cmp:str = ''# -Company
        self.lev:int = 1
        self.iph:str = ''# \\moscow
        self.uph:str = ''# \\moscow

## --------------------------------------------------------------------------------------------------------------------
    def __setattr__(self, key:str, value:Any)->None:
        # if isinstance(fusr.__dict__[key], str):
        if key in ('omc','usn','dm1','dm0','srv','uou','grt'):
            fusr.__dict__[key].__set__(self, value.lower().strip())
        else:
            fusr.__dict__[key].__set__(self, value)
## --------------------------------------------------------------------------------------------------------------------
    def __str__(self)->str:
        return f'omc = {self.omc} usn = {self.usn} {self.dm1}.{self.dm0} srv = {self.srv} grt = {self.grt} OU = {self.uou} \n\
{self.cmp} lev={self.lev} iph ={self.iph} uph = {self.uph}'
##----------------------------------------------------------------------------------------------------------------------------
    def __repr__(self)->str:
        return f'omc={self.omc} usn={self.usn} domain={self.dm1}.{self.dm0} srv={self.srv} grt={self.grt} uou={self.uou} \n\
cmp={self.cmp}  lev={self.lev}  iph={self.iph}  uph={self.uph}'
###############################################################################################################################
def testa(Gu_Af,dbg:bool = False):
    while True:
        try:
            ##------------------------------------------------------------------
            userlist = {'dev2600101': False, 'dev2600103': True, 'dev2600104': False, 'dev2600105': True, 'dev2600106': True}
            rpn('\t[green1]Выберите пользователей для подключения базы')
            for _iu,_ii in userlist.items():
                if _ii:
                    rpn(f'\t\t[green1]{int(_iu[-2:]):3} [cyan1]{_iu}')
                else:
                    rpn(f'\t\t[green1]{' '*3} [cyan]{_iu}')
            ##-------------------------------------------------------------------------------------------------------------
            rpn('\n\t[cyan1]Введите номера через пробел.')
            rpn('\t[green1]A(a)[cyan1]  - добавить всем пользователям.')
            rpn('\t[green1]  0[green] Enter[cyan1] - завершить/выход.')
            usrlst = []
            while True:
                if (inkey := input('\t:-)>').strip()) in ('0'):
                    # raise OmcError('Выход при вводе пользователя')
                    rpn('Выход при вводе пользователя')
                    break
                    # break
                Lst = inkey.split()
                rpn(f'{Lst = }')
                LsIB = ['0' * (2 - len(_x)) + _x for _x in Lst]
                rpn(f'{LsIB = }')
                if any(chk in LsIB for chk in ('0A','0a','0А','0а')):#Метим экспорт все значения
                    usrlst = [_a for _a,_b in userlist.items() if _b]
                    rpn(f'{usrlst = }')
                    break
                # for chk in ('A','a','А','а'):
                    # rpn(f'{chk = }')
                    # if chk in LsIB:
                        # rpn()
                    
                # сия конструкция проверяет что номер соответсвует USERID из списка и значение TRUE
                if dbg:rpn('Не сработала по А')
                if all((_d := f'{Gu_Af.omc}{_c.strip()}') in userlist and userlist[_d] for _c in LsIB):
                    usrlst = [f'{Gu_Af.omc}{_e.strip()}' for _e in LsIB if userlist.get(f'{Gu_Af.omc}{_e.strip()}',False)]
                    # all(ix.isdecimal() for ix in LsIB):
                    break
                rpn('\t[bright_yellow] Неверное значение. Только цифры или "А"("a").Повторите ввод.')
            ##----------------------------------------------------------
        except Exception as Mess:
            rpn(f'[yellow]{traceback.format_exc()}')
            rpn(f'[orchid]{Mess}')
        ##-------------------------------------------------------------------------------------------------------------
        if input('Повтор? :-)> '):break
###################################################################################################################################
if __name__ == '__main__':
##-----------------------------------------------------------------------
    Test = fusr()
    Test.omc = 'dev26003'
    Test.usn = 'dev2600303'
    Test.dm1 = '1more'
    Test.dm0 = 'cloud'
    Test.srv = 'tandadev'
    Test.grt = 'Clients-test' # standard-tarif
    Test.uou = 'OU=dev26001-OU,OU=Clients-dev,DC=1more,DC=cloud'
    Test.uph = r'\\moscow\FILES'
    Test.iph = r'\\moscow\ibases'
    testa(Test,True)
    input('Exit? :-)> ')
