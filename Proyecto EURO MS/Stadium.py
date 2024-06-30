class Stadium():
    def __init__(self,id,name,city,capacity,restaurants):
        self.id = id 
        self.name = name 
        self.city = city
        self.capacity= capacity 
        self.restaurants = restaurants
        self.seats_taken = []
        self.seats = []


    def __str__(self):
        return f'Stadium: {self.name}, Stadium ID'

    def show_stadium(self):
        print(self.name)
        

    def show_stadium_id(self):
        print(f"""
        {self.id} - {self.name}
        """)

    def show_capacity(self):
        print(self.capacity)


    def map(self,capacity):
        x = int((capacity[0] + capacity[1])) // 10
        y = 10
        for _ in range(x):
            row = ["x" if f"{_}-{b}" in self.seats_taken else f"{_}-{b}" for b in range(y)]
            self.seats.append(row)
            print("|".join(row))
            print()

    def show_restaurant(self):
        print(self.restaurants)