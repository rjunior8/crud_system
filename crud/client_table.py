import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3

class ClientTable(QWidget):
  name, cpf, born, sex, city, nbd, uf, tel, cel, whatsapp, email, addr, number, debit, low, parcels, value_parcels, \
  balance, date, service = range(20)
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.setWindowTitle("Tabela de cliente")
    self.setFixedSize(500, 500)
    self.setWindowIcon(QIcon("table2.png"))

    self.lbl_search = QLabel("Nome:", self)
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
    model = QStandardItemModel(0, 20, parent)
    model.setHeaderData(self.name, Qt.Horizontal, "Nome")
    model.setHeaderData(self.cpf, Qt.Horizontal, "CPF")
    model.setHeaderData(self.born, Qt.Horizontal, "Data de nascimento")
    model.setHeaderData(self.sex, Qt.Horizontal, "Sexo")
    model.setHeaderData(self.city, Qt.Horizontal, "Cidade")
    model.setHeaderData(self.nbd, Qt.Horizontal, "Bairro")
    model.setHeaderData(self.uf, Qt.Horizontal, "UF")
    model.setHeaderData(self.tel, Qt.Horizontal, "Telefone")
    model.setHeaderData(self.cel, Qt.Horizontal, "Celular")
    model.setHeaderData(self.whatsapp, Qt.Horizontal, "Whatsapp")
    model.setHeaderData(self.email, Qt.Horizontal, "Email")
    model.setHeaderData(self.addr, Qt.Horizontal, "Endereço")
    model.setHeaderData(self.number, Qt.Horizontal, "Nº")
    model.setHeaderData(self.debit, Qt.Horizontal, "Débito")
    model.setHeaderData(self.low, Qt.Horizontal, "Baixa")
    model.setHeaderData(self.parcels, Qt.Horizontal, "Nº Parcelas")
    model.setHeaderData(self.value_parcels, Qt.Horizontal, "Vº Parcelas")
    model.setHeaderData(self.balance, Qt.Horizontal, "Saldo a receber")
    model.setHeaderData(self.date, Qt.Horizontal, "Data de cadastro")
    model.setHeaderData(self.service, Qt.Horizontal, "Serviço realizado")
    return model

  def add_data(self, model, name, cpf, born, sex, city, nbd, uf, tel, cel, whatsapp,
              email, addr, number, debit, low, parcels, value_parcels, balance, date, service):
    model.insertRow(0)
    model.setData(model.index(0, self.name), name)
    model.setData(model.index(0, self.cpf), cpf)
    model.setData(model.index(0, self.born), born)
    model.setData(model.index(0, self.sex), sex)
    model.setData(model.index(0, self.city), city)
    model.setData(model.index(0, self.nbd), nbd)
    model.setData(model.index(0, self.uf), uf)
    model.setData(model.index(0, self.tel), tel)
    model.setData(model.index(0, self.cel), cel)
    model.setData(model.index(0, self.whatsapp), whatsapp)
    model.setData(model.index(0, self.email), email)
    model.setData(model.index(0, self.addr), addr)
    model.setData(model.index(0, self.number), number)
    model.setData(model.index(0, self.debit), debit)
    model.setData(model.index(0, self.low), low)
    model.setData(model.index(0, self.parcels), parcels)
    model.setData(model.index(0, self.value_parcels), value_parcels)
    model.setData(model.index(0, self.balance), balance)
    model.setData(model.index(0, self.date), date)
    model.setData(model.index(0, self.service), service)

  def search(self):
    try:
      name = self.txt_search.text()
      if name != "":
        self.txt_search.setText("")
        return search_data(name)
      else:
        QMessageBox.warning(self, "Error!", "Campo de pesquisa está vazio!")
    except Exception as e:
      print(e)
      QMessageBox.warning(win, "Error!", "Dados incorretos!")

def search_data(name):
  try:
    conn_db = sqlite3.connect("client.db")
    conn_db.text_factory = str
    cursor = conn_db.cursor()
    cursor.execute("SELECT name, cpf, born, sex, city, nbd, uf, tel, cel, whatsapp, email, addr, number, debit,low,"
                  "parcel,service,year,month, day, hour, minute, sec FROM data WHERE name LIKE '{}%'".format(name))
    l2 = cursor.fetchall()
    conn_db.close()
    return ref(l2)
  except Exception as e:
    print(e)
    QMessageBox.warning(win, "Error!", "Dados incorretos!")

def ref(l2):
  try:
    win.add_data(win.model, "=========", "=========", "=========", "=========", "=========", "========="
                , "=========", "=========", "=========", "=========", "=========", "=========", "========="
                , "=========", "=========", "=========", "=========", "=========", "=========", "=========")
    for item in l2:
      cpf = item[1]
      a = cpf[0] + cpf[1] + cpf[2]
      b = cpf[3] + cpf[4] + cpf[5]
      c = cpf[6] + cpf[7] + cpf[8]
      d = cpf[9] + cpf[10]
      born = item[2]
      e = born[0] + born[1]
      f = born[2] + born[3]
      g = born[4] + born[5] + born[6] + born[7]
      tel = item[7]
      h = tel[0] + tel[1]
      i = tel[2] + tel[3] + tel[4] + tel[5]
      j = tel[6] + tel[7] + tel[8] + tel[9]
      cel = item[8]
      l = cel[0] + cel[1]
      m = cel[2]
      n = cel[3] + cel[4] + cel[5] + cel[6]
      o = cel[7] + cel[8] + cel[9] + cel[10]
      whats = item[9]
      p = whats[0] + whats[1]
      q = whats[2]
      r = whats[3] + whats[4] + whats[5] + whats[6]
      s = whats[7] + whats[8] + whats[9] + whats[10]

      debit = item[13]
      low = item[14]
      balance = debit - low

      number_parcels = item[15]
      value = 0
      if number_parcels != 0:
        value = debit / number_parcels

        win.add_data(win.model,item[0],"{}.{}.{}-{}".format(a, b, c, d),"{}/{}/{}".format(e, f, g),item[3], item[4],
                    item[5], item[6], "({}){}-{}".format(h, i, j), "({}){}.{}-{}".format(l, m, n, o),
                    "({}){}.{}-{}".format(p, q, r, s), item[10], item[11], item[12],
                    "R${:.2f}".format(debit).replace('.', ','), "R${:.2f}".format(low).replace('.', ','), item[15],
                    "R${:.2f}".format(value).replace('.', ','), "R${:.2f}".format(balance).replace('.', ','),
                    "{}/{}/{} - {}:{}:{}".format(item[19], item[18], item[17], item[20], item[21], item[22]),
                    item[16])
  except Exception as e:
    print(e)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = ClientTable()
  sys.exit(app.exec_())