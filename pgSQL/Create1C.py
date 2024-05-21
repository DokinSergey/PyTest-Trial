import psycopg as pg
import time

with pg.connect(dbname="Test",
        host = 'DokinPC',
        user="dokin",
        password="619838",
        port="5432"
        ) as conn:

    with conn.cursor() as cursor:
        sql_txt  = 'INSERT INTO customers.ctasks (command, omcid,context,status)'
        sql_txt += 'VALUES (%s,%s,%s,%s) RETURNING TaskID;'
        datasql = ("Create_v8i","dev24002","vasypupkin@mmail.ru", "open")
        cursor.execute(sql_txt, datasql)
        SessID = cursor.fetchone()[0]

        sql_txt  = 'INSERT INTO customers.Base1C (TaskID, TypeIB,BaseStr,FoldStr)'
        sql_txt += 'VALUES (%s,%s,%s,%s) RETURNING TaskID;'
        datasql = (SessID,"acc","Мазуриков ИП", "Предприниматели")
        cursor.execute(sql_txt, datasql)

    print('\t[', end = '', flush=True)
    for ici in range(121):
        if not ici % 5:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT status FROM customers.ctasks WHERE TaskID = {SessID}")
                res = cursor.fetchone()[0]
            if res in ('completed', 'error', 'delivered'):
                print(']')
                print(res)
                break
            else:
                print(ici, end = '', flush=True)
        else:
            print('#', end = '', flush=True)
            time.sleep(1) #Ждём 5с
    else:
        print(']')
        print("\tTimeOut!!!")