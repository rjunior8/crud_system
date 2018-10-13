import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QIcon


class Backup(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.setWindowTitle("Backup")
    self.setFixedSize(280, 130)
    self.setWindowIcon(QIcon("progress_bar.png"))
    
    self.pbar = QProgressBar(self)
    self.pbar.setGeometry(55, 40, 200, 25)
    
    self.btn = QPushButton("Iniciar", self)
    self.btn.move(100, 80)
    self.btn.clicked.connect(self.do_action)
    
    self.timer = QBasicTimer()
    self.step = 0
    
    self.center()
    self.show()

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

  def timerEvent(self, e):
    if self.step >= 100:
      self.timer.stop()
      self.btn.setText("Fechar")
      return

    self.step = self.step + 1
    self.pbar.setValue(self.step)

  def do_action(self):
    if self.timer.isActive():
      self.timer.stop()
      self.btn.setText("Iniciar")
    elif self.btn.text() == "Fechar":
      self.btn.clicked.connect(self.close)
    else:
      self.timer.start(100, self)
      self.btn.setText("Parar")


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ex = Backup()
  sys.exit(app.exec_())
