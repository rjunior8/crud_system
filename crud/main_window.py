# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os

class MainWindow(QMainWindow):
  def __init__(self, parent=None):
    super().__init__(parent)

    self.central = Central(parent=self)
    self.setCentralWidget(self.central)

    self.setWindowTitle("Sistema CRUD")
    self.setWindowIcon(QIcon("17_download_program.png"))
    #self.setFixedSize(640, 400)
    self.setGeometry(0, 0, 640, 400)

    main_menu = self.menuBar()
    file_menu = main_menu.addMenu("Arquivo")
    client_menu = main_menu.addMenu("Cliente")
    product_menu = main_menu.addMenu("Produto")
    backup_menu = main_menu.addMenu("Backup")

    exit_btn = QAction(QIcon("exit.png"), "Sair", self)
    exit_btn.setShortcut("Ctrl+Q")
    exit_btn.setStatusTip("Exit application")
    exit_btn.triggered.connect(self.close)
    file_menu.addAction(exit_btn)

    add_btn = QAction(QIcon("add_user.png"), "Adicionar", self)
    add_btn.setShortcut("Ctrl+A")
    add_btn.triggered.connect(self.add_client)
    client_menu.addAction(add_btn)

    search_btn = QAction(QIcon("find.png"), "Pesquisar", self)
    search_btn.setShortcut("Ctrl+F")
    search_btn.triggered.connect(self.search_client)
    client_menu.addAction(search_btn)

    update_btn = QAction(QIcon("update.png"), "Atualizar", self)
    update_btn.setShortcut("Ctrl+U")
    update_btn.triggered.connect(self.update_client)
    client_menu.addAction(update_btn)

    delete_btn = QAction(QIcon("erase.png"), "Deletar", self)
    delete_btn.setShortcut("Ctrl+D")
    delete_btn.triggered.connect(self.delete_client)
    client_menu.addAction(delete_btn)

    table_btn = QAction(QIcon("table.png"), "Tabela", self)
    table_btn.setShortcut("Ctrl+T")
    table_btn.triggered.connect(self.table_client)
    client_menu.addAction(table_btn)

    add_btn2 = QAction(QIcon("system_software_installer.png"), "Adicionar", self)
    add_btn2.setShortcut("Ctrl+Alt+A")
    add_btn2.triggered.connect(self.add_product)
    product_menu.addAction(add_btn2)

    search_btn2 = QAction(QIcon("find.png"), "Pesquisar", self)
    search_btn2.setShortcut("Ctrl+Alt+F")
    search_btn2.triggered.connect(self.search_product)
    product_menu.addAction(search_btn2)

    update_btn2 = QAction(QIcon("update.png"), "Atualizar", self)
    update_btn2.setShortcut("Ctrl+Alt+U")
    update_btn2.triggered.connect(self.update_product)
    product_menu.addAction(update_btn2)

    delete_btn2 = QAction(QIcon("erase.png"), "Deletar", self)
    delete_btn2.setShortcut("Ctrl+Alt+D")
    delete_btn2.triggered.connect(self.delete_product)
    product_menu.addAction(delete_btn2)

    table_btn2 = QAction(QIcon("table.png"), "Tabela", self)
    table_btn2.setShortcut("Ctrl+Alt+T")
    table_btn2.triggered.connect(self.table_product)
    product_menu.addAction(table_btn2)

    sale_btn = QAction(QIcon("shoppingbag_sale.png"), "Vendas", self)
    sale_btn.setShortcut("Ctrl+S")
    sale_btn.triggered.connect(self.sale)
    product_menu.addAction(sale_btn)

    backup_btn = QAction(QIcon("gnome_system.png"), "Backup", self)
    backup_btn.setShortcut("Ctrl+B")
    backup_btn.triggered.connect(self.backup)
    backup_menu.addAction(backup_btn)

  def add_client(self):
    os.system('python tela_cadastrar_cliente.py')

  def search_client(self):
    os.system('python tela_ler_cliente.py')

  def update_client(self):
    os.system('python tela_atualizar_cliente.py')

  def delete_client(self):
    os.system('python tela_deletar_cliente.py')

  def table_client(self):
    os.system('python tabela_cliente.py')

  def add_product(self):
    os.system('python tela_cadastrar_produto.py')

  def search_product(self):
    os.system('python tela_ler_produto.py')

  def update_product(self):
    os.system('python tela_atualizar_produto.py')

  def delete_product(self):
    os.system('python tela_deletar_produto.py')

  def table_product(self):
    os.system('python tabela_produto.py')

  def sale(self):
    os.system('python venda_produto.py')

  def backup(self):
    os.system('python tela_backup.py')

class Central(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)

    self.grid_layout = QGridLayout(self)

    """self.text_box = QTextEdit(self)
    self.grid_layout.addWidget(self.text_box, 0, 0, 1, 3)"""

    lbl_img = QLabel(self)
    pixmap = QPixmap("pic.jpg")
    lbl_img.setPixmap(pixmap)
    #lbl_img.move(260, 110)
    #lbl_img.resize(200, 200)
    lbl_img.show()

    #lbl_copyright = QLabel("Copyright Ⓒ Robson Marques Júnior 2018", self)
    #lbl_copyright.move(370, 370)
    #lbl_copyright.resize(260, 28)

    self.grid_layout.addWidget(lbl_img, 0, 0, 1, 3)
    #self.grid_layout.addWidget(lbl_copyright, 1, 2)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = MainWindow()
  win.show()
  sys.exit(app.exec_())


