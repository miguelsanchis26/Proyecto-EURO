class Restaurant:
    def __init__(self, name, products) :
        self.name = name
        self.products = products

    def __str__(self):
       return f'Nombre: {self.name}, Productos: {self.products}'