class Ticket():
    def __init__(self, match_id,type,price,code,seat):
        self.match_id = match_id
        self.type = type 
        self.price = price
        self.code = code
        self.seat = seat


    def show_ticket(self):
        print(f"""
        ID del partido: {self.match_id}
        Tipo de entrada: {self.type}
        Precio: {self.price}
        Codigo:  {self.code}
        seat: {self.seat}
        """)
