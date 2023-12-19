import sys
from PyQt6.QtWidgets import QApplication

from Services.coin_dispenser import CoinDispenser
from Services.display import Display
from Services.holder import Holder
from Services.vending_machine import VendingMachine
# from main_frame import MainFrame
from app_window import MyWindow

from assortiment import assort


if __name__ == "__main__":   

    hold1 = Holder(4, 4)
    coinDesp = CoinDispenser(0)
    disp = Display()

    venMachine = VendingMachine(hold1, coinDesp, assort, disp)

    for prod in venMachine.getProducts():
        print(prod)


    app = QApplication(sys.argv)
    # myFrame = MainFrame(venMachine.getProducts())
    myFrame = MyWindow(venMachine.getProducts())
    myFrame.show()
    sys.exit(app.exec())
