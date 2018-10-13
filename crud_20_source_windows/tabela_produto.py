import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3

class ProductTable(QWidget):
  desc, qtt, value_buy, value_sale = range(4)
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.setWindowTitle("Tabela de produto")
    self.setFixedSize(500, 500)
    self.setWindowIcon(QIcon("table(1).png"))

    self.lbl_search = QLabel("Descrição:", self)
    self.txt_search = QLineEdit(self)
    self.txt_search.returnPressed.connect(self.search)

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
    self.main_layout.addWidget(self.lbl_search)
    self.main_layout.addWidget(self.txt_search)
    self.main_layout.addWidget(self.data_group_box)
    self.main_layout.addWidget(self.btn_close)
    self.setLayout(self.main_layout)

    self.center()
    self.show()

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

  def create_data_model(self, parent):
    model = QStandardItemModel(0, 4, parent)
    model.setHeaderData(self.desc, Qt.Horizontal, "Descrição")
    model.setHeaderData(self.qtt, Qt.Horizontal, "Quantidade")
    model.setHeaderData(self.value_buy, Qt.Horizontal, "Valor de compra")
    model.setHeaderData(self.value_sale, Qt.Horizontal, "Valor de venda")
    return model

  def add_data(self, model, desc, qtt, value_buy, value_sale):
    model.insertRow(0)
    model.setData(model.index(0, self.desc), desc)
    model.setData(model.index(0, self.qtt), qtt)
    model.setData(model.index(0, self.value_buy), value_buy)
    model.setData(model.index(0, self.value_sale), value_sale)

  def search(self):
    try:
      desc = self.txt_search.text()
      if desc != "":
        self.txt_search.setText("")
        return search_data(desc)
      else:
        QMessageBox.warning(self, "Error!", "Campo de pesquisa está vazio!")
    except Exception as e:
      print(e)
      QMessageBox.warning(win, "Error!", "Dados incorretos!")

def search_data(desc):
  try:
    conn_db = sqlite3.connect("product.db")
    conn_db.text_factory = str
    cursor = conn_db.cursor()
    cursor.execute("SELECT desc, qtt, value_buy, value_sale FROM data WHERE desc LIKE '{}%'".format(desc))
    l2 = cursor.fetchall()
    conn_db.close()
    return ref(l2)
  except Exception as e:
    print(e)
    QMessageBox.warning(win, "Error!", "Dados incorretos!")

def ref(l2):
  try:
    win.add_data(win.model, "=========", "=========", "=========", "=========")
    for item in l2:
      win.add_data(win.model, item[0], item[1], "R${:.2f}".format(item[2]).replace('.', ','),
                  "R${:.2f}".format(item[3]).replace('.', ','))
  except Exception as e:
    print(e)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = ProductTable()
  sys.exit(app.exec_())