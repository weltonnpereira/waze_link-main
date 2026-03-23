import urllib.parse
import os

def generate_waze_link(address: str) -> str:
    format_address = urllib.parse.quote_plus(address)
    link = f"https://waze.com/ul?q={format_address}"
    return link

if __name__ == "__main__":
    while True:
        address = input("Digite o endereço completo: ")
        link = generate_waze_link(address)
        print("\n🔗 Link do Waze:")
        print(link)
import sys
import logging
from PyQt5.QtWidgets import (QApplication)

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from features.generator import WazeLink
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QHBoxLayout, QComboBox, QScrollArea, QFrame
from PyQt5.QtCore import QSize

import mysql.connector as mc 

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

class WazeLinkGUI(QWidget):
    def __init__(self): 
        super().__init__()
          
        self.logo = QLabel("Mani's Esfirras", self)
        self.link_label = QLabel("Digite o endereço completo:", self)
        self.link_input = QLineEdit(self)
        self.get_link_button = QPushButton("Formatar", self)

        self.res_link = QLabel()
        self.res_link.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.copy_button = QPushButton("Copiar Link")
        self.copy_button.setEnabled(False)
        self.copied_link = QLabel()

        self.initUI()
        
    def initUI(self):
        vbox = QVBoxLayout()
        vbox.setContentsMargins(50, 30, 50, 50)

        vbox.addWidget(self.logo)
        vbox.addWidget(self.link_label)
        vbox.addWidget(self.link_input)
        vbox.addWidget(self.get_link_button)
        vbox.addWidget(self.res_link)
        vbox.addWidget(self.copy_button)
        vbox.addWidget(self.copied_link)

        self.setLayout(vbox)

        self.logo.setAlignment(Qt.AlignCenter)
        self.link_label.setAlignment(Qt.AlignCenter)
        self.link_input.setAlignment(Qt.AlignCenter)
        self.res_link.setAlignment(Qt.AlignCenter)
        self.copied_link.setAlignment(Qt.AlignCenter)

        self.logo.setObjectName("logo")
        self.link_label.setObjectName("link_label")
        self.link_input.setObjectName("link_input")
        self.get_link_button.setObjectName("get_link_button")
        self.res_link.setObjectName("res_link")
        self.copied_link.setObjectName("copied_link")

        self.setStyleSheet("""
            QWidget{
                background-color: #750101;
            }
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#logo{
                font-size: 40px;
                font-weight: bold;
                color: #e3812b;
            }
            QLabel#link_label{
                color: white;
                font-size: 40px;
                font-weight: bold;
            }
            QLineEdit#link_input{
                color: white;
                font-size: 30px;   
                background: transparent;
                border: none;
                outline: none;
                border: 2px solid rgba(255, 255, 255, 0.2);
                border-radius: 10px;
                color: #fff;
                padding: 5px 5px;
            
            }
            QPushButton{
                padding: 5px 5px;
                font-size: 30px;
                color: white;
                font-weight: bold;
                background-color: #e3812b;
                border-radius: 10px;
            }          
            QLabel#res_link{
                font-size: 35px;
                color: white;
            }
            QLabel#copied_link{
                font-size: 35px;
                color: white;
            }
        """)

        self.get_link_button.clicked.connect(self.get_link)
        self.copy_button.clicked.connect(self.copy_link)
        
    def get_link(self):
        link = self.link_input.text()

        if not link:
            self.res_link.setText("Digite um endereço.")
            self.copy_button.setEnabled(False)
            self.copied_link.clear()
            self.adjustSize()
            return 

        address = WazeLink.generate_waze_link(link)
        self.res_link.setText(address)
        self.copy_button.setEnabled(True)
        self.copied_link.clear()
        self.link_input.clear()

        self.adjustSize()

    def copy_link(self):
        QApplication.clipboard().setText(self.res_link.text())
        self.copied_link.setText("Link Copiado.")
        
class RegisterProductsGUI(QWidget):
    def __init__(self):
        super().__init__()
          
        self.logo = QLabel("Mani's Esfirras", self)
        self.product_label = QLabel("Registre seus itens:", self)
        self.product_input = QLineEdit(self)
        self.price_input = QLineEdit(self)
        self.register_button = QPushButton("Registrar", self)

        self.initUI()
        
    def initUI(self):
        vbox = QVBoxLayout()
        vbox.setContentsMargins(50, 50, 50, 50)
        vbox.setSpacing(15)

        vbox.addWidget(self.logo)
        vbox.addSpacing(10)

        vbox.addWidget(self.product_label)
        vbox.addSpacing(20)

        vbox.addWidget(self.product_input)
        vbox.addSpacing(15)

        vbox.addWidget(self.price_input)
        vbox.addSpacing(25)

        vbox.addWidget(self.register_button)

        vbox.addStretch()
        
        self.setLayout(vbox)

        self.logo.setAlignment(Qt.AlignCenter)
        self.product_label.setAlignment(Qt.AlignCenter)
        self.product_input.setAlignment(Qt.AlignCenter)
        self.price_input.setAlignment(Qt.AlignCenter)
        
        self.product_input.setPlaceholderText("Nome do produto")
        self.price_input.setPlaceholderText("Preço do produto")

        self.logo.setObjectName("logo")
        self.product_label.setObjectName("product_label")
        self.product_input.setObjectName("product_input")
        self.price_input.setObjectName("price_input")
        self.register_button.setObjectName("register_button")

        self.setStyleSheet("""
            QWidget{
                background-color: #750101;
            }
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#logo{
                font-size: 40px;
                font-weight: bold;
                color: #e3812b;
            }
            QLabel#product_label{
                color: white;
                font-size: 40px;
                font-weight: bold;
            }
            QLineEdit{
                color: white;
                font-size: 30px;   
                background: transparent;
                border: none;
                outline: none;
                border: 2px solid rgba(255, 255, 255, 0.2);
                border-radius: 10px;
                color: #fff;
                padding: 5px 5px;
            
            }
            QPushButton{
                padding: 5px 5px;
                font-size: 30px;
                color: white;
                font-weight: bold;
                background-color: #e3812b;
                border-radius: 10px;
            }          
        """)
        
        self.register_button.clicked.connect(self.registerItem)
        
    def registerItem(self):
        product = self.product_input.text()
        price_text = self.price_input.text()
        
        if not product:
            self.product_label.setText("Por favor, digite o nome do produto.")
            # self.adjustSize()
            return
        
        if not price_text:
            self.product_label.setText("Por favor, digite o preço do produto.")
            # self.adjustSize()
            return
        
        price = price_text.replace(" ", "").replace(",", ".")
        
        try:
            decimal = Decimal(price)
            
            if decimal <= 0:
                self.product_label.setText("O preço do produto não pode ser menor que zero.")
                return
            
            if decimal.as_tuple().exponent < -2:
                self.product_label.setText("Use somente duas casas decimais.")
                return
            
            decimal = decimal.quantize(Decimal("0.01"))
            price_cents = int(decimal * 100)
        except InvalidOperation:
            self.product_label.setText("Digite um valor válido.")
            return
        
        print("Preço do produto inserido pelo user: ", price_text)
        print("Preço do produto em centavos: ", price_cents)
        
        self.product_label.setText("Produto cadastrado com sucesso!")
        return self.add_product(product, price_cents)
    
    def add_product(self, name, price):
        query = QSqlQuery()
        sql = f"INSERT INTO products (name, price) VALUES (?, ?)"
        
        query.prepare(sql)
        query.addBindValue(name)
        query.addBindValue(price)
        
        if query.exec_():
            print(f"Produto {name} salvo!")
            return True
        else:
            err = query.lastError().text()
            if "UNIQUE constraint failed" in err:
                self.product_label.setText(f"{name} já existe!")
                print(f"Erro: O produto '{name}' já existe.")
            else:
                print("Erro ao inserir:", err)
            return False
        
class CalculateItemsGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.items_list = []
        
        self.initUI()
        
    def initUI(self):
        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(50, 30, 50, 50)
        self.vbox.setSpacing(15)
        
        self.logo = QLabel("Mani's Esfirras")
        self.logo.setObjectName("logo")
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setStyleSheet("font-size: 40px; font-weight: bold; color: #e3812b;")
        
        self.desc_label = QLabel("Adicione produtos para calcular o preço")
        self.desc_label.setObjectName("product_label")
        self.desc_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setStyleSheet("font-size: 30px; font-weight: bold; color: white;")
        
        self.vbox.addWidget(self.logo)
        self.vbox.addWidget(self.desc_label)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("background: transparent; border: none;")

        self.scroll_content = QWidget()
        self.items_vbox = QVBoxLayout(self.scroll_content)
        self.items_vbox.setAlignment(Qt.AlignTop)
        self.scroll.setWidget(self.scroll_content)
        
        self.vbox.addWidget(self.scroll)
        
        self.footer_layout = QHBoxLayout()
        
        self.total_label = QLabel("Total: R$ 0,00")
        self.total_label.setStyleSheet("font-size: 25px; color: white; font-weight: bold;")
        
        self.clear_all_btn = QPushButton("Limpar tudo")
        self.clear_all_btn.setFixedWidth(250)
        self.clear_all_btn.setStyleSheet("background-color: #e3812b; font-size: 20px; font-weight: bold; border-radius: 10px;")
        self.clear_all_btn.clicked.connect(self.clear_all_items)
        
        self.add_btn = QPushButton("Adicionar Item")
        self.add_btn.setFixedWidth(250)
        self.add_btn.clicked.connect(self.add_item_row)
        self.add_btn.setStyleSheet("background-color: #e3812b; font-size: 20px; font-weight: bold; border-radius: 10px;;")

        self.footer_layout.addWidget(self.total_label)
        self.footer_layout.addStretch()
        self.footer_layout.addWidget(self.clear_all_btn)
        self.footer_layout.addWidget(self.add_btn)
        
        self.vbox.addLayout(self.footer_layout)
        self.setLayout(self.vbox)
        
        self.add_item_row()
        
    def add_item_row(self):
        row_widget = QFrame()
        row_layout = QHBoxLayout(row_widget)
        row_layout.setContentsMargins(0, 5, 0, 5)
        
        combo = QComboBox()
        combo.setPlaceholderText("Selecione um produto")
        combo.setMinimumHeight(40)
        combo.setStyleSheet(self.get_combo_style())
        
        self.load_products(combo)
        
        price_display = QLineEdit()
        price_display.setPlaceholderText("R$: 0,00")
        price_display.setReadOnly(True)
        price_display.setFixedWidth(120)
        price_display.setAlignment(Qt.AlignCenter)
        price_display.setStyleSheet("font-size: 20px; color: white; font-weight: bold;")
        
        remove_btn = QPushButton("✕")
        remove_btn.setFixedHeight(40)
        remove_btn.setStyleSheet("background-color: #a30000; font-size: 18px; border-radius: 5px;")
        
        combo.currentIndexChanged.connect(lambda: self.update_price(combo, price_display))
        
        remove_btn.clicked.connect(lambda: self.remove_item(row_widget, combo))
        
        row_layout.addWidget(combo, 3)
        row_layout.addWidget(price_display, 1)
        row_layout.addWidget(remove_btn)
        
        self.items_vbox.addWidget(row_widget)
        
        item_data = {'widget': row_widget, 'combo_product': combo, 'price': price_display}
        self.items_list.append(item_data)
        
    def load_products(self, combo_product):
        query = QSqlQuery("SELECT name, price FROM products")
        if not query.exec_():
            print("Erro ao buscar produtos:", query.lastError().text())
            return
        
        while query.next():
            name = query.value(0)
            price = query.value(1)
            combo_product.addItem(name, price)
        combo_product.setCurrentIndex(-1)
        
    def remove_item(self, row_widget, combo):
        self.items_list = [item for item in self.items_list if item['combo_product'] != combo]
        row_widget.deleteLater()
        self.calculate_total()
        
    def clear_all_items(self):
        for item in self.items_list:
            item['widget'].deleteLater()
            
        self.items_list.clear()
        self.calculate_total()
        self.add_item_row()
            
    def update_price(self, combo, price):
        price_cents = combo.currentData()
        if price_cents is not None:
            price_real = price_cents / 100
            price.setText(f"R$ {price_real:,.2f}")
        self.calculate_total()
        
    def calculate_total(self):
        total = 0
        for item in self.items_list:
            price_cents = item['combo_product'].currentData()
            if price_cents:
                total += price_cents
                
        total_real = total / 100
        self.total_label.setText(f"Total: R${total_real:,.2f}")
        
    def get_combo_style(self):
        return """
            QComboBox {
                color: white; font-size: 20px; background: transparent;
                border: 2px solid rgba(255, 255, 255, 0.2); border-radius: 10px; padding: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: #750101; color: white; selection-background-color: #e3812b;
            }
        """

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("shared/icons/logo.ico"))
        
        if self.create_connection():
            self.create_table()
            
        self.setWindowTitle("Mani's Manager")
        self.resize(900, 600)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.main_layout = QHBoxLayout(self.central_widget)

        self.menu_widget = QWidget()
        self.menu_widget.setFixedWidth(80)
        self.menu_layout = QVBoxLayout(self.menu_widget)

        self.btn_waze = QPushButton()
        self.btn_waze.setIcon(QIcon("shared/icons/link.png"))
        self.btn_waze.setIconSize(QSize(24, 24))
        
        self.btn_products = QPushButton()
        self.btn_products.setIcon(QIcon("shared/icons/products.png"))
        self.btn_products.setIconSize(QSize(24, 24))
        
        self.btn_calculate = QPushButton()
        self.btn_calculate.setIcon(QIcon("shared/icons/calculator.png"))
        self.btn_calculate.setIconSize(QSize(24, 24))

        self.menu_widget.setObjectName("menu")
        
        self.btn_waze.setObjectName("menu_button")
        self.btn_products.setObjectName("menu_button")
        self.btn_calculate.setObjectName("menu_button")

        self.menu_layout.addWidget(self.btn_waze)
        self.menu_layout.addWidget(self.btn_products)
        self.menu_layout.addWidget(self.btn_calculate)
        self.menu_layout.addStretch()

        self.stack = QStackedWidget()

        self.waze_screen = WazeLinkGUI()
        self.products_screen = RegisterProductsGUI()
        self.calculate_items = CalculateItemsGUI()

        self.stack.addWidget(self.waze_screen)
        self.stack.addWidget(self.products_screen)
        self.stack.addWidget(self.calculate_items)

        self.main_layout.addWidget(self.menu_widget)
        self.main_layout.addWidget(self.stack)

        self.stack.setCurrentIndex(0)

        self.btn_waze.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.btn_products.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.btn_calculate.clicked.connect(lambda: self.stack.setCurrentIndex(2))

        self.setStyleSheet("""
            QWidget{
                background-color: #750101;
            }
            QPushButton#menu_button{
                padding: 15px;
                font-size: 18px;
                color: white;
                font-weight: bold;
                background-color: #e3812b;
                border-radius: 8px;
            }
            QPushButton#menu_button:hover{
                background-color: #ff9f45;
            }
        """)
        
    def create_connection(self):
        # criamos a conexão iniciando qual será o driver dele
        # no caso carregamos o driver do mysql
        db = QSqlDatabase.addDatabase("QSQLITE")
        # db.setHostName(os.environ.get("host"))
        # db.setDatabaseName(os.environ.get("database"))
        db_name = os.environ.get("database")
        # db.setUserName(os.environ.get("user"))
        # db.setPassword(os.environ.get("password"))
        
        if not db_name:
            print("Erro: variavel de ambiente database não encontrada.")
            return False
        
        db.setDatabaseName(db_name)
        
        if not db.open():
            print("Erro ao conectar: ", db.lastError().text())
            return None
        
        print("Mysql conectado com sucesso!")
        return db
    
    def create_table(self, table_name="products"):
        query = QSqlQuery()
        sql = f"""
        CREATE TABLE IF NOT EXISTS `{table_name}` (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            price INTEGER NOT NULL
        );
        """
        
        if query.exec_(sql):
            print(f"Tabela {table_name} criada/carregada com sucesso!")
        else:
            print("Erro ao criar a tabela: ", query.lastError().text())
        
    

def main():
    # cria a aplicação
    app = QApplication(sys.argv)
    # janela principal
    window = MainWindow()
    window.show()
    # looping de eventos
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()