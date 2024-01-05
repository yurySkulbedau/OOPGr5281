class StudentSteam:
    def __init__(self, groups: list, id_steam: int):
        self.groups = groups
        self.id_steam = id_steam

    # Кажется, в Python логичнее использовать более простой способ для определения полей класса с помощью только self.field = value 
    # вместо методов get_field и set_field.
    
    def __str__(self) -> str:
        return f'Поток #{self.id_steam} включает в себя группы ' + ', '.join([str(group.getIdGroup()) for group in self.groups])
    
    def __iter__(self):
        return iter(self.groups)