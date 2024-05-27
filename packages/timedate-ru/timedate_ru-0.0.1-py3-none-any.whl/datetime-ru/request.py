connection.py:

import pymysql

class Database:
    def __init__(self, host, user, password, database):
        try:
            self.connection = pymysql.connect(host=host, user=user, password=password, database=database)
            self.cursor = self.connection.cursor()
            print("успешно")
        except Exception as e:
            print(f'ошибка {e}')

    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

db = Database(host='localhost', user='root', password='', database='book_club')

------------------------------------------------------------

auth.py:

import sys

from PyQt5.QtWidgets import QApplication, QDialog, QWidget,QMainWindow,QMessageBox
from PyQt5.uic import loadUi
from database.connection import Database

class Auth(QMainWindow):
    def __init__(self):
        super(Auth, self).__init__()
        loadUi("../ui_forms/auth.ui", self)
        self.db= Database(host='localhost', user='root', password='', database='book_club')
        self.pushButton.clicked.connect(self.auth)

    def auth(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()

        query = "SELECT username,password,id_role FROM user WHERE username = %s AND password = %s"
        self.db.cursor.execute(query,(login,password))
        result = self.db.cursor.fetchone()

        user = result[2]



        if result:
            if user == 1:
                from admin import Admin
                QMessageBox.information(self, "Успешно", "Вы вошли как администратор ")
                self.close()
                self.admin_form = Admin()
                self.admin_form.show()
            elif user == 2:
                from manager import Manager
                QMessageBox.information(self, "Успешно", "Вы вошли как менеджер")
                self.close()
                self.products_form = Manager()
                self.products_form.show()
            elif user == 3:
                from products import Products
                QMessageBox.information(self, "Успешно", "Вы вошли как клиент")
                self.close()
                self.products_form = Products()
                self.products_form.show()



        else:
            QMessageBox.warning(self, "Ошибка", "Ошибка логин или пароль")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Auth()
    window.show()
    app.exit(app.exec_())

---------------------------------------------------------------------------

products.py:

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QComboBox, QGridLayout, QMessageBox
from PyQt5.QtGui import QPixmap, QImage, QFont
from PyQt5.uic import loadUi
from database.connection import Database

class Products(QMainWindow):
    def __init__(self):
        super(Products, self).__init__()
        loadUi("../ui_forms/products_view.ui", self)
        self.db = Database(host='localhost', user='root', password='', database='book_club')
        self.combobox_show()
        self.comboBox.currentIndexChanged.connect(self.combobox_view)
        self.update_total()
        self.pushButton.clicked.connect(self.show_basket)

    def show_basket(self):
        from basket import Basket
        self.close()
        self.basket_form = Basket()
        self.basket_form.show()

    def combobox_show(self):
        query = "SELECT name FROM category"
        self.db.cursor.execute(query)
        result = self.db.cursor.fetchall()
        for combo in result:
            self.comboBox.addItem(combo[0])

    def combobox_view(self):
        comboID = self.comboBox.currentIndex() + 1
        query = "SELECT id, name, price, image FROM product WHERE category_id = %s"
        self.db.cursor.execute(query, (comboID,))
        products = self.db.cursor.fetchall()
        self.db.connection.commit()

        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)

        self.product_data = products

        row = 0
        col = 0

        for product in products:
            product_id = product[0]
            product_name = product[1]
            product_price = product[2]
            product_image_data = product[3]

            image_label = QLabel(self)
            if product_image_data:
                image = QImage.fromData(product_image_data)
                if not image.isNull():
                    pixmap = QPixmap.fromImage(image)
                    image_label.setPixmap(pixmap.scaled(200, 200, aspectRatioMode=1))
                else:
                    image_label.setText("Ошибка загрузки изображения")
            else:
                image_label.setText("Нет доступного изображения")

            product_label = QLabel(product_name, self)
            product_font = QFont()
            product_font.setBold(True)
            product_font.setPointSize(8)
            product_label.setFont(product_font)

            price_label = QLabel(f"Цена: {product_price}", self)
            price_font = QFont()
            price_font.setBold(True)
            price_label.setFont(price_font)

            add_button = QPushButton("Добавить в корзину", self)
            add_button.clicked.connect(lambda ch, pid=product_id, pprice=product_price: self.add_to_cart(pid, pprice))

            description_button = QPushButton("Описание", self)
            description_button.clicked.connect(lambda ch, id=product_id: self.show_description(id))

            layout = QVBoxLayout()
            layout.setSpacing(5)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(image_label)
            layout.addWidget(product_label)
            layout.addWidget(price_label)
            layout.addWidget(add_button)
            layout.addWidget(description_button)

            container = QWidget()
            container.setLayout(layout)

            self.gridLayout.addWidget(container, row, col)

            col += 1
            if col == 3:
                col = 0
                row += 1

    def add_to_cart(self, product_id, product_price):
        query = "INSERT INTO orderdetails (product_id, user_id, price) VALUES (%s, %s, %s)"
        user_id = 3  # Здесь можно указать текущий user_id, если он известен
        self.db.cursor.execute(query, (product_id, user_id, product_price))
        self.db.connection.commit()
        QMessageBox.information(self, "Успех", "Товар добавлен в корзину")
        self.update_total()

    def update_total(self):
        query = "SELECT SUM(price) FROM orderdetails WHERE user_id = %s"
        user_id = 3  # Здесь можно указать текущий user_id, если он известен
        self.db.cursor.execute(query, (user_id,))
        total = self.db.cursor.fetchone()[0]
        if total is None:
            total = 0
        self.label_2.setText(f"Итого: {total} руб.")

    def show_description(self, product_id):
        query = "SELECT name, description, manufactur FROM product WHERE id = %s"
        self.db.cursor.execute(query, (product_id,))
        result = self.db.cursor.fetchone()
        if result:
            name = result[0]
            description = result[1]
            manufactur = result[2]
            message = f"Название: {name}\n\nОписание: {description}\n\nПроизводство: {manufactur}"
            QMessageBox.information(self, "Описание товара", message)
        else:
            QMessageBox.warning(self, "Ошибка", "Описание не найдено")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Products()
    window.show()
    sys.exit(app.exec_())
----------------------------------------------------------------------------------

menager.py:

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog
from PyQt5.uic import loadUi
import os
from database.connection import Database  # Предполагаем, что ваш класс Database импортируется отсюда

# Конфигурация подключения к базе данных
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'book_club'
}


class Manager(QMainWindow):
    def __init__(self):
        super(Manager, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), '../ui_forms/manager_view.ui')
        loadUi(ui_path, self)
        self.db = Database(**db_config)  # Передаем конфигурацию подключения

        self.pushButton.clicked.connect(self.view_products)
        self.pushButton_2.clicked.connect(self.view_orders)
        self.pushButton_3.clicked.connect(self.add_order_row)
        self.pushButton_4.clicked.connect(self.edit_order)
        self.pushButton_save_order.clicked.connect(self.save_order)
        self.pushButton_save_changes.clicked.connect(self.save_changes)  # Добавлено

    def view_products(self):
        try:
            query = """
                SELECT p.id, p.name, p.description, p.manufactur, p.price, p.count, p.discount, c.name as category_name
                FROM product p
                JOIN category c ON p.category_id = c.id
            """
            results = self.db.fetch_all(query)
            self.tableWidget.clear()  # Очищаем таблицу перед добавлением новых данных
            if results:
                self.tableWidget.setRowCount(len(results))
                self.tableWidget.setColumnCount(len(results[0]))
                headers = ['id', 'name', 'description', 'manufactur', 'price', 'count', 'discount', 'category_name']
                self.tableWidget.setHorizontalHeaderLabels(headers)
                for row_index, row_data in enumerate(results):
                    for col_index, col_data in enumerate(row_data):
                        self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            else:
                QMessageBox.information(self, "Информация", "Нет данных для отображения.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при просмотре товаров: {e}")


    def view_orders(self):
        try:
            query = """
                SELECT o.id, o.orderdate, o.ordernumber, o.totalamount, o.discountamount, 
                       o.orderstatus, pp.adress as pickup_address, o.pickup_code, o.id_order_details
                FROM orders o
                JOIN pickuppoint pp ON o.pickup_id = pp.id
            """
            results = self.db.fetch_all(query)
            self.tableWidget.clear()  # Очищаем таблицу перед добавлением новых данных
            if results:
                self.tableWidget.setRowCount(len(results) + 1)  # Добавляем дополнительную строку для нового заказа
                self.tableWidget.setColumnCount(len(results[0]))
                headers = ['id', 'orderdate', 'ordernumber', 'totalamount', 'discountamount', 'orderstatus', 'pickup_address', 'pickup_code', 'id_order_details']
                self.tableWidget.setHorizontalHeaderLabels(headers)
                for row_index, row_data in enumerate(results):
                    for col_index, col_data in enumerate(row_data):
                        self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
                self.tableWidget.setItem(len(results), 0, QTableWidgetItem("new"))  # Для новой строки
            else:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setColumnCount(9)
                headers = ['id', 'orderdate', 'ordernumber', 'totalamount', 'discountamount', 'orderstatus', 'pickup_address', 'pickup_code', 'id_order_details']
                self.tableWidget.setHorizontalHeaderLabels(headers)
                QMessageBox.information(self, "Информация", "Нет данных для отображения.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при просмотре заказов: {e}")

    def add_order_row(self):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

    def save_order(self):
        try:
            row_position = self.tableWidget.rowCount() - 1  # Последняя строка
            orderdate = self.tableWidget.item(row_position, 1).text()
            ordernumber = self.tableWidget.item(row_position, 2).text()
            totalamount = self.tableWidget.item(row_position, 3).text()
            discountamount = self.tableWidget.item(row_position, 4).text()
            orderstatus = self.tableWidget.item(row_position, 5).text()
            pickup_id = self.tableWidget.item(row_position, 6).text()
            pickup_code = self.tableWidget.item(row_position, 7).text()
            id_order_details = self.tableWidget.item(row_position, 8).text()

            query = """
                INSERT INTO orders (orderdate, ordernumber, totalamount, discountamount, orderstatus, pickup_id, pickup_code, id_order_details)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            params = (orderdate, ordernumber, totalamount, discountamount, orderstatus, pickup_id, pickup_code, id_order_details)
            self.db.execute(query, params)
            QMessageBox.information(self, "Успех", "Заказ успешно создан!")
            self.view_orders()  # Обновить таблицу
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при создании заказа: {e}")


    def save_changes(self):
        try:
            for row in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(row, 0) and self.tableWidget.item(row, 0).text() != "new":
                    order_id = int(self.tableWidget.item(row, 0).text())
                    orderdate = self.tableWidget.item(row, 1).text()
                    ordernumber = self.tableWidget.item(row, 2).text()
                    totalamount = self.tableWidget.item(row, 3).text()
                    discountamount = self.tableWidget.item(row, 4).text()
                    orderstatus = self.tableWidget.item(row, 5).text()
                    pickup_id = self.tableWidget.item(row, 6).text()
                    pickup_code = self.tableWidget.item(row, 7).text()
                    id_order_details = self.tableWidget.item(row, 8).text()

                    query = """
                        UPDATE orders
                        SET orderdate = %s, ordernumber = %s, totalamount = %s, discountamount = %s, orderstatus = %s, pickup_id = %s, pickup_code = %s, id_order_details = %s
                        WHERE id = %s
                    """
                    params = (orderdate, ordernumber, totalamount, discountamount, orderstatus, pickup_id, pickup_code, id_order_details, order_id)
                    self.db.execute(query, params)
            QMessageBox.information(self, "Успех", "Изменения успешно сохранены!")
            self.view_orders()  # Обновить таблицу
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при сохранении изменений: {e}")

    def edit_order(self):
        try:
            order_id, ok = QInputDialog.getInt(self, 'Редактирование заказа', 'Введите ID заказа для редактирования:')
            if ok:
                query = "SELECT * FROM orders WHERE id = %s"
                order = self.db.fetch_all(query, (order_id,))
                if order:
                    orderdate, ok1 = QInputDialog.getText(self, 'Редактирование заказа', 'Введите дату заказа (YYYY-MM-DD):', text=order[0][1])
                    ordernumber, ok2 = QInputDialog.getInt(self, 'Редактирование заказа', 'Введите номер заказа:', value=order[0][2])
                    totalamount, ok3 = QInputDialog.getDouble(self, 'Редактирование заказа', 'Введите общую сумму:', value=order[0][3])
                    discountamount, ok4 = QInputDialog.getInt(self, 'Редактирование заказа', 'Введите сумму скидки:', value=order[0][4])
                    orderstatus, ok5 = QInputDialog.getText(self, 'Редактирование заказа', 'Введите статус заказа:', text=order[0][5])
                    pickup_id, ok6 = QInputDialog.getInt(self, 'Редактирование заказа', 'Введите ID пункта выдачи:', value=order[0][6])
                    pickup_code, ok7 = QInputDialog.getText(self, 'Редактирование заказа', 'Введите код выдачи:', text=order[0][7])
                    id_order_details, ok8 = QInputDialog.getInt(self, 'Редактирование заказа', 'Введите ID деталей заказа:', value=order[0][8])

                    if ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7 and ok8:
                        query = """
                            UPDATE orders
                            SET orderdate = %s, ordernumber = %s, totalamount = %s, discountamount = %s, orderstatus = %s, pickup_id = %s, pickup_code = %s, id_order_details = %s
                            WHERE id = %s
                        """
                        params = (orderdate, ordernumber, totalamount, discountamount, orderstatus, pickup_id, pickup_code, id_order_details, order_id)
                        self.db.execute(query, params)
                        QMessageBox.information(self, "Успех", "Заказ успешно обновлен!")
                        self.view_orders()  # Обновить таблицу
                else:
                    QMessageBox.information(self, "Информация", "Заказ с таким ID не найден.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при редактировании заказа: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Manager()
    window.show()
    sys.exit(app.exec_())

-------------------------------------------------------------------------------------

basket.py:

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QCheckBox, QComboBox,  QMessageBox

from PyQt5.uic import loadUi
from database.connection import Database
from datetime import datetime
import datetime

class Basket(QMainWindow):
    def __init__(self):
        super(Basket, self).__init__()
        loadUi("../ui_forms/basket_view.ui", self)
        self.db = Database(host='localhost', user='root', password='', database='book_club')
        self.pushButton_3.clicked.connect(self.prev)
        self.pushButton_2.clicked.connect(self.remove_selected_items)
        self.pushButton.clicked.connect(self.place_order)
        self.checkboxes = []
        self.load_basket_items()
        self.update_total()
        self.load_pickup_addresses()
    #     self.pushButton.clicked.connect(self.insert)
    #
    # # def insert(self):
    # #     order_number = 1
    # #     query = "INSERT INTO orders(orderdate, ordernumber, totalamount, pickup_id, pickup_code, id_order_details) VALUES"
    # #

    def load_pickup_addresses(self):
        query = "SELECT id, adress FROM pickuppoint"
        self.db.cursor.execute(query)
        addresses = self.db.cursor.fetchall()

        self.comboBox.clear()
        for address in addresses:
            self.comboBox.addItem(address[1], address[0])  # address[0] is id, address[1] is adress

    def prev(self):
        from products import Products
        self.close()
        self.Products_form = Products()
        self.Products_form.show()

    def load_basket_items(self):
        query = """
        SELECT p.name, od.price, p.id
        FROM orderdetails od
        JOIN product p ON od.product_id = p.id
        WHERE od.user_id = %s
        """
        user_id = 3  # Здесь можно указать текущий user_id, если он известен
        self.db.cursor.execute(query, (user_id,))
        products = self.db.cursor.fetchall()

        for product in products:
            product_name = product[0]
            product_price = product[1]
            product_id = product[2]

            checkbox = QCheckBox(f"{product_name} - {product_price}")
            checkbox.setObjectName(f"checkbox_{product_id}")
            self.verticalLayout.addWidget(checkbox)
            self.checkboxes.append((checkbox, product_id, product_price))

    def update_total(self):
        query = "SELECT SUM(price) FROM orderdetails WHERE user_id = %s"
        user_id = 3  # Здесь можно указать текущий user_id, если он известен
        self.db.cursor.execute(query, (user_id,))
        total = self.db.cursor.fetchone()[0]
        if total is None:
            total = 0
        self.label_3.setText(f"{total} руб.")

    def remove_selected_items(self):
        user_id = 3  # Здесь можно указать текущий user_id, если он известен
        for checkbox, product_id, _ in self.checkboxes:
            if checkbox.isChecked():
                query = "DELETE FROM orderdetails WHERE user_id = %s AND product_id = %s"
                self.db.cursor.execute(query, (user_id, product_id))
                self.db.connection.commit()
                self.verticalLayout.removeWidget(checkbox)
                checkbox.deleteLater()
        self.checkboxes = [(cb, pid, price) for cb, pid, price in self.checkboxes if not cb.isChecked()]
        self.update_total()  # Пересчитать итоговую сумму после удаления

    def place_order(self):
        order_detail = 1
        user_id = 3  # Здесь можно указать текущий user_id, если он известен
        order_date = "2024-05-15"
        order_status = 'новый'
        pickup_id = self.comboBox.currentData()  # Получение выбранного pickup_id
        pickup_code = "random_code"  # Замените это на реальный код, если он генерируется
        query_total = "SELECT SUM(price) FROM orderdetails WHERE user_id = %s"
        self.db.cursor.execute(query_total, (user_id,))
        total_amount = self.db.cursor.fetchone()[0]
        if total_amount is None:
            total_amount = 0

        query_order = """
        INSERT INTO orders (orderdate, ordernumber, totalamount, orderstatus, pickup_id, pickup_code, id_order_details)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        order_number = self.get_next_order_number()
        self.db.cursor.execute(query_order,
                               (order_date, order_number, total_amount, order_status, pickup_id, pickup_code, order_detail))
        self.db.connection.commit()

        QMessageBox.information(self, "Успех", "Заказ успешно оформлен")
        self.clear_basket()

    def get_next_order_number(self):
        query = "SELECT MAX(ordernumber) FROM orders"
        self.db.cursor.execute(query)
        result = self.db.cursor.fetchone()[0]
        if result is None:
            return 1
        else:
            return result + 1

    def clear_basket(self):
        user_id = 3  # Здесь можно указать текущий user_id, если он известен
        query = "DELETE FROM orderdetails WHERE user_id = %s"
        self.db.cursor.execute(query, (user_id,))
        self.db.connection.commit()
        for checkbox, _, _ in self.checkboxes:
            self.verticalLayout.removeWidget(checkbox)
            checkbox.deleteLater()
        self.checkboxes.clear()
        self.update_total()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Basket()
    window.show()
    sys.exit(app.exec_())

--------------------------------------------------------------------------------------------------

admin.py:

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QDialog
from PyQt5.uic import loadUi
import os
from database.connection import Database  # Предполагаем, что ваш класс Database импортируется отсюда

# Конфигурация подключения к базе данных
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'book_club'
}


class AddEditProductDialog(QDialog):
    def __init__(self, parent=None):
        super(AddEditProductDialog, self).__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), '../ui_forms/add_edit_product_dialog.ui')
        loadUi(ui_path, self)

    def get_data(self):
        return (
            self.name_input.text(),
            self.description_input.text(),
            self.manufactur_input.text(),
            self.price_input.text(),
            self.count_input.text(),
            self.discount_input.text(),
            self.category_id_input.text()
        )

    def set_data(self, data):
        self.name_input.setText(data[0])
        self.description_input.setText(data[1])
        self.manufactur_input.setText(data[2])
        self.price_input.setText(data[3])
        self.count_input.setText(data[4])
        self.discount_input.setText(data[5])
        self.category_id_input.setText(data[6])


class Admin(QMainWindow):
    def __init__(self):
        super(Admin, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), '../ui_forms/admin_view.ui')
        loadUi(ui_path, self)
        self.db = Database(**db_config)  # Передаем конфигурацию подключения

        self.pushButton_view_products.clicked.connect(self.view_products)
        self.pushButton_add_product.clicked.connect(self.add_product)
        self.pushButton_edit_product.clicked.connect(self.edit_product)
        self.pushButton_delete_product.clicked.connect(self.delete_product)
        self.pushButton_save_changes.clicked.connect(self.save_changes)

    def view_products(self):
        try:
            query = """
                SELECT p.id, p.name, p.description, p.manufactur, p.price, p.count, p.discount, c.name as category_name
                FROM product p
                JOIN category c ON p.category_id = c.id
            """
            results = self.db.fetch_all(query)
            self.tableWidget.clear()  # Очищаем таблицу перед добавлением новых данных
            if results:
                self.tableWidget.setRowCount(len(results))
                self.tableWidget.setColumnCount(len(results[0]))
                headers = ['id', 'name', 'description', 'manufactur', 'price', 'count', 'discount', 'category_name']
                self.tableWidget.setHorizontalHeaderLabels(headers)
                for row_index, row_data in enumerate(results):
                    for col_index, col_data in enumerate(row_data):
                        self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            else:
                QMessageBox.information(self, "Информация", "Нет данных для отображения.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при просмотре товаров: {e}")

    def add_product(self):
        try:
            dialog = AddEditProductDialog()
            if dialog.exec_() == QDialog.Accepted:
                data = dialog.get_data()
                query = """
                    INSERT INTO product (name, description, manufactur, price, count, discount, category_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                params = (data[0], data[1], data[2], data[3], data[4], data[5], data[6])
                self.db.execute(query, params)
                QMessageBox.information(self, "Успех", "Товар успешно добавлен!")
                self.view_products()  # Обновить таблицу
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при добавлении товара: {e}")


    def edit_product(self):
        try:
            row = self.tableWidget.currentRow()
            if row != -1:
                dialog = AddEditProductDialog()
                product_id = self.tableWidget.item(row, 0).text()
                data = [
                    self.tableWidget.item(row, i).text() for i in range(1, 8)
                ]
                dialog.set_data(data)
                if dialog.exec_() == QDialog.Accepted:
                    new_data = dialog.get_data()
                    query = """
                        UPDATE product 
                        SET name = %s, description = %s, manufactur = %s, price = %s, count = %s, discount = %s, category_id = %s
                        WHERE id = %s
                    """
                    params = (*new_data, product_id)
                    self.db.execute(query, params)
                    QMessageBox.information(self, "Успех", "Товар успешно обновлен!")
                    self.view_products()  # Обновить таблицу
            else:
                QMessageBox.warning(self, "Внимание", "Пожалуйста, выберите товар для редактирования.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при редактировании товара: {e}")

    def delete_product(self):
        try:
            row = self.tableWidget.currentRow()
            if row != -1:
                product_id = self.tableWidget.item(row, 0).text()
                query = "DELETE FROM product WHERE id = %s"
                self.db.execute(query, (product_id,))
                QMessageBox.information(self, "Успех", "Товар успешно удален!")
                self.view_products()  # Обновить таблицу
            else:
                QMessageBox.warning(self, "Внимание", "Пожалуйста, выберите товар для удаления.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при удалении товара: {e}")

    def save_changes(self):
        try:
            for row in range(self.tableWidget.rowCount()):
                product_id = self.tableWidget.item(row, 0).text()
                name = self.tableWidget.item(row, 1).text()
                description = self.tableWidget.item(row, 2).text()
                manufactur = self.tableWidget.item(row, 3).text()
                price = self.tableWidget.item(row, 4).text()
                count = self.tableWidget.item(row, 5).text()
                discount = self.tableWidget.item(row, 6).text()
                category_id = self.tableWidget.item(row, 7).text()

                query = """
                    UPDATE product 
                    SET name = %s, description = %s, manufactur = %s, price = %s, count = %s, discount = %s, category_id = %s
                    WHERE id = %s
                """
                params = (name, description, manufactur, price, count, discount, category_id, product_id)
                self.db.execute(query, params)
            QMessageBox.information(self, "Успех", "Изменения успешно сохранены!")
            self.view_products()  # Обновить таблицу
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при сохранении изменений: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Admin()
    window.show()
    sys.exit(app.exec_())


--------------------------------------------------------------------------------

add_edit_product_dialog.ui:

<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>AddEditProductDialog</class>
 <widget class="QDialog" name="AddEditProductDialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Add/Edit Product</string>
  </property>
  <widget class="QWidget" name="gridLayoutWidget">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>20</y>
     <width>361</width>
     <height>241</height>
    </rect>
   </property>
   <layout class="QGridLayout" name="gridLayout">
    <item row="0" column="0">
     <widget class="QLabel" name="label_name">
      <property name="text">
       <string>Name:</string>
      </property>
     </widget>
    </item>
    <item row="0" column="1">
     <widget class="QLineEdit" name="name_input"/>
    </item>
    <item row="1" column="0">
     <widget class="QLabel" name="label_description">
      <property name="text">
       <string>Description:</string>
      </property>
     </widget>
    </item>
    <item row="1" column="1">
     <widget class="QLineEdit" name="description_input"/>
    </item>
    <item row="2" column="0">
     <widget class="QLabel" name="label_manufactur">
      <property name="text">
       <string>Manufacturer:</string>
      </property>
     </widget>
    </item>
    <item row="2" column="1">
     <widget class="QLineEdit" name="manufactur_input"/>
    </item>
    <item row="3" column="0">
     <widget class="QLabel" name="label_price">
      <property name="text">
       <string>Price:</string>
      </property>
     </widget>
    </item>
    <item row="3" column="1">
     <widget class="QLineEdit" name="price_input"/>
    </item>
    <item row="4" column="0">
     <widget class="QLabel" name="label_count">
      <property name="text">
       <string>Count:</string>
      </property>
     </widget>
    </item>
    <item row="4" column="1">
     <widget class="QLineEdit" name="count_input"/>
    </item>
    <item row="5" column="0">
     <widget class="QLabel" name="label_discount">
      <property name="text">
       <string>Discount:</string>
      </property>
     </widget>
    </item>
    <item row="5" column="1">
     <widget class="QLineEdit" name="discount_input"/>
    </item>
    <item row="6" column="0">
     <widget class="QLabel" name="label_category_id">
      <property name="text">
       <string>Category ID:</string>
      </property>
     </widget>
    </item>
    <item row="6" column="1">
     <widget class="QLineEdit" name="category_id_input"/>
    </item>
   </layout>
  </widget>
  <widget class="QDialogButtonBox" name="buttonBox">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>260</y>
     <width>341</width>
     <height>32</height>
    </rect>
   </property>
   <property name="standardButtons">
    <set>QDialogButtonBox::Cancel|QDialogButtonBox::Ok</set>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

--------------------------------------------------------------------------------------

admin_view.ui:

<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Admin Panel</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>20</y>
      <width>760</width>
      <height>400</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_view_products">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>430</y>
      <width>111</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>View Products</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_add_product">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>430</y>
      <width>111</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Add Product</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_edit_product">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>430</y>
      <width>111</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Edit Product</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_delete_product">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>430</y>
      <width>111</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Delete Product</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_save_changes">
    <property name="geometry">
     <rect>
      <x>540</x>
      <y>430</y>
      <width>111</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Save Changes</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>

---------------------------------------------------------------------------------

auth.ui:

<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>450</width>
    <height>500</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>450</width>
    <height>500</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>450</width>
    <height>500</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Авторизация</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 255, 255);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>380</y>
      <width>301</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:21px;</string>
    </property>
    <property name="text">
     <string>ВОЙТИ</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>401</width>
      <height>91</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Авторизация </string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>140</y>
      <width>141</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>9</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(141, 141, 141);</string>
    </property>
    <property name="text">
     <string>Имя пользователя</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>170</y>
      <width>391</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(107, 107, 107);</string>
    </property>
    <property name="inputMask">
     <string/>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="placeholderText">
     <string>Введите своё имя пользователя</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>270</y>
      <width>391</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(107, 107, 107);</string>
    </property>
    <property name="inputMask">
     <string/>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="maxLength">
     <number>32767</number>
    </property>
    <property name="echoMode">
     <enum>QLineEdit::Password</enum>
    </property>
    <property name="dragEnabled">
     <bool>false</bool>
    </property>
    <property name="placeholderText">
     <string>Введите свой пароль</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>240</y>
      <width>141</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>9</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(141, 141, 141);</string>
    </property>
    <property name="text">
     <string>Пароль</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>450</width>
     <height>26</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu">
    <property name="title">
     <string>Сотрудник?</string>
    </property>
    <addaction name="action"/>
    <addaction name="action_2"/>
    <addaction name="action_3"/>
   </widget>
   <addaction name="menu"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="action">
   <property name="text">
    <string>Администратор</string>
   </property>
  </action>
  <action name="action_2">
   <property name="text">
    <string>Менеджнр</string>
   </property>
  </action>
  <action name="action_3">
   <property name="text">
    <string>Клиент</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>

------------------------------------------------------------------------------------

basket_view.ui:

<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>900</width>
    <height>900</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>900</width>
    <height>900</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>900</width>
    <height>900</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Корзина</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 255, 255);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>780</y>
      <width>301</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:21px;</string>
    </property>
    <property name="text">
     <string>ЗАКАЗАТЬ </string>
    </property>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>80</y>
      <width>841</width>
      <height>451</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout"/>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>710</y>
      <width>301</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:21px;</string>
    </property>
    <property name="text">
     <string>УДАЛИТЬ</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>490</x>
      <y>760</y>
      <width>131</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>ИТОГО:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>30</y>
      <width>141</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>КОРЗИНА</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_3">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>10</y>
      <width>101</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:21px;</string>
    </property>
    <property name="text">
     <string>НАЗАД</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>630</x>
      <y>760</y>
      <width>131</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>580</y>
      <width>91</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Место выдачи</string>
    </property>
   </widget>
   <widget class="QComboBox" name="comboBox">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>610</y>
      <width>821</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>900</width>
     <height>26</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu">
    <property name="title">
     <string>Сотрудник?</string>
    </property>
    <addaction name="action"/>
    <addaction name="action_2"/>
    <addaction name="action_3"/>
   </widget>
   <addaction name="menu"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="action">
   <property name="text">
    <string>Администратор</string>
   </property>
  </action>
  <action name="action_2">
   <property name="text">
    <string>Менеджнр</string>
   </property>
  </action>
  <action name="action_3">
   <property name="text">
    <string>Клиент</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>

------------------------------------------------------------------------------

manager_view.ui:

<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>900</width>
    <height>900</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>900</width>
    <height>900</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>900</width>
    <height>900</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Форма Менееджера</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 255, 255);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>80</y>
      <width>831</width>
      <height>301</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>390</y>
      <width>121</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Посмотреть товары</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>390</y>
      <width>111</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Посмотреть заказы</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_3">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>390</y>
      <width>121</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Создать заказ</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_4">
    <property name="geometry">
     <rect>
      <x>470</x>
      <y>390</y>
      <width>121</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Редактировать заказ</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_save_order">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>420</y>
      <width>121</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Сохранить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_save_changes">
    <property name="geometry">
     <rect>
      <x>470</x>
      <y>420</y>
      <width>121</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Сохранить</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>900</width>
     <height>21</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu">
    <property name="title">
     <string>Сотрудник?</string>
    </property>
    <addaction name="action"/>
    <addaction name="action_2"/>
    <addaction name="action_3"/>
   </widget>
   <addaction name="menu"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="action">
   <property name="text">
    <string>Администратор</string>
   </property>
  </action>
  <action name="action_2">
   <property name="text">
    <string>Менеджнр</string>
   </property>
  </action>
  <action name="action_3">
   <property name="text">
    <string>Клиент</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>

---------------------------------------------------------------------------------------

products_view.ui:

<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>900</width>
    <height>900</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>900</width>
    <height>900</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>900</width>
    <height>900</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Продукты</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 255, 255);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>540</x>
      <y>790</y>
      <width>301</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:21px;</string>
    </property>
    <property name="text">
     <string>КОРЗИНА</string>
    </property>
   </widget>
   <widget class="QComboBox" name="comboBox">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>40</y>
      <width>751</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
   </widget>
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>150</y>
      <width>841</width>
      <height>591</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout"/>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>800</y>
      <width>341</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>20</y>
      <width>131</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Выберите категорию</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>100</y>
      <width>161</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Товары</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>900</width>
     <height>26</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu">
    <property name="title">
     <string>Сотрудник?</string>
    </property>
    <addaction name="action"/>
    <addaction name="action_2"/>
    <addaction name="action_3"/>
   </widget>
   <addaction name="menu"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="action">
   <property name="text">
    <string>Администратор</string>
   </property>
  </action>
  <action name="action_2">
   <property name="text">
    <string>Менеджнр</string>
   </property>
  </action>
  <action name="action_3">
   <property name="text">
    <string>Клиент</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
