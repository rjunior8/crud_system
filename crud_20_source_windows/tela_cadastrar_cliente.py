import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys
from datetime import datetime

class AddClient(QWidget):
  def __init__(self):
    super().__init__()
    self.debitos = 0
    self.baixas = 0
    self.initUI()

  def initUI(self):
    self.setWindowTitle("Cadastro de Cliente")
    self.setWindowIcon(QIcon("user_add(1).png"))
    self.setFixedSize(345, 550)

    self.lbl_name = QLabel("*Nome:", self)
    self.lbl_name.move(10, 10)
    self.txt_name = QLineEdit(self)
    self.txt_name.move(70, 10)
    self.txt_name.resize(260, 28)
    self.txt_name.setMaxLength(100)

    self.lbl_cpf = QLabel("*CPF:", self)
    self.lbl_cpf.move(10, 50)
    self.txt_cpf = QLineEdit(self)
    self.txt_cpf.move(70, 50)
    self.txt_cpf.resize(80, 28)
    self.txt_cpf.setMaxLength(11)

    self.lbl_born = QLabel("*Data de nascimento:", self)
    self.lbl_born.move(152, 50)
    self.txt_born = QLineEdit(self)
    self.txt_born.move(260, 50)
    self.txt_born.resize(70, 28)
    self.txt_born.setMaxLength(8)

    self.lbl_city = QLabel("*Cidade:", self)
    self.lbl_city.move(10, 90)
    self.txt_city = QLineEdit(self)
    self.txt_city.move(70, 90)
    self.txt_city.resize(180, 28)
    self.txt_city.setMaxLength(100)

    self.lbl_uf = QLabel("*UF:", self)
    self.lbl_uf.move(260, 90)
    self.txt_uf = QLineEdit(self)
    self.txt_uf.move(300, 90)
    self.txt_uf.resize(30, 28)
    self.txt_uf.setMaxLength(2)

    self.lbl_nbd = QLabel("*Bairro:", self)
    self.lbl_nbd.move(10, 130)
    self.txt_nbd = QLineEdit(self)
    self.txt_nbd.move(70, 130)
    self.txt_nbd.resize(180, 28)
    self.txt_nbd.setMaxLength(100)

    self.lbl_number = QLabel("*Nº:", self)
    self.lbl_number.move(260, 130)
    self.txt_number = QLineEdit(self)
    self.txt_number.move(290, 130)
    self.txt_number.resize(40, 28)
    self.txt_number.setMaxLength(4)

    self.lbl_addr = QLabel("*Endereço:", self)
    self.lbl_addr.move(10, 170)
    self.txt_addr = QLineEdit(self)
    self.txt_addr.move(70, 170)
    self.txt_addr.resize(260, 28)
    self.txt_addr.setMaxLength(100)

    self.lbl_tel = QLabel("Telefone:", self)
    self.lbl_tel.move(10, 210)
    self.txt_tel = QLineEdit(self)
    self.txt_tel.move(70, 210)
    self.txt_tel.resize(80, 28)
    self.txt_tel.setMaxLength(10)

    self.lbl_cel = QLabel("*Celular:", self)
    self.lbl_cel.move(180, 210)
    self.txt_cel = QLineEdit(self)
    self.txt_cel.move(245, 210)
    self.txt_cel.resize(85, 28)
    self.txt_cel.setMaxLength(11)

    self.lbl_whatsapp = QLabel("Whatsapp:", self)
    self.lbl_whatsapp.move(10, 250)
    self.txt_whatsapp = QLineEdit(self)
    self.txt_whatsapp.move(70, 250)
    self.txt_whatsapp.resize(85, 28)
    self.txt_whatsapp.setMaxLength(11)

    self.lbl_sex = QLabel("*Sexo:", self)
    self.lbl_sex.move(210, 250)
    self.combo = QComboBox(self)
    self.combo.addItem("Masculino")
    self.combo.addItem("Feminino")
    self.txt_sex = self.combo
    self.txt_sex.move(258, 250)

    self.lbl_email = QLabel("Email:", self)
    self.lbl_email.move(10, 290)
    self.txt_email = QLineEdit(self)
    self.txt_email.move(70, 290)
    self.txt_email.resize(260, 28)
    self.txt_email.setMaxLength(100)

    self.lbl_debit = QLabel("Débito:", self)
    self.lbl_debit.move(10, 330)
    self.txt_debit = QLineEdit(self)
    self.txt_debit.move(70, 330)
    self.txt_debit.resize(60, 28)
    self.txt_debit.setMaxLength(8)

    self.lbl_parcels = QLabel("Nº de Parcelas:", self)
    self.lbl_parcels.move(200, 330)
    self.txt_parcels = QLineEdit(self)
    self.txt_parcels.move(290, 330)
    self.txt_parcels.resize(40, 28)
    self.txt_parcels.setMaxLength(3)

    self.lbl_low = QLabel("Baixa:", self)
    self.lbl_low.move(10, 370)
    self.txt_low = QLineEdit(self)
    self.txt_low.move(70, 370)
    self.txt_low.resize(60, 28)
    self.txt_low.setMaxLength(8)

    self.lbl_value = QLabel("Vº:", self)
    self.lbl_value.move(140, 370)
    self.txt_value = QLineEdit(self)
    self.txt_value.move(170, 370)
    self.txt_value.resize(60, 28)
    self.txt_value.setMaxLength(8)

    self.txt_service = QPlainTextEdit(self)
    self.txt_service.move(10, 410)
    self.txt_service.resize(330, 100)
    self.lbl_obs = QLabel("(Observações)", self)
    self.lbl_obs.move(10, 510)

    self.btn_calc = QPushButton("Calcular parcela", self)
    self.btn_calc.move(248, 370)
    self.btn_calc.clicked.connect(self.calc)

    self.btn_ok = QPushButton("Cadastrar", self)
    self.btn_ok.move(258, 510)
    self.btn_ok.clicked.connect(self.on_commit_clicked)

    self.btn_cancel = QPushButton("Cancelar", self)
    self.btn_cancel.move(180, 510)
    self.btn_cancel.clicked.connect(self.close)

    self.center()
    self.show()

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

  def calc(self):
    try:
      debit = self.txt_debit.text().replace(',', '.')
      debit = float(debit)
      number_parcels = int(self.txt_parcels.text())
      value_parcels = debit / number_parcels
      self.txt_value.setText("R${:.2f}".format(value_parcels).replace('.', ','))
    except ValueError:
      QMessageBox.warning(self, "Error!", "Dados incorretos!")

  def on_commit_clicked(self):
    try:
      name = self.txt_name.text()
      cpf = self.txt_cpf.text()
      born = self.txt_born.text().replace('/', "").replace('-', "")
      sex = self.txt_sex.currentText()
      city = self.txt_city.text()
      nbd = self.txt_nbd.text()
      uf = self.txt_uf.text()
      tel = self.txt_tel.text()
      cel = self.txt_cel.text()
      whatsapp = self.txt_whatsapp.text()
      email = self.txt_email.text()
      addr = self.txt_addr.text()
      number = self.txt_number.text()
      debit = self.txt_debit.text().replace('.', "").replace("R$", "")
      low = self.txt_low.text().replace('.', "").replace("R$", "")
      number_parcels = self.txt_parcels.text()
      service = self.txt_service.toPlainText()
      date_register = datetime.now()
      year = date_register.year
      month = date_register.month
      day = date_register.day
      hour = date_register.hour
      minute = date_register.minute
      sec = date_register.second

      if tel == "":
        tel = "0000000000"

      if whatsapp == "":
        whatsapp = "00000000000"

      if debit == "":
        debit = '0'

      if low == "":
        low = '0'

      if number_parcels == "":
        number_parcels = '0'

      if name != "" and cpf != "" and cpf.isdigit() and len(cpf) == 11 and born != "" \
                    and born.isdigit() and len(born) == 8 and sex != "" \
                    and sex.isalpha() and city != "" and uf != "" and uf.isalpha \
                    and tel.isdigit() and len(tel) == 10 and cel != "" and len(cel) == 11 \
                    and cel.isdigit() and whatsapp.isdigit() and len(whatsapp) == 11 \
                    and debit != '0' and low != '0' and nbd != "" and addr != "" and number != "" \
                    and debit.__contains__(',') and low.__contains__(','):

        deb = debit.replace(',', '.')
        bx = low.replace(',', '.')
        self.debitos = float(deb)
        self.baixas = float(bx)

        return commit_data(name.title().replace(" Da "," da ").replace(" De "," de ").replace(" Dos "," dos ").
                           replace(" Das ", " das "), cpf, born, sex, city.title().replace(" Da "," da ").
                           replace(" De "," de ").replace(" Do "," do ").replace(" Das ", " das ").
                           replace(" Dos ", " dos "), nbd.title().replace(" Da "," da ").replace(" De "," de ").
                           replace(" Dos "," dos ").replace(" Das ", " das ").replace(" Do ", " do "),
                           uf.upper(), tel, cel, whatsapp,
                           email, addr.title().replace(" Da "," da ").replace(" De "," de ").
                           replace(" Dos "," dos ").replace(" Das ", " das ").replace(" Do ", " do "), number,
                           self.debitos, self.baixas, number_parcels, service, year, month, day, hour, minute, sec)

      elif name != "" and cpf != "" and cpf.isdigit() and len(cpf) == 11 and born != "" \
                      and born.isdigit() and len(born) == 8 and sex != "" and nbd != "" and addr != "" \
                      and sex.isalpha() and city != "" and uf != "" and uf.isalpha and number != "" \
                      and tel.isdigit() and len(tel) == 10 and cel != "" and len(cel) == 11 \
                      and cel.isdigit() and whatsapp.isdigit() and len(whatsapp) == 11 \
                      and (debit != '0' and debit.__contains__(',')) and (low == '0'):

        deb = debit.replace(',', '.')
        bx = low.replace(',', '.')
        self.debitos = float(deb)
        self.baixas = float(bx)

        return commit_data(name.title().replace(" Da "," da ").replace(" De "," de ").replace(" Dos "," dos ").
                           replace(" Das ", " das "), cpf, born, sex, city.title().replace(" Da "," da ").
                           replace(" De "," de ").replace(" Do "," do ").replace(" Das ", " das ").
                           replace(" Dos ", " dos "), nbd.title().replace(" Da "," da ").replace(" De "," de ").
                           replace(" Dos "," dos ").replace(" Das ", " das "), uf.upper(), tel, cel, whatsapp,
                           email, addr.title().replace(" Da "," da ").replace(" De "," de ").
                           replace(" Dos "," dos ").replace(" Das ", " das "), number, self.debitos,
                           self.baixas, number_parcels, service, year, month, day, hour, minute, sec)

      elif name != "" and cpf != "" and cpf.isdigit() and len(cpf) == 11 and born != "" \
                      and born.isdigit() and len(born) == 8 and sex != "" and nbd != "" and addr != "" \
                      and sex.isalpha() and city != "" and uf != "" and uf.isalpha and number != "" \
                      and tel.isdigit() and len(tel) == 10 and cel != "" and len(cel) == 11 \
                      and cel.isdigit() and whatsapp.isdigit() and len(whatsapp) == 11 \
                      and debit == '0' and low == '0':

        return commit_data(name.title().replace(" Da "," da ").replace(" De "," de ").replace(" Dos "," dos ").
                           replace(" Das ", " das "), cpf, born, sex, city.title().replace(" Da "," da ").
                           replace(" De "," de ").replace(" Do "," do ").replace(" Das ", " das ").
                           replace(" Dos ", " dos "), nbd.title().replace(" Da "," da ").replace(" De "," de ").
                           replace(" Dos "," dos ").replace(" Das ", " das "), uf.upper(), tel, cel, whatsapp,
                           email, addr.title().replace(" Da "," da ").replace(" De "," de ").
                           replace(" Dos "," dos ").replace(" Das ", " das "), number, self.debitos,
                           self.baixas, number_parcels, service, year, month, day, hour, minute, sec)

      elif (debit != '0' and not debit.__contains__(',')) and \
           (low != '0' and not low.__contains__(',')):
        QMessageBox.warning(self, "Error!", "Valor(es) deve(m) conter centavos após vírgula!")

      elif (debit != '0' and not debit.__contains__(',')) or \
           (low != '0' and not low.__contains__(',')):
        QMessageBox.warning(self, "Error!", "Valor(es) deve(m) conter centavos após vírgula!")

      else:
        QMessageBox.warning(self, "Error!", "Dados incorretos!")
    except Exception as e:
      print(e)
      QMessageBox.warning(self, "Error!", "Dados incorretos!")

def commit_data(*args):
  try:
    conn = sqlite3.connect("client.db")
    conn.text_factory = str
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
                   "name VARCHAR(100) NOT NULL, cpf VARCHAR(11) NOT NULL UNIQUE, born VARCHAR(8), "
                   "sex VARCHAR(10), city VARCHAR(100), nbd VARCHAR(100), uf VARCHAR(2), tel VARCHAR(10), "
                   "cel VARCHAR(11), whatsapp VARCHAR(11), email VARCHAR(100), addr VARCHAR(100), "
                   "number VARCHAR(4), debit FLOAT, low FLOAT, parcel INTEGER, service VARCHAR, year VARCHAR(4), "
                   "month VARCHAR(2), day VARCHAR(2), hour VARCHAR(2), minute VARCHAR(2), sec VARCHAR(2))")

    cursor.execute("INSERT INTO data VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", args)
    conn.commit()
    conn.close()
    QMessageBox.information(win, "Informação!", "Operação realizada com sucesso!")
    return clear()
  except TypeError:
    QMessageBox.warning(win, "Error!", "Dados incorretos!")
  except sqlite3.IntegrityError:
    QMessageBox.warning(win, "Error de Cpf!", "CPF já está cadastrado!")

def clear():
  win.txt_name.setText("")
  win.txt_cpf.setText("")
  win.txt_born.setText("")
  win.txt_city.setText("")
  win.txt_nbd.setText("")
  win.txt_uf.setText("")
  win.txt_tel.setText("")
  win.txt_cel.setText("")
  win.txt_whatsapp.setText("")
  win.txt_email.setText("")
  win.txt_addr.setText("")
  win.txt_number.setText("")
  win.txt_debit.setText("")
  win.txt_low.setText("")
  win.txt_parcels.setText("")
  win.txt_value.setText("")
  win.txt_service.clear()

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = AddClient()
  sys.exit(app.exec_())
