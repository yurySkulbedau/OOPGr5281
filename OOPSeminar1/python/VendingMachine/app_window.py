from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QFont

from Domain.product import Product

class MyWindow(QWidget):
    def __init__(self, coin_dispenser, vending_machine):
        super().__init__()

        self.coin_dispenser = coin_dispenser
        self.vending_machine = vending_machine
        assort = vending_machine.getProducts()

        self.setWindowTitle("VendingMachine")
        self.mainFont = QFont("Segoe print", 18)
        self.secondFont = QFont("Segoe print", 12)

        self.tfMoney = QLineEdit()
        self.tfMoney.setFont(self.mainFont)

        inputLayout = QHBoxLayout()
        inputLayout.addWidget(QLabel("Put your money:", font=self.secondFont))
        inputLayout.addWidget(self.tfMoney)

        layout = QVBoxLayout()

        for product in assort:
            button = QPushButton(f"{product.name}, {product.price}")
            button.clicked.connect(lambda checked, p=product: self.on_button_clicked(p))
            button.setFont(self.mainFont)
            layout.addWidget(button)

        self.setLayout(layout)
        layout.addLayout(inputLayout)

        self.setStyleSheet("background-color: rgb(128, 184, 255);")

    def on_button_clicked(self, p: Product):
        sender = self.sender()  # self.sender() возвращает объект, который отправил текущий сигнал. В контексте кода, self.sender() вернет объект кнопки, которая была нажата.
        money = self.tfMoney.text()
        self.coin_dispenser.nominal = int(money) if money else 0

        print(f"Button {sender.text()} clicked! Deposited money: {self.coin_dispenser.get_sum()}")

        self.vending_machine.buyProduct(p)
