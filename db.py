import psycopg2
from config import *
db = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)
cursor = db.cursor()


def select_db(whatis="*", fromis="users", whereis=''):
    global db, cursor
    try:
        if whereis == "":
            cursor.execute("""SELECT {} FROM {} ORDER BY id ASC;""".format(whatis, fromis))
        else:
            cursor.execute(
                """SELECT {} FROM {} WHERE {} ORDER BY id ASC;""".format(whatis, fromis, whereis))
        return cursor.fetchall()
    except Exception as e:
        db.close()
        db = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        cursor = db.cursor()
        print("+++++++++++++++++++++++++++ОТЧЁТ ОБ ОШИБКЕ+++++++++++++++++\n\n--------------Ошибка в блоке select -----------\n\n\n\nЗапрос:\n\n")
        print("""SELECT {} FROM {} WHERE {} ORDER BY id ASC;""".format(whatis, fromis, whereis))
        print(f"ОШИБКА: \n\n{e}\n\n\n_______________________________КОНЕЦ ОТЧЁТА __________________________________")
        return []

def insert_db(name_table, column, values):
    global db, cursor
    try:
        if None in values:
            val = list(values)
            val[val.index(None)] = ""
            values = tuple(val)
        column = str(column).replace("'", "")
        # print(f"""INSERT INTO {name_table} {column} VALUES{value>
        cursor.execute(
            f"""INSERT INTO {name_table} {column} VALUES{values};"""
        )
        db.commit()
    except Exception as e:
        db.close()
        db = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        cursor = db.cursor()
        print("+++++++++++++++++++++++++++ОТЧЁТ ОБ ОШИБКЕ++++++++++++++++++++++++")
        print(f"""INSERT INTO {name_table} {column} VALUES{values}""")
        print(f"ОШИБКА: \n\n{e}\n\n\n_____________________________")
        return []

    
def delete_db(name_table, where):
    global db, cursor
    try:
        # print(f"""-- DELETE FROM {name_table} WHERE {where};""")
        cursor.execute(
            f"""DELETE FROM {name_table} WHERE {where};""")
        db.commit()
    except Exception as e:
        db.close()
        db = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        cursor = db.cursor()
        print("+++++++++++++++++++++++++++ОТЧЁТ ОБ ОШИБКЕ+++++++++++++++++\n\n--------------Ошибка в блоке delete -----------\n\n\n\nЗапрос:\n\n")
        print(f"""-- DELETE FROM {name_table} WHERE {where};""")
        print(f"ОШИБКА: \n\n{e}\n\n\n_______________________________КОНЕЦ ОТЧЁТА __________________________________")
        return []


def update_db(name_table, column, value, whereis):
    global db, cursor
    try:
        # print(f"""UPDATE {name_table} SET {column} = {value} WHERE {whereis};""")
        cursor.execute(
            f"""UPDATE {name_table} SET {column} = {value} WHERE {whereis};""")
        db.commit()
    except Exception as e:
        db.close()
        db = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        cursor = db.cursor()
        print("+++++++++++++++++++++++++++ОТЧЁТ ОБ ОШИБКЕ+++++++++++++++++\n\n--------------Ошибка в блоке update -----------\n\n\n\nЗапрос:\n\n")
        print(f"""UPDATE {name_table} SET {column} = {value} WHERE {whereis};""")
        print(f"ОШИБКА: \n\n{e}\n\n\n_______________________________КОНЕЦ ОТЧЁТА __________________________________")
        return []
