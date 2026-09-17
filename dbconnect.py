from unicodedata import category

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

def getCategories():
    conn = get_db_connect()
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, title FROM categories")
        categories = cursor.fetchall()
    cursor.close()
    return categories

def getSuppliers():
    conn = get_db_connect()
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, name FROM suppliers")
        suppliers = cursor.fetchall()
    cursor.close()
    return suppliers
    
get_db_connect()

