class StudentStream:
    def __init__(self, groups: list, id_stream: int):
        self.groups = groups
        self.id_stream = id_stream

    def get_stream(self):
        return self.stream

    def set_stream(self, stream):
        self.stream = stream

    def get_id_stream(self):
        return self.id_stream

    def set_id_stream(self, id_stream):
        self.id_stream = id_stream
    
    def __str__(self) -> str:
        return f'Поток #{self.id_stream} включает в себя группы ' + ', '.join([str(group.getIdGroup()) for group in self.groups])
    
    def __iter__(self):
        return iter(self.groups)