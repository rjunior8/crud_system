import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys
from datetime import datetime

class AddProduct(QWidget):
  def __init__(self):
    super().__init__()
    self.val_buy, self.val_sale = 0, 0
    self.initUI()

  def initUI(self):
    self.setWindowTitle("Cadastro de produto")
    self.setWindowIcon(QIcon("shopcartadd.png"))
    self.setFixedSize(260, 280)

    self.lbl_desc = QLabel("Descrição:", self)
    self.lbl_desc.move(10, 10)
    self.txt_desc = QLineEdit(self)
    self.txt_desc.move(100, 10)
    self.txt_desc.resize(150, 28)
    self.txt_desc.setMaxLength(50)

    self.lbl_quantity = QLabel("Quantidade:", self)
    self.lbl_quantity.move(10, 50)
    self.txt_quantity = QLineEdit(self)
    self.txt_quantity.move(100, 50)
    self.txt_quantity.resize(40, 28)
    self.txt_quantity.setMaxLength(5)

    self.lbl_value_buy = QLabel("Valor de compra:", self)
    self.lbl_value_buy.move(10, 90)
    self.txt_value_buy = QLineEdit(self)
    self.txt_value_buy.move(100, 90)
    self.txt_value_buy.resize(60, 28)
    self.txt_value_buy.setMaxLength(8)

    self.lbl_value_sale = QLabel("Valor de venda:", self)
    self.lbl_value_sale.move(10, 130)
    self.txt_value_sale = QLineEdit(self)
    self.txt_value_sale.move(100, 130)
    self.txt_value_sale.resize(60, 28)
    self.txt_value_sale.setMaxLength(8)

    self.lbl_date = QLabel("Data:", self)
    self.lbl_date.move(10, 170)
    self.txt_date = QLineEdit(self)
    self.txt_date.move(100, 170)
    self.txt_date.resize(60, 28)
    self.txt_date.setMaxLength(8)

    self.lbl_tot_value = QLabel("Valor total:", self)
    self.lbl_tot_value.move(10, 210)
    self.txt_tot_value = QLineEdit(self)
    self.txt_tot_value.move(100, 210)
    self.txt_tot_value.resize(70, 28)

    self.btn_tot_sum = QPushButton("Somar total", self)
    self.btn_tot_sum.move(180, 210)
    #self.btn_tot_sum.resize(100, 28)
    self.btn_tot_sum.clicked.connect(self.tot_sum)

    self.btn_ok = QPushButton("Cadastrar", self)
    self.btn_ok.move(180, 250)
    self.btn_ok.clicked.connect(self.add)

    self.btn_cancel = QPushButton("Cancelar", self)
    self.btn_cancel.move(95, 250)
    self.btn_cancel.clicked.connect(self.close)

    self.center()
    self.show()

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

  def tot_sum(self):
    try:
      value = self.txt_value_buy.text().replace(',', '.')
      value = float(value)
      quantity = int(self.txt_quantity.text())
      tot_value = quantity * value
      self.txt_tot_value.setText("{:.2f}".format(tot_value).replace('.', ','))
    except ValueError:
      QMessageBox.warning(self, "Error!", "Dados incorretos!")

  def add(self):
    try:
      desc = self.txt_desc.text()
      qtt = self.txt_quantity.text()
      value_buy = self.txt_value_buy.text().replace('.', '').replace("R$", "")
      value_sale = self.txt_value_sale.text().replace('.', '').replace("R$", "")
      date = self.txt_date.text().replace('/', "").replace('-', "")
      date_register = datetime.now()
      year = date_register.year
      month = date_register.month
      day = date_register.day
      hour = date_register.hour
      minute = date_register.minute
      sec = date_register.second

      if date == "":
        date = "00000000"

      if value_buy == "":
        value_buy = '0'

      if value_sale == "":
        value_sale = '0'

      if desc != "" and qtt != "" and qtt.isdigit() and date.isdigit() and value_buy != '0' \
                    and value_buy.__contains__(',') and len(date) == 8 and value_sale != '0' \
                    and value_sale.__contains__(','):

        v_buy = value_buy.replace(',', '.')
        self.val_buy = float(v_buy)
        v_sale = value_sale.replace(',', '.')
        self.val_sale = float(v_sale)

        return commit_data(desc.title().replace(" De ", " de "), qtt, self.val_buy, self.val_sale, date, year,
                           month, day, hour, minute, sec)

      elif desc != "" and qtt != "" and qtt.isdigit() and date.isdigit() \
                      and (value_buy != '0' and value_buy.__contains__(',')) and (value_sale == '0'):

        v_buy = value_buy.replace(',', '.')
        self.val_buy = float(v_buy)
        v_sale = value_sale.replace(',', '.')
        self.val_sale = float(v_sale)

        return commit_data(desc.title().replace(" De ", " de "), qtt, self.val_buy, self.val_sale, date, year,
                           month, day, hour, minute, sec)

      elif desc != "" and qtt != "" and qtt.isdigit() and date.isdigit() and value_buy == '0' \
                      and value_sale == '0':
        return commit_data(desc.title().replace(" De ", " de "), qtt, self.val_buy, self.val_sale, date, year,
                           month, day, hour, minute, sec)

      elif (value_buy != '0' and not value_buy.__contains__(',')) and \
           (value_sale != '0' and not value_sale.__contains__(',')):
        QMessageBox.warning(self, "Error!", "Valor(es) deve conter centavos após vírgula!")

      elif (value_buy != '0' and not value_buy.__contains__(',')) or \
           (value_sale != '0' and not value_sale.__contains__(',')):
        QMessageBox.warning(self, "Error!", "Valor(es) deve conter centavos após vírgula!")

      elif len(date) < 8:
        QMessageBox.warning(self, "Error!", "A data deve estar completa!\nExemplo: 01052017")
      else:
        QMessageBox.warning(self, "Error!", "Dados incorretos!")
    except Exception as e:
      print(e)
      QMessageBox.warning(self, "Error!", "Dados incorretos!")

def commit_data(*args):
  try:
    conn = sqlite3.connect("product.db")
    conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
                   "desc VARCHAR(20) NOT NULL, qtt INTEGER, value_buy FLOAT, value_sale FLOAT, date VARCHAR(10), "
                   "year VARCHAR(4), month VARCHAR(2), day VARCHAR(2), hour VARCHAR(2), "
                   "minute VARCHAR(2), sec VARCHAR(2))")
    cursor.execute("INSERT INTO data VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", args)
    conn.commit()
    conn.close()
    QMessageBox.information(win, "Informação!", "Operação realizada com sucesso!")
    return clear()
  except Exception as e:
    print(e)
    QMessageBox.warning(win, "Error!", "Dados incorretos!")

def clear():
  win.txt_desc.setText("")
  win.txt_quantity.setText("")
  win.txt_value_buy.setText("")
  win.txt_value_sale.setText("")
  win.txt_date.setText("")
  win.txt_tot_value.setText("")

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = AddProduct()
  sys.exit(app.exec_())
