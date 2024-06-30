import requests
import json
from Customer import *
from Match import *
from Product import *
from Restaurant import *
from Stadium import *
from Team import *
from Ticket import *
#Al rededor de este codigo se puede ver que realice el codigo en ingles y español, 
# ya que algunas cosas se me facilitaban escribirlo en ingles y otras en español.

class Main():

    #Primero creo las listas que se va utilizar a lo largo del programa
    def __init__(self):
        self.teams = []
        self.stadiums = [] 
        self.matches = []
        self.customers = []
        self.restaurants = []
        self.tickets_sales = []
        self.seats_taken = []
        self.seats = []
        self.codes = []
        self.products = []
        self.alcoholic_beverages = []
        self.non_alcoholic_beverages = []
        self.food_plate = []
        self.food_package = []
        self.receipt = []

    def info_api(self):
        url_teams ='https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json' 
        e = requests.get(url_teams)
        if e.status_code == 200:
            e = e.json()
            for team in e:
                team = Team(team["id"],team["code"],team["name"],team["group"])
                self.teams.append(team)
#Para cada  API, extraje sus valores y los converti en atributos para poder crear el objeto team 

        url_stadiums = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json'
        stadiums = requests.get(url_stadiums)
        if stadiums.status_code == 200:
            stadiums = stadiums.json()
            for stadium in stadiums:
                stadium = Stadium(stadium["id"],stadium["name"],stadium["city"],stadium["capacity"],stadium["restaurants"])
                self.stadiums.append(stadium)
            for a in stadiums:
                for restaurant in a["restaurants"]:
                    restaurant = Restaurant(restaurant["name"], restaurant["products"])
                    self.restaurants.append(restaurant)
            for b in stadiums:
                for k in b["restaurants"]:
                    for product in k["products"]:
                        product = Product(product["name"],product["quantity"],product["price"],product["stock"],product["adicional"])
                        self.products.append(product)
#Para cada stadium/ estadio en la API, extraje sus valores y los converti en atributos para poder crear el objeto stadium
# Tambien converti los restaurants en objetos y sus products en objetos, por si mas adelante me hacian falta 

        url_matches = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json'
        matches = requests.get(url_matches)
        if matches.status_code == 200:
            matches = matches.json()
            home = None
            away = None 
            st = None
            attendance = 0
            for _ in matches:
                for team in self.teams:
                    if team.name == _["home"]:
                        home = team 
                    elif team.name == _["away"]:
                        away = team 
                for stadium in self.stadiums:
                    if stadium.id == _["stadium Id"]:
                        st = stadium
                        
                match = Match(_["id"],home,away, _["date"],st,attendance)
                self.matches.append(match)

        #Aca esta la  Data de la api de los equipos/teams,iteramos sobre la respuesta que creamos para poder cargar la informacion en una lista
        response=requests.request("GET",'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json')
        response=json.loads(response.text)
        for i in range (0,len(response)):
            id=response[i]['id']
            code=response[i]['code']
            name=response[i]['name']
            group=response[i]['group']

            self.teams.append(Team(id,code,name,group))

    def sort_matches(self):
        option = input("""
        Select how do you wish to sort Euro 2024 matches:

        [1] Team
        [2] Stadium
        [3] Date

        Option:
        """)
        while not option.isnumeric() or int(option) not in range(1,4):
            option = input("\nERROR, Select a valid option: ")
#Hice un mini menu para que se pudiera escoger el filtro a utilizar para buscar los matchs

        if option == "1":
            for _ in self.teams:
                _.show_country()
            option2 = input("Team name to look for: ")

            matchs_equipo = []
            for _ in self.matches:
                if option2 == _.home:
                    matchs_equipo.append(_)
                elif option2 == _.away1:
                    matchs_equipo.append(_)
            for _ in matchs_equipo:
               #Para que esto funcione tenemos que poner el home/casa team primero y despues away/visitante despues 
               # Despues para que aparezca el estadio, dia y hora, y el ID del partido 
                _.home.show_team() 
                print("vs")
                _.away.show_team()
                print("Stadium:") 
                _.stadiumId.show_stadium()
                print("Date:") 
                _.show_date()
                print("Match ID:") 
                _.show_match_id()
                print("""
                
                """)
#En el filtro por equipo, se muestra el nombre del equipo. 
# Si ese nombre coincide con el del equipo visitante o local de un partido, ese partido se guarda y se lo muestra       
               
        
        elif option == "2":
            all_stadium_id = []
            for _ in self.stadiums:
                _.show_stadiumId()
                all_stadium_id.append(_.stadiumId)

            option3 = input("Type the Stadium ID to look for: ")
            while option3 not in all_stadium_id:
                option3 = int(input("ERROR, type the Stadium ID to look for: "))
            matches_stadiums = []
            for _ in self.matches:
                if option3 == _.stadiumId:
                    matches_stadiums.append(_)
            for _ in matches_stadiums:
                
                _.home.show_team() 
                print("vs")
                _.away.show_team()
                print("Stadium:") 
                _.stadiumId.show_stadium()
                print("Date:") 
                _.show_date()
                print("Match ID:") 
                _.show_match_id()
                print("""
                
                """)

#En esta opcion lo que se hizo fue parecido a la anterior, solo que se utilizo el ID del estadio

        else:
            option4 = input("Type the date which to look for [FORMAT (MM/DD/YYYY)]: ")
            matchs_Date = []
            for _ in self.matches:
                if option4 in _.date:
                    matchs_Date.append(_)
            for _ in matchs_Date:

                print(_.home) 
                print("vs")
                print(_.away) 
                print("Stadium:") 
                _.stadiumId.show_stadium()
                print("Date:") 
                _.show_date()
                print("Match ID:") 
                _.show_match_id()
                print("""
                
                """)
# con la Date/la data, lo que hice fue pedirla y si se encontraba contenida en el atributo Date del match, este se mostraba
                
    def buy_ticket(self):

        match_to_buy = []
        name = input("Type your name: ")
        while not name.isalpha():
            name = input("ERROR, Type your name: ")
        dni = input("Type your ID or DNI: ")
        while not dni.isnumeric() or dni == 0:
            dni = input("ERROR, Type your ID or DNI: ")
        age = input("Type your age: ")
        while not age.isnumeric() or age == 0:
            age = input("ERROR, Type your age: ")
        for _ in self.matches:
            _.home.show_team() 
            print("vs")
            _.awayshow_team()
            print("Stadium:") 
            _.stadiumId.show_stadium()
            print("Date:") 
            _.show_date()
            print("Match ID:") 
            _.show_match_id()
            print("""
                
             """)
        match_id = input("Type the Match ID of the game you're interested in: ")
        while not match_id.isnumeric() or int(match_id) not in range(1,49):
            match_id = input("ERROR, type a valid Match ID: ")
#Al usuario se le va a pedir Data para ir recolectando los atributos del objeto customer/consumidor que se crea mas adelante, despues 
#se muestran los matchs/partidos para que seleccione al cual va a asistir

        for _ in self.matches:
            if match_id in _.match_id:
                match_to_buy.append(_)
        type = input("Select the ticket type you wish to buy (G/VIP): ").upper()
        while not type == "G" or type == "VIP":
            type = input("ERROR, Select the Seat Type to buy (G/VIP): ").upper()
        price = 0 
        if type == "G":
            price += 50
        else:
            price += 120
#Dependiendo del tipo de ticket que compre la variable price/precio cambia
        for _ in match_to_buy:
           capacity = (_.stadiumId.capacity)
           Stadium.map(self, capacity)
           seat = input("Select your wished seat: ")
           seat.split()
           code=str(_.match_id)+"/"+str(seat[0])+chr(int(seat[2]))
#Luego de que se muestra el mapa de los asientos del Stadium/estadio y el usuario selecciona uno, se crea un codigo de ticket
#Este codigo se crea con el Match ID, seguido de la fila del seat/asiento + un caracter especifico del numero del seat/asiento
        iva = price*0.16 
        total = price + iva
        ticket = Ticket(match_id,type,total,code,seat)
        ticket.show_ticket()
        option = input("Confirm purchase? (y/n): ").lower()
        if option == "y":
            customer = Customer(name, dni, age, ticket)
            self.customers.append(customer)
            self.seats_taken.append(seat)
            self.tickets_sales.append(ticket)
            print(" You have succesfully completed your purchase ")
        else: 
            print("Your purchase has not been completed, try again later.")
#Despues se calcula el price/precio con el IVA y se crea el objeto ticket y si el usuario confirma la purchase/compra y crea el objeto customer
#el cual posee como atributo la ticket que el costumer/consumidor compro

    def verify_attendance(self):
        code = input("Type ticket code: ")
        if code in self.codes:
                print("DENIED")
        else:
            for _ in self.customers:
                if code == _.ticket.code:
                    for par in self.matches:
                        if _.ticket.match_id == par.match_id:
                            _.attendance + 1
                            self.codes.append(code)
                            print("ACCESS GRANTED")
#Se coloca el codigo del ticket y si ya se encuantra en la lista de codigos entonces se le suma 1 al attendance/asistencia del match/partido cuyo ID
#sea el que esta en la ticket
        
    def manage_products(self):
        for product in self.products:
            if product.adicional == "non-alcoholic":
                self.non_alcoholic_beverages.append(product)
            elif product.adicional == "alcoholic":
                self.alcoholic_beverages.append(product)
            elif product.adicional == "package":
                self.food_package.append(product)
            elif product.adicional == "plate":
                self.food_plate.append(product)
#Como ya se habia creado una clase product, se creo una lista para cada tipo de producto y se le agrego su product correspondiente

    def sort_products(self):
        option = input("""
        Sort by:

        [1] Name
        [2] Type
        [3] Price Range

        Select an option: 
        
        """)
        while not option.isnumeric() or int(option) not in range(1,4):
            option = input("ERROR, Select a valid option: ")
#Se muestra un mini menu para seleccionar como va a ser el filtro
        if option == "1":
            option2 = input("Type product name: ")
            for product in self.products:
                if product.name == option2:
                    product.show_product()
#En la primera opcion se pide el nombre del product y se muestra los products con ese nombre
        elif option == "2":
            option3 = input(" What kind of product are you looking for? (beverage/food): ").lower()
            while not option3 == "beverage" or option3 == "food":
                option3 = input("ERROR, What kind of product you wish to look for? (beverage/food): ").lower()
            if option3 == "beverage":
                for product in self.products:
                    if product.type == "beverages":
                        product.show_product()
            elif option3 == "food":
                for product in self.products:
                    if product.type == "food":
                        product.show_product()
#En la segunda opcion se le pide el tipo de product que se desea ver y dependiendo de la respuesta se muestra uno u otro
        elif option == "3":
            start = int(input("Set your range start: "))
            while not start.isnumeric():
                start = int(input("ERROR, Set your range start: "))
            end = int(input("Set your range end: "))
            while not end.isnumeric():
                end = int(input("ERROR, Set your range end: "))
            for product in self.products:
                if product.price in range(start, end +1):
                    product.show_product()
# se le pide al usuario determinar un rango de precio y se muestran los productos cuyo precio este dentro de ese rango 
#El  problema es que con este modulo es que la muestra de productos vendria siendo general y no por restaurantes especificos

    def purchase_restaurant(self):
        option = input("Type your ID: ")
        total = 0
        for customer in self.customers:
            age = None
            if customer.dni == option and customer.ticket.type == "VIP":
                age = customer.age
                option2 = input("Which product you wish to purchase? (beverage/food)").lower()
                if option2 == "beverage":
                    option3 = input("What kind of beverage you wish to buy? (alcoholic/ non alcoholic").lower()
                    if option3 == "alcoholic":
                        if int(age) < 18:
                            print("You have to be over 18 to be able to purchase alcoholic beverages")
                        else:
                            for alcohol in self.alcoholic_beverages:
                                alcohol.show_product()
                                purchase = input("Type the name of the product you wish to purchase: ")
                    elif option3 == "non alcoholic":
                        for beverage in self.non_alcoholic_beverages:
                            beverage.show_product()
                            purchase = input("Type the name of the product you wish to purchase: ")
                elif option2 == "food":
                    for food in self.food_package:
                        food.show_product()
                    for a in self.food_plate:
                        a.show_product()
                        purchase =  input("Type the name of the product you wish to purchase: ")
                for p in self.products:
                    if purchase == p.name:
                        p.show_product()
                        payment = total + int(p.price)
                        print(f'The total ammount to pay is: {payment}')
            else:
                print("You shall purchase a VIP ticket")
#En este modulo was que luego de pedir la ID, se buscara que customer ya registrado tenia la misma ID, 
# de no estarlo se pedira que se registre. 
                        
    def stats(self):
        while True:
             print("Select the stat you wish to see")
             print("""
                [1] Average spent VIP
                [2] Matches stats
                [3] Most attended match
                [4] Game with most ticket sales
                [5] Top 3 best selling products
                [6] Top 3 most consuming customers
                [0] Exit stats
                """)
             option = input("Selection: ")
             while not option.isnumeric() or int(option) not in range(0,7):
                option = input("ERROR, Type a valid option")

# como yo realice mi codigo hay stats que no se podrian hacer de una forma sencilla
# En la estadistica 3 se compara las attendances de los matchs en la lista de los matchs para ver cual tuvo mayor presencia

             if option == "1":
                pass
                
             elif option == "2":
                pass

             elif option == "3":
                winner = self.matches[0]
                for match in self.matches:
                    if match.attendance > winner.attendance:
                        winner = match
                        print(f"""

                        The Most attended match was: {winner}
                        
                        """)

             elif option == "4":
                for ticket in self.tickets_sales:
                    pass
                       

             elif option == "5":
                pass

             elif option == "6":
                pass

             else:
                break


#El MAIN MENU donde el programa donde todas las funciones se ejecutan
    def menu(self):
        self.info_api()
        file = open("Data.txt","a")
        while True:
            print("\nMAIN MENU")
            print("""
            [1] Match management
            [2] Buy tickets
            [3] Attendance
            [4] Product management
            [5] Attend restaurant
            [6] stats
            [0] Salir
            """)
        
            option = input("Selection")
            while not option.isnumeric() or int(option) not in range(1,8):
                option = input("ERROR, Type a valid option")

            if option == "1":
                self.sort_matches()
                
            elif option == "2":
                self.buy_ticket()

            elif option == "3":
                self.verify_attendance()

            elif option == "4":
                self.manage_products()
                self.sort_products()

            elif option == "5":
                self.purchase_restaurant()

            elif option == "6":
                self.stats()

            else:
                file.close
                break


m = Main()

m.menu()