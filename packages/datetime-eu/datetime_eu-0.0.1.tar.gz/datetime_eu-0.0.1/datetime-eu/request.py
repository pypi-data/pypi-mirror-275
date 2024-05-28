Admin.py:

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QCheckBox, QComboBox, QMessageBox, QTableWidgetItem, QInputDialog
from PyQt5.uic import loadUi
from database.database import Database
from datetime import datetime

class Admin(QMainWindow):
    def __init__(self):
        super(Admin, self).__init__()
        loadUi("../UI_forms/admin.ui", self)
        self.db = Database(host='localhost', user='root', password='', database='book_club')
        self.pushButton_add_product.clicked.connect(self.add_product)
        self.pushButton_edit_product.clicked.connect(self.edit_product)
        self.pushButton_delete_product.clicked.connect(self.delete_product)
        self.pushButton_view_orders.clicked.connect(self.show_orders)
        self.pushButton_edit_order.clicked.connect(self.edit_order)
        self.pushButton.clicked.connect(self.show_products)

    def add_product(self):
        # Ввод данных для нового товара
        name, ok1 = QInputDialog.getText(self, "Добавить товар", "Введите название товара:")
        description, ok2 = QInputDialog.getText(self, "Добавить товар", "Введите описание товара:")
        manufactur, ok3 = QInputDialog.getText(self, "Добавить товар", "Введите производителя товара:")
        price, ok4 = QInputDialog.getDouble(self, "Добавить товар", "Введите цену товара:")
        count, ok5 = QInputDialog.getInt(self, "Добавить товар", "Введите количество товара:")
        discount, ok6 = QInputDialog.getDouble(self, "Добавить товар", "Введите скидку на товар:")
        category_id, ok7 = QInputDialog.getInt(self, "Добавить товар", "Введите ID категории товара:")

        if ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7:
            query = """
            INSERT INTO product (name, description, manufactur, price, count, discount, category_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            self.db.cursor.execute(query, (name, description, manufactur, price, count, discount, category_id))
            self.db.connection.commit()
            QMessageBox.information(self, "Успех", "Товар успешно добавлен")
            self.show_products()

    def edit_product(self):
        # Ввод ID товара для редактирования
        product_id, ok = QInputDialog.getInt(self, "Редактировать товар", "Введите ID товара:")
        if ok:
            query = "SELECT * FROM product WHERE id = %s"
            self.db.cursor.execute(query, (product_id,))
            product = self.db.cursor.fetchone()

            if product:
                # Установка значений по умолчанию, если они None
                price_default = product[4] if product[4] is not None else 0.0
                count_default = product[5] if product[5] is not None else 0
                discount_default = product[6] if product[6] is not None else 0.0
                category_id_default = product[7] if product[7] is not None else 0

                # Ввод новых данных для товара
                name, ok1 = QInputDialog.getText(self, "Редактировать товар", "Введите новое название товара:",
                                                 text=product[1])
                description, ok2 = QInputDialog.getText(self, "Редактировать товар", "Введите новое описание товара:",
                                                        text=product[2])
                manufactur, ok3 = QInputDialog.getText(self, "Редактировать товар",
                                                       "Введите нового производителя товара:", text=product[3])
                price, ok4 = QInputDialog.getDouble(self, "Редактировать товар", "Введите новую цену товара:",
                                                    value=price_default)
                count, ok5 = QInputDialog.getInt(self, "Редактировать товар", "Введите новое количество товара:",
                                                 value=count_default)
                discount, ok6 = QInputDialog.getDouble(self, "Редактировать товар", "Введите новую скидку на товар:",
                                                       value=discount_default)
                category_id, ok7 = QInputDialog.getInt(self, "Редактировать товар",
                                                       "Введите новый ID категории товара:", value=category_id_default)

                if ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7:
                    query = """
                    UPDATE product 
                    SET name = %s, description = %s, manufactur = %s, price = %s, count = %s, discount = %s, category_id = %s 
                    WHERE id = %s
                    """
                    self.db.cursor.execute(query, (
                    name, description, manufactur, price, count, discount, category_id, product_id))
                    self.db.connection.commit()
                    QMessageBox.information(self, "Успех", "Товар успешно обновлен")
                    self.show_products()
            else:
                QMessageBox.warning(self, "Ошибка", "Товар не найден")

    def delete_product(self):
        # Ввод ID товара для удаления
        product_id, ok = QInputDialog.getInt(self, "Удалить товар", "Введите ID товара:")
        if ok:
            query = "DELETE FROM product WHERE id = %s"
            self.db.cursor.execute(query, (product_id,))
            self.db.connection.commit()
            QMessageBox.information(self, "Успех", "Товар успешно удален")
            self.show_products()

    def show_orders(self):
        query = """
        SELECT 
            o.id,
            o.orderdate, 
            o.ordernumber, 
            o.totalamount, 
            o.discountamount, 
            o.orderstatus, 
            p.adress as pickup_address, 
            o.pickup_code, 
            o.id_order_details 
        FROM 
            orders o
        JOIN 
            pickuppoint p ON o.pickup_id = p.id
        """

        self.db.cursor.execute(query)
        orders = self.db.cursor.fetchall()

        column_names = ['id', 'Order Date', 'Order Number', 'Total Amount', 'Discount Amount', 'Order Status',
                        'Pickup Address', 'Pickup Code', 'Order Details']

        self.tableWidget.setRowCount(len(orders))
        self.tableWidget.setColumnCount(len(column_names))

        self.tableWidget.setHorizontalHeaderLabels(column_names)

        for row_index, row_data in enumerate(orders):
            for column_index, column_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))

    def edit_order(self):
        # Ввод ID заказа для редактирования
        order_id, ok = QInputDialog.getInt(self, "Редактировать заказ", "Введите ID заказа:")
        if ok:
            query = "SELECT * FROM orders WHERE id = %s"
            self.db.cursor.execute(query, (order_id,))
            order = self.db.cursor.fetchone()

            if order:
                # Преобразование даты в строку
                order_date_str = order[1].strftime("%Y-%m-%d") if isinstance(order[1], datetime) else order[1]
                # Преобразование номера заказа и деталей заказа в строку
                order_number_str = str(order[2])
                order_details_str = str(order[8])

                # Установка значений по умолчанию, если они None
                total_amount_default = order[3] if order[3] is not None else 0.0
                discount_amount_default = order[4] if order[4] is not None else 0.0

                # Ввод новых данных для заказа
                order_date, ok1 = QInputDialog.getText(self, "Редактировать заказ",
                                                       "Введите новую дату заказа (YYYY-MM-DD):", text=order_date_str)
                order_number, ok2 = QInputDialog.getText(self, "Редактировать заказ", "Введите новый номер заказа:",
                                                         text=order_number_str)
                total_amount, ok3 = QInputDialog.getDouble(self, "Редактировать заказ",
                                                           "Введите новую общую сумму заказа:",
                                                           value=total_amount_default)
                discount_amount, ok4 = QInputDialog.getDouble(self, "Редактировать заказ",
                                                              "Введите новую сумму скидки:",
                                                              value=discount_amount_default)
                order_status, ok5 = QInputDialog.getText(self, "Редактировать заказ", "Введите новый статус заказа:",
                                                         text=order[5])
                pickup_id, ok6 = QInputDialog.getInt(self, "Редактировать заказ", "Введите новый ID пункта выдачи:",
                                                     value=order[6])
                pickup_code, ok7 = QInputDialog.getText(self, "Редактировать заказ", "Введите новый код выдачи:",
                                                        text=order[7])
                order_details, ok8 = QInputDialog.getText(self, "Редактировать заказ", "Введите новые детали заказа:",
                                                          text=order_details_str)

                if ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7 and ok8:
                    query = """
                    UPDATE orders 
                    SET orderdate = %s, ordernumber = %s, totalamount = %s, discountamount = %s, orderstatus = %s, 
                        pickup_id = %s, pickup_code = %s, id_order_details = %s 
                    WHERE id = %s
                    """
                    self.db.cursor.execute(query, (
                        order_date, order_number, total_amount, discount_amount, order_status, pickup_id, pickup_code,
                        order_details, order_id))
                    self.db.connection.commit()
                    QMessageBox.information(self, "Успех", "Заказ успешно обновлен")
                    self.show_orders()
            else:
                QMessageBox.warning(self, "Ошибка", "Заказ не найден")

    def show_products(self):
        query = """
        SELECT 
            p.id, p.name, p.description, p.manufactur, p.price, p.count, p.discount, c.name as category_name
        FROM 
            product p
        JOIN 
            category c ON p.category_id = c.id
        """

        self.db.cursor.execute(query)
        products = self.db.cursor.fetchall()

        # Установим имена столбцов
        column_names = ['id','Name', 'Description', 'Manufacturer', 'Price', 'Count', 'Discount', 'Category']

        self.tableWidget.setRowCount(len(products))
        self.tableWidget.setColumnCount(len(column_names))

        # Установка заголовков колонок
        self.tableWidget.setHorizontalHeaderLabels(column_names)

        # Заполнение таблицы данными
        for row_index, row_data in enumerate(products):
            for column_index, column_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))

    def load_admin_auth(self):
        from Auth import AdminAuth
        self.close()
        self.admin_window = AdminAuth()
        self.admin_window.show()

    def load_manager_auth(self):
        from Auth import ManagerAuth
        self.close()
        self.manager_window = ManagerAuth()
        self.manager_window.show()

    def load_client_auth(self):
        from Auth import ClientAuth
        self.close()
        self.client_window = ClientAuth()
        self.client_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Admin()
    window.show()
    sys.exit(app.exec_())
----------------------------------------------------------------------------------------------------------

Auth.py:

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from database.database import Database
from UI_forms import *

class AdminAuth(QMainWindow):
    def __init__(self):
        super(AdminAuth, self).__init__()
        loadUi("../UI_forms/admin_auth.ui", self)
        self.db = Database(host='localhost', user='root', password='', database='book_club')
        self.action.triggered.connect(self.load_admin_auth)
        self.action_2.triggered.connect(self.load_manager_auth)
        self.action_3.triggered.connect(self.load_client_auth)
        self.pushButton.clicked.connect(self.auth_admin)

    def auth_admin(self):
        try:
            admin_login = self.lineEdit.text()
            admin_password = self.lineEdit_2.text()
            query = 'SELECT username, password FROM user WHERE username = %s AND password = %s AND id_role = 1'
            self.db.cursor.execute(query, (admin_login, admin_password))
            result = self.db.cursor.fetchone()
            if result:
                print("Успешный вход")
                from admin import Admin
                self.close()
                self.admin = Admin()
                self.admin.show()
            else:
                print("Неправильный пароль")
        except Exception as e:
            print(f"Ошибка {e}")

    def load_admin_auth(self):
        self.close()
        self.admin_window = AdminAuth()
        self.admin_window.show()

    def load_manager_auth(self):
        self.close()
        self.manager_window = ManagerAuth()
        self.manager_window.show()

    def load_client_auth(self):
        self.close()
        self.client_window = ClientAuth()
        self.client_window.show()

class ManagerAuth(QMainWindow):
    def __init__(self):
        super(ManagerAuth, self).__init__()
        loadUi("../UI_forms/manager_auth.ui", self)
        self.db = Database(host='localhost', user='root', password='', database='book_club')
        self.action.triggered.connect(self.load_admin_auth)
        self.action_2.triggered.connect(self.load_manager_auth)
        self.action_3.triggered.connect(self.load_client_auth)
        self.pushButton.clicked.connect(self.auth_manager)

    def auth_manager(self):
        try:
            manager_login = self.lineEdit.text()
            manager_password = self.lineEdit_2.text()
            query = 'SELECT username, password FROM user WHERE username = %s AND password = %s AND id_role = 2'
            self.db.cursor.execute(query, (manager_login, manager_password))
            result = self.db.cursor.fetchone()
            if result:
                print("Успешный вход")
                from manager import Manager
                self.close()
                self.manager_window = Manager()
                self.manager_window.show()
            else:
                print("Неправильный пароль")
        except Exception as e:
            print(f"Ошибка {e}")

    def load_admin_auth(self):
        self.close()
        self.admin_window = AdminAuth()
        self.admin_window.show()

    def load_manager_auth(self):
        self.close()
        self.manager_window = ManagerAuth()
        self.manager_window.show()

    def load_client_auth(self):
        self.close()
        self.client_window = ClientAuth()
        self.client_window.show()

class ClientAuth(QMainWindow):
    def __init__(self):
        super(ClientAuth, self).__init__()
        loadUi("../UI_forms/client_auth.ui", self)
        self.action.triggered.connect(self.load_admin_auth)
        self.action_2.triggered.connect(self.load_manager_auth)
        self.action_3.triggered.connect(self.load_client_auth)
        self.pushButton.clicked.connect(self.show_products)

    def show_products(self):
        self.close()
        from py.products import Products
        self.products_view = Products()
        self.products_view.show()

    def load_admin_auth(self):
        self.close()
        self.admin_window = AdminAuth()
        self.admin_window.show()

    def load_manager_auth(self):
        self.close()
        self.manager_window = ManagerAuth()
        self.manager_window.show()

    def load_client_auth(self):
        self.close()
        self.client_window = ClientAuth()
        self.client_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClientAuth()
    window.show()
    sys.exit(app.exec_())
-----------------------------------------------------------------------------------------------------------

basket.py:

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QCheckBox, QComboBox,  QMessageBox

from PyQt5.uic import loadUi
from database.database import Database
from datetime import datetime


class Basket(QMainWindow):
    def __init__(self):
        super(Basket, self).__init__()
        loadUi("../UI_forms/basket_view.ui", self)
        self.db = Database(host='localhost', user='root', password='', database='book_club')
        self.pushButton_3.clicked.connect(self.prev)
        self.pushButton_2.clicked.connect(self.remove_selected_items)
        self.pushButton.clicked.connect(self.place_order)
        self.checkboxes = []
        self.load_basket_items()
        self.update_total()
        self.load_pickup_addresses()



    def insert_order(self):
        print("123")



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
        user_id = 3

        pickup_id = self.comboBox.currentData()

        pickup_code = "random_code"
        query_total = "SELECT SUM(price) FROM orderdetails WHERE user_id = %s"
        self.db.cursor.execute(query_total, (user_id,))
        total_amount = self.db.cursor.fetchone()[0]
        if total_amount is None:
            total_amount = 0

        # Получаем все id из orderdetails для данного пользователя
        query_order_details_ids = "SELECT id FROM orderdetails WHERE user_id = %s"
        self.db.cursor.execute(query_order_details_ids, (user_id,))
        order_details_ids = self.db.cursor.fetchall()

        if not order_details_ids:
            QMessageBox.warning(self, "Ошибка", "Нет деталей заказа для данного пользователя")
            return

        query_order = """
        INSERT INTO orders (ordernumber, totalamount, pickup_id, pickup_code,id_order_details)
        VALUES (%s, %s, %s, %s, %s)
        """
        for order_detail_id in order_details_ids:
            order_number = self.get_next_order_number()
            self.db.cursor.execute(query_order, (order_number,total_amount,pickup_id,pickup_code,order_detail_id[0]))

        self.db.connection.commit()

        QMessageBox.information(self, "Успех", "Заказ успешно оформлен")
        # self.clear_basket()

    def get_next_order_number(self):
        query = "SELECT MAX(ordernumber) FROM orders"
        self.db.cursor.execute(query)
        result = self.db.cursor.fetchone()[0]
        if result is None:
            return 1
        else:
            return result + 1

    # def clear_basket(self):
    #     user_id = 3  # Здесь можно указать текущий user_id, если он известен
    #     query = "DELETE FROM orderdetails WHERE user_id = %s"
    #     self.db.cursor.execute(query, (user_id,))
    #     self.db.connection.commit()
    #     for checkbox, _, _ in self.checkboxes:
    #         self.verticalLayout.removeWidget(checkbox)
    #         checkbox.deleteLater()
    #     self.checkboxes.clear()
    #     self.update_total()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Basket()
    window.show()
    sys.exit(app.exec_())
-------------------------------------------------------------------------------------------

manager.py:

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QCheckBox, QComboBox,  QMessageBox,QTableWidgetItem,QInputDialog

from PyQt5.uic import loadUi
from database.database import Database
from datetime import datetime

class Manager(QMainWindow):
    def __init__(self):
        super(Manager, self).__init__()
        loadUi("../UI_forms/manager.ui", self)
        self.db = Database(host='localhost', user='root', password='', database='book_club')
        self.action.triggered.connect(self.load_admin_auth)
        self.action_2.triggered.connect(self.load_manager_auth)
        self.action_3.triggered.connect(self.load_client_auth)
        self.pushButton.clicked.connect(self.show_products)
        self.pushButton_4.clicked.connect(self.show_orders)
        self.pushButton_2.clicked.connect(self.create_order)
        self.pushButton_5.clicked.connect(self.edit_order)
        self.pushButton_3.clicked.connect(self.prev)

    def prev(self):
        self.close()
        from Auth import ManagerAuth
        self.manager_window = ManagerAuth()
        self.manager_window.show()

    def edit_order(self):
        # Ввод ID заказа для редактирования
        order_id, ok = QInputDialog.getInt(self, "Редактировать заказ", "Введите ID заказа:")
        if ok:
            query = "SELECT * FROM orders WHERE id = %s"
            self.db.cursor.execute(query, (order_id,))
            order = self.db.cursor.fetchone()

            if order:
                # Преобразование даты в строку
                order_date_str = order[1].strftime("%Y-%m-%d") if isinstance(order[1], datetime) else order[1]
                # Преобразование номера заказа и деталей заказа в строку
                order_number_str = str(order[2])
                order_details_str = str(order[8])

                # Установка значений по умолчанию, если они None
                total_amount_default = order[3] if order[3] is not None else 0.0
                discount_amount_default = order[4] if order[4] is not None else 0.0

                # Ввод новых данных для заказа
                order_date, ok1 = QInputDialog.getText(self, "Редактировать заказ",
                                                       "Введите новую дату заказа (YYYY-MM-DD):", text=order_date_str)
                order_number, ok2 = QInputDialog.getText(self, "Редактировать заказ", "Введите новый номер заказа:",
                                                         text=order_number_str)
                total_amount, ok3 = QInputDialog.getDouble(self, "Редактировать заказ",
                                                           "Введите новую общую сумму заказа:",
                                                           value=total_amount_default)
                discount_amount, ok4 = QInputDialog.getDouble(self, "Редактировать заказ",
                                                              "Введите новую сумму скидки:",
                                                              value=discount_amount_default)
                order_status, ok5 = QInputDialog.getText(self, "Редактировать заказ", "Введите новый статус заказа:",
                                                         text=order[5])
                pickup_id, ok6 = QInputDialog.getInt(self, "Редактировать заказ", "Введите новый ID пункта выдачи:",
                                                     value=order[6])
                pickup_code, ok7 = QInputDialog.getText(self, "Редактировать заказ", "Введите новый код выдачи:",
                                                        text=order[7])
                order_details, ok8 = QInputDialog.getText(self, "Редактировать заказ", "Введите новые детали заказа:",
                                                          text=order_details_str)

                if ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7 and ok8:
                    query = """
                    UPDATE orders 
                    SET orderdate = %s, ordernumber = %s, totalamount = %s, discountamount = %s, orderstatus = %s, 
                        pickup_id = %s, pickup_code = %s, id_order_details = %s 
                    WHERE id = %s
                    """
                    self.db.cursor.execute(query, (
                    order_date, order_number, total_amount, discount_amount, order_status, pickup_id, pickup_code,
                    order_details, order_id))
                    self.db.connection.commit()
                    QMessageBox.information(self, "Успех", "Заказ успешно обновлен")
                    self.show_orders()
            else:
                QMessageBox.warning(self, "Ошибка", "Заказ не найден")

    def create_order(self):
       try:
           # Ввод данных для нового заказа
           order_date, ok1 = QInputDialog.getText(self, "Создать заказ", "Введите дату заказа (YYYY-MM-DD):")
           order_number, ok2 = QInputDialog.getText(self, "Создать заказ", "Введите номер заказа:")
           total_amount, ok3 = QInputDialog.getDouble(self, "Создать заказ", "Введите общую сумму заказа:")
           discount_amount, ok4 = QInputDialog.getDouble(self, "Создать заказ", "Введите сумму скидки:")
           order_status, ok5 = QInputDialog.getText(self, "Создать заказ", "Введите статус заказа:")
           pickup_id, ok6 = QInputDialog.getInt(self, "Создать заказ", "Введите ID пункта выдачи:")
           pickup_code, ok7 = QInputDialog.getText(self, "Создать заказ", "Введите код выдачи:")
           order_details, ok8 = QInputDialog.getText(self, "Создать заказ", "Введите детали заказа:")

           if ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7 and ok8:
               query = """
                      INSERT INTO orders (orderdate, ordernumber, totalamount, discountamount, orderstatus, pickup_id, pickup_code, id_order_details)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                      """
               self.db.cursor.execute(query, (
                   order_date, order_number, total_amount, discount_amount, order_status, pickup_id, pickup_code,
                   order_details))
               self.db.connection.commit()
               QMessageBox.information(self, "Успех", "Заказ успешно создан")
               self.show_orders()
               print("Успещно")
       except:
           print("Ошибка доавления данных")

    def show_orders(self):
        query = """
        SELECT 
            o.id,
            o.orderdate, 
            o.ordernumber, 
            o.totalamount, 
            o.discountamount, 
            o.orderstatus, 
            p.adress as pickup_address, 
            o.pickup_code, 
            o.id_order_details 
        FROM 
            orders o
        JOIN 
            pickuppoint p ON o.pickup_id = p.id
        """

        self.db.cursor.execute(query)
        orders = self.db.cursor.fetchall()

        column_names = ['id','Order Date', 'Order Number', 'Total Amount', 'Discount Amount', 'Order Status',
                        'Pickup Address', 'Pickup Code', 'Order Details']

        self.tableWidget.setRowCount(len(orders))
        self.tableWidget.setColumnCount(len(column_names))

        self.tableWidget.setHorizontalHeaderLabels(column_names)

        for row_index, row_data in enumerate(orders):
            for column_index, column_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))

    def show_products(self):
        query = """
        SELECT 
            p.name, p.description, p.manufactur, p.price, p.count, p.discount, c.name as category_name
        FROM 
            product p
        JOIN 
            category c ON p.category_id = c.id
        """

        self.db.cursor.execute(query)
        products = self.db.cursor.fetchall()

        # Установим имена столбцов
        column_names = ['Name', 'Description', 'Manufacturer', 'Price', 'Count', 'Discount', 'Category']

        self.tableWidget.setRowCount(len(products))
        self.tableWidget.setColumnCount(len(column_names))

        # Установка заголовков колонок
        self.tableWidget.setHorizontalHeaderLabels(column_names)

        # Заполнение таблицы данными
        for row_index, row_data in enumerate(products):
            for column_index, column_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))

    def load_admin_auth(self):
        from Auth import AdminAuth
        self.close()
        self.admin_window = AdminAuth()
        self.admin_window.show()

    def load_manager_auth(self):
        from Auth import ManagerAuth
        self.close()
        self.manager_window = ManagerAuth()
        self.manager_window.show()

    def load_client_auth(self):
        from Auth import ClientAuth
        self.close()
        self.client_window = ClientAuth()
        self.client_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Manager()
    window.show()
    sys.exit(app.exec_())

-----------------------------------------------------------------------------------------------------------

products.py:

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QComboBox, QGridLayout, QMessageBox
from PyQt5.QtGui import QPixmap, QImage, QFont
from PyQt5.uic import loadUi
from database.database import Database

class Products(QMainWindow):
    def __init__(self):
        super(Products, self).__init__()
        loadUi("../UI_forms/products_view.ui", self)
        self.db = Database(host='localhost', user='root', password='', database='book_club')
        self.combobox_show()
        self.comboBox.currentIndexChanged.connect(self.combobox_view)
        self.update_total()
        self.pushButton.clicked.connect(self.show_basket)
        self.action.triggered.connect(self.load_admin_auth)
        self.action_2.triggered.connect(self.load_manager_auth)
        self.action_3.triggered.connect(self.load_client_auth)

    def load_admin_auth(self):
        from Auth import AdminAuth
        self.close()
        self.admin_window = AdminAuth()
        self.admin_window.show()

    def load_manager_auth(self):
        from Auth import ManagerAuth
        self.close()
        self.manager_window = ManagerAuth()
        self.manager_window.show()

    def load_client_auth(self):
        from Auth import ClientAuth
        self.close()
        self.client_window = ClientAuth()
        self.client_window.show()

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
