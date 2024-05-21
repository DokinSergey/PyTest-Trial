import psycopg as pg
import time
#Создаем подключение к базе на host
# with pg.connect(
        # dbname="OMControl",
        # host="dns-15",
        # user="Customer",
        # password="619838",
        # port="5432"
        # ) as conn:
with pg.connect(dbname="Test",
        host = 'DokinPC',
        user="dokin",
        password="619838",
        port="5432"
        ) as conn:
    #----------------------------------------------------------------------------
    # with conn.cursor() as cursor:
        #Записываем в таблицу индекс сессии
        # sql_txt  = "INSERT INTO customers.session (contex) VALUES(%s) RETURNING ssid;"
        # datasql = ('vasypupkin@mmail.ru',)
        # cursor.execute(sql_txt, datasql)
        # SessID = cursor.fetchone()[0]
        # print(SessID)
     # #Записываем в таблицу команду создать OMCID
    with conn.cursor() as cursor:
        sql_txt  = 'INSERT INTO customers.ctasks (command, omcid, cuinn, phone, umail, tsevr,status)'
        sql_txt += 'VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING TaskID;'
        datasql = ("Create_OMCID","dev24002","504834567890", "+7-985-365-24-49", "vasypupkin@mmail.ru", "bali", "open")
        # cursor.execute(sql_txt, datasql)
        # SessID = cursor.fetchone()[0]
        SessID = 7
        # print(SessID)
        #----------------------------------------------------------------------------
        #Записываем в таблицу команду создать User
        # sql_txt  = 'INSERT INTO customers.ctasks (TaskID,command,omcid,tsevr,usrID,upass)\n'
        # sql_txt += 'VALUES (%s,%s,%s,%s,%s,%s);'
        # datasql = (SessID,'Create_User','dev24002','bali','dev2400201','12345678DevA')
        # cursor.execute(sql_txt, datasql)
        #-----------------------------------------------------------------------------
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

# res = cursor.fetchone()
# open
# run
# completed
# executed
# error
# delivered