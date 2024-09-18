from rich import print as rpn

Userlist=(
'dev2400501',
'dev24005011',
'omc2415852',
'om24159123',
'de25126583',
)
rpn('   USERID   :  OMCID  : Nusr :       :')
rpn('------------:---------:------:-------:')
for istr in Userlist:
    if istr[2:3].isdecimal():
        rpn(f'[cyan1]{istr:^12}:{istr[:7]:^9}:{istr[7:]:^6}:2-5-3  :')
    else:
        rpn(f'[yellow]{istr:^12}:{istr[:8]:^9}:{istr[8:]:^6}:3-5-3/2:')