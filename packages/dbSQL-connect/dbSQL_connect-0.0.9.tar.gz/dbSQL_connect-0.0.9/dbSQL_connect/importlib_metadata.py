#ADMIN
# import mysql.connector
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
#
# from config import db_config
#
# class Ui_admin2(object):
#     def setupUi(self, admin2):
#         admin2.setObjectName("admin2")
#         admin2.resize(869, 850)
#         self.centralwidget = QtWidgets.QWidget(admin2)
#         self.centralwidget.setObjectName("centralwidget")
#         self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(0, 0, 861, 341))
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setColumnCount(0)
#         self.tableWidget.setRowCount(0)
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(150, 420, 55, 16))
#         self.label.setText("")
#         self.label.setObjectName("label")
#         self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit.setGeometry(QtCore.QRect(220, 420, 113, 22))
#         self.lineEdit.setObjectName("lineEdit")
#         self.label_2 = QtWidgets.QLabel(self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(134, 420, 71, 21))
#         self.label_2.setObjectName("label_2")
#         self.label_3 = QtWidgets.QLabel(self.centralwidget)
#         self.label_3.setGeometry(QtCore.QRect(150, 450, 55, 16))
#         self.label_3.setText("")
#         self.label_3.setObjectName("label_3")
#         self.label_4 = QtWidgets.QLabel(self.centralwidget)
#         self.label_4.setGeometry(QtCore.QRect(134, 450, 71, 21))
#         self.label_4.setObjectName("label_4")
#         self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_2.setGeometry(QtCore.QRect(220, 450, 113, 22))
#         self.lineEdit_2.setObjectName("lineEdit_2")
#         self.label_5 = QtWidgets.QLabel(self.centralwidget)
#         self.label_5.setGeometry(QtCore.QRect(150, 480, 55, 16))
#         self.label_5.setText("")
#         self.label_5.setObjectName("label_5")
#         self.label_6 = QtWidgets.QLabel(self.centralwidget)
#         self.label_6.setGeometry(QtCore.QRect(104, 480, 101, 21))
#         self.label_6.setObjectName("label_6")
#         self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_3.setGeometry(QtCore.QRect(220, 480, 113, 22))
#         self.lineEdit_3.setObjectName("lineEdit_3")
#         self.label_7 = QtWidgets.QLabel(self.centralwidget)
#         self.label_7.setGeometry(QtCore.QRect(150, 510, 55, 16))
#         self.label_7.setText("")
#         self.label_7.setObjectName("label_7")
#         self.label_8 = QtWidgets.QLabel(self.centralwidget)
#         self.label_8.setGeometry(QtCore.QRect(134, 510, 71, 21))
#         self.label_8.setObjectName("label_8")
#         self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_4.setGeometry(QtCore.QRect(220, 510, 113, 22))
#         self.lineEdit_4.setObjectName("lineEdit_4")
#         self.label_9 = QtWidgets.QLabel(self.centralwidget)
#         self.label_9.setGeometry(QtCore.QRect(150, 540, 55, 16))
#         self.label_9.setText("")
#         self.label_9.setObjectName("label_9")
#         self.label_10 = QtWidgets.QLabel(self.centralwidget)
#         self.label_10.setGeometry(QtCore.QRect(134, 540, 71, 21))
#         self.label_10.setObjectName("label_10")
#         self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_5.setGeometry(QtCore.QRect(220, 540, 113, 22))
#         self.lineEdit_5.setObjectName("lineEdit_5")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(202, 600, 111, 28))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton.clicked.connect(self.add_goods)
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(202, 640, 111, 28))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.pushButton_2.clicked.connect(self.edit_goods)
#         self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_3.setGeometry(QtCore.QRect(202, 680, 111, 28))
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.pushButton_3.clicked.connect(self.delete_goods)
#         admin2.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(admin2)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 26))
#         self.menubar.setObjectName("menubar")
#         admin2.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(admin2)
#         self.statusbar.setObjectName("statusbar")
#         admin2.setStatusBar(self.statusbar)
#
#         self.retranslateUi(admin2)
#         QtCore.QMetaObject.connectSlotsByName(admin2)
#
#         self.load_items()
#
#     def retranslateUi(self, admin2):
#         _translate = QtCore.QCoreApplication.translate
#         admin2.setWindowTitle(_translate("admin2", "ООО\"Спорт\""))
#         self.label_2.setText(_translate("admin2", "Название"))
#         self.label_4.setText(_translate("admin2", "Описание"))
#         self.label_6.setText(_translate("admin2", "Производитель"))
#         self.label_8.setText(_translate("admin2", "Количество"))
#         self.label_10.setText(_translate("admin2", "Цена"))
#         self.pushButton.setText(_translate("admin2", "Добавить"))
#         self.pushButton_2.setText(_translate("admin2", "Редактировать"))
#         self.pushButton_3.setText(_translate("admin2", "Удалить"))
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
#                 QMessageBox.information(self.centralwidget, 'Success', 'Goods added successfully!')
#                 self.load_items()  # Refresh the goods to show the new item
#             except mysql.connector.Error as err:
#                 QMessageBox.critical(self.centralwidget, 'Database Error', f"Error: {err}")
#             finally:
#                 if conn:
#                     conn.close()
#         else:
#             QMessageBox.warning(self.centralwidget, 'Error', 'Invalid input!')
#
#     def delete_goods(self):
#         current_row = self.tableWidget.currentRow()
#         if current_row >= 0:
#             goods_id = int(self.tableWidget.item(current_row, 0).text())
#             reply = QMessageBox.question(self.centralwidget, 'Message', 'Are you sure to delete?',
#                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#
#             if reply == QMessageBox.Yes:
#                 try:
#                     conn = mysql.connector.connect(**db_config)
#                     cursor = conn.cursor()
#                     cursor.execute("DELETE FROM goods WHERE id = %s", (goods_id,))
#                     conn.commit()
#                     QMessageBox.information(self.centralwidget, 'Success', 'Goods deleted successfully!')
#                     self.load_items()  # Refresh the goods to show the remaining items
#                 except mysql.connector.Error as err:
#                     QMessageBox.critical(self.centralwidget, 'Database Error', f"Error: {err}")
#                 finally:
#                     if conn:
#                         conn.close()
#         else:
#             QMessageBox.warning(self.centralwidget, 'Error', 'Please select an item to delete!')
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
#                     QMessageBox.information(self.centralwidget, 'Success', 'Goods updated successfully!')
#                     self.load_items()  # Refresh the goods to show the updated item
#                 except mysql.connector.Error as err:
#                     QMessageBox.critical(self.centralwidget, 'Database Error', f"Error: {err}")
#                 finally:
#                     if conn:
#                         conn.close()
#             else:
#                 QMessageBox.warning(self.centralwidget, 'Error', 'Invalid input!')
#         else:
#             QMessageBox.warning(self.centralwidget, 'Error', 'Please select an item to edit!')
#
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     admin2 = QtWidgets.QMainWindow()
#     ui = Ui_admin2()
#     ui.setupUi(admin2)
#     admin2.show()
#     sys.exit(app.exec_())

#Avto
# import subprocess
# import sys
# import mysql.connector
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, QMessageBox
# from PyQt5 import QtCore
#
# from config import db_config
#
# class Ui_user(object):
#     def setupUi(self, user):
#         user.setObjectName("user")
#         user.resize(416, 430)
#         self.centralwidget = QWidget(user)
#         self.centralwidget.setObjectName("centralwidget")
#         self.pushButton_2 = QPushButton("Войти без Авторизации", self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(100, 340, 171, 31))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.pushButton = QPushButton("Войти", self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(140, 280, 93, 28))
#         self.pushButton.setObjectName("pushButton")
#         self.label = QLabel("Логин", self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(70, 140, 55, 16))
#         self.label.setObjectName("label")
#         self.label_2 = QLabel("Пароль", self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(70, 180, 55, 16))
#         self.label_2.setObjectName("label_2")
#         self.lineEdit = QLineEdit(self.centralwidget)
#         self.lineEdit.setGeometry(QtCore.QRect(120, 180, 113, 22))
#         self.lineEdit.setObjectName("lineEdit")
#         self.lineEdit.setEchoMode(QLineEdit.Password)  # Make the password field masked
#         self.lineEdit_2 = QLineEdit(self.centralwidget)
#         self.lineEdit_2.setGeometry(QtCore.QRect(120, 140, 113, 22))
#         self.lineEdit_2.setObjectName("lineEdit_2")
#         user.setCentralWidget(self.centralwidget)
#
#         self.retranslateUi(user)
#         QtCore.QMetaObject.connectSlotsByName(user)
#
#         self.pushButton.clicked.connect(self.check_login)
#         self.pushButton_2.clicked.connect(self.open_user_window)
#
#     def retranslateUi(self, user):
#         user.setWindowTitle("ООО\"Спорт\"")
#         self.pushButton_2.setText("Войти без Авторизации")
#         self.pushButton.setText("Войти")
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
#
# from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QLabel, QComboBox
# from PyQt5 import QtCore, QtGui, QtWidgets
#
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
#         self.pushButton_2.setText(_translate("cart", "Создать заказ "))
#         self.label.setText(_translate("cart", "Выбирите адрес "))
#
#     def fill_addresses(self):
#         # Подключение к базе данных и извлечение адресов
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor()
#         cursor.execute("SELECT address FROM Address")
#         addresses = cursor.fetchall()
#         conn.close()
#
#         # Добавление адресов в ComboBox
#         for address in addresses:
#             self.comboBox.addItem(address[0])
#
#     def create_order(self):
#         # Подключение к базе данных
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor()
#
#         # Получение выбранного адреса
#         address = self.comboBox.currentText()
#
#         cursor.execute("SELECT id FROM Address WHERE address = %s", (address,))
#         address_id = cursor.fetchone()[0]
#
#         # Получение данных из таблицы корзины
#         cursor.execute("SELECT user_id, goods_id, SUM(quantity) FROM cart GROUP BY goods_id")
#         cart_items = cursor.fetchall()
#
#         if not cart_items:
#             print("Корзина пуста")
#             conn.close()
#             return
#
#         # Создание заказа в таблице orders
#         today = date.today()
#         for item in cart_items:
#             user_id, goods_id, total_quantity = item
#             cursor.execute("INSERT INTO orders (id_user, id_goods, quantities, data, id_address, status, cod) "
#                            "VALUES (%s, %s, %s, %s, %s, 'В обработке', '123456')",
#                            (user_id, goods_id, total_quantity, today, address_id))
#
#         # Очистка таблицы cart
#         cursor.execute("DELETE FROM cart")
#         conn.commit()
#         conn.close()
#
#         # Обновление отображения таблицы cart
#         self.tableWidget.setRowCount(0)
#         print("Заказ успешно создан и корзина очищена")
#
#     def load_items(self):
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             cursor.execute("SELECT id, user_id, goods_id, quantity FROM cart")  # Исправлено на "cart"
#             items = cursor.fetchall()
#             self.tableWidget.setRowCount(len(items))
#             self.tableWidget.setColumnCount(4)  # Изменил на количество колонок в запросе
#             self.tableWidget.setHorizontalHeaderLabels(["ID", "ID-пользователя", "ID-Товара", "Количество"])
#
#             for i, item in enumerate(items):
#                 for j, value in enumerate(item):
#                     self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))
#         except mysql.connector.Error as err:
#             QMessageBox.critical(None, 'Database Error', f"Error: {err}")  # Исправлено
#         finally:
#             if conn:
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

#COnfig
# db_config = {
#     'user': 'root',
#     'password': '',
#     'host': '127.0.0.1',
#     'database': 'Shop_2',
#     'raise_on_warnings': True
# }

#Manager
# import sys
# import mysql.connector
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox, QTableWidgetItem
# from PyQt5 import QtWidgets, QtCore
#
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
#         self.lineEdit_cod = QtWidgets.QLineEdit(self.centralwidget)  # Swapped position
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
#         self.lineEdit_quantities = QtWidgets.QLineEdit(self.centralwidget)  # Swapped position
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
#         self.populate_combobox_from_table("Address", self.comboBox_3, "id")
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
#             cursor.execute("SELECT id, id_user, id_goods, quantities, data, id_address, cod, status FROM orders")
#             items = cursor.fetchall()
#             self.tableWidget.setRowCount(len(items))
#             self.tableWidget.setColumnCount(8)
#             self.tableWidget.setHorizontalHeaderLabels(
#                 ["ID", "ID пользователя", "ID товаров", "количество", "Дата оформления", "ID адреса", "Код заказа", "Статус"])
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
#     def populate_combobox_from_table(self, table_name, combobox, id_column):
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#
#             cursor.execute(f"SELECT {id_column} FROM {table_name}")
#             ids = cursor.fetchall()
#             combobox.addItems([str(id[0]) for id in ids])
#         except mysql.connector.Error as err:
#             QMessageBox.critical(self.centralwidget, 'Database Error', f"Error: {err}")
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
#             cod = self.lineEdit_cod.text()  # Swapped position
#             data = self.dateEdit.date().toString("yyyy-MM-dd")
#             quantities = self.lineEdit_quantities.text()  # Swapped position
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
#             QMessageBox.information(self.centralwidget, 'Success', 'Заказ успешно создан.')
#         except mysql.connector.Error as err:
#             QMessageBox.critical(self.centralwidget, 'Database Error', f"Error: {err}")
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
#             cod = self.lineEdit_cod.text()  # Swapped position
#             data = self.dateEdit.date().toString("yyyy-MM-dd")
#             quantities = self.lineEdit_quantities.text()  # Swapped position
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
#             QMessageBox.information(self.centralwidget, 'Success', 'Заказ успешно отредактирован.')
#         except mysql.connector.Error as err:
#             QMessageBox.critical(self.centralwidget, 'Database Error', f"Error: {err}")
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

#User
# from PyQt5 import QtCore, QtGui, QtWidgets
# import mysql.connector
# from PyQt5.QtWidgets import QMessageBox
#
# from config import db_config  # Убедитесь, что у вас есть файл config.py с данными для подключения к базе данных
# from cart import Ui_cart  # Предполагается, что у вас есть файл cart.py с интерфейсом корзины
#
# class Ui_user(object):
#     def __init__(self, user_id):
#         self.user_id = user_id
#
#     def setupUi(self, user):
#         self.user = user
#         user.setObjectName("user")
#         user.resize(808, 548)
#         self.centralwidget = QtWidgets.QWidget(user)
#         self.centralwidget.setObjectName("centralwidget")
#         self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(0, 0, 801, 311))
#         self.tableWidget.setObjectName("tableWidget")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(600, 440, 121, 31))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(10, 440, 131, 31))
#         self.pushButton_2.setObjectName("pushButton_2")
#         user.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(user)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 26))
#         self.menubar.setObjectName("menubar")
#         user.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(user)
#         self.statusbar.setObjectName("statusbar")
#         user.setStatusBar(self.statusbar)
#
#         self.retranslateUi(user)
#         QtCore.QMetaObject.connectSlotsByName(user)
#
#         self.load_items()  # Загрузка товаров при открытии окна
#
#         # Подключаем обработчик к кнопке "Добавить в корзину"
#         self.pushButton_2.clicked.connect(self.add_to_cart)
#
#         # Подключаем обработчик к кнопке "Корзина"
#         self.pushButton.clicked.connect(self.open_cart)
#
#     def retranslateUi(self, user):
#         _translate = QtCore.QCoreApplication.translate
#         user.setWindowTitle(_translate("user", "ООО\"Спорт\""))
#         self.pushButton.setText(_translate("user", "Корзина"))
#         self.pushButton_2.setText(_translate("user", "Добавить в корзину"))
#
#     def load_items(self):
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             cursor.execute("SELECT id, name_goods, discription, manufacturer, quantities, price FROM goods")
#             items = cursor.fetchall()
#             self.tableWidget.setRowCount(len(items))
#             self.tableWidget.setColumnCount(6)
#             self.tableWidget.setHorizontalHeaderLabels(["ID", "Название", "Описание", "Производитель", "Количество", "Цена"])
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
#             # Добавляем товар в таблицу cart
#             cursor.execute(
#                 "INSERT INTO cart (user_id, goods_id, quantity) VALUES (%s, %s, %s)",
#                 (self.user_id, item_id, 1)
#             )
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
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     user = QtWidgets.QMainWindow()
#     user_id = 2  # Укажите реальный идентификатор пользователя
#     ui = Ui_user(user_id)
#     ui.setupUi(user)
#     user.show()
#     sys.exit(app.exec_())

#SQL
#-- phpMyAdmin SQL Dump
# -- version 5.2.0
# -- https://www.phpmyadmin.net/
# --
# -- Хост: 127.0.0.1:3306
# -- Время создания: Май 27 2024 г., 19:35
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
# -- Структура таблицы `Address`
# --
#
# CREATE TABLE `Address` (
#   `id` int(11) NOT NULL,
#   `address` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
#
# --
# -- Дамп данных таблицы `Address`
# --
#
# INSERT INTO `Address` (`id`, `address`) VALUES
# (1, 'Ул. Пушки дом. Колотушкина ');
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
# (2, 'Лыжи ночные', 'горные лыжи ', 'Stels', '21', '10000.00'),
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
# (1, 3, 5, 2, '2024-05-14', 1, 'в обработке', '123456'),
# (2, 3, 2, 356, '2000-01-01', 1, 'создан', '356'),
# (14, 2, 2, 1, '2024-05-27', 1, 'В обработке', '123456'),
# (15, 2, 2, 3, '2000-01-01', 1, 'отклонен', '');
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
# -- Индексы таблицы `Address`
# --
# ALTER TABLE `Address`
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
# -- AUTO_INCREMENT для таблицы `Address`
# --
# ALTER TABLE `Address`
#   MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
#
# --
# -- AUTO_INCREMENT для таблицы `cart`
# --
# ALTER TABLE `cart`
#   MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
#
# --
# -- AUTO_INCREMENT для таблицы `goods`
# --
# ALTER TABLE `goods`
#   MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
#
# --
# -- AUTO_INCREMENT для таблицы `orders`
# --
# ALTER TABLE `orders`
#   MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
#
# --
# -- AUTO_INCREMENT для таблицы `User`
# --
# ALTER TABLE `User`
#   MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
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
#   ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`id_address`) REFERENCES `Address` (`id`),
#   ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`id_goods`) REFERENCES `goods` (`id`),
#   ADD CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`id_user`) REFERENCES `User` (`id`);
# COMMIT;
#
# /*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
# /*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
# /*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
