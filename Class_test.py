from rich import print as rpn

class fusr():
    """Тип данных user - domen."""
    __slots__ = ['omc','usn','dm1','dm0','srv','grt','uou','cmp','lev','iph','uph','pss','srk']
    def __init__(self)-> None:
        self.omc:str = 'dev35035' # OMCID dev23001
        self.usn:str = 'dev3503535' # User name dev2300101
        self.dm1:str = '1more'
        self.dm0:str = 'cloud'
        self.srv:str = 'baramba.1more'# bali
        self.grt:str = 'baramba_group'# standard-tarif
        self.uou:str = 'dev35035-ou'# OU=omc53467-ou,OU=Clients_CL-33,DC=1more,DC=cloud'
        self.cmp:str = 'Barambas company'# -Company
        self.lev:int = 1
        self.iph:str = r'\\moscow\ibases'# \\moscow
        self.uph:str = r'\\moscow\FILES'# \\moscow
        self.pss:str = ''# список баз пользователя
        self.srk:str = r'\\more\COPY\_log'
    def __str__(self)->str:
        return f'omc = {self.omc} usn = {self.usn} {self.dm1}.{self.dm0} srv = {self.srv} grt = {self.grt} OU = {self.uou} \n\
{self.cmp} lev={self.lev} iph ={self.iph} uph = {self.uph} srk = {self.srk}'
        
    def __repr__(self)->str:
        return f'omc={self.omc} usn={self.usn} domain={self.dm1}.{self.dm0} srv={self.srv} grt={self.grt} uou={self.uou} \n\
cmp={self.cmp} lev={self.lev} iph = {self.iph} uph = {self.uph} srk = {self.srk}'
#----------------------------------------------------
rpn(f'{fusr()}')
rpn(f'{fusr() = }')
input(' :-)> ')
