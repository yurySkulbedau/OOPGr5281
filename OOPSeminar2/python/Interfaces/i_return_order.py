from abc import ABC, abstractmethod

class iReturnOrder(ABC):
    @abstractmethod
    def initiate_return(self, order_id: int) -> str:
        pass

    @abstractmethod
    def check_return_status(self, order_id: int) -> str:
        pass