from typing import List, TypeVar

from domain.person import Person
from domain.teacher import Teacher

T = TypeVar('T', bound='Person')

class AccountController:
    @staticmethod
    def pay_salary(person: Teacher, salary: int) -> None:
        print(f"{person.name} выплачено зарплата {salary}р.")

    @staticmethod
    def average_age(people: List[T]) -> float:
        """Возвращает средний возраст списка людей."""
        if not people:
            return 0.0
        total_age = sum(person.age for person in people)
        return total_age / len(people)
    