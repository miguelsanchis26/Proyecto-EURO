class Customer:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def show_attr(self):
        return f'Name:{self.name}, ID: {self.id}, Age:{self.age}'