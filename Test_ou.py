from rich import print as rpn

def test_ou(uo_in:str,nou:str = '')->None:
    name_ou = nou.lower() if nou else uo_in.strip().split(',',1)[0].split('=')[-1].lower()
    if (path_ou := uo_in.strip().split(',',1)[-1].lower()) == name_ou:path_ou = ''
    rpn(f'{name_ou:10}  {path_ou:50}  {uo_in}')
########################################################################################################################
if __name__ == '__main__':
    ou_list = [
        'OU=dev26105-ou,OU=Clients-DEV,DC=1more,DC=cloud',
        'dev26105-ou',
        'OU=Clients-DEV,DC=1more,DC=cloud',
        '',
    ]
    for ii in ou_list:
        test_ou(ii,'dev26105-fur-ou')
    input('Exit :-)> ')
