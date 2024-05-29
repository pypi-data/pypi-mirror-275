# Admin
# import mysql.connector
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
#
# from config import db_config
# class Ui_admin(object):
#     def setupUi(self, admin):
#         admin.setObjectName("admin")
#         admin.resize(846, 880)
#         self.centralwidget = QtWidgets.QWidget(admin)
#         self.centralwidget.setObjectName("centralwidget")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(370, 680, 141, 31))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(370, 710, 141, 31))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_3.setGeometry(QtCore.QRect(370, 740, 141, 28))
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(0, 0, 841, 381))
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setColumnCount(0)
#         self.tableWidget.setRowCount(0)
#         self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit.setGeometry(QtCore.QRect(380, 440, 113, 22))
#         self.lineEdit.setObjectName("lineEdit")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(300, 440, 71, 20))
#         self.label.setObjectName("label")
#         self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_2.setGeometry(QtCore.QRect(380, 470, 113, 22))
#         self.lineEdit_2.setObjectName("lineEdit_2")
#         self.label_2 = QtWidgets.QLabel(self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(300, 470, 71, 20))
#         self.label_2.setObjectName("label_2")
#         self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_3.setGeometry(QtCore.QRect(380, 500, 113, 22))
#         self.lineEdit_3.setObjectName("lineEdit_3")
#         self.label_3 = QtWidgets.QLabel(self.centralwidget)
#         self.label_3.setGeometry(QtCore.QRect(280, 500, 91, 20))
#         self.label_3.setObjectName("label_3")
#         self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_4.setGeometry(QtCore.QRect(380, 530, 113, 22))
#         self.lineEdit_4.setObjectName("lineEdit_4")
#         self.label_4 = QtWidgets.QLabel(self.centralwidget)
#         self.label_4.setGeometry(QtCore.QRect(290, 530, 71, 20))
#         self.label_4.setObjectName("label_4")
#         self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_5.setGeometry(QtCore.QRect(380, 560, 113, 22))
#         self.lineEdit_5.setObjectName("lineEdit_5")
#         self.label_5 = QtWidgets.QLabel(self.centralwidget)
#         self.label_5.setGeometry(QtCore.QRect(320, 560, 41, 20))
#         self.label_5.setObjectName("label_5")
#         self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_4.setGeometry(QtCore.QRect(20, 790, 111, 28))
#         self.pushButton_4.setObjectName("pushButton_4")
#         admin.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(admin)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 26))
#         self.menubar.setObjectName("menubar")
#         admin.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(admin)
#         self.statusbar.setObjectName("statusbar")
#         admin.setStatusBar(self.statusbar)
#
#         self.retranslateUi(admin)
#         QtCore.QMetaObject.connectSlotsByName(admin)
#
#         self.pushButton.clicked.connect(self.add_goods)
#         self.pushButton_2.clicked.connect(self.edit_goods)
#         self.pushButton_3.clicked.connect(self.delete_goods)
#         self.pushButton_4.clicked.connect(self.logout)
#         self.load_items()
#
#     def retranslateUi(self, admin):
#         _translate = QtCore.QCoreApplication.translate
#         admin.setWindowTitle(_translate("admin", "ООО12"))
#         self.pushButton.setText(_translate("admin", "Добавить"))
#         self.pushButton_2.setText(_translate("admin", "Редактировать "))
#         self.pushButton_3.setText(_translate("admin", "Удалить "))
#         self.label.setText(_translate("admin", "Название"))
#         self.label_2.setText(_translate("admin", "Описание"))
#         self.label_3.setText(_translate("admin", "Производитель"))
#         self.label_4.setText(_translate("admin", "Количество"))
#         self.label_5.setText(_translate("admin", "Цена"))
#         self.pushButton_4.setText(_translate("admin", "Выйти"))
#
#
#
#     def load_items(self):
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             cursor.execute("SELECT id, name_goods, discription, manufacturer, quantities, price FROM goods")
#             items = cursor.fetchall()
#             self.tableWidget.setRowCount(len(items))
#             self.tableWidget.setColumnCount(6)
#             self.tableWidget.setHorizontalHeaderLabels(
#                 ["ID", "Название", "Описание", "Производитель", "Количество", "Цена"])
#
#             for i, item in enumerate(items):
#                 for j, value in enumerate(item):
#                     self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))
#         except mysql.connector.Error as err:
#             QMessageBox.critical(self.centralwidget, 'Database Error', f"Error: {err}")
#         finally:
#             if conn:
#                 conn.close()
#
#     def add_goods(self):
#         name = self.lineEdit.text()
#         description = self.lineEdit_2.text()
#         manufacturer = self.lineEdit_3.text()
#         quantities = self.lineEdit_4.text()
#         price = self.lineEdit_5.text()
#
#         if name and description and manufacturer and quantities and price:
#             try:
#                 conn = mysql.connector.connect(**db_config)
#                 cursor = conn.cursor()
#                 cursor.execute(
#                     "INSERT INTO goods (name_goods, discription, manufacturer, quantities, price) VALUES (%s, %s, %s, %s, %s)",
#                     (name, description, manufacturer, quantities, price))
#                 conn.commit()
#                 QMessageBox.information(self.centralwidget, 'Success', 'Отлично, данные добавлены!')
#                 self.load_items()  # Refresh the goods to show the new item
#             except mysql.connector.Error as err:
#                 QMessageBox.critical(self.centralwidget, 'Database Error', f"Error: {err}")
#             finally:
#                 if conn:
#                     conn.close()
#         else:
#             QMessageBox.warning(self.centralwidget, 'Error', 'Неверный ввод')
#
#     def delete_goods(self):
#         current_row = self.tableWidget.currentRow()
#         if current_row >= 0:
#             goods_id = int(self.tableWidget.item(current_row, 0).text())
#             reply = QMessageBox.question(self.centralwidget, 'Message', 'Вы точно хотите удалить это!',
#                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#
#             if reply == QMessageBox.Yes:
#                 try:
#                     conn = mysql.connector.connect(**db_config)
#                     cursor = conn.cursor()
#                     cursor.execute("DELETE FROM goods WHERE id = %s", (goods_id,))
#                     conn.commit()
#                     QMessageBox.information(self.centralwidget, 'Success', 'Отлично, данные удалены')
#                     self.load_items()  # Refresh the goods to show the remaining items
#                 except mysql.connector.Error as err:
#                     QMessageBox.critical(self.centralwidget, 'Database Error', f"Error: {err}")
#                 finally:
#                     if conn:
#                         conn.close()
#         else:
#             QMessageBox.warning(self.centralwidget, 'Error', 'Пожалуйста выберите элемент для удаления')
#
#     def edit_goods(self):
#         current_row = self.tableWidget.currentRow()
#         if current_row >= 0:
#             goods_id = int(self.tableWidget.item(current_row, 0).text())
#             name = self.lineEdit.text()
#             description = self.lineEdit_2.text()
#             manufacturer = self.lineEdit_3.text()
#             quantities = self.lineEdit_4.text()
#             price = self.lineEdit_5.text()
#
#             if name and description and manufacturer and quantities and price:
#                 try:
#                     conn = mysql.connector.connect(**db_config)
#                     cursor = conn.cursor()
#                     cursor.execute(
#                         "UPDATE goods SET name_goods = %s, discription = %s, manufacturer = %s, quantities = %s, price = %s WHERE id = %s",
#                         (name, description, manufacturer, quantities, price, goods_id))
#                     conn.commit()
#                     QMessageBox.information(self.centralwidget, 'Success', 'Отлично, данные изменены')
#                     self.load_items()  # Refresh the goods to show the updated item
#                 except mysql.connector.Error as err:
#                     QMessageBox.critical(self.centralwidget, 'Database Error', f"Error: {err}")
#                 finally:
#                     if conn:
#                         conn.close()
#             else:
#                 QMessageBox.warning(self.centralwidget, 'Error', 'Неверный ввод!')
#         else:
#             QMessageBox.warning(self.centralwidget, 'Error', 'Пожалуйста, выберите элемент для редактирования!')
#
#
#     def logout(self):
#         # Закрываем текущее окно
#         self.user.close()
#         # Здесь можно добавить дополнительные действия, такие как очистка данных сеанса
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     admin = QtWidgets.QMainWindow()
#     ui = Ui_admin()
#     ui.setupUi(admin)
#     admin.show()
#     sys.exit(app.exec_())

#Auto

# import subprocess
# import sys
# import mysql.connector
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, QMessageBox
# from PyQt5 import QtCore
#
# from config import db_config
#
#
# class Ui_user(object):
#     def setupUi(self, user):
#         user.setObjectName("user")
#         user.resize(416, 430)
#         self.centralwidget = QWidget(user)
#         self.centralwidget.setObjectName("centralwidget")
#
#         self.pushButton = QPushButton("Войти", self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(140, 280, 93, 28))
#         self.pushButton.setObjectName("pushButton")
#
#         self.pushButton_register = QPushButton("Регистрация", self.centralwidget)
#         self.pushButton_register.setGeometry(QtCore.QRect(140, 320, 93, 28))
#         self.pushButton_register.setObjectName("pushButton_register")
#
#         self.label = QLabel("Логин", self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(70, 140, 55, 16))
#         self.label.setObjectName("label")
#
#         self.label_2 = QLabel("Пароль", self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(70, 180, 55, 16))
#         self.label_2.setObjectName("label_2")
#
#         self.lineEdit = QLineEdit(self.centralwidget)
#         self.lineEdit.setGeometry(QtCore.QRect(120, 180, 113, 22))
#         self.lineEdit.setObjectName("lineEdit")
#         self.lineEdit.setEchoMode(QLineEdit.Password)  # Make the password field masked
#
#         self.lineEdit_2 = QLineEdit(self.centralwidget)
#         self.lineEdit_2.setGeometry(QtCore.QRect(120, 140, 113, 22))
#         self.lineEdit_2.setObjectName("lineEdit_2")
#
#         user.setCentralWidget(self.centralwidget)
#
#         self.retranslateUi(user)
#         QtCore.QMetaObject.connectSlotsByName(user)
#
#         self.pushButton.clicked.connect(self.check_login)
#         self.pushButton_register.clicked.connect(self.open_register_window)
#
#     def retranslateUi(self, user):
#         user.setWindowTitle("ООО\"Спорт\"")
#         self.pushButton.setText("Войти")
#         self.pushButton_register.setText("Регистрация")
#
#     def check_login(self):
#         user = self.lineEdit_2.text()
#         pwd = self.lineEdit.text()
#
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             cursor.execute("SELECT role FROM User WHERE login=%s AND password=%s", (user, pwd))
#             result = cursor.fetchone()
#
#             if result:
#                 role = result[0]
#                 if role == 'User':
#                     self.open_user_window()
#                 elif role == 'manager':
#                     self.open_manager_window()
#                 elif role == 'admin':
#                     self.open_admin_window()
#             else:
#                 QMessageBox.warning(self.user, 'Error', 'Неверный логин или пароль')
#
#         except mysql.connector.Error as err:
#             QMessageBox.critical(self.user, 'Database Error', f"Error: {err}")
#         finally:
#             cursor.close()
#             conn.close()
#
#     def open_user_window(self):
#         subprocess.Popen(["python", "user.py"])
#         self.user.close()
#
#     def open_manager_window(self):
#         subprocess.Popen(["python", "manager.py"])
#         self.user.close()
#
#     def open_admin_window(self):
#         subprocess.Popen(["python", "admin1.py"])
#         self.user.close()
#
#     def open_register_window(self):
#         self.register_window = RegisterWindow()
#         self.register_window.show()
#
#
# class RegisterWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setObjectName("register")
#         self.resize(416, 500)
#         self.centralwidget = QWidget(self)
#         self.centralwidget.setObjectName("centralwidget")
#
#         self.label_login = QLabel("Логин", self.centralwidget)
#         self.label_login.setGeometry(QtCore.QRect(70, 60, 55, 16))
#         self.label_login.setObjectName("label_login")
#
#         self.label_password = QLabel("Пароль", self.centralwidget)
#         self.label_password.setGeometry(QtCore.QRect(70, 100, 55, 16))
#         self.label_password.setObjectName("label_password")
#
#         self.label_name = QLabel("Имя", self.centralwidget)
#         self.label_name.setGeometry(QtCore.QRect(70, 140, 55, 16))
#         self.label_name.setObjectName("label_name")
#
#         self.label_surname = QLabel("Фамилия", self.centralwidget)
#         self.label_surname.setGeometry(QtCore.QRect(70, 180, 55, 16))
#         self.label_surname.setObjectName("label_surname")
#
#         self.label_phone = QLabel("Телефон", self.centralwidget)
#         self.label_phone.setGeometry(QtCore.QRect(70, 220, 55, 16))
#         self.label_phone.setObjectName("label_phone")
#
#         self.lineEdit_login = QLineEdit(self.centralwidget)
#         self.lineEdit_login.setGeometry(QtCore.QRect(140, 60, 113, 22))
#         self.lineEdit_login.setObjectName("lineEdit_login")
#
#         self.lineEdit_password = QLineEdit(self.centralwidget)
#         self.lineEdit_password.setGeometry(QtCore.QRect(140, 100, 113, 22))
#         self.lineEdit_password.setObjectName("lineEdit_password")
#         self.lineEdit_password.setEchoMode(QLineEdit.Password)  # Make the password field masked
#
#         self.lineEdit_name = QLineEdit(self.centralwidget)
#         self.lineEdit_name.setGeometry(QtCore.QRect(140, 140, 113, 22))
#         self.lineEdit_name.setObjectName("lineEdit_name")
#
#         self.lineEdit_surname = QLineEdit(self.centralwidget)
#         self.lineEdit_surname.setGeometry(QtCore.QRect(140, 180, 113, 22))
#         self.lineEdit_surname.setObjectName("lineEdit_surname")
#
#         self.lineEdit_phone = QLineEdit(self.centralwidget)
#         self.lineEdit_phone.setGeometry(QtCore.QRect(140, 220, 113, 22))
#         self.lineEdit_phone.setObjectName("lineEdit_phone")
#
#         self.pushButton_submit = QPushButton("Регистрация", self.centralwidget)
#         self.pushButton_submit.setGeometry(QtCore.QRect(140, 270, 93, 28))
#         self.pushButton_submit.setObjectName("pushButton_submit")
#
#         self.setCentralWidget(self.centralwidget)
#
#         self.retranslateUi()
#         QtCore.QMetaObject.connectSlotsByName(self)
#
#         self.pushButton_submit.clicked.connect(self.register_user)
#
#     def retranslateUi(self):
#         self.setWindowTitle("Регистрация")
#         self.pushButton_submit.setText("Регистрация")
#
#     def register_user(self):
#         login = self.lineEdit_login.text()
#         password = self.lineEdit_password.text()
#         name = self.lineEdit_name.text()
#         surname = self.lineEdit_surname.text()
#         phone = self.lineEdit_phone.text()
#         role = 'User'  # Default role for new users
#
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             cursor.execute(
#                 "INSERT INTO User (login, password, role, surname, name, phone) VALUES (%s, %s, %s, %s, %s, %s)",
#                 (login, password, role, surname, name, phone))
#             conn.commit()
#
#             QMessageBox.information(self, 'Success', 'Регистрация прошла успешно')
#             self.close()
#
#         except mysql.connector.Error as err:
#             QMessageBox.critical(self, 'Database Error', f"Error: {err}")
#         finally:
#             cursor.close()
#             conn.close()
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     user = QMainWindow()
#     ui = Ui_user()
#     ui.setupUi(user)
#     user.show()
#     sys.exit(app.exec_())

#CART

# import mysql.connector
# from datetime import date
# from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QLabel, QComboBox
# from PyQt5 import QtCore, QtGui, QtWidgets
# from config import db_config
#
#
# class Ui_cart(object):
#     def setupUi(self, cart):
#         cart.setObjectName("cart")
#         cart.resize(483, 383)
#         self.centralwidget = QtWidgets.QWidget(cart)
#         self.centralwidget.setObjectName("centralwidget")
#         self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(10, 0, 461, 221))
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setColumnCount(0)
#         self.tableWidget.setRowCount(0)
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(20, 280, 93, 28))
#         self.pushButton.setObjectName("pushButton")
#
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(140, 280, 141, 28))
#         self.pushButton_2.setObjectName("pushButton_2")
#
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(20, 240, 141, 16))
#         self.label.setObjectName("label")
#         self.comboBox = QtWidgets.QComboBox(self.centralwidget)
#         self.comboBox.setGeometry(QtCore.QRect(140, 240, 161, 22))
#         self.comboBox.setObjectName("comboBox")
#         cart.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(cart)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 483, 26))
#         self.menubar.setObjectName("menubar")
#         cart.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(cart)
#         self.statusbar.setObjectName("statusbar")
#         cart.setStatusBar(self.statusbar)
#
#         self.retranslateUi(cart)
#         QtCore.QMetaObject.connectSlotsByName(cart)
#
#         # Заполнение ComboBox адресами
#         self.fill_addresses()
#
#         # Подключение обработчика к кнопке "Создать заказ"
#         self.pushButton_2.clicked.connect(self.create_order)
#
#         # Подключение обработчика к кнопке "Назад"
#         self.pushButton.clicked.connect(cart.close)
#
#         self.load_items()
#
#     def retranslateUi(self, cart):
#         _translate = QtCore.QCoreApplication.translate
#         cart.setWindowTitle(_translate("cart", "MainWindow"))
#         self.pushButton.setText(_translate("cart", "Назад"))
#         self.pushButton_2.setText(_translate("cart", "Создать заказ"))
#         self.label.setText(_translate("cart", "Выберите адрес"))
#
#     def fill_addresses(self):
#         try:
#             # Подключение к базе данных и извлечение адресов
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             cursor.execute("SELECT id, CONCAT(street, ', ', city, ', ', state) AS address FROM Addresses")
#             addresses = cursor.fetchall()
#             conn.close()
#
#             # Добавление адресов в ComboBox
#             for address in addresses:
#                 self.comboBox.addItem(address[1], address[0])  # Добавление текста и ID адреса
#
#         except mysql.connector.Error as err:
#             QMessageBox.critical(None, 'Database Error', f"Error: {err}")
#
#     def create_order(self):
#         try:
#             # Подключение к базе данных
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#
#             # Получение выбранного адреса ID
#             address_id = self.comboBox.currentData()
#
#             # Получение данных из таблицы корзины
#             cursor.execute("SELECT user_id, goods_id, SUM(quantity) FROM cart GROUP BY goods_id")
#             cart_items = cursor.fetchall()
#
#             if not cart_items:
#                 QMessageBox.warning(None, 'Внимание', 'Корзина пуста.')
#                 conn.close()
#                 return
#
#             # Создание заказа в таблице orders
#             today = date.today()
#             for item in cart_items:
#                 user_id, goods_id, total_quantity = item
#                 cursor.execute("INSERT INTO orders (id_user, id_goods, quantities, data, id_address, status, cod) "
#                                "VALUES (%s, %s, %s, %s, %s, 'В обработке', '123456')",
#                                (user_id, goods_id, total_quantity, today, address_id))
#
#             # Очистка таблицы cart
#             cursor.execute("DELETE FROM cart")
#             conn.commit()
#             conn.close()
#
#             # Обновление отображения таблицы cart
#             self.tableWidget.setRowCount(0)
#             QMessageBox.information(None, 'Успех', 'Заказ успешно создан и корзина очищена.')
#
#         except mysql.connector.Error as err:
#             QMessageBox.critical(None, 'Database Error', f"Error: {err}")
#         finally:
#             if conn.is_connected():
#                 conn.close()
#
#     def load_items(self):
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             cursor.execute("SELECT id, user_id, goods_id, quantity FROM cart")
#             items = cursor.fetchall()
#             self.tableWidget.setRowCount(len(items))
#             self.tableWidget.setColumnCount(4)
#             self.tableWidget.setHorizontalHeaderLabels(["ID", "ID-пользователя", "ID-Товара", "Количество"])
#
#             for i, item in enumerate(items):
#                 for j, value in enumerate(item):
#                     self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))
#         except mysql.connector.Error as err:
#             QMessageBox.critical(None, 'Database Error', f"Error: {err}")
#         finally:
#             if conn.is_connected():
#                 conn.close()
#
#
# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     cart = QtWidgets.QMainWindow()
#     ui = Ui_cart()
#     ui.setupUi(cart)
#     cart.show()
#     sys.exit(app.exec_())

#CONFIG

# db_config = {
#     'user': 'root',
#     'password': '',
#     'host': '127.0.0.1',
#     'database': 'Shop_2',
#     'raise_on_warnings': True
# }

#MANAGER

# import sys
# import mysql.connector
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox, QTableWidgetItem
# from PyQt5 import QtWidgets, QtCore
# from config import db_config
#
# class Ui_manager2(object):
#     def setupUi(self, manager2):
#         manager2.setObjectName("manager2")
#         manager2.resize(739, 655)
#         self.centralwidget = QtWidgets.QWidget(manager2)
#         self.centralwidget.setObjectName("centralwidget")
#         self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(0, 0, 721, 341))
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setColumnCount(0)
#         self.tableWidget.setRowCount(0)
#         self.comboBox = QtWidgets.QComboBox(self.centralwidget)
#         self.comboBox.setGeometry(QtCore.QRect(50, 370, 111, 22))
#         self.comboBox.setObjectName("comboBox")
#         self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
#         self.comboBox_2.setGeometry(QtCore.QRect(50, 400, 111, 22))
#         self.comboBox_2.setObjectName("comboBox_2")
#         self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
#         self.dateEdit.setGeometry(QtCore.QRect(50, 440, 110, 22))
#         self.dateEdit.setObjectName("dateEdit")
#         self.lineEdit_cod = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_cod.setGeometry(QtCore.QRect(50, 480, 113, 22))
#         self.lineEdit_cod.setObjectName("lineEdit_cod")
#         self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
#         self.comboBox_3.setGeometry(QtCore.QRect(50, 520, 111, 22))
#         self.comboBox_3.setObjectName("comboBox_3")
#         self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
#         self.comboBox_4.setGeometry(QtCore.QRect(50, 590, 111, 22))
#         self.comboBox_4.setObjectName("comboBox_4")
#         self.comboBox_4.addItems(["создан", "отклонен", "отправлен"])
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(550, 480, 121, 28))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton.clicked.connect(self.create_order)
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(550, 520, 121, 28))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.pushButton_2.clicked.connect(self.update_order)
#         self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_3.setGeometry(QtCore.QRect(550, 560, 121, 28))
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.pushButton_3.clicked.connect(self.delete_order)
#         self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_4.setGeometry(QtCore.QRect(550, 600, 121, 28))
#         self.pushButton_4.setObjectName("pushButton_4")
#         self.pushButton_4.setText("Выйти")
#         self.pushButton_4.clicked.connect(manager2.close)
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(170, 370, 141, 16))
#         self.label.setObjectName("label")
#         self.label_2 = QtWidgets.QLabel(self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(170, 400, 111, 16))
#         self.label_2.setObjectName("label_2")
#         self.label_3 = QtWidgets.QLabel(self.centralwidget)
#         self.label_3.setGeometry(QtCore.QRect(170, 440, 141, 16))
#         self.label_3.setObjectName("label_3")
#         self.label_4 = QtWidgets.QLabel(self.centralwidget)
#         self.label_4.setGeometry(QtCore.QRect(170, 480, 101, 16))
#         self.label_4.setObjectName("label_4")
#         self.label_5 = QtWidgets.QLabel(self.centralwidget)
#         self.label_5.setGeometry(QtCore.QRect(180, 516, 121, 20))
#         self.label_5.setObjectName("label_5")
#         self.label_6 = QtWidgets.QLabel(self.centralwidget)
#         self.label_6.setGeometry(QtCore.QRect(180, 590, 121, 16))
#         self.label_6.setObjectName("label_6")
#         self.lineEdit_quantities = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_quantities.setGeometry(QtCore.QRect(50, 560, 113, 20))
#         self.lineEdit_quantities.setObjectName("lineEdit_quantities")
#         self.label_7 = QtWidgets.QLabel(self.centralwidget)
#         self.label_7.setGeometry(QtCore.QRect(180, 560, 111, 16))
#         self.label_7.setObjectName("label_7")
#         manager2.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(manager2)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 21))
#         self.menubar.setObjectName("menubar")
#         manager2.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(manager2)
#         self.statusbar.setObjectName("statusbar")
#         manager2.setStatusBar(self.statusbar)
#
#         self.populate_combobox_from_table("User", self.comboBox, "id")
#         self.populate_combobox_from_table("Goods", self.comboBox_2, "id")
#         self.populate_combobox_from_table("Addresses", self.comboBox_3, "id")
#         self.retranslateUi(manager2)
#         QtCore.QMetaObject.connectSlotsByName(manager2)
#
#         self.load_items()
#
#     def retranslateUi(self, manager2):
#         _translate = QtCore.QCoreApplication.translate
#         manager2.setWindowTitle(_translate("manager2", "ООО\"Спорт\""))
#         self.pushButton.setText(_translate("manager2", "Сформировать"))
#         self.pushButton_2.setText(_translate("manager2", "Редактировать"))
#         self.pushButton_3.setText(_translate("manager2", "Удалить"))
#         self.label.setText(_translate("manager2", "ID Пользователя"))
#         self.label_2.setText(_translate("manager2", "ID Товара"))
#         self.label_3.setText(_translate("manager2", "Дата оформления"))
#         self.label_4.setText(_translate("manager2", "Код заказа"))
#         self.label_5.setText(_translate("manager2", "ID Адреса"))
#         self.label_6.setText(_translate("manager2", "Статус"))
#         self.label_7.setText(_translate("manager2", "Количество"))
#
#     def load_items(self):
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             cursor.execute("SELECT id, id_user, id_goods, quantities, data, id_address, status, cod FROM orders")
#             items = cursor.fetchall()
#             self.tableWidget.setRowCount(len(items))
#             self.tableWidget.setColumnCount(8)
#             self.tableWidget.setHorizontalHeaderLabels(
#                 ["ID", "ID пользователя", "ID товаров", "количество", "Дата оформления", "ID адреса", "Код заказа", "Статус"])
#
#             for i, item in enumerate(items):
#                 for j, value in enumerate(item):
#                     self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
#         except mysql.connector.Error as err:
#             QMessageBox.critical(self.centralwidget, 'Ошибка базы данных', f"Ошибка: {err}")
#         finally:
#             if conn:
#                 conn.close()
#
#     def populate_combobox_from_table(self, table_name, combobox, id_column):
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#
#             cursor.execute(f"SELECT {id_column} FROM {table_name}")
#             ids = cursor.fetchall()
#             combobox.addItems([str(id[0]) for id in ids])
#         except mysql.connector.Error as err:
#             QMessageBox.critical(self.centralwidget, 'Ошибка базы данных', f"Ошибка: {err}")
#         finally:
#             if conn:
#                 conn.close()
#
#     def create_order(self):
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#
#             # Fetching IDs from User, Goods, and Address tables
#             id_user = self.comboBox.currentText()
#             id_goods = self.comboBox_2.currentText()
#             id_address = self.comboBox_3.currentText()
#
#             # Getting other details from UI
#             cod = self.lineEdit_cod.text()
#             data = self.dateEdit.date().toString("yyyy-MM-dd")
#             quantities = self.lineEdit_quantities.text()
#             status = self.comboBox_4.currentText()
#
#             # Inserting a new record into the orders table
#             cursor.execute(
#                 "INSERT INTO orders (id_user, id_goods, quantities, data, id_address, cod, status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
#                 (id_user, id_goods, quantities, data, id_address, cod, status))
#             conn.commit()
#
#             # Updating the table
#             self.load_items()
#
#             QMessageBox.information(self.centralwidget, 'Успех', 'Заказ успешно создан.')
#         except mysql.connector.Error as err:
#             QMessageBox.critical(self.centralwidget, 'Ошибка базы данных', f"Ошибка: {err}")
#         finally:
#             if conn:
#                 conn.close()
#
#     def update_order(self):
#         selected_row = self.tableWidget.currentRow()
#         if selected_row == -1:
#             QMessageBox.warning(self.centralwidget, 'Предупреждение', 'Пожалуйста, выберите строку для редактирования.')
#             return
#
#         order_id = self.tableWidget.item(selected_row, 0).text()
#
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#
#             # Fetching IDs from User, Goods, and Address tables
#             id_user = self.comboBox.currentText()
#             id_goods = self.comboBox_2.currentText()
#             id_address = self.comboBox_3.currentText()
#
#             # Getting other details from UI
#             cod = self.lineEdit_cod.text()
#             data = self.dateEdit.date().toString("yyyy-MM-dd")
#             quantities = self.lineEdit_quantities.text()
#             status = self.comboBox_4.currentText()
#
#             # Updating the selected record in the orders table
#             cursor.execute(
#                 "UPDATE orders SET id_user=%s, id_goods=%s, quantities=%s, data=%s, id_address=%s, cod=%s, status=%s WHERE id=%s",
#                 (id_user, id_goods, quantities, data, id_address, cod, status, order_id))
#             conn.commit()
#
#             # Updating the table
#             self.load_items()
#
#             QMessageBox.information(self.centralwidget, 'Успех', 'Заказ успешно отредактирован.')
#         except mysql.connector.Error as err:
#             QMessageBox.critical(self.centralwidget, 'Ошибка базы данных', f"Ошибка: {err}")
#         finally:
#             if conn:
#                 conn.close()
#
#     def delete_order(self):
#         selected_row = self.tableWidget.currentRow()
#         if selected_row == -1:
#             QMessageBox.warning(self.centralwidget, 'Предупреждение', 'Пожалуйста, выберите строку для удаления.')
#             return
#
#         order_id = self.tableWidget.item(selected_row, 0).text()
#         confirmation = QMessageBox.question(self.centralwidget, 'Подтверждение',
#                                             'Вы уверены, что хотите удалить этот заказ?',
#                                             QMessageBox.Yes | QMessageBox.No)
#         if confirmation == QMessageBox.Yes:
#             try:
#                 conn = mysql.connector.connect(**db_config)
#                 cursor = conn.cursor()
#                 cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
#                 conn.commit()
#
#                 self.load_items()
#
#                 QMessageBox.information(self.centralwidget, 'Успех', 'Заказ успешно удален.')
#             except mysql.connector.Error as err:
#                 QMessageBox.critical(self.centralwidget, 'Ошибка базы данных', f"Ошибка: {err}")
#             finally:
#                 if conn:
#                     conn.close()
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     manager2 = QtWidgets.QMainWindow()
#     ui = Ui_manager2()
#     ui.setupUi(manager2)
#     manager2.show()
#     sys.exit(app.exec_())

#TEST

# import unittest
# from unittest.mock import patch
# from PyQt5 import QtWidgets
# from admin import Ui_admin2
#
# class TestAdminFunctionality(unittest.TestCase):
#     def test_add_goods(self):
#         # Создаем экземпляр приложения
#         app = QtWidgets.QApplication([])
#
#         # Создаем главное окно
#         admin_window = QtWidgets.QMainWindow()
#
#         # Создаем экземпляр класса Ui_admin2
#         ui = Ui_admin2()
#         ui.setupUi(admin_window)
#
#         # Настроим значения для нового товара
#         ui.lineEdit.setText("Новый товар")
#         ui.lineEdit_2.setText("Описание нового товара")
#         ui.lineEdit_3.setText("Производитель нового товара")
#         ui.lineEdit_4.setText("10")  # Количество
#         ui.lineEdit_5.setText("100")  # Цена
#
#         # Создаем мок-объект для метода load_items класса Ui_admin2
#         with patch.object(Ui_admin2, 'load_items') as mock_load_items:
#             # Запускаем метод добавления товара
#             ui.add_goods()
#
#             # Проверяем, был ли вызван метод load_items после добавления товара
#             self.assertTrue(mock_load_items.called)
#
# if __name__ == '__main__':
#     unittest.main()

#USER

# from PyQt5 import QtCore, QtGui, QtWidgets
# import mysql.connector
# from PyQt5.QtWidgets import QMessageBox
#
# from config import db_config  # Убедитесь, что у вас есть файл config.py с данными для подключения к базе данных
# from cart import Ui_cart  # Предполагается, что у вас есть файл cart.py с интерфейсом корзины
#
# class Ui_User(object):
#     def setupUi(self, User):
#         self.user = User
#         User.setObjectName("User")
#         User.resize(896, 525)
#         self.centralwidget = QtWidgets.QWidget(User)
#         self.centralwidget.setObjectName("centralwidget")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(480, 400, 141, 31))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(630, 400, 141, 31))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_3.setGeometry(QtCore.QRect(0, 400, 141, 28))
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(0, 0, 881, 381))
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setColumnCount(0)
#         self.tableWidget.setRowCount(0)
#         User.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(User)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 896, 26))
#         self.menubar.setObjectName("menubar")
#         User.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(User)
#         self.statusbar.setObjectName("statusbar")
#         User.setStatusBar(self.statusbar)
#
#         self.retranslateUi(User)
#         QtCore.QMetaObject.connectSlotsByName(User)
#
#         self.load_items()  # Загрузка товаров при открытии окна
#
#         # Подключаем обработчик к кнопке "Добавить в корзину"
#         self.pushButton.clicked.connect(self.add_to_cart)
#
#         # Подключаем обработчик к кнопке "Корзина"
#         self.pushButton_2.clicked.connect(self.open_cart)
#
#         # Подключаем обработчик к кнопке "Выйти"
#         self.pushButton_3.clicked.connect(self.logout)
#
#     def retranslateUi(self, User):
#         _translate = QtCore.QCoreApplication.translate
#         User.setWindowTitle(_translate("User", "ООО12"))
#         self.pushButton.setText(_translate("User", "Добавить в корзину "))
#         self.pushButton_2.setText(_translate("User", "Корзина"))
#         self.pushButton_3.setText(_translate("User", "Выйти"))
#
#     def load_items(self):
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             cursor.execute("SELECT id, name_goods, discription, manufacturer, quantities, price FROM goods")
#             items = cursor.fetchall()
#             self.tableWidget.setRowCount(len(items))
#             self.tableWidget.setColumnCount(6)
#             self.tableWidget.setHorizontalHeaderLabels(
#                 ["ID", "Название", "Описание", "Производитель", "Количество", "Цена"])
#
#             for i, item in enumerate(items):
#                 for j, value in enumerate(item):
#                     self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))
#         except mysql.connector.Error as err:
#             QMessageBox.critical(self.user, 'Database Error', f"Error: {err}")
#         finally:
#             if conn:
#                 conn.close()
#
#     def add_to_cart(self):
#         selected_row = self.tableWidget.currentRow()
#         if selected_row < 0:
#             QMessageBox.warning(self.user, 'Selection Error', 'Пожалуйста, выберите товар для добавления в корзину.')
#             return
#
#         # Получаем данные выбранного товара
#         item_id = int(self.tableWidget.item(selected_row, 0).text())
#         quantities = int(self.tableWidget.item(selected_row, 4).text())
#
#         if quantities <= 0:
#             QMessageBox.warning(self.user, 'Quantity Error', 'Выбранный товар закончился на складе.')
#             return
#
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#
#             # Уменьшаем количество товара в таблице goods
#             cursor.execute("UPDATE goods SET quantities = quantities - 1 WHERE id = %s", (item_id,))
#
#             # Проверяем, есть ли товар уже в корзине
#             cursor.execute("SELECT quantity FROM cart WHERE user_id = %s AND goods_id = %s", (self.user_id, item_id))
#             result = cursor.fetchone()
#             if result:
#                 cursor.execute("UPDATE cart SET quantity = quantity + 1 WHERE user_id = %s AND goods_id = %s", (self.user_id, item_id))
#             else:
#                 cursor.execute("INSERT INTO cart (user_id, goods_id, quantity) VALUES (%s, %s, %s)", (self.user_id, item_id, 1))
#
#             conn.commit()
#
#             # Обновляем отображаемые данные
#             self.load_items()
#
#             QMessageBox.information(self.user, 'Success', 'Товар добавлен в корзину.')
#         except mysql.connector.Error as err:
#             QMessageBox.critical(self.user, 'Database Error', f"Error: {err}")
#         finally:
#             if conn:
#                 conn.close()
#
#     def open_cart(self):
#         self.cart_window = QtWidgets.QMainWindow()
#         self.cart_ui = Ui_cart()
#         self.cart_ui.setupUi(self.cart_window)
#         self.cart_window.show()
#
#     def logout(self):
#         # Закрываем текущее окно
#         self.user.close()
#         # Здесь можно добавить дополнительные действия, такие как очистка данных сеанса
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     User = QtWidgets.QMainWindow()
#     ui = Ui_User()
#     ui.user_id = 3  # Установите ID пользователя для примера
#     ui.setupUi(User)
#     User.show()
#     sys.exit(app.exec_())

#SQL

# -- phpMyAdmin SQL Dump
# -- version 5.2.0
# -- https://www.phpmyadmin.net/
# --
# -- Хост: 127.0.0.1:3306
# -- Время создания: Май 28 2024 г., 21:18
# -- Версия сервера: 5.5.62-log
# -- Версия PHP: 7.2.34
#
# SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
# START TRANSACTION;
# SET time_zone = "+00:00";
#
#
# /*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
# /*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
# /*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
# /*!40101 SET NAMES utf8mb4 */;
#
# --
# -- База данных: `shop_2`
# --
#
# -- --------------------------------------------------------
#
# --
# -- Структура таблицы `Addresses`
# --
#
# CREATE TABLE `Addresses` (
#   `id` int(11) NOT NULL,
#   `street` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `city` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `state` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
#
# --
# -- Дамп данных таблицы `Addresses`
# --
#
# INSERT INTO `Addresses` (`id`, `street`, `city`, `state`) VALUES
# (1, 'Пушкина ', 'Москва ', 'Россия'),
# (2, 'Ленина ', 'Москва ', 'Россия');
#
# -- --------------------------------------------------------
#
# --
# -- Структура таблицы `cart`
# --
#
# CREATE TABLE `cart` (
#   `id` int(11) NOT NULL,
#   `user_id` int(11) NOT NULL,
#   `goods_id` int(11) NOT NULL,
#   `quantity` int(11) NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
#
# -- --------------------------------------------------------
#
# --
# -- Структура таблицы `goods`
# --
#
# CREATE TABLE `goods` (
#   `id` int(11) NOT NULL,
#   `name_goods` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `discription` varchar(52) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `manufacturer` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `quantities` char(4) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `price` decimal(10,2) NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
#
# --
# -- Дамп данных таблицы `goods`
# --
#
# INSERT INTO `goods` (`id`, `name_goods`, `discription`, `manufacturer`, `quantities`, `price`) VALUES
# (2, 'к', 'к', 'к', '2', '2.00'),
# (5, 'Лыжи', 'НОрм', 'ПРО', '2', '500.00');
#
# -- --------------------------------------------------------
#
# --
# -- Структура таблицы `orders`
# --
#
# CREATE TABLE `orders` (
#   `id` int(11) NOT NULL,
#   `id_user` int(11) NOT NULL,
#   `id_goods` int(11) NOT NULL,
#   `quantities` int(11) NOT NULL,
#   `data` date NOT NULL,
#   `id_address` int(11) NOT NULL,
#   `status` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'В обработке',
#   `cod` char(6) COLLATE utf8mb4_unicode_ci NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
#
# --
# -- Дамп данных таблицы `orders`
# --
#
# INSERT INTO `orders` (`id`, `id_user`, `id_goods`, `quantities`, `data`, `id_address`, `status`, `cod`) VALUES
# (16, 2, 2, 2, '2023-11-21', 1, 'создан', '325'),
# (18, 2, 2, 2, '2023-11-21', 1, 'создан', '325');
#
# -- --------------------------------------------------------
#
# --
# -- Структура таблицы `User`
# --
#
# CREATE TABLE `User` (
#   `id` int(11) NOT NULL,
#   `login` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `password` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `role` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `surname` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `name` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `phone` char(11) COLLATE utf8mb4_unicode_ci NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
#
# --
# -- Дамп данных таблицы `User`
# --
#
# INSERT INTO `User` (`id`, `login`, `password`, `role`, `surname`, `name`, `phone`) VALUES
# (2, 'user1', 'pass1', 'User', 'Иванов', 'Иван', '89619555324'),
# (3, 'm1', 'm1', 'manager', 'Сидоров', 'Фёдор', '89619555324'),
# (4, 'ad1', 'ad2', 'admin', 'Печкин', 'Илья', '88005553535');
#
# --
# -- Индексы сохранённых таблиц
# --
#
# --
# -- Индексы таблицы `Addresses`
# --
# ALTER TABLE `Addresses`
#   ADD PRIMARY KEY (`id`);
#
# --
# -- Индексы таблицы `cart`
# --
# ALTER TABLE `cart`
#   ADD PRIMARY KEY (`id`),
#   ADD KEY `user_id` (`user_id`),
#   ADD KEY `goods_id` (`goods_id`);
#
# --
# -- Индексы таблицы `goods`
# --
# ALTER TABLE `goods`
#   ADD PRIMARY KEY (`id`);
#
# --
# -- Индексы таблицы `orders`
# --
# ALTER TABLE `orders`
#   ADD PRIMARY KEY (`id`),
#   ADD KEY `id_address` (`id_address`),
#   ADD KEY `id_goods` (`id_goods`),
#   ADD KEY `id_user` (`id_user`);
#
# --
# -- Индексы таблицы `User`
# --
# ALTER TABLE `User`
#   ADD PRIMARY KEY (`id`);
#
# --
# -- AUTO_INCREMENT для сохранённых таблиц
# --
#
# --
# -- AUTO_INCREMENT для таблицы `Addresses`
# --
# ALTER TABLE `Addresses`
#   MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
#
# --
# -- AUTO_INCREMENT для таблицы `cart`
# --
# ALTER TABLE `cart`
#   MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
#
# --
# -- AUTO_INCREMENT для таблицы `goods`
# --
# ALTER TABLE `goods`
#   MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
#
# --
# -- AUTO_INCREMENT для таблицы `orders`
# --
# ALTER TABLE `orders`
#   MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
#
# --
# -- AUTO_INCREMENT для таблицы `User`
# --
# ALTER TABLE `User`
#   MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
#
# --
# -- Ограничения внешнего ключа сохраненных таблиц
# --
#
# --
# -- Ограничения внешнего ключа таблицы `cart`
# --
# ALTER TABLE `cart`
#   ADD CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`id`),
#   ADD CONSTRAINT `cart_ibfk_2` FOREIGN KEY (`goods_id`) REFERENCES `goods` (`id`);
#
# --
# -- Ограничения внешнего ключа таблицы `orders`
# --
# ALTER TABLE `orders`
#   ADD CONSTRAINT `orders_ibfk_4` FOREIGN KEY (`id_address`) REFERENCES `Addresses` (`id`),
#   ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`id_goods`) REFERENCES `goods` (`id`),
#   ADD CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`id_user`) REFERENCES `User` (`id`);
# COMMIT;
#
# /*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
# /*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
# /*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;




