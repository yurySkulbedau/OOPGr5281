from Classes.actor import Actor


class PromoClient(Actor):
    number_of_participants = 50  # типа статическое поле   

    def __init__(self, name: str, promo: str, client_id: int, participants=number_of_participants):
        super().__init__(name)
        self.promo = promo
        self.client_id = client_id
        self.participants = participants
    
    
    def isTakeOrder(self):
        return super().getTakeOrder()

    def setTakeOrder(self, takenOrder):
        super().setTakeOrder(takenOrder)

    def isMakeOrder(self):
        return super().getMakeOrder()

    def setMakeOrder(self, makeOrder):
        super().setMakeOrder(makeOrder)

    def getActor(self):
        return self.getName()

    def getName(self):
        return super().getName()

    def setName(self, name):
        self.name = name

    def get_client_id(self):
        return self.client_id

    def set_client_id(self, client_id):
        self.client_id = client_id