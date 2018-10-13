import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3
from datetime import datetime
import os

class ProductSale(QWidget):
  value_sale, value_tot_sale = range(2)
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.setWindowTitle("Venda de produto")
    self.setFixedSize(500, 500)
    self.setWindowIcon(QIcon("corbeille_box_sale_v.png"))

    self.lbl_sale = QLabel("Valor da venda:", self)
    self.txt_sale = QLineEdit(self)
    self.txt_sale.returnPressed.connect(self.save)

    self.lbl_sale_day = QLabel("Vendas do dia:", self)
    self.txt_sale_day = QLineEdit(self)
    self.txt_sale_day.returnPressed.connect(self.search_day)

    self.btn_search_day = QPushButton("Pesquisar", self)
    self.btn_search_day.clicked.connect(self.search_day)

    self.btn_search_month = QPushButton("Pesquisar por mês", self)
    self.btn_search_month.clicked.connect(self.search_month)

    self.btn_save = QPushButton("Salvar", self)
    self.btn_save.clicked.connect(self.save)

    self.btn_sum_tot = QPushButton("Somar total", self)
    self.btn_sum_tot.clicked.connect(self.sum_tot)

    self.btn_close = QPushButton("Fechar", self)
    self.btn_close.clicked.connect(self.close)

    self.data_group_box = QGroupBox()
    self.data_view = QTreeView()
    self.data_view.setRootIsDecorated(False)
    self.data_view.setAlternatingRowColors(True)

    self.data_layout = QHBoxLayout()
    self.data_layout.addWidget(self.data_view)
    self.data_group_box.setLayout(self.data_layout)

    self.model = self.create_data_model(self)
    self.data_view.setModel(self.model)

    self.main_layout = QVBoxLayout()
    self.main_layout.addWidget(self.lbl_sale)
    self.main_layout.addWidget(self.txt_sale)
    self.main_layout.addWidget(self.lbl_sale_day)
    self.main_layout.addWidget(self.txt_sale_day)
    self.main_layout.addWidget(self.btn_search_day)
    self.main_layout.addWidget(self.btn_search_month)
    self.main_layout.addWidget(self.data_group_box)
    self.main_layout.addWidget(self.btn_save)
    self.main_layout.addWidget(self.btn_sum_tot)
    self.main_layout.addWidget(self.btn_close)
    self.setLayout(self.main_layout)

    self.center()
    self.show()

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

  def save(self):
    try:
      value_sale = self.txt_sale.text()
      date_register = datetime.now()
      year = date_register.year
      month = date_register.month
      day = date_register.day
      hour = date_register.hour
      minute = date_register.minute
      second = date_register.second
      current_month = datetime.now()
      if value_sale == "":
        QMessageBox.warning(self, "Atenção!", "Campo valor de venda está vazio!")
      elif value_sale != "" and not value_sale.__contains__(','):
        QMessageBox.warning(self, "Error!", "Valor deve conter centavos após vírgula!")
      else:
        value_sale = value_sale.replace(',', '.')
        value_sale = float(value_sale)
        return commit_data(value_sale, day, month, year, hour, minute, second, current_month.strftime("%B"))
    except Exception as e:
      print(e)

  def search_day(self):
    try:
      date = self.txt_sale_day.text().replace('/', '').replace('-', '')
      if date == "":
        QMessageBox.warning(self, "Atenção!", "Campo de pesquisa está vazio!")
      elif date != "" and len(date) < 7:
        QMessageBox.warning(self, "Atenção!", "Data incorreta!")
      elif len(date) == 7:
        day = date[0] + date[1]
        month = date[2]
        year = date[3] + date[4] + date[5] + date[6]
        return result_day(day, month, year)
      else:
        day = date[0] + date[1]
        month = date[2] + date[3]
        year = date[4] + date[5] + date[6] + date[7]
        return result_day(day, month, year)
    except Exception as e:
      print(e)

  def search_month(self):
    self.close()
    os.system('python venda_produto2.py')

  def sum_tot(self):
    try:
      date = self.txt_sale_day.text().replace('/', '').replace('-', '')
      if date == "":
        QMessageBox.warning(self, "Atenção!", "Campo de pesquisa está vazio!")
      elif len(date) == 7:
        day = date[0] + date[1]
        month = date[2]
        year = date[3] + date[4] + date[5] + date[6]
        return sum_tot_day(day, month, year)
      else:
        day = date[0] + date[1]
        month = date[2] + date[3]
        year = date[4] + date[5] + date[6] + date[7]
        return sum_tot_day(day, month, year)
      except Exception as e:
        print(e)

  def create_data_model(self, parent):
    model = QStandardItemModel(0, 1, parent)
    model.setHeaderData(self.value_sale, Qt.Horizontal, "Valor de cada venda do dia")
    return model

  def add_data(self, model, value_sale):
    model.insertRow(0)
    model.setData(model.index(0, self.value_sale), value_sale)

def commit_data(*args):
  try:
    conn = sqlite3.connect("sale.db")
    conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS data (value_sale FLOAT, day VARCHAR(2), month VARCHAR(2), "
                   "year VARCHAR(4), hour VARCHAR(2), minute VARCHAR(2), second VARCHAR(2), "
                   "current_month VARCHAR(10))")
    cursor.execute("INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?, ?)", args)
    conn.commit()
    conn.close()
    win.txt_sale.setText("")
  except Exception as e:
    print(e)

def result_day(day, month, year):
  try:
    conn_db = sqlite3.connect("sale.db")
    conn_db.text_factory = str
    cursor = conn_db.cursor()
    cursor.execute("SELECT value_sale FROM data WHERE day = '{}' AND month = '{}' "
                   "AND year = '{}'".format(day, month, year))
    l2 = cursor.fetchall()
    conn_db.close()
    return ref(l2)
  except Exception as e:
    print(e)
    QMessageBox.warning(win, "Error!", "Dados incorretos!")

def ref(l2):
  try:
    win.add_data(win.model, "=================")
    for item in l2:
      win.add_data(win.model, "R${:.2f}".format(item[0]).replace('.', ','))
  except Exception as e:
    print(e)

def sum_tot_day(day, month, year):
  try:
    conn_db = sqlite3.connect("sale.db")
    conn_db.text_factory = str
    cursor = conn_db.cursor()
    cursor.execute("SELECT SUM(value_sale) FROM data WHERE day = '{}' AND month = '{}' "
                   "AND year = '{}'".format(day, month ,year))
    for item in cursor.fetchall():
      QMessageBox.information(win, "Informação!", "O valor total do dia {}/{}/{} é:\nR${:.2f}".format(day, month, year, item[0]).replace('.', ','))
    conn_db.close()
  except Exception as e:
    print(e)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = ProductSale()
  sys.exit(app.exec_())
