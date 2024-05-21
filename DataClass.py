from dataclasses import dataclass

@dataclass
class FRes():
    """Тип данных возврат результата функции"""
    __slots__ = ['err','res','Mess1','Mess2','Mess3']
    def __init__(self):
        self.err: int = 0
        self.res: int = 0
        self.Mess1: str = ''
        self.Mess2: str = ''
        self.Mess3: str = ''


dr = FRes()
dr.err = 1
print(dr.err)
# dr.drt = 10
# print(dr.drt)
