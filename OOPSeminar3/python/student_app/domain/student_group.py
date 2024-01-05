class StudentGroup:
    def __init__(self, group, idGroup):
        self.group = group
        self.idGroup = idGroup


    def getGroup(self):
        return self.group

    def setGroup(self, group):
        self.group = group

    def getIdGroup(self):
        return self.idGroup

    def setIdGroup(self, idGroup):
        self.idGroup = idGroup

    def __str__(self):
        return f'Группа №{self.getIdGroup()}, количество студентов: {len(self)}\n' + '\n'.join([str(student) for student in self.group])

    def __iter__(self):
        return iter(self.group)
    
    def __len__(self):
        return len(self.group)
    
    # Для сортировки, кажется, достаточно одной функции __lt__()
    def __lt__(self, other, key=None):
        """
        По умолчанию сортируем по количеству студентов, затем по идентификатору группы
        """
        if key is None:
            key = lambda x: (len(x), x.idGroup)

        return key(self) < key(other)
  
    # def __gt__(self, other): 
    #     return len(self) > len(other) 
  
    # def __le__(self, other): 
    #     return len(self) <= len(other) 
  
    # def __ge__(self, other): 
    #     return len(self) >= len(other) 
  
    # def __eq__(self, other): 
    #     return len(self) == len(other) 