class Team:
    def __init__(self,id,code,name,group):
        self.id = id
        self.code= code
        self.name = name
        self.group = group

    def __str__(self):
        return f'FIFA ID:{self.id}, Code: {self.code},Name:{self.name}, Group: {self.group}'
    
    def show_country(self):
        print(f"""
        {self.id} - {self.name}
        """)

    def show_team(self):
        print(self.name)
        