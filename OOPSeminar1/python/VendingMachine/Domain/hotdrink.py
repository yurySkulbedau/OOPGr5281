from Domain.product import Product

class HotDrink(Product):  
    def __init__(self, price=-1, place=-1, name="Неизвестно", id=-1, hot_drink_temp=0):
        super().__init__(price, place, name, id)
        self.hot_drink_temp = hot_drink_temp
    
    def get_hot_drink_temp(self):
        return self.hot_drink_temp
    
    def set_hot_drink_temp(self, hot_drink_temp):
        self.hot_drink_temp = hot_drink_temp

    def __str__(self):
        return super().__str__() + f"temperature = {self.get_hot_drink_temp()}"