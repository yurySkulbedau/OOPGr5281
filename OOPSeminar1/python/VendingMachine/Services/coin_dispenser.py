class CoinDispenser:
    def __init__(self, nominal):
        self.nominal = nominal


    # def __str__(self):
    #     return "Номинал монеты равен " + str(self.nominal)
        
    def __str__(self):
        return f"You put {self.nominal} rubles"

    def getSumm(self, insertCoin, outCoin):
        summCoin = insertCoin + outCoin
        return summCoin

    def giveChahge(self, summCoin, price):
        if price < summCoin:
            return summCoin - price
        return 0

    # def dispense(self, price):
    #     return False