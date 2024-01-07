from domain.person import Person


class Teacher(Person):
    def __init__(self, name, age, degree):
        super().__init__(name, age)
        self.degree = degree
    
    def __str__(self):
        return f"{self.name}, Возраст: {self.age}, Степень: {self.degree}"