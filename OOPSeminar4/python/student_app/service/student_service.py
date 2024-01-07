from domain.person_comparator import PersonComparator
from domain.student import Student
from service.i_person_service import IPersonService

class StudentService(IPersonService):
    def __init__(self):
        self.count = 0
        self.students = []

    def get_all(self):
        return self.students

    def create(self, name: str, age: int):
        stud = Student(name, age)
        self.count += 1
        self.students.append(stud)

    def sort_by_fio(self):
        pers_comp = PersonComparator()
        self.students.sort(key=pers_comp.compare)
        