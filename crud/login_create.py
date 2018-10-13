import hashlib
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
import sys
import os

class RegisterLogin(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    screen  = app.primaryScreen()
    size = screen.size()
    self.setWindowTitle("Cadastro de Login")
    self.setWindowIcon(QIcon("login(1).png"))
    self.setFixedSize(270, 190)
    #self.setGeometry(0, 0, 270, 190)
    #self.setGeometry(0, 0, size.width(), size.height())

    self.lbl_user = QLabel("Usuário:", self)
    self.lbl_user.move(67, 10)
    self.txt_user = QLineEdit(self)
    self.txt_user.move(130, 10)
    self.txt_user.resize(130, 25)
    self.txt_user.setMaxLength(10)

    self.lbl_pwd = QLabel("Senha:", self)
    self.lbl_pwd.move(75, 50)
    self.txt_pwd = QLineEdit(self)
    self.txt_pwd.move(130, 50)
    self.txt_pwd.resize(130, 25)
    self.txt_pwd.setMaxLength(16)
    self.txt_pwd.setEchoMode(QLineEdit.Password)

    self.lbl_pwd_confirm = QLabel("Confirmar senha:", self)
    self.lbl_pwd_confirm.move(10, 90)
    self.txt_pwd_confirm = QLineEdit(self)
    self.txt_pwd_confirm.move(130, 90)
    self.txt_pwd_confirm.resize(130, 25)
    self.txt_pwd_confirm.setMaxLength(16)
    self.txt_pwd_confirm.setEchoMode(QLineEdit.Password)
    self.txt_pwd_confirm.returnPressed.connect(self.add)

    self.btn_link = QPushButton("Já possui cadastro? Clique aqui", self)
    self.btn_link.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")
    self.btn_link.setFlat(True)
    self.btn_link.move(30, 120)
    self.btn_link.clicked.connect(self.login)

    self.btn_ok = QPushButton("Ok", self)
    self.btn_ok.move(180, 160)
    self.btn_ok.clicked.connect(self.add)

    self.btn_cancel = QPushButton("Cancelar", self)
    self.btn_cancel.move(90, 160)
    self.btn_cancel.clicked.connect(self.close)

    """self.grid_layout = QGridLayout(self)

    self.grid_layout.addWidget(self.lbl_user)
    self.grid_layout.addWidget(self.txt_user)
    self.grid_layout.addWidget(self.lbl_pwd)
    self.grid_layout.addWidget(self.txt_pwd)
    self.grid_layout.addWidget(self.lbl_pwd_confirm)
    self.grid_layout.addWidget(self.txt_pwd_confirm)
    self.grid_layout.addWidget(self.btn_link)
    self.grid_layout.addWidget(self.btn_ok)
    self.grid_layout.addWidget(self.btn_cancel)"""

    self.center()
    self.show()

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

  def login(self):
    self.close()
    os.system('python tela_login.py')

  def add(self):
    try:
      user = self.txt_user.text()
      pwd = self.txt_pwd.text()
      pwd_confirm = self.txt_pwd_confirm.text()

      hash1 = hashlib.sha512(bin(int(pwd)).encode("utf-8")).hexdigest()
      hash2 = hashlib.sha512(bin(int(pwd_confirm)).encode("utf-8")).hexdigest()

      if user != "" and user.isalnum() and pwd != "" and len(pwd) > 3 and pwd.isdigit() \
                    and pwd_confirm == pwd and not user.__contains__(" ") and len(pwd) <= 16:
        return commit_data(user, hash1, hash2)
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
    except TypeError:
      QMessageBox.warning(self, "Error de Senha!", "Confirmação de senha incorreta!")
    except ValueError:
      QMessageBox.warning(self, "Error de senha!", "Senha deve conter apenas números!")

def commit_data(*args):
  try:
    conn = sqlite3.connect("login.db")
    conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
                   "user VARCHAR(10) NOT NULL UNIQUE, pwd VARCHAR NOT NULL, pwd_confirm VARCHAR NOT NULL)")
    cursor.execute("INSERT INTO data VALUES (NULL, ?, ?, ?)", args)
    conn.commit()
    conn.close()
    QMessageBox.information(win, "Informação!", "Cadastro efetuado com sucesso!")
    win.close()
    return func()
  except TypeError:
    QMessageBox.warning(win, "ERROR!", "Error ao cadastrar!")
  except sqlite3.IntegrityError:
    QMessageBox.warning(win, "Error de usuário!", "Usuário já cadastrado!")

def func():
  try:
    os.system('python tela_login.py')
  except Exception as e:
    print(e)
    QMessageBox.warning(win, "ERROR!", "Error na operação!")

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = RegisterLogin()
  sys.exit(app.exec_())
