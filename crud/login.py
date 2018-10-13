import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import os
import hashlib
import sqlite3

class Login(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.setWindowTitle("Login")
    self.setWindowIcon(QIcon("preferences_system_login.png"))
    self.setFixedSize(200, 130)

    self.lbl_user = QLabel("Usuário:", self)
    self.lbl_user.move(10, 10)
    self.txt_user = QLineEdit(self)
    self.txt_user.move(70, 10)
    self.txt_user.resize(120, 25)
    self.txt_user.setMaxLength(10)

    self.lbl_pwd = QLabel("Senha:", self)
    self.lbl_pwd.move(10, 50)
    self.txt_pwd = QLineEdit(self)
    self.txt_pwd.move(70, 50)
    self.txt_pwd.resize(120, 25)
    self.txt_pwd.setMaxLength(16)
    self.txt_pwd.setEchoMode(QLineEdit.Password)
    self.txt_pwd.returnPressed.connect(self.login)

    self.btn_ok = QPushButton("Ok", self)
    self.btn_ok.move(105, 100)
    self.btn_ok.resize(65, 22)
    self.btn_ok.clicked.connect(self.login)

    self.btn_cancel = QPushButton("Cancelar", self)
    self.btn_cancel.move(35, 100)
    self.btn_cancel.resize(65, 22)
    self.btn_cancel.clicked.connect(self.close)

    self.center()
    self.show()

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

  def login(self):
    try:
      user = self.txt_user.text()
      pwd = self.txt_pwd.text()

      hash1 = hashlib.sha512(bin(int(pwd)).encode("utf-8")).hexdigest()

      if user != "" and user.isalnum() and pwd != "" and pwd.isdigit() and len(pwd) > 3 \
                    and not user.__contains__(" "):
        return check_data(user, hash1)
      elif user.__contains__(" "):
        QMessageBox.warning(self, "Error de usuário!", "Usuário não pode conter espaço!")
      elif not user.isalnum():
        QMessageBox.warning(self, "Error de usuário!", "Usuário não pode conter dígitos especiais!")
      elif len(pwd) <= 3 or len(pwd) > 16:
        QMessageBox.warning(self, "Error de senha!", "Senha deve conter no mínimo 4 e no máximo 16 dígitos!")
      elif not pwd.isdigit():
        QMessageBox.warning(self, "Error de senha!", "Senha deve conter apenas números!")
      else:
        QMessageBox.warning(self, "Error de Senha!", "Confirmação de senha incorreta!")
    except ValueError:
      QMessageBox.warning(self, "Error de senha!", "Senha deve conter apenas números!")

def check_data(user, hash1):
  try:
    conn = sqlite3.connect("login.db")
    conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data WHERE user = ? AND pwd = ?", (user, hash1))

    if cursor.fetchall():
      QMessageBox.information(win, "Informação!", "Login efetuado com sucesso!")
      win.close()
      return func()
    else:
      QMessageBox.warning(win, "Error de dados!", "Usuário e/ou senha incorreto(s)!")

    conn.close()
  except Exception as e:
    print(e)
    QMessageBox.warning(win, "Error de dados!", "Usuário e/ou senha incorreto(s)!")

def func():
  try:
    os.system('python menus.py')
  except Exception as e:
    print(e)
    QMessageBox.warning(win, "ERROR!", "Error na operação!")

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = Login()
  sys.exit(app.exec_())
