class CoinDispenser:
    def __init__(self, nominal):
        self._nominal = nominal

    @property
    def nominal(self):
        return self._nominal

    @nominal.setter
    def nominal(self, value):
        self._nominal = value

    # def __str__(self):
    #     return "Номинал монеты равен " + str(self.nominal)
        
    def __str__(self):
        return f"You have {self.nominal} rubles"

    # def getSumm(self, insertCoin, outCoin):
    #     summCoin = insertCoin + outCoin
    #     return summCoin

    def get_sum(self):
        return self.nominal

    def give_change(self, price):
        # if price < self.nominal:
        change = self.nominal - price if price < self.nominal else self.nominal
        self.nominal = 0
        return change
        # return self.nominal

    # def dispense(self, price):
    #     return False

