from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QFont

class MyWindow(QWidget):
    def __init__(self, assort):
        super().__init__()

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
            button.clicked.connect(self.on_button_clicked)  # Подключите слот (метод), который будет вызываться при нажатии кнопки
            button.setFont(self.mainFont)
            layout.addWidget(button)

        self.setLayout(layout)
        layout.addLayout(inputLayout)

        self.setStyleSheet("background-color: rgb(128, 184, 255);")

    def on_button_clicked(self):
        sender = self.sender()
        print(f"Button {sender.text()} clicked!")
