import sys
import pymysql
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

        self.button_login = QPushButton("Hyr", self)

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
            password="root",
            database="vsc"
        )
app = QApplication(sys.argv)
login_window = LoginWindow()
login_window.show()
sys.exit(app.exec_())
