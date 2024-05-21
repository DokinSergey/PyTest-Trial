import psycopg2

#Создаем подключение к базе на host
with psycopg2.connect(database="OMControl",
                        host="dns-15",
                        user="Customer",
                        password="619838",
                        port="5432") as conn:
    #----------------------------------------------------------------------------
    cursor = conn.cursor()
    # #Записываем в таблицу команду создать OMCID
    sql_txt  = 'INSERT INTO customers.ctasks (command, omcid, cuinn, phone, umail, tsevr)\n'
    sql_txt += 'VALUES (%s,%s,%s,%s,%s,%s);'
    datasql = ('Create_OMCID','dev24002','504834567890', '+7-985-365-24-49', 'vasypupkin@mmail.ru', 'bali')
    cursor.execute(sql_txt, datasql)
    # # #----------------------------------------------------------------------------
    # #Записываем в таблицу команду создать User
    # sql_txt  = 'INSERT INTO customers.ctasks (command,omcid,tsevr,usrID,upass)\n'
    # sql_txt += 'VALUES (%s,%s,%s,%s,%s);'
    # datasql = ('Create_User','dev24002','bali','dev2400201','12345678DevA')
    # cursor.execute(sql_txt, datasql)
    #-----------------------------------------------------------------------------
    # cursor = conn.cursor()
    cursor.execute("SELECT ssid,command,omcid,cuinn,phone,umail,tsevr,usrID,upass,timing FROM customers.ctasks ") #WHERE ctasks.tid = 1
    res = cursor.fetchall()
    for ires in res:
        print(ires)

# with sqlite3.connect(_SQLBaseRep) as conn:
    # sql_txt  = f'INSERT INTO {TabName} (IdOmcdUser,iTermOrOU,iAction,iUserName,iCompName)\n'
    # sql_txt += "VALUES (?,?,?,?,?)"
    # DataS = (IdOmcdUser,iTrOu,iAction,_USERNAME,_COMPNAME)
    # conn.execute(sql_txt, DataS)

# res = cursor.fetchone()

