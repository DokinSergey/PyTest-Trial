from rich import print as rpn

Userlist=(
r'1more\dev2400501',
r'1more.cloud\dev24005101',
'omc2415852@1more.cloud',
'omc2415853',
r'1more\om24159123',
r'1more.cloud\de25126583',
'mc24158155@1more.cloud',
'mc24158157',
)


rpn('   USERID   :  OMCID  : Nusr :       :')
rpn('------------:---------:------:-------:')
for ist in Userlist:
    istr = istr.rsplit('\\').rsplit('@')[-1]#[2:3].isdecimal():lenomc = 7
    if istr[2:3].isdecimal():
        rpn(f'[cyan1]{istr:^12}:{istr[:7]:^9}:{istr[7:]:^6}:2-5-3  :')
    else:
        rpn(f'[yellow]{istr:^12}:{istr[:8]:^9}:{istr[8:]:^6}:3-5-3/2:')