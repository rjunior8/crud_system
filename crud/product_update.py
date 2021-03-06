import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys

class UpdateProduct(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.setWindowTitle("Atualização de produto")
    self.setWindowIcon(QIcon("agt_update_drivers.png"))
    self.setFixedSize(260, 400)

    self.lbl_search = QLabel("Pesquisar:", self)
    self.lbl_search.move(10, 10)
    self.txt_search = QLineEdit(self)
    self.txt_search.move(100, 10)
    self.txt_search.resize(150, 28)
    self.txt_search.returnPressed.connect(self.search)

    self.lbl_desc = QLabel("Descrição:", self)
    self.lbl_desc.move(10, 50)
    self.txt_desc = QLineEdit(self)
    self.txt_desc.move(100, 50)
    self.txt_desc.resize(150, 28)
    self.txt_desc.setMaxLength(50)

    self.lbl_id = QLabel(self)
    self.lbl_id.move(310, 90)
    self.lbl_id.setVisible(False)

    self.lbl_quantity = QLabel("Quantidade:", self)
    self.lbl_quantity.move(10, 90)
    self.txt_quantity = QLineEdit(self)
    self.txt_quantity.move(100, 90)
    self.txt_quantity.resize(40, 28)
    self.txt_quantity.setMaxLength(5)

    self.lbl_value_buy = QLabel("Valor de compra:", self)
    self.lbl_value_buy.move(10, 130)
    self.txt_value_buy = QLineEdit(self)
    self.txt_value_buy.move(100, 130)
    self.txt_value_buy.resize(80, 28)
    self.txt_value_buy.setMaxLength(10)

    self.lbl_value_sale = QLabel("Valor de venda:", self)
    self.lbl_value_sale.move(10, 170)
    self.txt_value_sale = QLineEdit(self)
    self.txt_value_sale.move(100, 170)
    self.txt_value_sale.resize(80, 28)
    self.txt_value_sale.setMaxLength(10)

    self.lbl_date = QLabel("Data:", self)
    self.lbl_date.move(10, 210)
    self.txt_date = QLineEdit(self)
    self.txt_date.move(100, 210)
    self.txt_date.resize(70, 28)
    self.txt_date.setMaxLength(10)

    self.lbl_tot_value = QLabel("Valor total:", self)
    self.lbl_tot_value.move(10, 250)
    self.txt_tot_value = QLineEdit(self)
    self.txt_tot_value.move(100, 250)
    self.txt_tot_value.resize(100, 28)

    self.lbl_date_register = QLabel("Data de cadastro:", self)
    self.lbl_date_register.move(10, 290)
    self.txt_date_register = QLabel(self)
    self.txt_date_register.move(110, 290)
    self.txt_date_register.resize(80, 13)

    self.lbl_hour_register = QLabel("Hora de cadastro:", self)
    self.lbl_hour_register.move(10, 330)
    self.txt_hour_register = QLabel(self)
    self.txt_hour_register.move(110, 330)
    self.txt_hour_register.resize(80, 13)

    self.btn_ok = QPushButton("Pesquisar", self)
    self.btn_ok.move(180, 370)
    self.btn_ok.clicked.connect(self.search)

    self.btn_update = QPushButton("Atualizar", self)
    self.btn_update.move(95, 370)
    self.btn_update.clicked.connect(self.on_update_clicked)

    self.btn_cancel = QPushButton("Cancelar", self)
    self.btn_cancel.move(10, 370)
    self.btn_cancel.clicked.connect(self.close)

    self.center()
    self.show()

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

  def search(self):
    try:
      desc = self.txt_search.text()
      if desc != "":
        return select_data(desc.title().replace(" De ", " de "))
      else:
        QMessageBox.warning(self, "Error!", "Campo de pesquisa está vazio!")
    except Exception as e:
      print(e)
      QMessageBox.warning(win, "Error!", "Dados incorretos!")

  def on_update_clicked(self):
    try:
      id_product = self.lbl_id.text()
      if id_product != "":
        return update_data(id_product)
      else:
        QMessageBox.warning(self, "Error!", "Nenhum produto selecionado!")
    except Exception as e:
      print(e)
      QMessageBox.warning(win, "Error!", "Dados incorretos!")

def select_data(desc):
  try:
    conn = sqlite3.connect("product.db")
    conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data WHERE desc = '%s'" % desc)
    data = cursor.fetchone()

    date = data[5]
    day = date[0] + date[1]
    month = date[2] + date[3]
    year = date[4] + date[5] + date[6] + date[7]

    qtt = data[2]
    value_buy = data[3]
    tot_value_buy = qtt * value_buy

    value_sale = data[4]

    win.lbl_id.setText(str(data[0]))
    win.txt_desc.setText(str(data[1]))
    win.txt_quantity.setText(str(qtt))
    win.txt_value_buy.setText("R${:.2f}".format(value_buy).replace('.', ','))
    win.txt_value_sale.setText("R${:.2f}".format(value_sale).replace('.', ','))
    win.txt_date.setText("{}/{}/{}".format(day, month, year))
    win.txt_tot_value.setText("R${:.2f}".format(tot_value_buy).replace('.', ','))
    win.txt_date_register.setText("{}/{}/{}".format(str(data[8]), str(data[7]), str(data[6])))
    win.txt_hour_register.setText("{}:{}:{}".format(str(data[9]), str(data[10]), str(data[11])))

    conn.close()
  except Exception as e:
    print(e)
    QMessageBox.warning(win, "Error!", "Dados incorretos!")

def update_data(id_product):
  try:
    conn = sqlite3.connect("product.db")
    conn.text_factory = str
    cursor = conn.cursor()

    desc = win.txt_desc.text().title().replace(" De ", " de ")
    qtt = win.txt_quantity.text()
    value_buy = win.txt_value_buy.text().replace("R$", '').replace('.', '')
    value_sale = win.txt_value_sale.text().replace("R$", '').replace('.', '')
    date = win.txt_date.text().replace('/', "").replace('-', "")

    if (value_buy != '0' and not value_buy.__contains__(',')) and \
       (value_sale != '0' and not value_sale.__contains__(',')):
      QMessageBox.warning(win, "Error!", "Valor(es) deve conter centavos após vírgula!")
    elif (value_buy != '0' and not value_buy.__contains__(',')) or \
         (value_sale != '0' and not value_sale.__contains__(',')):
      QMessageBox.warning(win, "Error!", "Valor(es) deve conter centavos após vírgula!")
    elif len(date) < 8:
      QMessageBox.warning(win, "Error!", "A data deve estar completa!\nExemplo: 01052017")
    else:
      value_buy = value_buy.replace(',', '.')
      value_sale = value_sale.replace(',', '.')
      cursor.execute("UPDATE data SET desc = ?, qtt = ?, value_buy = ?, value_sale = ?, date = ? WHERE id = ?",
                    (desc, qtt, value_buy, value_sale, date, id_product))
    conn.commit()
    conn.close()
    QMessageBox.information(win, "Informação!", "Operação realizada com sucesso!")
    return updated_data(desc)
  except Exception as e:
    print(e)
    QMessageBox.warning(win, "Error!", "Dados incorretos!")

def updated_data(desc):
  try:
    conn = sqlite3.connect("product.db")
    conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data WHERE desc = '%s'" % desc)
    data = cursor.fetchone()

    date = data[5]
    day = date[0] + date[1]
    month = date[2] + date[3]
    year = date[4] + date[5] + date[6] + date[7]

    qtt = data[2]
    value_buy = data[3]
    tot_value_buy = qtt * value_buy

    value_sale = data[4]

    win.lbl_id.setText(str(data[0]))
    win.txt_desc.setText(str(data[1]))
    win.txt_quantity.setText(str(qtt))
    win.txt_value_buy.setText("R${:.2f}".format(value_buy).replace('.', ','))
    win.txt_value_sale.setText("R${:.2f}".format(value_sale).replace('.', ','))
    win.txt_date.setText("{}/{}/{}".format(day, month, year))
    win.txt_tot_value.setText("R${:.2f}".format(tot_value_buy).replace('.', ','))
    win.txt_date_register.setText("{}/{}/{}".format(str(data[8]), str(data[7]), str(data[6])))
    win.txt_hour_register.setText("{}:{}:{}".format(str(data[9]), str(data[10]), str(data[11])))

    conn.close()
  except Exception as e:
    print(e)
    QMessageBox.warning(win, "Error!", "Dados incorretos!")

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = UpdateProduct()
  sys.exit(app.exec_())
