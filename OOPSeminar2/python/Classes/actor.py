from Interfaces.i_actor_behaviour import iActorBehaviour
from Interfaces.i_return_order import iReturnOrder

class Actor(iActorBehaviour, iReturnOrder):
    """
    Базовый класс Actor с использованием интерфейсов iActorBehaviour и iReturnOrder.
    """

    name: str
    isTakeOrder: bool = False
    isMakeOrder: bool = False

    def __init__(self, name: str):
        """Инициализация объекта Actor.
        Args:
            name (str): Имя актора.
        """
        self.name = name

    def setName(self, name: str):
        """Установка имени актора.
        Args:
            name (str): Новое имя актора.
        """
        self.name = name

    def getName(self) -> str:
        """Получение имени актора.
        Returns:
            str: Имя актора.
        """
        return self.name
    
    def setTakeOrder(self, value: bool):
        """Установка состояния принятия заказов.
        Args:
            value (bool): Новое состояние.
        """
        self.isTakeOrder = value

    def getTakeOrder(self) -> bool:
        """Получение состояния принятия заказов.
        Returns:
            bool: True, если актор пролучил свои заказы, False - в противном случае.
        """
        return self.isTakeOrder
    
    def setMakeOrder(self, value: bool):
        """Установка состояния создания заказов.
        Args:
            value (bool): Новое состояние.
        """
        self.isMakeOrder = value

    def getMakeOrder(self) -> bool:
        """Получение состояния создания заказов.
        Returns:
            bool: True, если актор сделал заказ, False в противном случае.
        """
        return self.isMakeOrder
    
    def initiate_return(self, order_id: int) -> str:
        """Инициирование возврата товара.
        Args:
            order_id (int): Идентификатор заказа (РЕАЛИЗОВАТЬ в других методах).
        Returns:
            str: Сообщение о начале возврата.
        """
        print(f"Initiating return for order {order_id} from {self.getName()}")

    def check_return_status(self, order_id: int) -> str:
        """Проверка статуса возврата товара.
        Args:
            order_id (int): Идентификатор заказа.
        Returns:
            str: Сообщение о проверке статуса возврата.
        """
        print(f"Checking return status for order {order_id} from {self.getName()}")




