import sys
import pymysql
import bcrypt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_successful = False
        self.setWindowTitle("Autentifikimi")
        self.setGeometry(100, 100, 300, 200)

        self.label_username = QLabel("Username:", self)
        self.label_password = QLabel("Password:", self)
        self.lineedit_username = QLineEdit(self)
        self.lineedit_password = QLineEdit(self)
        self.lineedit_password.setEchoMode(QLineEdit.Password)

        self.button_login = QPushButton("Login", self)
        self.button_login.clicked.connect(self.login)
        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.lineedit_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.lineedit_password)
        layout.addWidget(self.button_login)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="vsc"
        )
    def login(self):
        username = self.lineedit_username.text()
        password = self.lineedit_password.text()
        cursor = self.db.cursor()
        sql = "SELECT saltedHash FROM users WHERE username = %s"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()
        if result:
            hashed_password = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                QMessageBox.information(self, "Sukses", "Welcome Back!")
            else:
                QMessageBox.warning(self, "Gabim", "Password or username wrong!")
            self.db.commit()
            
        cursor.close()
        self.db.close()
        
app = QApplication(sys.argv)
signup_window = LoginWindow()
signup_window.show()
sys.exit(app.exec_())





   
