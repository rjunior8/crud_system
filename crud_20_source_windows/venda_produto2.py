import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3
import os
import calendar
from translate import Translator

class ProductSale(QWidget):
  value_sale, day = range(2)
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.setWindowTitle("Vendas")
    self.setFixedSize(500, 500)
    self.setWindowIcon(QIcon("corbeille_box_sale_v.png"))

    self.lbl_sale_month = QLabel("Vendas do mês:", self)
    self.txt_sale_month = QComboBox(self)
    for month in calendar.month_name:
      self.txt_sale_month.addItem(month)

    self.btn_search_month = QPushButton("Pesquisar", self)
    self.btn_search_month.clicked.connect(self.search_month)

    self.btn_search_day = QPushButton("Pesquisar por dia", self)
    self.btn_search_day.clicked.connect(self.search_day)

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
    self.main_layout.addWidget(self.lbl_sale_month)
    self.main_layout.addWidget(self.txt_sale_month)
    self.main_layout.addWidget(self.btn_search_month)
    self.main_layout.addWidget(self.btn_search_day)
    self.main_layout.addWidget(self.data_group_box)
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

  def search_month(self):
    try:
      month = self.txt_sale_month.currentText()
      return result_month(month)
    except Exception as e:
      print(e)

  def search_day(self):
    self.close()
    os.system('python venda_produto.py')

  def sum_tot(self):
    try:
      month = self.txt_sale_month.currentText()
      return sum_tot_month(month)
    except Exception as e:
      print(e)

  def create_data_model(self, parent):
    model = QStandardItemModel(0, 2, parent)
    model.setHeaderData(self.value_sale, Qt.Horizontal, "Valor da venda")
    model.setHeaderData(self.day, Qt.Horizontal, "Data")
    return model

  def add_data(self, model, value_sale, day):
    model.insertRow(0)
    model.setData(model.index(0, self.value_sale), value_sale)
    model.setData(model.index(0, self.day), day)

def result_month(month):
  try:
    conn_db = sqlite3.connect("sale.db")
    conn_db.text_factory = str
    cursor = conn_db.cursor()
    cursor.execute("SELECT value_sale, day, month, year FROM data WHERE current_month = '{}'".format(month))
    l2 = cursor.fetchall()
    conn_db.close()
    return ref(l2)
  except Exception as e:
    print(e)
    QMessageBox.warning(win, "Error!", "Dados incorretos!")

def ref(l2):
  try:
    win.add_data(win.model, "=================", "=================")
    for item in l2:
      day, month, year = item[1], item[2], item[3]
      win.add_data(win.model, "R${:.2f}".format(item[0]).replace('.', ','), "{}/{}/{}".format(day, month, year))
  except Exception as e:
    print(e)

def sum_tot_month(month):
  try:
    conn_db = sqlite3.connect("sale.db")
    conn_db.text_factory = str
    cursor = conn_db.cursor()
    cursor.execute("SELECT SUM(value_sale) FROM data WHERE current_month = '{}'".format(month))
    translator = Translator(to_lang="pt")
    for item in cursor.fetchall():
      QMessageBox.information(win, "Informação!", "O valor total do mês {} é:\nR${:.2f}".format(translator.translate(month), item[0]).replace('.', ','))
    conn_db.close()
  except Exception as e:
    print(e)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = ProductSale()
  sys.exit(app.exec_())
