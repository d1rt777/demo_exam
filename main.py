import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem

import dbconnect
from ui_add_product import Ui_add_product
from ui_product_cart import Ui_MainWindow
from ui_product_list import Ui_PeoductList
from ui_window_login import Ui_Dialog

def add_product():
    global add_window
    global add_ui

    add_window = QDialog()

    add_ui = Ui_add_product()
    add_ui.setupUi(add_window)

    add_ui.buttonBox.accepted.connect(setProduct)

    add_window.show()

    product_ui.add_window = add_window


def check_login(loginValue, passValue):
    conn = dbconnect.get_db_connect()

    with conn.cursor() as cursor:
        cursor.execute(
            f"SELECT login, password FROM users WHERE login = '{loginValue}' AND password = '{passValue}'"
        )

        user = cursor.fetchone()

    conn.close()

    if user:
        return True

    return False


def login():
    loginValue = ui.textEdit.toPlainText()
    passValue = ui.textEdit_2.toPlainText()

    print("Логин:", loginValue)
    print("Пароль:", passValue)

    if check_login(loginValue, passValue):
        print("Авторизация успешна")

        window.close()

        global product_window
        global product_ui

        product_window = QMainWindow()
        product_ui = Ui_PeoductList()
        product_ui.setupUi(product_window)

        load_products()

        product_ui.pushButton_2.clicked.connect(add_product)

        product_ui.tableWidget.cellDoubleClicked.connect(open_product)

        product_window.show()

    else:
        print("Неверный логин или пароль")


def get_products():
    conn = dbconnect.get_db_connect()

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

    conn.close()

    return products


def load_products():
    products = get_products()

    product_ui.tableWidget.setRowCount(len(products))
    product_ui.tableWidget.setColumnCount(4)

    product_ui.tableWidget.setHorizontalHeaderLabels(
        ["ID", "Название", "Цена", "Количество"]
    )

    for row, product in enumerate(products):
        product_ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(product["id"])))

        product_ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(product["title"])))

        product_ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(product["price"])))

        product_ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(product["count"])))


def get_product(product_id):
    conn = dbconnect.get_db_connect()

    with conn.cursor() as cursor:
        cursor.execute(
            f"""
            SELECT
                products.*,
                categories.title AS category,
                suppliers.name AS supplier
            FROM products
            LEFT JOIN categories
                ON products.category_id = categories.id
            LEFT JOIN suppliers
                ON products.supplier_id = suppliers.id
            WHERE products.id = {product_id}
            """
        )

        product = cursor.fetchone()

    conn.close()

    return product

def open_product(row, column):
    product_id = product_ui.tableWidget.item(row, 0).text()

    product = get_product(product_id)

    if product:
        global cart_window
        global cart_ui

        cart_window = QMainWindow()

        cart_ui = Ui_MainWindow()
        cart_ui.setupUi(cart_window)

        cart_ui.label_3.setText(str(product["category"]))
        cart_ui.label_5.setText(str(product["title"]))

        cart_ui.label_6.setText(
            "Описание товара: " + str(product["desription"])
        )

        cart_ui.label_7.setText(
            "Производитель: " + str(product["brand"])
        )

        cart_ui.label_8.setText(
            "Поставщик: " + str(product["supplier"])
        )

        cart_ui.label_9.setText(
            "Цена: " + str(product["price"])
        )
        cart_ui.label_10.setText(
            "Единица измерения: шт"
        )

        cart_ui.label_11.setText(
            "Количество на складе: " + str(product["count"])
        )

        cart_window.show()

def setProduct():
    title = add_ui.lineEdit.text()
    category = add_ui.comboBox.currentText()
    supplier = add_ui.comboBox_2.currentText()
    description = add_ui.textEdit.toPlainText()
    brand = add_ui.lineEdit_2.text()
    count = add_ui.spinBox.value()
    price = add_ui.spinBox_2.value()

    print(title)
    print(category)
    print(supplier)
    print(description)
    print(brand)
    print(count)
    print(price)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(window)

    ui.pushButton.clicked.connect(login)

    window.show()
    sys.exit(app.exec())
