import pymysql

def get_db_connect():
    return pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='demo_exam',
        cursorclass=pymysql.cursors.DictCursor
    )


def set_role():
    conn = get_db_connect()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO roles (title)VALUES ('Админ');")

    conn.commit()
    conn.close()

get_db_connect()

