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
    coinDisp = CoinDispenser(0)
    disp = Display()

    venMachine = VendingMachine(hold1, coinDisp, assort, disp)

    for prod in venMachine.getProducts():
        print(prod)


    app = QApplication(sys.argv)
    # myFrame = MainFrame()
    myFrame = MyWindow(coinDisp, venMachine)
    myFrame.show()
    sys.exit(app.exec())
