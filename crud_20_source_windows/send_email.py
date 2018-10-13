import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from tela_ler_cliente import SearchClient

class SendEmail(QMainWindow, SearchClient):
    def __init__(self):
        sc = SearchClient()
        super(SendEmail, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Enviar por email")
        self.setFixedSize(440, 400)
        self.setWindowIcon(QIcon("mail_new.png"))

        self.lbl_from = QLabel("De:", self)
        self.lbl_from.move(10, 10)
        self.txt_from = QLineEdit(self)
        self.txt_from.move(70, 10)

        self.lbl_to = QLabel("Para:", self)
        self.lbl_to.move(10, 50)
        self.txt_to = QLineEdit(self)
        self.txt_to.move(70, 50)

        self.lbl_subject = QLabel("Assunto:", self)
        self.lbl_subject.move(10, 90)
        self.txt_subject = QLineEdit(self)
        self.txt_subject.move(70, 90)

        self.content = QPlainTextEdit(self)
        self.content.move(10, 130)
        self.content.resize(400, 200)
        self.content.insertPlainText()

        self.btn_send = QPushButton("Enviar", self)
        self.btn_send.move(310, 350)
        self.btn_send.clicked.connect(self.send)

        self.btn_close = QPushButton("Fechar", self)
        self.btn_close.move(200, 350)
        self.btn_close.clicked.connect(self.close)

        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def send(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SendEmail()
    sys.exit(app.exec_())