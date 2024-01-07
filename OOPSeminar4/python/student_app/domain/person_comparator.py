from typing import TypeVar  # TypeVar - это средство в Python для создания обобщенных (generic) типов. 
from domain.person import Person

T = TypeVar('T', bound='Person')  # создает обобщенный тип T, который ограничен типом Person.
# т.е. PersonComparator может работать с любым подклассом Person или самим Person.

class PersonComparator:
    def compare(self, o1: T, o2: T) -> int:
        """Сравнивает два объекта типа T (или его подклассов) на основе их имен.
        Функция использует сравнение строк, полученных через метод get_name().

        Args:
            o1 (T): Первый объект для сравнения.
            o2 (T): Второй объект для сравнения.

        Returns:
            int: отрицательное число, если o1 < o2,
             положительное число, если o1 > o2,
             и ноль, если o1 равен o2 по именам.
        """
        return (o1.get_name() > o2.get_name()) - (o1.get_name() < o2.get_name())
    