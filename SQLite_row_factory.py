import os
import traceback
# import chardet
import sqlite3
# from sqlite3 import connect,Row,OperationalError,
from rich import print as rpn


def read_sql_row_factory(_FileSQL:str,_TabName:str)->None:
    sql_txt = ''
    try:
        if not os.path.isfile(_FileSQL):
            rpn(f'\tФайл {_FileSQL} не найден или недоступен')
            return
        ## -------------------------------------------------------------------------------------------------------------
        with sqlite3.connect(_FileSQL) as SQLite:
            sql_txt = f"SELECT * FROM {_TabName} ORDER BY Id"
            SQLite.row_factory = sqlite3.Row
            cursor = SQLite.cursor()
            cursor.execute(sql_txt)
            row_str = cursor.fetchall()
        for irs in row_str:
            rpn(dict(irs))


    except sqlite3.OperationalError as Oarm:
        rpn(f'[orange1]{Oarm}')
    except sqlite3.Warning as Warn:
        rpn(f'[orange1]{Warn}')
    except sqlite3.Error as DErr:
        rpn(f'[bright_red]{DErr}')
        rpn(f'[bright_red]{sql_txt}')
    except Exception as err:
        rpn(f'[bright_red]{err}')
        rpn(f'[bright_red]{traceback.format_exc()}')
########################################################################################################################
if __name__ == '__main__':
    FileSQL = r'C:\Exe\Customer_csv\csv_tascs.db3'
    TabName = 'DevTest'
    read_sql_row_factory(FileSQL,TabName)
    input(' :-)> ')
