import sys
import pymysql
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class SignupWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Regjistrimi")
        self.setGeometry(100, 100, 300, 200)

        self.label_username = QLabel("Përdoruesi:", self)
        self.label_password = QLabel("Fjalëkalimi:", self)
        self.label_email = QLabel("Email:", self)
        self.lineedit_username = QLineEdit(self)
        self.lineedit_password = QLineEdit(self)
        self.lineedit_email = QLineEdit(self)
        self.lineedit_password.setEchoMode(QLineEdit.Password)

        self.button_signup = QPushButton("Regjistrohu", self)

        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.lineedit_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.lineedit_password)
        layout.addWidget(self.label_email)
        layout.addWidget(self.lineedit_email)
        layout.addWidget(self.button_signup)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="vsc"
        )
        
        def signup(self):
            username = self.lineedit_username.text()
            password = self.lineedit_password.text()
            email = self.lineedit_email.text()

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            cursor = self.db.cursor()
            try:
                sql = "INSERT INTO users (username, slatedHash, email) VALUES (%s, %s, %s)"
                values = (username, hashed_password, email)
                cursor.execute(sql, values)
            except:
                print("Username Already been taken. Please try another one!")
            self.db.commit()
            cursor.close()
            self.db.close()

app = QApplication(sys.argv)
signup_window = SignupWindow()
signup_window.show()
sys.exit(app.exec_())
