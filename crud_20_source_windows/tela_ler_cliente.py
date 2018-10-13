import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys

class SearchClient(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.setWindowTitle("Pesquisa de Cliente")
    self.setWindowIcon(QIcon("search_files.png"))
    self.setFixedSize(340, 640)

    self.lbl_search = QLabel("Pesquisar:", self)
    self.lbl_search.move(10, 10)
    self.txt_search = QLineEdit(self)
    self.txt_search.move(70, 10)
    self.txt_search.resize(260, 28)
    self.txt_search.returnPressed.connect(self.search)

    self.lbl_name = QLabel("*Nome:", self)
    self.lbl_name.move(10, 50)
    self.txt_name = QLineEdit(self)
    self.txt_name.move(70, 50)
    self.txt_name.resize(260, 28)
    self.txt_name.setMaxLength(100)

    self.lbl_cpf = QLabel("*CPF:", self)
    self.lbl_cpf.move(10, 90)
    self.txt_cpf = QLineEdit(self)
    self.txt_cpf.move(70, 90)
    self.txt_cpf.resize(85, 28)
    self.txt_cpf.setMaxLength(14)

    self.lbl_born = QLabel("*Data de nascimento:", self)
    self.lbl_born.move(155, 90)
    self.txt_born = QLineEdit(self)
    self.txt_born.move(260, 90)
    self.txt_born.resize(70, 28)
    self.txt_born.setMaxLength(10)

    self.lbl_city = QLabel("*Cidade:", self)
    self.lbl_city.move(10, 130)
    self.txt_city = QLineEdit(self)
    self.txt_city.move(70, 130)
    self.txt_city.resize(180, 28)
    self.txt_city.setMaxLength(100)

    self.lbl_uf = QLabel("*UF:", self)
    self.lbl_uf.move(260, 130)
    self.txt_uf = QLineEdit(self)
    self.txt_uf.move(300, 130)
    self.txt_uf.resize(30, 28)
    self.txt_uf.setMaxLength(2)

    self.lbl_nbd = QLabel("*Bairro:", self)
    self.lbl_nbd.move(10, 170)
    self.txt_nbd = QLineEdit(self)
    self.txt_nbd.move(70, 170)
    self.txt_nbd.resize(180, 28)
    self.txt_nbd.setMaxLength(100)

    self.lbl_number = QLabel("*Nº:", self)
    self.lbl_number.move(260, 170)
    self.txt_number = QLineEdit(self)
    self.txt_number.move(290, 170)
    self.txt_number.resize(40, 28)
    self.txt_number.setMaxLength(4)

    self.lbl_addr = QLabel("*Endereço:", self)
    self.lbl_addr.move(10, 210)
    self.txt_addr = QLineEdit(self)
    self.txt_addr.move(70, 210)
    self.txt_addr.resize(260, 28)
    self.txt_addr.setMaxLength(100)

    self.lbl_tel = QLabel("Telefone:", self)
    self.lbl_tel.move(10, 250)
    self.txt_tel = QLineEdit(self)
    self.txt_tel.move(70, 250)
    self.txt_tel.resize(90, 28)
    self.txt_tel.setMaxLength(13)

    self.lbl_cel = QLabel("*Celular:", self)
    self.lbl_cel.move(180, 250)
    self.txt_cel = QLineEdit(self)
    self.txt_cel.move(240, 250)
    self.txt_cel.resize(90, 28)
    self.txt_cel.setMaxLength(15)

    self.lbl_whatsapp = QLabel("Whatsapp:", self)
    self.lbl_whatsapp.move(10, 290)
    self.txt_whatsapp = QLineEdit(self)
    self.txt_whatsapp.move(70, 290)
    self.txt_whatsapp.resize(90, 28)
    self.txt_whatsapp.setMaxLength(15)

    self.lbl_sex = QLabel("*Sexo:", self)
    self.lbl_sex.move(210, 290)
    self.combo = QComboBox(self)
    self.combo.addItem("Masculino")
    self.combo.addItem("Feminino")
    self.txt_sex = self.combo
    self.txt_sex.move(258, 290)

    self.lbl_email = QLabel("Email:", self)
    self.lbl_email.move(10, 330)
    self.txt_email = QLineEdit(self)
    self.txt_email.move(70, 330)
    self.txt_email.resize(260, 28)
    self.txt_email.setMaxLength(100)

    self.lbl_debit = QLabel("Débito:", self)
    self.lbl_debit.move(10, 370)
    self.txt_debit = QLineEdit(self)
    self.txt_debit.move(70, 370)
    self.txt_debit.resize(100, 28)
    self.txt_debit.setMaxLength(10)

    self.lbl_parcels = QLabel("Nº de Parcelas:", self)
    self.lbl_parcels.move(200, 370)
    self.txt_parcels = QLineEdit(self)
    self.txt_parcels.move(290, 370)
    self.txt_parcels.resize(40, 28)
    self.txt_parcels.setMaxLength(3)

    self.lbl_low = QLabel("Baixa:", self)
    self.lbl_low.move(10, 410)
    self.txt_low = QLineEdit(self)
    self.txt_low.move(70, 410)
    self.txt_low.resize(100, 28)
    self.txt_low.setMaxLength(10)

    self.lbl_value = QLabel("Vº Parcelas:", self)
    self.lbl_value.move(180, 410)
    self.txt_value = QLineEdit(self)
    self.txt_value.move(250, 410)
    self.txt_value.resize(80, 28)
    self.txt_value.setMaxLength(10)

    self.lbl_balance = QLabel("Saldo a receber:", self)
    self.lbl_balance.move(10, 450)
    self.txt_balance = QLineEdit(self)
    self.txt_balance.move(100, 450)
    self.txt_balance.resize(100, 28)
    self.txt_balance.setMaxLength(10)

    #self.lbl_date = QLabel("Data de Cadastro:", self)
    #self.lbl_date.move(200, 450)
    self.txt_date = QLabel(self)
    self.txt_date.move(230, 450)
    self.txt_date.resize(140, 22)

    self.txt_service = QPlainTextEdit(self)
    self.txt_service.move(10, 490)
    self.txt_service.resize(330, 100)
    self.lbl_obs = QLabel("(Observações)", self)
    self.lbl_obs.move(10, 600)

    #content = self.txt_service.toPlainText()

    self.btn_ok = QPushButton("Pesquisar", self)
    self.btn_ok.move(255, 600)
    self.btn_ok.clicked.connect(self.search)

    self.btn_cancel = QPushButton("Cancelar", self)
    self.btn_cancel.move(175, 600)
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
      name = self.txt_search.text()
      if name != "":
        return select_data(name.title().replace(" Da ", " da ").replace(" De ", " de ").
                                replace(" Dos ", " dos ").replace(" Das ", " das "))
      else:
        QMessageBox.warning(self, "Error!", "Campo de pesquisa está vazio!")
    except Exception as e:
      print(e)
      QMessageBox.warning(self, "Error!", "Dados incorretos!")

def select_data(nome):
  try:
    conn = sqlite3.connect("client.db")
    conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data WHERE name = '%s'" % nome)
    data = cursor.fetchone()

    cpf = str(data[2])
    a = cpf[0] + cpf[1] + cpf[2]
    b = cpf[3] + cpf[4] + cpf[5]
    c = cpf[6] + cpf[7] + cpf[8]
    d = cpf[9] + cpf[10]
    born = str(data[3])
    e = born[0] + born[1]
    f = born[2] + born[3]
    g = born[4] + born[5] + born[6] + born[7]
    tel = str(data[8])
    h = tel[0] + tel[1]
    i = tel[2] + tel[3] + tel[4] + tel[5]
    j = tel[6] + tel[7] + tel[8] + tel[9]
    cel = str(data[9])
    l = cel[0] + cel[1]
    m = cel[2]
    n = cel[3] + cel[4] + cel[5] + cel[6]
    o = cel[7] + cel[8] + cel[9] + cel[10]
    whats = str(data[10])
    p = whats[0] + whats[1]
    q = whats[2]
    r = whats[3] + whats[4] + whats[5] + whats[6]
    s = whats[7] + whats[8] + whats[9] + whats[10]

    debit = data[14]
    low = data[15]
    balance = debit - low

    number_parcels = data[16]
    value = 0
    if number_parcels != 0:
      value = debit / number_parcels

    win.txt_name.setText(str(data[1]))
    win.txt_cpf.setText("{}.{}.{}-{}".format(a, b, c, d))
    win.txt_born.setText("{}/{}/{}".format(e, f, g))
    win.txt_sex.setCurrentText(str(data[4]))
    win.txt_city.setText(str(data[5]))
    win.txt_nbd.setText(str(data[6]))
    win.txt_uf.setText(str(data[7]))
    win.txt_tel.setText("({}){}-{}".format(h, i, j))
    win.txt_cel.setText("({}){}.{}-{}".format(l, m, n, o))
    win.txt_whatsapp.setText("({}){}.{}-{}".format(p, q, r, s))
    win.txt_email.setText(str(data[11]))
    win.txt_addr.setText(str(data[12]))
    win.txt_number.setText(str(data[13]))
    win.txt_debit.setText("R${:.2f}".format(debit).replace('.', ','))
    win.txt_low.setText("R${:.2f}".format(low).replace('.', ','))
    win.txt_parcels.setText(str(data[16]))
    win.txt_value.setText("R${:.2f}".format(value).replace('.', ','))
    win.txt_balance.setText("R${:.2f}".format(balance).replace('.', ','))
    win.txt_date.setText("{}/{}/{} - {}:{}:{}".format(str(data[20]), str(data[19]), str(data[18]),
                         str(data[21]), str(data[22]), str(data[23])))
    win.txt_service.clear()
    win.txt_service.insertPlainText(str(data[17]))

    conn.close()
  except Exception as e:
    print(e)
    QMessageBox.warning(win, "Error!", "Dados incorretos!")

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = SearchClient()
  sys.exit(app.exec_())
