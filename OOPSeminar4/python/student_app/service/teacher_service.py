from domain.person_comparator import PersonComparator
from domain.teacher import Teacher
from service.i_person_service import IPersonService
from typing import List
from functools import cmp_to_key

class TeacherService(IPersonService):
    def __init__(self):
        self.teachers: List[Teacher] = []

    def get_all(self) -> List[Teacher]:
        """Возвращает список всех учителей."""
        return self.teachers

    def create(self, name: str, age: int, degree: str):
        """Создает нового учителя и добавляет его в список."""
        tchr = Teacher(name, age, degree)
        self.teachers.append(tchr)

    def sort_by_fio(self):
        """Сортирует список учителей по ФИО с использованием PersonComparator."""
        pers_comp = PersonComparator()
        self.teachers.sort(key=cmp_to_key(pers_comp.compare))
        