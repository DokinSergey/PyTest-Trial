import os
from rich import print as rpn
dup = {
    'ias2018101':r'\\sh-vds-02.shumeiko.local\E$',
    'ias2018102':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018103':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018104':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018105':r'\\sh-vds-02.shumeiko.local\E$',
    'ias2018106':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018107':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018108':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018109':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018111':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018112':r'\\sh-vds-02.shumeiko.local\E$',
    'ias2018113':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018115':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018116':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018117':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018118':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018121':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018124':r'\\sh-vds-02.shumeiko.local\E$',
    'ias2018126':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018129':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018130':r'\\sh-vds-02.shumeiko.local\E$',
    'ias2018132':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018133':r'\\sh-vds-02.shumeiko.local\E$',
    'ias2018134':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018135':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018137':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018138':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018140':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018142':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018143':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018144':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018145':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018150':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018151':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018152':r'\\sh-vds-02.shumeiko.local\E$',
    'ias2018153':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018154':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018155':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018156':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018157':r'\\sh-vds-01.shumeiko.local\E$',
    'ias2018158':r'\\sh-vds-02.shumeiko.local\E$',
}
############################################################################################
if __name__ == '__main__':
    for ta,tb in dup.items():
        abpath = os.path.join(os.path.join(tb,ta),r'AppData\Roaming\1C\1CEStart')
        try:
            tc = os.path.isdir(abpath)
            rpn(ta,tc)
        except Exception as Mess:
            rpn(f'[red]{Mess}')
    input(':-)>')
