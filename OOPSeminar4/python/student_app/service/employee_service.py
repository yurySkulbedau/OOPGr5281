from domain.person_comparator import PersonComparator
from domain.employee import Employee
from service.i_person_service import IPersonService

class EmployeeService(IPersonService):
    def __init__(self):
        self.count = 0
        self.employees = []

    def get_all(self):
        return self.employees

    def create(self, name: str, age: int):
        epls = Employee(name, age, "basic")
        self.count += 1
        self.employees.append(epls)

    def sort_by_fio(self):
        pers_comp = PersonComparator()
        self.employees.sort(key=pers_comp.compare)
        