class Product():
    def __init__(self, name, quantity, price, stock, adicional):
        self.name = name 
        self.quantity = quantity
        self.price = price
        self.stock = stock
        self.adicional = adicional


    def show_product(self):
        return f"""
        
        Name = {self.name}
        Quantity = {self.quantity}
        Price = {self.price}
        Type = {self.type}
        Adicional = {self.adicional}
        
        """
        