class Match():
    def __init__(self,matchId,home,away,date,stadiumId,attendance):
        self.matchId = matchId
        self.home = home
        self.away = away
        self.date = date
        self.stadiumId = stadiumId
        self.attendance = attendance

    def show_match(self):
        print(f"""
        Home Team = {self.home}
        Away Team = {self.away}
        Date = {self.date}
        Stadium ID = {self.stadiumId}
        Match ID = {self.matchId}
        Attendance = {self.attendance}
        """)
        
    def show_date(self):
        print(self.date)

    def show_match_id(self):
        print(self.matchId)

    def show_stadium_id(self):
        print(self.stadiumId)
    
    def show_attendance(self):
        print(self.attendance)

    def show_home(self):
        print(self.home)
    def show_away(self):
        print(self.away)